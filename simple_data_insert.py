"""
Simple script to insert test data into Atlas
"""
from pymongo import MongoClient
from datetime import datetime
import uuid

# Connection with longer timeout
ATLAS_URI = 'mongodb+srv://tungalabhanuprakash3_db_user:bhanu%40143@cluster0.xpeq7r7.mongodb.net/bloodsmear?retryWrites=true&w=majority'

print("Connecting to MongoDB Atlas...")
print("This may take 30-60 seconds, please wait...")
print("=" * 60)

try:
    # Connect with very long timeout
    client = MongoClient(
        ATLAS_URI,
        serverSelectionTimeoutMS=60000,  # 60 seconds
        connectTimeoutMS=60000,
        socketTimeoutMS=60000
    )
    
    db = client['bloodsmear']
    
    # Test connection
    print("Testing connection...")
    client.admin.command('ping')
    print("✓ Connected successfully!\n")
    
    # Insert test user
    print("Inserting test user...")
    users = db['users']
    
    test_user = {
        'user_id': str(uuid.uuid4()),
        'email': 'testuser@bloodsmear.com',
        'password': 'test123',
        'name': 'Test User',
        'role': 'technician',
        'created_at': datetime.utcnow()
    }
    
    result = users.insert_one(test_user)
    print(f"✓ User inserted! ID: {result.inserted_id}\n")
    
    # Verify
    print("Verifying data...")
    count = users.count_documents({})
    print(f"✓ Total users in database: {count}\n")
    
    # Show all users
    print("All users in database:")
    for user in users.find():
        print(f"  - {user.get('name')} ({user.get('email')})")
    
    print("\n" + "=" * 60)
    print("✓ SUCCESS! Data is being stored in Atlas!")
    print("=" * 60)
    print("\nYou can now:")
    print("1. View this data in MongoDB Compass")
    print("2. Deploy to Vercel")
    print("3. Your app will work with this database")
    
    client.close()
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Check your internet connection")
    print("2. Try running the script again")
    print("3. If it keeps failing, we can deploy to Vercel anyway")
    print("   (The database will work once deployed)")

input("\nPress Enter to exit...")
