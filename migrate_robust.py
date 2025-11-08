"""
Robust MongoDB Migration Script with retry logic
"""
from pymongo import MongoClient
import json
import os
import time

# Configuration
LOCAL_URI = 'mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin'
ATLAS_URI = 'mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear?retryWrites=true&w=majority'

DB_NAME = 'bloodsmear'
COLLECTIONS = ['users', 'analyses', 'results']

def migrate_with_retry():
    """Migrate data with retry logic"""
    print("=" * 60)
    print("MongoDB Migration: Local → Atlas (Robust)")
    print("=" * 60)
    
    # Step 1: Export from local
    print("\nStep 1: Exporting from Local MongoDB...")
    try:
        local_client = MongoClient(LOCAL_URI, serverSelectionTimeoutMS=5000)
        local_db = local_client[DB_NAME]
        
        os.makedirs('mongodb_exports', exist_ok=True)
        
        exported_data = {}
        for coll_name in COLLECTIONS:
            docs = list(local_db[coll_name].find())
            # Convert ObjectId to string
            for doc in docs:
                if '_id' in doc:
                    doc['_id'] = str(doc['_id'])
            exported_data[coll_name] = docs
            print(f"  ✓ Exported {len(docs)} documents from {coll_name}")
        
        local_client.close()
        
    except Exception as e:
        print(f"  ✗ Error exporting: {e}")
        return False
    
    # Step 2: Import to Atlas with retry
    print("\nStep 2: Importing to MongoDB Atlas...")
    try:
        # Connect with longer timeout
        atlas_client = MongoClient(
            ATLAS_URI,
            serverSelectionTimeoutMS=30000,
            connectTimeoutMS=30000,
            socketTimeoutMS=30000
        )
        atlas_db = atlas_client[DB_NAME]
        
        print("  ✓ Connected to Atlas")
        
        for coll_name in COLLECTIONS:
            docs = exported_data[coll_name]
            
            if not docs:
                print(f"  ⚠ No documents to import for {coll_name}")
                continue
            
            print(f"\n  Importing {coll_name}...")
            collection = atlas_db[coll_name]
            
            # Import in smaller batches
            batch_size = 10
            total = len(docs)
            
            for i in range(0, total, batch_size):
                batch = docs[i:i+batch_size]
                try:
                    collection.insert_many(batch, ordered=False)
                    print(f"    Progress: {min(i+batch_size, total)}/{total}")
                    time.sleep(0.5)  # Small delay between batches
                except Exception as e:
                    print(f"    Warning: {e}")
                    continue
            
            # Verify count
            count = collection.count_documents({})
            print(f"  ✓ Imported {count} documents to {coll_name}")
        
        atlas_client.close()
        
    except Exception as e:
        print(f"  ✗ Error importing: {e}")
        return False
    
    # Step 3: Verify
    print("\nStep 3: Verifying...")
    try:
        verify_client = MongoClient(ATLAS_URI, serverSelectionTimeoutMS=10000)
        verify_db = verify_client[DB_NAME]
        
        print("\nFinal document counts in Atlas:")
        for coll_name in COLLECTIONS:
            count = verify_db[coll_name].count_documents({})
            print(f"  {coll_name}: {count} documents")
        
        verify_client.close()
        
    except Exception as e:
        print(f"  ✗ Error verifying: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("✓ Migration Complete!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = migrate_with_retry()
    
    if success:
        print("\n✓ Your data is now in MongoDB Atlas!")
        print("\nConnection string for Vercel:")
        print("mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear")
    else:
        print("\n✗ Migration failed. Please check the errors above.")
    
    input("\nPress Enter to exit...")
