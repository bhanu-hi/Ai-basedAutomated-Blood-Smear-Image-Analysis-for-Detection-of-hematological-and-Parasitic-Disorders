// MongoDB User Setup Script
// This script creates the required user for the Blood Smear Analysis application

// Connect to admin database
db = db.getSiblingDB('admin');

// Create user with credentials
db.createUser({
  user: "bhanu",
  pwd: "bhanu123",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" },
    { role: "dbAdminAnyDatabase", db: "admin" }
  ]
});

print("✅ User 'bhanu' created successfully!");

// Switch to bloodsmear database
db = db.getSiblingDB('bloodsmear');

// Create collections
db.createCollection('users');
db.createCollection('analyses');
db.createCollection('results');

print("✅ Database 'bloodsmear' and collections created!");
print("\n📋 Connection String:");
print("mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin");
