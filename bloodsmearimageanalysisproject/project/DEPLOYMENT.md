# 🚀 Deployment Guide

## Prerequisites

- Node.js 14.x or later
- MongoDB Atlas account (for production database)
- Vercel account (for deployment)
- Git (for version control)

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# MongoDB Configuration
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>?retryWrites=true&w=majority
MONGODB_DB_NAME=bloodsmear

# Vercel Configuration
VERCEL_ORG_ID=your-vercel-org-id
VERCEL_PROJECT_ID=your-vercel-project-id
```

## Local Development

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Deployment to Vercel

### Automatic Deployment

1. Push your code to GitHub
2. Connect your GitHub repository to Vercel
3. Vercel will automatically detect and deploy your project

### Manual Deployment

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy to production:
   ```bash
   vercel --prod
   ```

## Environment Setup in Vercel

Add these environment variables in your Vercel project settings:

1. Go to your Vercel project
2. Click on "Settings" > "Environment Variables"
3. Add the following:
   - `MONGODB_URI`: Your MongoDB connection string
   - `MONGODB_DB_NAME`: Your database name (default: bloodsmear)

## Testing the API

You can test the API endpoints using the following cURL commands:

### Test Endpoint
```bash
curl https://your-vercel-app.vercel.app/api/test
```

### Register User
```bash
curl -X POST https://your-vercel-app.vercel.app/api/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123","full_name":"Test User"}'
```

### Login
```bash
curl -X POST https://your-vercel-app.vercel.app/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password123"}'
```

## Troubleshooting

### Common Issues

1. **MongoDB Connection Failed**
   - Verify your MongoDB Atlas IP whitelist
   - Check your connection string
   - Ensure your database user has the correct permissions

2. **CORS Errors**
   - Verify the `Access-Control-Allow-Origin` headers in your API responses
   - Check if your frontend URL is allowed in the CORS configuration

3. **Environment Variables Not Loading**
   - Ensure all required environment variables are set in Vercel
   - Redeploy after adding new environment variables

## Support

For any issues, please open an issue on GitHub or contact support.
