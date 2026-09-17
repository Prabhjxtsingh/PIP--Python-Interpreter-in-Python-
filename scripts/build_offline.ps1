# Navigate to frontend and build
Write-Host "Building React Frontend..."
cd frontend
npm run build
cd ..

# Ensure static dir exists in offline-app
Write-Host "Copying build to offline-app static directory..."
if (Test-Path offline-app\static) {
    Remove-Item -Recurse -Force offline-app\static
}
Copy-Item -Recurse frontend\dist offline-app\static

# Run PyInstaller
Write-Host "Running PyInstaller..."
cd offline-app
.\venv\Scripts\activate
pyinstaller --noconfirm --onedir --windowed --add-data "static;static" app.py

Write-Host "Build complete! Executable is located in offline-app\dist\app\app.exe"
