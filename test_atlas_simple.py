"""
Simple Atlas connection test
"""
from pymongo import MongoClient

# Your Atlas connection string
ATLAS_URI = 'mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear'

print("Testing MongoDB Atlas connection...")
print("=" * 60)

try:
    # Try to connect
    print("\n1. Connecting to Atlas...")
    client = MongoClient(ATLAS_URI, serverSelectionTimeoutMS=10000)
    
    # Test the connection
    print("2. Testing connection...")
    client.admin.command('ping')
    print("   ✓ Connection successful!")
    
    # Access database
    print("\n3. Accessing database...")
    db = client['bloodsmear']
    
    # List collections
    collections = db.list_collection_names()
    print(f"   ✓ Found {len(collections)} collections: {collections}")
    
    # Count documents
    print("\n4. Document counts:")
    for coll in collections:
        count = db[coll].count_documents({})
        print(f"   - {coll}: {count} documents")
    
    print("\n" + "=" * 60)
    print("✓ SUCCESS! Atlas is working perfectly!")
    print("=" * 60)
    
    client.close()
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    print("\n" + "=" * 60)
    print("Troubleshooting steps:")
    print("1. Wait 2-3 minutes after adding IP to whitelist")
    print("2. Check your internet connection")
    print("3. Verify password is correct: bhanu@143")
    print("4. Try restarting your computer")
    print("=" * 60)

input("\nPress Enter to exit...")
