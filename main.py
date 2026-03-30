import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

# Change to backend directory to access all modules
os.chdir(os.path.join(os.path.dirname(__file__), 'backend'))

# Import and run the main application
if __name__ == "__main__":
    from main import app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8001)))
