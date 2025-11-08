# Model Deployment Guide for Render

## ✅ Current Status

The app now uses **lazy loading** - the model loads on the first analysis request instead of at startup. This prevents deployment timeout issues.

## 🔧 Two Options to Deploy the Model

### **Option 1: Upload Model to Google Drive (Recommended)**

1. **Upload the model file**:
   - Go to [Google Drive](https://drive.google.com)
   - Upload `bloodsmearimageanalysisproject/project/backend/models/best_model.pth`
   - Right-click → Share → Change to "Anyone with the link"
   - Copy the link (format: `https://drive.google.com/file/d/FILE_ID/view`)

2. **Get direct download link**:
   - Extract the FILE_ID from the URL
   - Create direct download URL: `https://drive.google.com/uc?export=download&id=FILE_ID`

3. **Add to Render Environment Variables**:
   - Go to Render Dashboard → Your Service → Environment
   - Add new variable:
     - **Key**: `MODEL_URL`
     - **Value**: `https://drive.google.com/uc?export=download&id=YOUR_FILE_ID`

4. **Redeploy**: The app will automatically download the model on first use

---

### **Option 2: Use Hugging Face Hub (More Professional)**

1. **Create Hugging Face account**: https://huggingface.co/join

2. **Install Hugging Face CLI** (locally):
   ```bash
   pip install huggingface_hub
   ```

3. **Login and upload**:
   ```bash
   huggingface-cli login
   huggingface-cli upload bhanu-hi/bloodsmear-model bloodsmearimageanalysisproject/project/backend/models/best_model.pth
   ```

4. **Add to Render Environment Variables**:
   - **Key**: `MODEL_URL`
   - **Value**: `https://huggingface.co/bhanu-hi/bloodsmear-model/resolve/main/best_model.pth`

---

## 🚀 Current Deployment Should Work

The latest code changes mean:
- ✅ App starts immediately (no model loading at startup)
- ✅ Model loads on first `/api/analyze` request
- ✅ If model file exists locally, it uses it
- ✅ If not, it downloads from `MODEL_URL` environment variable
- ✅ Health check works without loading model

## 📝 Next Steps

1. **Let current deployment finish** - It should now start successfully
2. **Upload model to Google Drive** (easiest option)
3. **Add MODEL_URL to Render environment variables**
4. **Test the `/api/analyze` endpoint** - Model will download on first use

## 🧪 Testing

Once deployed:
1. Check health: `https://your-app.onrender.com/api/health`
2. Should return: `{"status": "healthy", "model_loaded": false, "mongodb_connected": true}`
3. Make first analysis request - model will download and load
4. Subsequent requests will be fast (model already loaded)

---

**Note**: The first analysis request will take 1-2 minutes (model download + loading). After that, all requests will be fast.
