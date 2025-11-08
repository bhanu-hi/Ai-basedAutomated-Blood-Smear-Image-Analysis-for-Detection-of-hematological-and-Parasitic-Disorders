# 🔄 MongoDB Migration Guide
## From Local MongoDB Compass → MongoDB Atlas

Since you're using MongoDB Compass locally, here's how to migrate your data to MongoDB Atlas for Vercel deployment.

---

## 📊 Current Setup

- **Local MongoDB**: Running on `localhost:27017`
- **Database**: `bloodsmear`
- **Collections**: `users`, `analyses`, `results`
- **User**: `bhanu` / `bhanu123`

---

## 🎯 Step 1: Export Your Local Data

### Using MongoDB Compass (GUI Method)

1. **Open MongoDB Compass**
2. **Connect to local database**:
   ```
   mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin
   ```

3. **Export each collection**:
   
   **For `users` collection**:
   - Click on `bloodsmear` database
   - Click on `users` collection
   - Click **"Export Collection"** (top right)
   - Format: **JSON**
   - Save as: `users_export.json`
   
   **For `analyses` collection**:
   - Click on `analyses` collection
   - Click **"Export Collection"**
   - Format: **JSON**
   - Save as: `analyses_export.json`
   
   **For `results` collection**:
   - Click on `results` collection
   - Click **"Export Collection"**
   - Format: **JSON**
   - Save as: `results_export.json`

### Using Command Line (Alternative)

```bash
# Export users collection
mongoexport --uri="mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin" --collection=users --out=users_export.json

# Export analyses collection
mongoexport --uri="mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin" --collection=analyses --out=analyses_export.json

# Export results collection
mongoexport --uri="mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin" --collection=results --out=results_export.json
```

---

## ☁️ Step 2: Create MongoDB Atlas Account

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)
2. Sign up with:
   - Email
   - Google account
   - GitHub account
3. Verify your email

---

## 🗄️ Step 3: Create Free Cluster

1. **Create Organization** (if prompted):
   - Name: `Personal` or `BloodSmearProject`
   - Click **Next** → **Create Organization**

2. **Create Project**:
   - Name: `BloodSmearAnalysis`
   - Click **Next** → **Create Project**

3. **Build Database**:
   - Click **"Build a Database"**
   - Choose **FREE** M0 tier (0.5GB storage)
   - Cloud Provider: **AWS** (or any)
   - Region: Choose closest to you (e.g., `Mumbai (ap-south-1)` for India)
   - Cluster Name: `Cluster0` (default)
   - Click **"Create"**

---

## 🔐 Step 4: Create Database User

1. **Security Quickstart** will appear
2. **Authentication Method**: Username and Password
   - Username: `bhanu`
   - Password: `bhanu123` (or create a strong password)
   - Click **"Create User"**

3. **Add entries to IP Access List**:
   - Click **"Add My Current IP Address"** (for your local access)
   - Click **"Add a Different IP Address"**
   - Enter: `0.0.0.0/0` (allows access from anywhere - needed for Vercel)
   - Description: `Allow all (Vercel deployment)`
   - Click **"Add Entry"**

4. Click **"Finish and Close"**

---

## 🔗 Step 5: Get Connection String

1. Click **"Connect"** on your cluster
2. Choose **"Connect with MongoDB Compass"**
3. Copy the connection string:
   ```
   mongodb+srv://bhanu:<password>@cluster0.xxxxx.mongodb.net/
   ```

4. **Replace `<password>`** with your actual password:
   ```
   mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear
   ```

---

## 📥 Step 6: Import Data to Atlas

### Method 1: Using MongoDB Compass (Easiest)

1. **In MongoDB Compass**, click **"New Connection"**
2. **Paste your Atlas connection string**:
   ```
   mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear
   ```
3. Click **"Connect"**

4. **Create database**:
   - Click **"Create Database"**
   - Database Name: `bloodsmear`
   - Collection Name: `users`
   - Click **"Create Database"**

5. **Import each collection**:
   
   **Import users**:
   - Select `bloodsmear` → `users` collection
   - Click **"Add Data"** → **"Import JSON or CSV file"**
   - Select `users_export.json`
   - Click **"Import"**
   
   **Import analyses**:
   - Click **"Create Collection"** → Name: `analyses`
   - Click **"Add Data"** → **"Import JSON or CSV file"**
   - Select `analyses_export.json`
   - Click **"Import"**
   
   **Import results**:
   - Click **"Create Collection"** → Name: `results`
   - Click **"Add Data"** → **"Import JSON or CSV file"**
   - Select `results_export.json`
   - Click **"Import"**

### Method 2: Using Command Line

```bash
# Import users
mongoimport --uri="mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear" --collection=users --file=users_export.json

# Import analyses
mongoimport --uri="mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear" --collection=analyses --file=analyses_export.json

# Import results
mongoimport --uri="mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear" --collection=results --file=results_export.json
```

---

## ✅ Step 7: Verify Migration

1. In MongoDB Compass (connected to Atlas)
2. Check `bloodsmear` database
3. Verify all collections exist:
   - ✅ `users` - Check document count matches
   - ✅ `analyses` - Check document count matches
   - ✅ `results` - Check document count matches

---

## 🔧 Step 8: Update Your Application

### For Local Development

Update `backend/app.py` line 20:

```python
# Old (local MongoDB)
MONGO_URI = 'mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin'

# New (MongoDB Atlas)
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear')
```

### Create .env file

Create `bloodsmearimageanalysisproject/project/backend/.env`:

```env
MONGO_URI=mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear
```

### Update .gitignore

Already done! `.env` is in `.gitignore` so your credentials won't be committed.

---

## 🚀 Step 9: Deploy to Vercel

Now that you have MongoDB Atlas:

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Import your GitHub repo: `BhanU303545/bloodsmearimageanalysisproject`
3. Add Environment Variable:
   - Key: `MONGO_URI`
   - Value: `mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear`
4. Click **Deploy**

---

## 🧪 Step 10: Test Everything

### Test Local Connection to Atlas

```bash
cd bloodsmearimageanalysisproject/project
python test_mongodb_connection.py
```

Should connect to Atlas now!

### Test in MongoDB Compass

Keep both connections saved:
- **Local**: `mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin`
- **Atlas**: `mongodb+srv://bhanu:bhanu123@cluster0.xxxxx.mongodb.net/bloodsmear`

---

## 💡 Benefits of MongoDB Atlas

✅ **Free Forever** - M0 tier (512MB storage)
✅ **Automatic Backups** - Daily snapshots
✅ **Global Access** - Access from anywhere
✅ **Scalable** - Upgrade when needed
✅ **Secure** - Built-in security features
✅ **Works with Vercel** - Perfect for serverless

---

## 🔄 Keeping Both Databases in Sync

### Option 1: Use Atlas for Everything
- Update local app to use Atlas
- Keep local MongoDB as backup

### Option 2: Dual Setup
- Development: Local MongoDB
- Production: MongoDB Atlas
- Use environment variables to switch

---

## 📋 Migration Checklist

- [ ] Export data from local MongoDB
- [ ] Create MongoDB Atlas account
- [ ] Create free M0 cluster
- [ ] Create database user
- [ ] Whitelist IPs (0.0.0.0/0)
- [ ] Get connection string
- [ ] Import data to Atlas
- [ ] Verify all collections
- [ ] Update application code
- [ ] Test connection
- [ ] Deploy to Vercel

---

## 🐛 Troubleshooting

### "Authentication failed"
- Check username/password are correct
- Verify user has read/write permissions

### "Connection timeout"
- Check IP whitelist includes `0.0.0.0/0`
- Verify connection string is correct

### "Database not found"
- Atlas creates database on first write
- Make sure database name is in connection string

### "Cannot connect from Compass"
- Update MongoDB Compass to latest version
- Check internet connection
- Verify connection string format

---

## 📞 Need Help?

- [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com/)
- [MongoDB Compass Guide](https://docs.mongodb.com/compass/)
- [Migration Tools](https://docs.mongodb.com/database-tools/)

---

**Ready to migrate?** Follow the steps above to move your data to MongoDB Atlas! 🚀
