"""
Quick script to check MongoDB Atlas data
"""
from pymongo import MongoClient
from urllib.parse import quote_plus

# Your Atlas connection
ATLAS_URI = 'mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear'
DB_NAME = 'bloodsmear'

print("=" * 60)
print("Checking MongoDB Atlas Database")
print("=" * 60)

try:
    # Connect to Atlas
    client = MongoClient(ATLAS_URI)
    db = client[DB_NAME]
    
    print(f"\n✓ Connected to Atlas!")
    print(f"Database: {DB_NAME}")
    
    # List all collections
    collections = db.list_collection_names()
    print(f"\nCollections found: {len(collections)}")
    
    if not collections:
        print("\n⚠ No collections found in database")
        print("You may need to run the migration script first.")
    else:
        print("\nDocument counts:")
        print("-" * 40)
        
        for collection_name in collections:
            count = db[collection_name].count_documents({})
            print(f"  {collection_name}: {count} documents")
            
            # Show sample document
            if count > 0:
                sample = db[collection_name].find_one()
                print(f"    Sample fields: {list(sample.keys())[:5]}")
        
        print("\n" + "=" * 60)
        print("✓ Your data is in Atlas!")
        print("=" * 60)
        
        print("\nTo view in browser:")
        print("1. Go to: https://cloud.mongodb.com/")
        print("2. Click 'Database' → 'Browse Collections'")
        print("3. Select 'bloodsmear' database")
    
    client.close()
    
except Exception as e:
    print(f"\n✗ Error connecting to Atlas: {e}")
    print("\nTroubleshooting:")
    print("1. Check your internet connection")
    print("2. Verify IP whitelist includes 0.0.0.0/0")
    print("3. Check username/password are correct")
    print("4. Make sure cluster is running")

print("\n" + "=" * 60)
input("Press Enter to exit...")
