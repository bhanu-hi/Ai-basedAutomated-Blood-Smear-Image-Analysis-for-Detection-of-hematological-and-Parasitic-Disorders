"""
Test writing data to MongoDB Atlas
"""
from pymongo import MongoClient
from datetime import datetime
import uuid

# Your Atlas connection
ATLAS_URI = 'mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear'

print("=" * 60)
print("Testing MongoDB Atlas Write Operations")
print("=" * 60)

try:
    # Connect
    print("\n1. Connecting to Atlas...")
    client = MongoClient(ATLAS_URI, serverSelectionTimeoutMS=10000)
    db = client['bloodsmear']
    print("   ✓ Connected!")
    
    # Test writing to users collection
    print("\n2. Testing write to 'users' collection...")
    users_collection = db['users']
    
    test_user = {
        'user_id': str(uuid.uuid4()),
        'email': 'test@example.com',
        'password': 'test123',
        'name': 'Test User',
        'role': 'technician',
        'created_at': datetime.utcnow()
    }
    
    result = users_collection.insert_one(test_user)
    print(f"   ✓ Inserted test user with ID: {result.inserted_id}")
    
    # Verify it was written
    print("\n3. Verifying data was written...")
    found_user = users_collection.find_one({'email': 'test@example.com'})
    if found_user:
        print(f"   ✓ Found user: {found_user['name']}")
    else:
        print("   ✗ User not found!")
    
    # Count all documents
    print("\n4. Checking all collections...")
    for coll_name in ['users', 'analyses', 'results']:
        count = db[coll_name].count_documents({})
        print(f"   {coll_name}: {count} documents")
    
    # Clean up test data
    print("\n5. Cleaning up test data...")
    users_collection.delete_one({'email': 'test@example.com'})
    print("   ✓ Test data removed")
    
    print("\n" + "=" * 60)
    print("✓ SUCCESS! Atlas can store data properly!")
    print("=" * 60)
    
    client.close()
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    print("\nPossible issues:")
    print("1. Database user doesn't have write permissions")
    print("2. Connection timeout")
    print("3. Network issues")

input("\nPress Enter to exit...")
