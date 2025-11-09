# Vercel Deployment Checklist

## ✅ Pre-Deployment Checklist

### 1. MongoDB Atlas Setup
- [ ] Login to MongoDB Atlas (https://cloud.mongodb.com)
- [ ] Navigate to **Network Access**
- [ ] Add IP Address: `0.0.0.0/0` (Allow access from anywhere)
- [ ] Navigate to **Database Access**
- [ ] Verify user exists: `tungalabhanuprakash3_db_user`
- [ ] Verify password: `bhanu@143`
- [ ] Verify user has **Read and Write** permissions on `bloodsmear` database

### 2. Vercel Environment Variables
- [ ] Go to Vercel Dashboard → Your Project → Settings → Environment Variables
- [ ] Add `MONGODB_URI`:
  ```
  mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear?retryWrites=true&w=majority
  ```
- [ ] Add `MONGODB_DB_NAME`: `bloodsmear`
- [ ] Set environment for: **Production**, **Preview**, and **Development**

### 3. Code Changes (Already Applied)
- [x] Updated `server/server.js` to use environment variables
- [x] Fixed MongoDB Atlas URI with URL-encoded password
- [x] Added `module.exports = app` for serverless
- [x] Created `vercel.json` configuration

### 4. Files to Verify
- [ ] `.env` is in `.gitignore` (don't commit secrets!)
- [ ] `vercel.json` exists in project root
- [ ] `server/server.js` exports the app

## 🚀 Deployment Commands

### Option 1: Deploy via Vercel CLI
```bash
# Install Vercel CLI (if not installed)
npm i -g vercel

# Login to Vercel
vercel login

# Deploy to production
vercel --prod
```

### Option 2: Deploy via GitHub
```bash
# Commit changes
git add .
git commit -m "Fix MongoDB connection for Vercel deployment"

# Push to GitHub
git push origin main
```
Vercel will automatically deploy when you push to your connected GitHub repository.

## 🧪 Testing After Deployment

1. **Visit your Vercel URL** (e.g., https://your-app.vercel.app)
2. **Test Registration:**
   - Click "Register" tab
   - Fill in the form
   - Click "Create Account"
   - Should see success message (not "Database not connected")
3. **Test Login:**
   - Use the credentials you just created
   - Should redirect to dashboard
4. **Check Vercel Logs:**
   - Go to Vercel Dashboard → Deployments → Latest → Functions
   - Look for MongoDB connection logs

## ⚠️ Common Issues & Solutions

### Issue 1: "Database not connected"
**Solution:**
- Verify environment variables are set in Vercel dashboard
- Check MongoDB Atlas IP whitelist (should include 0.0.0.0/0)
- Verify MongoDB user credentials are correct

### Issue 2: "MongoServerError: bad auth"
**Solution:**
- Password in MongoDB Atlas doesn't match environment variable
- Reset password in MongoDB Atlas or update environment variable
- Make sure special characters are URL encoded

### Issue 3: "MongoServerError: IP not whitelisted"
**Solution:**
- Add `0.0.0.0/0` to MongoDB Atlas Network Access
- Wait 1-2 minutes for changes to propagate

### Issue 4: Function timeout
**Solution:**
- Vercel free tier has 10-second timeout for serverless functions
- Optimize database queries
- Consider upgrading to Pro plan for longer timeouts

## 📝 Environment Variable Format

### Correct Format:
```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database?retryWrites=true&w=majority
```

### URL Encoding Special Characters:
| Character | Encoded |
|-----------|---------|
| `@` | `%40` |
| `#` | `%23` |
| `$` | `%24` |
| `%` | `%25` |
| `&` | `%26` |
| `:` | `%3A` |
| `/` | `%2F` |

### Your Specific Values:
- Username: `tungalabhanuprakash3_db_user`
- Password: `bhanu@143` → `bhanu%40143` (URL encoded)
- Cluster: `cluster0.xpeq7r7.mongodb.net`
- Database: `bloodsmear`

## 🔒 Security Best Practices

1. **Never commit `.env` file** - Already in `.gitignore`
2. **Use Vercel environment variables** - Set in dashboard, not in code
3. **Rotate credentials regularly** - Change MongoDB password periodically
4. **Limit IP access** - If possible, use specific Vercel IPs instead of 0.0.0.0/0
5. **Use read-only users** - For features that only read data

## 📚 Additional Resources

- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [MongoDB Atlas IP Whitelist](https://docs.atlas.mongodb.com/security/ip-access-list/)
- [URL Encoding Reference](https://www.w3schools.com/tags/ref_urlencode.ASP)

## ✨ Success Indicators

After successful deployment, you should see:
- ✅ Registration works without "Database not connected" error
- ✅ Login works and redirects to dashboard
- ✅ Vercel function logs show "Connected to MongoDB (authenticated)"
- ✅ No errors in Vercel deployment logs

---

**Last Updated:** After fixing MongoDB connection for Vercel deployment
**Status:** Ready to deploy
