# 🔧 Render Deployment Troubleshooting

## 🚨 Common Errors & Solutions

### Error 1: "Could not open requirements file"
**✅ FIXED**: Created `requirements.txt` in root directory

### Error 2: "ModuleNotFoundError" or "ImportError"
**✅ FIXED**: Created `app.py` with proper path handling and error catching

### Error 3: "Build failed" during deployment
**✅ FIXED**: Updated `render.yaml` to use `app.py` instead of `main.py`

---

## 🔍 Debug Steps

### 1. Check Build Logs
In Render dashboard:
- Go to your service → "Logs" tab
- Look for specific error messages
- Check if all dependencies installed correctly

### 2. Verify Files
Make sure these files exist in your repository:
- ✅ `requirements.txt` (root directory)
- ✅ `app.py` (root directory)
- ✅ `render.yaml` (root directory)
- ✅ `backend/` folder with all modules

### 3. Test Locally
```bash
# Test the app.py locally
python app.py

# Check if it starts without errors
curl http://localhost:8001/health
```

---

## 🚀 Re-deployment Steps

### Step 1: Clean Deploy
1. Go to Render dashboard
2. Delete the failed service
3. Create a new web service

### Step 2: Correct Configuration
1. Connect: `priyas-04/ai-smart-grievance-system`
2. Environment: Python 3
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python app.py`
5. Health Check Path: `/health`

### Step 3: Environment Variables
Render will automatically set:
- `DATABASE_URL` (from PostgreSQL)
- `SECRET_KEY`
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`

---

## 🎯 Expected Success Indicators

### Build Success
- ✅ "Build succeeded" message
- ✅ All dependencies installed
- ✅ No import errors

### Service Running
- ✅ "Live" status in dashboard
- ✅ Health check passes
- ✅ Service URL accessible

### Test Endpoints
```bash
# Test health endpoint
curl https://your-service.onrender.com/health

# Expected response:
{"status": "healthy", "service": "ResolveAI API"}
```

---

## 🆘 If Still Failing

### Option 1: Manual Debug
1. Check Render logs for exact error
2. Verify all files are pushed to GitHub
3. Test `app.py` locally

### Option 2: Simplified Deployment
Create a minimal test app:
```python
# test_app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Test app working"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

### Option 3: Alternative Platforms
If Render still fails, try:
- **Railway** (similar to Render)
- **Heroku** (well-established)
- **DigitalOcean** (paid option)

---

## 📞 Get Help

1. **Render Docs**: https://render.com/docs
2. **GitHub Issues**: Check repository issues
3. **Logs**: Always check Render logs first

---

## 🎉 Success Checklist

When deployment succeeds:
- ✅ Service shows "Live" status
- ✅ Health check endpoint works
- ✅ API documentation accessible at `/docs`
- ✅ Frontend can connect to backend
- ✅ All features working correctly

**🚀 Your AI Smart Grievance System will be live!**
