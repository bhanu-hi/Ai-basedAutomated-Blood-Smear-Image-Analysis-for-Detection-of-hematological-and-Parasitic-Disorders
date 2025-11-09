# 🔧 Vercel Environment Variables Setup

## Current Issue: 500 Error

You're getting a 500 error because the API functions can't connect to MongoDB. The environment variables from your `.env` file are NOT automatically available in Vercel.

## Fix: Add Environment Variables in Vercel Dashboard

### Step 1: Go to Environment Variables
1. Open your Vercel Dashboard
2. Go to your project: **bloodsmearanalysis**
3. Click **Settings** → **Environment Variables**

### Step 2: Add These Variables

Add each of these variables:

#### Variable 1: MONGODB_URI
- **Key**: `MONGODB_URI`
- **Value**: 
  ```
  mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear?retryWrites=true&w=majority
  ```
- **Environment**: Select all (Production, Preview, Development)

#### Variable 2: MONGODB_DB_NAME
- **Key**: `MONGODB_DB_NAME`
- **Value**: `bloodsmear`
- **Environment**: Select all (Production, Preview, Development)

#### Variable 3: NODE_ENV
- **Key**: `NODE_ENV`
- **Value**: `production`
- **Environment**: Production only

### Step 3: Verify MongoDB Atlas Settings

Make sure your MongoDB Atlas is configured correctly:

1. **Go to MongoDB Atlas Dashboard**
2. **Network Access** → Check IP Whitelist
   - Add `0.0.0.0/0` to allow all IPs (Vercel uses dynamic IPs)
   - Or add specific Vercel IP ranges

3. **Database Access** → Verify User
   - Username: `tungalabhanuprakash3_db_user`
   - Password: `bhanu@143`
   - Has read/write permissions on `bloodsmear` database

### Step 4: Redeploy

After adding environment variables:
1. Go to **Deployments** tab
2. Click the **three dots (⋮)** on the latest deployment
3. Select **"Redeploy"**
4. **Uncheck** "Use existing Build Cache"
5. Click **"Redeploy"**

### Step 5: Check Function Logs

After redeployment:
1. Go to **Deployments** → Click on the latest deployment
2. Click **"Functions"** tab
3. Click on any API function (e.g., `api/register.js`)
4. View the logs to see if MongoDB connection is successful

## Common Issues

### Issue: Still getting 500 error
**Solution**: 
- Check Vercel Function Logs for the exact error message
- Verify environment variables are set correctly (no extra spaces)
- Ensure MongoDB Atlas IP whitelist includes `0.0.0.0/0`

### Issue: "MongoServerError: bad auth"
**Solution**:
- Verify the username and password in MongoDB Atlas
- Make sure `@` in password is URL-encoded as `%40`
- Check that the user has correct permissions

### Issue: "Connection timeout"
**Solution**:
- Add `0.0.0.0/0` to MongoDB Atlas IP whitelist
- Check that your cluster is running (not paused)

## Testing After Setup

Once environment variables are set and redeployed:

1. **Test API endpoint directly**:
   ```bash
   curl -X POST https://bloodsmearanalysis.vercel.app/api/test
   ```
   Should return a success message

2. **Test registration**:
   - Go to your site
   - Try to register a new user
   - Check browser console for errors

3. **Check Vercel logs**:
   - Any errors will appear in the Function Logs
   - Look for MongoDB connection errors

## Your Environment Variables

Based on your `.env` file, use these exact values in Vercel:

```
MONGODB_URI=mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear?retryWrites=true&w=majority
MONGODB_DB_NAME=bloodsmear
NODE_ENV=production
```

**IMPORTANT**: The `@` symbol in your password (`bhanu@143`) MUST be encoded as `%40` in the connection string, which is already done above.

## Next Steps

1. ✅ Add environment variables in Vercel Dashboard
2. ✅ Verify MongoDB Atlas IP whitelist
3. ✅ Redeploy the application
4. ✅ Test the API endpoints
5. ✅ Check Function Logs if still having issues

After completing these steps, the 500 error should be resolved and your API will connect to MongoDB successfully!
