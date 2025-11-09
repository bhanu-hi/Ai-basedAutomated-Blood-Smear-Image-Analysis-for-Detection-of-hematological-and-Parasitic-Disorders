@echo off
echo ========================================
echo Deploying to Vercel
echo ========================================
echo.

echo Step 1: Adding files to git...
git add .

echo.
echo Step 2: Committing changes...
git commit -m "Fix Vercel serverless deployment - add /api folder and update dependencies"

echo.
echo Step 3: Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo Deployment initiated!
echo ========================================
echo.
echo Vercel will automatically deploy your changes.
echo Check your Vercel dashboard for deployment status.
echo.
pause
