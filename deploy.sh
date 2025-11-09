#!/bin/bash

# Ensure we're in the right directory
cd "$(dirname "$0")"

# Install dependencies
echo "Installing dependencies..."
npm install

# Build the application
echo "Building the application..."
npm run build

echo "Deployment preparation complete!"
echo "Next steps:"
echo "1. Commit your changes to GitHub"
echo "2. Push to your GitHub repository"
echo "3. Import your repository to Vercel"
echo "4. Configure environment variables in Vercel"
echo "5. Deploy!"
