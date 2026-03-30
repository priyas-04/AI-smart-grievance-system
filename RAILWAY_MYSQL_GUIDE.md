# 🚀 Railway MySQL Deployment Guide

## ✅ Your MySQL Setup is Correct!

From the image, your setup looks good:
- ✅ **Service Name**: `resolveai-db`
- ✅ **Environment**: MySQL
- ✅ **Plan**: Free

---

## 🔑 Environment Variables You MUST Add

### **Step 1: Get Database URL**
After MySQL service is created:
1. Click on your MySQL service (`resolveai-db`)
2. Go to **"Variables"** tab
3. **Copy the `DATABASE_URL`** (it will look like):
   ```
   mysql://root:password@containers-us-west-xxx.railway.app:7926/railway
   ```

### **Step 2: Add Variables to Web Service**
Go to your **web service** (not database service) and add these:

#### **Database Connection**
```bash
DATABASE_URL=mysql://root:password@containers-us-west-xxx.railway.app:7926/railway
```
*(Copy the exact URL from your MySQL service)*

#### **Application Secrets**
```bash
SECRET_KEY=your-super-secret-production-key-change-this-1714456000
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 🚀 Complete Deployment Steps

### **Step 1: Deploy Web Service**
1. Go to Railway dashboard
2. Click **"New Project"**
3. Connect: `priyas-04/ai-smart-grievance-system`
4. **Don't add database yet** - deploy web service first

### **Step 2: Configure Web Service**
1. **Build Command**: `pip install -r requirements.txt`
2. **Start Command**: `python railway_app.py`
3. **Health Check Path**: `/health`

### **Step 3: Add MySQL Service**
1. In same project, click **"New Service"**
2. Select **"Database"** → **MySQL**
3. **Plan**: Free
4. **Service Name**: `resolveai-db`

### **Step 4: Connect Database to Web Service**
1. Go to your **web service** settings
2. Add environment variables (see above)
3. **Redeploy** the web service

---

## 🔍 Verify MySQL Connection

### **Test Database Connection**
After deployment, test these endpoints:

```bash
# Health check (should show MySQL)
curl https://your-service.railway.app/health

# Expected response:
{
  "status": "healthy",
  "service": "ResolveAI API", 
  "database": "MySQL"
}
```

### **Test API Documentation**
Visit: `https://your-service.railway.app/docs`

---

## 🎯 Expected Railway URLs

After successful deployment:
- **Backend**: `https://ai-smart-grievance-system-production.up.railway.app`
- **API Docs**: `https://ai-smart-grievance-system-production.up.railway.app/docs`
- **Health**: `https://ai-smart-grievance-system-production.up.railway.app/health`

---

## 🚨 Common Issues & Solutions

### **Issue 1: Database Connection Failed**
**Solution**: 
- Verify DATABASE_URL is correct
- Check MySQL service is running
- Ensure variables are added to web service (not database service)

### **Issue 2: Import Errors**
**Solution**:
- All backend files must be in GitHub
- Check railway_app.py has correct imports

### **Issue 3: Build Failed**
**Solution**:
- Use requirements.txt (not simple_requirements.txt)
- Ensure pymysql is in requirements.txt

---

## 📱 Deploy Frontend to Vercel

Once backend works:

### **Vercel Settings**
1. Go to [vercel.com](https://vercel.com)
2. Connect: `priyas-04/ai-smart-grievance-system`
3. Select `frontend` folder
4. Add environment variable:
   ```
   VITE_API_URL=https://your-backend.railway.app
   ```

---

## 🎉 Success Indicators

### ✅ Backend Success
- Web service shows "Running" status
- Health check returns MySQL status
- API documentation accessible
- No errors in logs

### ✅ Frontend Success
- Frontend loads without errors
- Can connect to Railway backend
- Registration/login works
- All features functional

---

## 💡 Railway Advantages

- ✅ **Free MySQL database** included
- ✅ **Automatic SSL certificates**
- ✅ **Easy environment variables**
- ✅ **Built-in logging**
- ✅ **GitHub integration**

---

**🚀 Your MySQL setup is correct! Just add the environment variables and deploy!**
