import os
import urllib.request
import gdown

def download_model():
    """Download model from Google Drive if it doesn't exist locally"""
    model_dir = os.path.join(os.path.dirname(__file__), 'models')
    model_path = os.path.join(model_dir, 'best_model.pth')
    
    # Create models directory if it doesn't exist
    os.makedirs(model_dir, exist_ok=True)
    
    # Check if model already exists
    if os.path.exists(model_path):
        print(f"Model already exists at {model_path}")
        return model_path
    
    # Google Drive file ID - UPDATE THIS WITH YOUR FILE ID
    # To get file ID: Share the file -> Get link -> Extract ID from URL
    # URL format: https://drive.google.com/file/d/FILE_ID/view
    file_id = os.getenv('MODEL_FILE_ID', 'YOUR_GOOGLE_DRIVE_FILE_ID')
    
    if file_id == 'YOUR_GOOGLE_DRIVE_FILE_ID':
        raise ValueError("Please set MODEL_FILE_ID environment variable with your Google Drive file ID")
    
    print(f"Downloading model from Google Drive...")
    url = f'https://drive.google.com/uc?id={file_id}'
    
    try:
        gdown.download(url, model_path, quiet=False)
        print(f"Model downloaded successfully to {model_path}")
        return model_path
    except Exception as e:
        print(f"Error downloading model: {e}")
        raise

if __name__ == "__main__":
    download_model()
