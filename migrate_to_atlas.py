"""
MongoDB Migration Script: Local → Atlas
Exports data from local MongoDB and imports to Atlas
"""

from pymongo import MongoClient
import json
import os
from datetime import datetime
from urllib.parse import quote_plus

# Configuration
LOCAL_URI = 'mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin'
ATLAS_URI = 'mongodb+srv://tungalabhanuprakash3_db_user:<db_password>@cluster0.xpeq7r7.mongodb.net/bloodsmear'

# Update this with your actual password!
ATLAS_PASSWORD = input("Enter your MongoDB Atlas password: ")
# URL encode the password to handle special characters
ATLAS_PASSWORD_ENCODED = quote_plus(ATLAS_PASSWORD)
ATLAS_URI = ATLAS_URI.replace('<db_password>', ATLAS_PASSWORD_ENCODED)

DB_NAME = 'bloodsmear'
COLLECTIONS = ['users', 'analyses', 'results']

def export_local_data():
    """Export data from local MongoDB"""
    print("=" * 60)
    print("Step 1: Exporting from Local MongoDB")
    print("=" * 60)
    
    try:
        client = MongoClient(LOCAL_URI)
        db = client[DB_NAME]
        
        # Create export directory
        os.makedirs('mongodb_exports', exist_ok=True)
        
        for collection_name in COLLECTIONS:
            print(f"\nExporting {collection_name}...")
            collection = db[collection_name]
            
            # Get all documents
            documents = list(collection.find())
            count = len(documents)
            
            # Convert ObjectId to string for JSON serialization
            for doc in documents:
                if '_id' in doc:
                    doc['_id'] = str(doc['_id'])
            
            # Save to JSON file
            filename = f'mongodb_exports/{collection_name}_export.json'
            with open(filename, 'w') as f:
                json.dump(documents, f, indent=2, default=str)
            
            print(f"✓ Exported {count} documents from {collection_name}")
            print(f"  Saved to: {filename}")
        
        client.close()
        print("\n✓ Local export completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error exporting local data: {e}")
        return False

def import_to_atlas():
    """Import data to MongoDB Atlas"""
    print("\n" + "=" * 60)
    print("Step 2: Importing to MongoDB Atlas")
    print("=" * 60)
    
    try:
        client = MongoClient(ATLAS_URI)
        db = client[DB_NAME]
        
        print(f"\n✓ Connected to Atlas: {DB_NAME}")
        
        for collection_name in COLLECTIONS:
            print(f"\nImporting {collection_name}...")
            collection = db[collection_name]
            
            # Read JSON file
            filename = f'mongodb_exports/{collection_name}_export.json'
            
            if not os.path.exists(filename):
                print(f"  ⚠ File not found: {filename}")
                continue
            
            with open(filename, 'r') as f:
                documents = json.load(f)
            
            if not documents:
                print(f"  ⚠ No documents to import for {collection_name}")
                continue
            
            # Clear existing data (optional)
            # collection.delete_many({})
            
            # Insert documents
            if documents:
                collection.insert_many(documents)
                print(f"✓ Imported {len(documents)} documents to {collection_name}")
        
        client.close()
        print("\n✓ Atlas import completed successfully!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error importing to Atlas: {e}")
        print("\nTroubleshooting:")
        print("1. Check your password is correct")
        print("2. Verify IP whitelist includes 0.0.0.0/0")
        print("3. Ensure database user has read/write permissions")
        return False

def verify_migration():
    """Verify data in Atlas"""
    print("\n" + "=" * 60)
    print("Step 3: Verifying Migration")
    print("=" * 60)
    
    try:
        client = MongoClient(ATLAS_URI)
        db = client[DB_NAME]
        
        print("\nDocument counts in Atlas:")
        for collection_name in COLLECTIONS:
            count = db[collection_name].count_documents({})
            print(f"  {collection_name}: {count} documents")
        
        client.close()
        print("\n✓ Verification completed!")
        return True
        
    except Exception as e:
        print(f"\n✗ Error verifying: {e}")
        return False

def main():
    print("=" * 60)
    print("MongoDB Migration: Local → Atlas")
    print("=" * 60)
    print(f"\nSource: Local MongoDB (localhost:27017)")
    print(f"Target: MongoDB Atlas")
    print(f"Database: {DB_NAME}")
    print(f"Collections: {', '.join(COLLECTIONS)}")
    print("\n" + "=" * 60)
    
    # Step 1: Export from local
    if not export_local_data():
        print("\n✗ Migration failed at export stage")
        return
    
    # Step 2: Import to Atlas
    if not import_to_atlas():
        print("\n✗ Migration failed at import stage")
        return
    
    # Step 3: Verify
    verify_migration()
    
    print("\n" + "=" * 60)
    print("✓ Migration Complete!")
    print("=" * 60)
    print("\nYour data is now in MongoDB Atlas!")
    print("\nNext steps:")
    print("1. Test connection in MongoDB Compass")
    print("2. Add connection string to Vercel:")
    print(f"   MONGO_URI={ATLAS_URI.replace(ATLAS_PASSWORD, '***')}")
    print("3. Deploy to Vercel!")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
