---
title: Todo Backend API
emoji: 📝
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# Todo Web Application Backend

FastAPI backend with JWT authentication for the Todo Web Application.

## 🚀 Live Endpoints

- **Health Check**: https://mnusrulah104-todo-backend.hf.space/health
- **API Documentation**: https://mnusrulah104-todo-backend.hf.space/docs
- **ReDoc**: https://mnusrulah104-todo-backend.hf.space/redoc

## 🔧 Features

- User registration and authentication
- JWT token-based security
- Task CRUD operations
- PostgreSQL database integration
- CORS configured for frontend
- **Automatic database initialization on startup**
- **Comprehensive error logging and handling**
- **Robust error recovery**

## 📊 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user

### Tasks
- `GET /api/{user_id}/tasks` - Get all tasks
- `POST /api/{user_id}/tasks` - Create task
- `GET /api/{user_id}/tasks/{task_id}` - Get specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Toggle completion

### System
- `GET /` - Welcome message
- `GET /health` - Health check

## 🔒 Environment Variables

Configure these in Space Settings → Repository secrets:

- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - JWT signing key (min 32 characters)
- `ALGORITHM` - JWT algorithm (HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiry time (default: 30)
- `BETTER_AUTH_SECRET` - Auth service secret
- `BETTER_AUTH_URL` - Backend URL
- `BACKEND_URL` - Backend URL
- `FRONTEND_URL` - Frontend URL for CORS (comma-separated for multiple)

**Example:**
```bash
DATABASE_URL=postgresql://user:pass@host:port/db?sslmode=require
SECRET_KEY=your-super-secret-key-min-32-characters
FRONTEND_URL=https://your-app.vercel.app,http://localhost:3000
```

## 🚀 Deployment

### Quick Start

1. **Configure Environment Variables** in Space Settings → Repository secrets
2. **Push Code** to Hugging Face Space
3. **Verify Deployment** using the verification script:
   ```bash
   python verify_deployment.py
   ```

### Troubleshooting

If you encounter authentication errors (500 status):
- Check `QUICK_FIX_GUIDE.md` for detailed troubleshooting steps
- Review `DEPLOYMENT_CHECKLIST.md` for complete deployment guide
- Check Space logs for specific error messages

### Key Features

✅ **Automatic Database Initialization** - Tables are created on startup
✅ **Comprehensive Error Logging** - All errors are logged with details
✅ **Robust Error Handling** - Graceful error handling for all endpoints
✅ **CORS Configuration** - Supports multiple frontend origins

## 📚 Documentation

- `QUICK_FIX_GUIDE.md` - Quick troubleshooting guide for common issues
- `DEPLOYMENT_CHECKLIST.md` - Complete deployment checklist
- `verify_deployment.py` - Automated deployment verification script

## 🌐 Frontend

Frontend deployed on Vercel: [Link to be added]

## 📝 Repository

GitHub: https://github.com/mnusrullah104/todo_web_phase2

## 🛠️ Tech Stack

- FastAPI
- PostgreSQL (Neon)
- SQLModel
- JWT Authentication
- Python 3.13
- Uvicorn
- Docker

## 🔍 Recent Updates

### Authentication Fix (Latest)
- Added automatic database table creation on startup
- Implemented comprehensive error handling and logging
- Enhanced CORS configuration for better frontend compatibility
- Added deployment verification tools
