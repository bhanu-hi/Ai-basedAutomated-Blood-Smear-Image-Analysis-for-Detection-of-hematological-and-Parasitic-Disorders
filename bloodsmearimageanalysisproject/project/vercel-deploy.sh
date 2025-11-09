#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Vercel deployment..."

# Install Vercel CLI if not installed
if ! command -v vercel &> /dev/null; then
    echo "Installing Vercel CLI..."
    npm install -g vercel
fi

# Login to Vercel (will open browser for authentication)
vercel login

# Set environment variables in Vercel
vercel env add MONGODB_URI production
vercel env add MONGODB_DB_NAME production

# Deploy to production
vercel --prod

echo "✅ Deployment complete! Your app is now live on Vercel."
