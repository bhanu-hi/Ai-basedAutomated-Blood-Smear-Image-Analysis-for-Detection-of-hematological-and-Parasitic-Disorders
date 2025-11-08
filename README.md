# Blood Smear Image Analysis Project

Automated Detection of Hematological and Parasitic Disorders using Deep Learning

## 🩸 Features

- **AI-Powered Analysis**: EfficientNet-B0 model with 99.35% accuracy
- **Multiple Disease Detection**: Detects 10+ conditions including:
  - Malaria (Parasitized/Uninfected)
  - Babesia, Leishmania, Trypanosome
  - Blood cell types: Basophil, Eosinophil, Lymphocyte, Monocyte, Neutrophil
- **User Authentication**: Secure login/registration system
- **Real-time Analysis**: Instant blood smear image analysis
- **Results Dashboard**: Track and view analysis history

## 🛠️ Tech Stack

### Backend
- **Python 3.x** - Core language
- **Flask** - Web framework
- **PyTorch** - Deep learning framework
- **MongoDB** - Database
- **EfficientNet-B0** - CNN model

### Frontend
- **HTML5/CSS3/JavaScript** - UI
- **Modern CSS** - Responsive design

## 📋 Prerequisites

- Python 3.8+
- MongoDB
- CUDA-capable GPU (optional, for faster inference)

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/bloodsmearimageanalysisproject.git
cd bloodsmearimageanalysisproject
```

### 2. Install Python dependencies
```bash
cd bloodsmearimageanalysisproject/project/backend
pip install -r requirements.txt
```

### 3. Setup MongoDB
```bash
# Start MongoDB service
net start MongoDB

# Create user (run the setup script)
cd ../
mongosh --eval "load('setup_mongodb_user.js')"
```

### 4. Start the Backend Server
```bash
cd backend
python app.py
```
Server will run on `http://localhost:5001`

### 5. Open the Application
Open `bloodsmearimageanalysisproject/project/index.html` in your browser

## 🌐 Deployment on Render

### Backend Deployment

1. **Create a new Web Service** on Render
2. **Connect your GitHub repository**
3. **Configure the service**:
   - **Build Command**: `pip install -r bloodsmearimageanalysisproject/project/backend/requirements.txt`
   - **Start Command**: `cd bloodsmearimageanalysisproject/project/backend && python app.py`
   - **Environment Variables**:
     - `MONGO_URI`: Your MongoDB connection string
     - `PORT`: 5001

### Frontend Deployment

1. **Create a Static Site** on Render
2. **Set publish directory**: `bloodsmearimageanalysisproject/project`

## 📊 Model Information

- **Architecture**: EfficientNet-B0 with custom classifier
- **Accuracy**: 99.35%
- **Input Size**: 224x224 RGB images
- **Classes**: 10 disease/cell types

## 🔒 Security Notes

- MongoDB credentials are stored in environment variables
- Never commit `.env` files to Git
- Use strong passwords in production
- Enable HTTPS in production

## 📝 API Endpoints

- `POST /api/register` - User registration
- `POST /api/login` - User login
- `POST /api/analyze` - Analyze blood smear image
- `GET /api/results?user_id=<id>` - Get user's analysis history
- `GET /api/stats/<user_id>` - Get user statistics
- `GET /api/health` - Health check

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Your Name - [GitHub Profile](https://github.com/YOUR_USERNAME)

## 🙏 Acknowledgments

- Dataset providers
- PyTorch team
- Flask community
