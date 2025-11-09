# 🚀 Blood Smear Analysis - Vercel Deployment Guide

This guide will walk you through deploying the Blood Smear Analysis application to Vercel.

## Prerequisites

1. **GitHub Account** - Your code should be in a GitHub repository
2. **Vercel Account** - Sign up at [vercel.com](https://vercel.com)
3. **MongoDB Atlas** - A free cloud database is required

## 🛠️ Setup Instructions

### 1. Environment Variables

Create a `.env` file in the `project` directory with the following variables:

```
MONGODB_URI=your_mongodb_atlas_connection_string
NODE_ENV=production
# Add any other environment variables your app needs
```

### 2. Deploy to Vercel

1. **Import your repository**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New" → "Project"
   - Import your GitHub repository

2. **Configure Project**
   - Framework Preset: Vite
   - Root Directory: `bloodsmearimageanalysisproject/project`
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`
   - Development Command: `npm run dev`

3. **Environment Variables**
   - Add all variables from your `.env` file in the Vercel project settings
   - Make sure to mark them for production environment

4. **Deploy**
   - Click "Deploy"
   - Vercel will automatically deploy your application

## 🚀 Post-Deployment

- Your application will be available at `https://your-project-name.vercel.app`
- Vercel will automatically deploy new changes when you push to your GitHub repository

## 🔧 Troubleshooting

- If you get build errors, check the Vercel deployment logs
- Ensure all environment variables are correctly set in Vercel
- Make sure your MongoDB Atlas IP whitelist includes Vercel's IP addresses

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [MongoDB Atlas Setup Guide](https://docs.atlas.mongodb.com/getting-started/)
- [Vite Documentation](https://vitejs.dev/guide/)
