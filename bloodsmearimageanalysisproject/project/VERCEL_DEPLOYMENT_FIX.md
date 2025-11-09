# Vercel Deployment Fix - Database Connection Error

## Problem
**Error:** "Database not connected" on Vercel deployment

## Root Causes

1. **Hardcoded localhost MongoDB URI** - The server was using `localhost:27017` which doesn't exist on Vercel
2. **Special characters in password** - The `@` symbol in password `bhanu@143` wasn't URL encoded
3. **Missing environment variables** - Vercel deployment wasn't configured with MongoDB Atlas credentials

## Fixes Applied

### 1. Updated `server/server.js`
Changed from hardcoded localhost to environment variables:

```javascript
// Before
const MONGODB_URI = 'mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin';

// After
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin';
const DB_NAME = process.env.MONGODB_DB_NAME || 'bloodsmear';
```

### 2. Fixed `.env` File
URL encoded the password (@ → %40):

```env
MONGODB_URI=mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear?retryWrites=true&w=majority
```

### 3. Created `vercel.json`
Added Vercel configuration for serverless deployment.

## Deployment Steps for Vercel

### Step 1: Set Environment Variables in Vercel Dashboard

1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add the following variables:

| Name | Value |
|------|-------|
| `MONGODB_URI` | `mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear?retryWrites=true&w=majority` |
| `MONGODB_DB_NAME` | `bloodsmear` |

**IMPORTANT:** Make sure to URL encode special characters in passwords:
- `@` → `%40`
- `#` → `%23`
- `$` → `%24`
- `%` → `%25`
- `&` → `%26`

### Step 2: Configure MongoDB Atlas

1. **Login to MongoDB Atlas** (https://cloud.mongodb.com)
2. **Whitelist Vercel IPs:**
   - Go to **Network Access**
   - Click **Add IP Address**
   - Select **Allow Access from Anywhere** (0.0.0.0/0)
   - Or add specific Vercel IPs if you know them

3. **Verify Database User:**
   - Go to **Database Access**
   - Ensure user `tungalabhanuprakash3_db_user` exists
   - Password should be `bhanu@143`
   - User should have read/write permissions on `bloodsmear` database

### Step 3: Update Server for Serverless

The current `server.js` uses `app.listen()` which doesn't work well with Vercel serverless functions. You need to export the app:

Add this at the end of `server/server.js`:

```javascript
// For Vercel serverless
module.exports = app;

// For local development
if (require.main === module) {
    app.listen(PORT, () => {
        console.log(`Server running on http://localhost:${PORT}`);
        console.log(`MongoDB URI: ${MONGODB_URI}`);
        console.log(`Database: ${DB_NAME}`);
    });
}
```

### Step 4: Redeploy to Vercel

```bash
# Option 1: Using Vercel CLI
vercel --prod

# Option 2: Push to GitHub
git add .
git commit -m "Fix MongoDB connection for Vercel deployment"
git push origin main
```

## Alternative: Use Vercel Environment Variables UI

Instead of using `vercel.json` env section, you can:

1. Remove the `env` section from `vercel.json`
2. Set environment variables directly in Vercel dashboard
3. This is more secure as secrets aren't in your code

## Testing the Fix

After deployment:

1. Visit your Vercel URL
2. Try to register a new account
3. You should see the account created successfully instead of "Database not connected"

## Troubleshooting

### Still getting "Database not connected"?

1. **Check Vercel Logs:**
   - Go to Vercel Dashboard → Deployments → Click on latest deployment → Functions
   - Look for MongoDB connection errors

2. **Verify Environment Variables:**
   - Vercel Dashboard → Settings → Environment Variables
   - Make sure `MONGODB_URI` is set correctly

3. **Test MongoDB Connection:**
   - Use MongoDB Compass or mongosh to test the connection string locally
   - Make sure the password is correct

4. **Check MongoDB Atlas:**
   - Verify IP whitelist includes 0.0.0.0/0
   - Check database user has correct permissions

### Connection String Format

Make sure your MongoDB Atlas connection string follows this format:

```
mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority
```

- Username: `tungalabhanuprakash3_db_user`
- Password: `bhanu%40143` (URL encoded)
- Cluster: `cluster0.xpeq7r7`
- Database: `bloodsmear`

## Important Notes

1. **Don't commit `.env` to Git** - Add it to `.gitignore`
2. **Use Vercel environment variables** for production secrets
3. **MongoDB Atlas free tier** has connection limits (500 concurrent connections)
4. **Serverless functions** have cold start times - first request may be slow

## Next Steps

1. Update `server.js` to export the app for serverless
2. Set environment variables in Vercel dashboard
3. Configure MongoDB Atlas IP whitelist
4. Redeploy to Vercel
5. Test registration and login functionality
