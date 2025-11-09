# 🔧 Vercel API Routing Fix

## Problem
The `/api/register` and `/api/login` endpoints were returning 404 errors because Vercel wasn't properly routing requests to the serverless functions.

## Solution Applied

### 1. Updated Root `vercel.json`
- Changed the build source from `server/**/*.js` to `api/**/*.js`
- Added explicit routes for each API endpoint
- Configured proper routing to the API directory

### 2. Updated Project `vercel.json`
- Added proper builds configuration for static files and API functions
- Configured routes to map `/api/*` requests to the corresponding serverless functions
- Added environment variable references

### 3. Vercel Project Settings

When deploying to Vercel, ensure these settings:

#### Root Directory
Set to: `bloodsmearimageanalysisproject/project`

#### Build & Development Settings
- **Framework Preset**: Vite
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`
- **Development Command**: `npm run dev`

#### Environment Variables (CRITICAL)
Add these in Vercel Dashboard → Settings → Environment Variables:

```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/bloodsmear?retryWrites=true&w=majority
MONGODB_DB_NAME=bloodsmear
NODE_ENV=production
```

### 4. API Endpoints Structure

Your API functions are located at:
```
bloodsmearimageanalysisproject/project/api/
├── register.js  → /api/register
├── login.js     → /api/login
└── test.js      → /api/test
```

Each file exports a serverless function handler:
```javascript
module.exports = async (req, res) => {
  // Handle request
};
```

## Testing After Deployment

1. **Test API endpoints**:
   ```bash
   curl -X POST https://your-app.vercel.app/api/test
   curl -X POST https://your-app.vercel.app/api/register -H "Content-Type: application/json" -d '{"email":"test@example.com","password":"test123","full_name":"Test User","role":"user"}'
   ```

2. **Check Vercel logs**:
   - Go to Vercel Dashboard → Your Project → Deployments
   - Click on the latest deployment
   - View the Function Logs to see any errors

## Common Issues & Solutions

### Issue: Still getting 404 errors
**Solution**: 
- Verify the Root Directory is set correctly in Vercel
- Check that environment variables are set
- Redeploy the project

### Issue: MongoDB connection errors
**Solution**:
- Ensure `MONGODB_URI` is correctly set in Vercel environment variables
- Verify MongoDB Atlas IP whitelist includes `0.0.0.0/0` (allow all) for Vercel
- Check MongoDB Atlas user credentials

### Issue: CORS errors
**Solution**:
- The API functions already include CORS headers
- If still having issues, check browser console for specific CORS error messages

## Next Steps

1. Push these changes to GitHub:
   ```bash
   git push origin main
   ```

2. Vercel will automatically redeploy

3. Test the API endpoints using the Vercel deployment URL

4. Monitor the deployment logs for any errors

## Additional Resources

- [Vercel Serverless Functions](https://vercel.com/docs/concepts/functions/serverless-functions)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [MongoDB Atlas Setup](https://docs.atlas.mongodb.com/getting-started/)
