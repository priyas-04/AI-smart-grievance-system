# AI Smart Grievance System

A production-ready, AI-driven grievance management platform that automatically routes citizen complaints to the correct government department using NLP and machine learning.

## 🏗️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLite/PostgreSQL** - Database with SQLAlchemy ORM
- **JWT Authentication** - Secure token-based auth
- **AI/ML Integration** - TF-IDF + NMF for text classification
- **Role-based Access Control** - Secure permission system

### Frontend
- **React 18** - Modern UI framework
- **Tailwind CSS** - Utility-first styling
- **React Router** - Client-side routing
- **Axios API** - HTTP client with interceptors
- **Toast Notifications** - User feedback system

## 🧪 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/priyas-04/ai-smart-grievance-system.git
   cd ai-smart-grievance-system
   ```

2. **Local development setup**
   ```bash
   # Backend setup
   cd backend
   pip install -r requirements.txt
   python main.py

   # Frontend setup (new terminal)
   cd frontend
   npm install
   npm run dev
   ```

3. **Access the application**
   - **Frontend**: http://localhost:5173
   - **Backend API**: http://localhost:8001
   - **Default Admin**: admin@resolveai.com / admin123

## 🎯 Key Features

### 🤖 AI-Powered Complaint Routing
- Automatic text classification using TF-IDF
- Topic modeling with NMF for department assignment
- Priority-based routing (high/medium/low)
- Smart keyword extraction and categorization

### 📊 Real-time Dashboard
- Role-based dashboards with live updates
- Interactive complaint tracking
- Performance analytics and reporting
- Department-wise statistics

### 🔐 Security & Performance
- JWT-based authentication with role permissions
- Input validation and sanitization
- Optimized database queries with proper indexing
- Responsive design with mobile support

## 🌐 Deployment

### 📱 Vercel (Frontend)
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy frontend
cd frontend
vercel --prod
```

### 🔧 Railway (Backend)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy backend
cd backend
railway login
railway up
```

**🚀 Production-ready AI Smart Grievance System!**
