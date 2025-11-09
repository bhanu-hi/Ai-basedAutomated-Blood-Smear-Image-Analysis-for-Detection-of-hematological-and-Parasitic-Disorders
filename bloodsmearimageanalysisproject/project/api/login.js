const { MongoClient } = require('mongodb');
const bcrypt = require('bcryptjs');

const MONGODB_URI = process.env.MONGODB_URI;
const DB_NAME = process.env.MONGODB_DB_NAME || 'bloodsmear';

let cachedDb = null;

async function connectToDatabase() {
    if (cachedDb) {
        return cachedDb;
    }
    
    const client = await MongoClient.connect(MONGODB_URI, {
        useUnifiedTopology: true
    });
    
    cachedDb = client.db(DB_NAME);
    return cachedDb;
}

module.exports = async (req, res) => {
    // Enable CORS
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    
    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }
    
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }
    
    try {
        const { email, password } = req.body;
        
        const db = await connectToDatabase();
        
        // Find user
        const user = await db.collection('users').findOne({ email });
        if (!user) {
            return res.json({ error: 'Invalid credentials' });
        }
        
        // Verify password
        const validPassword = await bcrypt.compare(password, user.password);
        if (!validPassword) {
            return res.json({ error: 'Invalid credentials' });
        }
        
        const userData = {
            user_id: user._id.toString(),
            email: user.email,
            full_name: user.full_name,
            role: user.role
        };
        
        res.json({ user: userData });
    } catch (error) {
        console.error('Login error:', error);
        res.status(500).json({ error: 'Login failed' });
    }
};
