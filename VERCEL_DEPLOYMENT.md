# 🚀 Vercel Deployment Guide

Complete guide to deploy your Blood Smear Analysis Project on Vercel.

---

## 📋 Prerequisites

1. **GitHub Account** - ✅ Already done (repo pushed)
2. **Vercel Account** - Sign up at [vercel.com](https://vercel.com)
3. **MongoDB Atlas** - Free cloud database (required)

---

## 🗄️ Step 1: Setup MongoDB Atlas

Vercel doesn't support local MongoDB, so you need MongoDB Atlas:

### Create MongoDB Atlas Account

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)
2. Sign up for FREE (no credit card required)
3. Create a new project: `BloodSmearAnalysis`

### Create Database Cluster

1. Click **"Build a Database"**
2. Choose **FREE** M0 tier
3. Select a cloud provider and region (closest to you)
4. Cluster Name: `Cluster0` (default)
5. Click **"Create"**

### Create Database User

1. Go to **"Database Access"** (left sidebar)
2. Click **"Add New Database User"**
3. Authentication Method: **Password**
   - Username: `bhanu` (or your choice)
   - Password: `bhanu123` (or create a strong password)
4. Database User Privileges: **Read and write to any database**
5. Click **"Add User"**

### Whitelist IP Addresses

1. Go to **"Network Access"** (left sidebar)
2. Click **"Add IP Address"**
3. Click **"Allow Access from Anywhere"** (adds `0.0.0.0/0`)
4. Click **"Confirm"**

### Get Connection String

1. Go to **"Database"** → Click **"Connect"**
2. Choose **"Connect your application"**
3. Driver: **Python**, Version: **3.12 or later**
4. Copy the connection string:
   ```
   mongodb+srv://bhanu:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
5. Replace `<password>` with your actual password
6. Add database name: `/bloodsmear` before the `?`
   ```
   mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear?retryWrites=true&w=majority
   ```

---

## 🚀 Step 2: Deploy to Vercel

### Option 1: Vercel Dashboard (Recommended)

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository:
   - Select: `BhanU303545/bloodsmearimageanalysisproject`
4. Configure Project:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave default)
   - **Build Command**: Leave empty
   - **Output Directory**: `bloodsmearimageanalysisproject/project`

5. **Environment Variables** (IMPORTANT):
   Click **"Environment Variables"** and add:
   
   | Name | Value |
   |------|-------|
   | `MONGO_URI` | Your MongoDB Atlas connection string |
   
   Example:
   ```
   mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear?retryWrites=true&w=majority
   ```

6. Click **"Deploy"**

### Option 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
cd c:\Users\SIVA\Desktop\bloodsmearimageanalysisproject
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? bloodsmearimageanalysisproject
# - Directory? ./
# - Override settings? No

# Add environment variable
vercel env add MONGO_URI
# Paste your MongoDB Atlas connection string
# Select: Production, Preview, Development
```

---

## ⚠️ Important: Model File Issue

Your model file (`best_model.pth`) is **too large** for Vercel (50MB limit for serverless functions).

### Solution Options:

### **Option 1: Use Hugging Face (Recommended)**

1. Create account at [huggingface.co](https://huggingface.co)
2. Upload your model:
   ```bash
   pip install huggingface_hub
   huggingface-cli login
   huggingface-cli upload your-username/bloodsmear-model models/best_model.pth
   ```
3. Update `vercel_app.py` to download from Hugging Face

### **Option 2: Use Google Drive**

1. Upload `best_model.pth` to Google Drive
2. Get shareable link → Make public
3. Convert to direct download link
4. Update `vercel_app.py`:

```python
import urllib.request
import os

MODEL_URL = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"
MODEL_PATH = "models/best_model.pth"

if not os.path.exists(MODEL_PATH):
    os.makedirs("models", exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
```

### **Option 3: Deploy Backend Separately**

Deploy the ML model on a different platform:
- **Railway** - Free tier with 500MB
- **Fly.io** - Free tier with 3GB
- **Render** - Free tier with persistent storage

Then update frontend to call that API.

---

## 🔧 Step 3: Update Configuration Files

### Update API Endpoint in Frontend

After deployment, Vercel will give you a URL like:
```
https://bloodsmearimageanalysisproject.vercel.app
```

Update `bloodsmearimageanalysisproject/project/js/api.js`:

```javascript
// Change this line:
const API_URL = 'http://localhost:5001/api';

// To:
const API_URL = 'https://your-vercel-url.vercel.app/api';
```

---

## 📝 Step 4: Push Changes to GitHub

```bash
cd c:\Users\SIVA\Desktop\bloodsmearimageanalysisproject

git add .
git commit -m "Add Vercel deployment configuration"
git push
```

Vercel will automatically redeploy when you push to GitHub!

---

## 🧪 Step 5: Test Your Deployment

1. Visit your Vercel URL: `https://your-project.vercel.app`
2. Try to register a new user
3. Login with credentials
4. Upload a blood smear image
5. Check if analysis works

### Test API Health:
```
https://your-project.vercel.app/api/health
```

Should return:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "device": "cpu"
}
```

---

## 🔄 Continuous Deployment

Every time you push to GitHub, Vercel automatically:
1. Detects the push
2. Builds your project
3. Deploys the new version
4. Provides a preview URL

```bash
# Make changes
git add .
git commit -m "Update feature"
git push

# Vercel automatically deploys!
```

---

## 🐛 Troubleshooting

### Error: "Module not found"
- Check `requirements.txt` includes all dependencies
- Vercel automatically installs from `requirements.txt`

### Error: "Function size exceeded"
- Model file is too large
- Use external storage (Hugging Face, Google Drive)
- Or deploy backend separately

### Error: "MongoDB connection failed"
- Check MongoDB Atlas connection string
- Verify IP whitelist includes `0.0.0.0/0`
- Check username/password are correct

### Error: "CORS policy"
- Update CORS in `vercel_app.py`:
```python
CORS(app, origins=["https://your-vercel-url.vercel.app"])
```

---

## 📊 Vercel Limits (Free Tier)

- ✅ **Bandwidth**: 100GB/month
- ✅ **Serverless Function Execution**: 100GB-Hrs
- ✅ **Serverless Function Size**: 50MB (compressed)
- ✅ **Build Time**: 6000 minutes/month
- ⚠️ **Function Duration**: 10 seconds max

---

## 🎯 Alternative: Hybrid Deployment

If model is too large for Vercel:

1. **Frontend on Vercel** (Static files)
   - Fast, free, CDN-powered
   
2. **Backend on Railway/Render** (ML model)
   - More resources for ML inference
   - Persistent storage for model

Update `js/api.js`:
```javascript
const API_URL = 'https://your-backend.railway.app/api';
```

---

## ✅ Deployment Checklist

- [ ] MongoDB Atlas cluster created
- [ ] Database user created
- [ ] IP whitelist configured (0.0.0.0/0)
- [ ] Connection string obtained
- [ ] Vercel account created
- [ ] GitHub repo connected to Vercel
- [ ] Environment variable `MONGO_URI` added
- [ ] Model file handled (external storage or separate deployment)
- [ ] API URL updated in frontend
- [ ] Changes pushed to GitHub
- [ ] Deployment tested

---

## 🌐 Your Deployment URLs

After deployment, you'll have:

- **Frontend**: `https://bloodsmearimageanalysisproject.vercel.app`
- **API**: `https://bloodsmearimageanalysisproject.vercel.app/api`
- **Health Check**: `https://bloodsmearimageanalysisproject.vercel.app/api/health`

---

## 📚 Resources

- [Vercel Documentation](https://vercel.com/docs)
- [MongoDB Atlas Docs](https://docs.atlas.mongodb.com/)
- [Vercel Python Runtime](https://vercel.com/docs/functions/serverless-functions/runtimes/python)

---

**Status**: Ready to deploy! 🚀

Follow the steps above to get your Blood Smear Analysis app live on Vercel!
