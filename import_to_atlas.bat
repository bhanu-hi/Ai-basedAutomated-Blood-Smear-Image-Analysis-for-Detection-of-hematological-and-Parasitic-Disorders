@echo off
echo ========================================
echo MongoDB Atlas Import Script
echo ========================================
echo.
echo IMPORTANT: Update this script with your Atlas connection string!
echo.
set /p ATLAS_URI="Enter your MongoDB Atlas connection string: "
echo.

if "%ATLAS_URI%"=="" (
    echo ERROR: Connection string cannot be empty
    pause
    exit /b 1
)

echo Importing data to MongoDB Atlas...
echo.

echo [1/3] Importing users collection...
mongoimport --uri="%ATLAS_URI%" --collection=users --file=mongodb_exports\users_export.json
if %errorlevel% neq 0 (
    echo ERROR: Failed to import users collection
    pause
    exit /b 1
)
echo ✓ Users imported successfully

echo.
echo [2/3] Importing analyses collection...
mongoimport --uri="%ATLAS_URI%" --collection=analyses --file=mongodb_exports\analyses_export.json
if %errorlevel% neq 0 (
    echo ERROR: Failed to import analyses collection
    pause
    exit /b 1
)
echo ✓ Analyses imported successfully

echo.
echo [3/3] Importing results collection...
mongoimport --uri="%ATLAS_URI%" --collection=results --file=mongodb_exports\results_export.json
if %errorlevel% neq 0 (
    echo ERROR: Failed to import results collection
    pause
    exit /b 1
)
echo ✓ Results imported successfully

echo.
echo ========================================
echo ✓ All data imported to Atlas!
echo ========================================
echo.
echo Your data is now in MongoDB Atlas
echo Ready to deploy to Vercel!
echo.
pause
