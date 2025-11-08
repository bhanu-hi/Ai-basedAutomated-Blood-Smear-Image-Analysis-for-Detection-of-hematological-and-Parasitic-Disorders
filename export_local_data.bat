@echo off
echo ========================================
echo MongoDB Data Export Script
echo ========================================
echo.
echo Exporting data from local MongoDB...
echo Database: bloodsmear
echo Collections: users, analyses, results
echo.

REM Create exports directory
if not exist "mongodb_exports" mkdir mongodb_exports

echo [1/3] Exporting users collection...
mongoexport --uri="mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin" --collection=users --out=mongodb_exports\users_export.json
if %errorlevel% neq 0 (
    echo ERROR: Failed to export users collection
    pause
    exit /b 1
)
echo ✓ Users exported successfully

echo.
echo [2/3] Exporting analyses collection...
mongoexport --uri="mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin" --collection=analyses --out=mongodb_exports\analyses_export.json
if %errorlevel% neq 0 (
    echo ERROR: Failed to export analyses collection
    pause
    exit /b 1
)
echo ✓ Analyses exported successfully

echo.
echo [3/3] Exporting results collection...
mongoexport --uri="mongodb://bhanu:bhanu123@localhost:27017/bloodsmear?authSource=admin" --collection=results --out=mongodb_exports\results_export.json
if %errorlevel% neq 0 (
    echo ERROR: Failed to export results collection
    pause
    exit /b 1
)
echo ✓ Results exported successfully

echo.
echo ========================================
echo ✓ All data exported successfully!
echo ========================================
echo.
echo Files saved in: mongodb_exports\
echo - users_export.json
echo - analyses_export.json
echo - results_export.json
echo.
echo Next steps:
echo 1. Create MongoDB Atlas account
echo 2. Create free cluster
echo 3. Import these files to Atlas
echo.
echo See MONGODB_MIGRATION.md for detailed instructions
echo.
pause
