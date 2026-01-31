# 🚀 Quick Deploy to Hugging Face Spaces

**Time**: 20 minutes | **Difficulty**: Easy

---

## Prerequisites

- Hugging Face account (free): https://huggingface.co/join
- Git installed
- OpenSSL or PowerShell (for generating secrets)

---

## Step 1: Generate Secrets (2 minutes)

```bash
# Generate SECRET_KEY
openssl rand -hex 32

# Generate BETTER_AUTH_SECRET
openssl rand -hex 32

# Save both outputs - you'll need them!
```

**Windows PowerShell alternative:**
```powershell
[Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Maximum 256 }))
```

---

## Step 2: Create Hugging Face Space (3 minutes)

1. Go to https://huggingface.co/new-space
2. Fill in:
   - **Space name**: `todo-backend`
   - **License**: MIT
   - **SDK**: **Docker** ⚠️ IMPORTANT!
   - **Hardware**: CPU basic (free)
   - **Visibility**: Public
3. Click **Create Space**

---

## Step 3: Clone and Setup (5 minutes)

```bash
# Clone your new Space
git clone https://huggingface.co/spaces/YOUR_USERNAME/todo-backend
cd todo-backend

# Copy backend files (adjust path to your project)
cp -r /path/to/hackathon_2/backend/* .

# Windows:
# xcopy /E /I D:\mna\hackathon_2\backend .\
```

---

## Step 4: Create README.md (2 minutes)

Create `README.md` in the Space root:

```markdown
---
title: Todo Backend API
emoji: 📝
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# Todo Web Application Backend

FastAPI backend with JWT authentication.

## Endpoints
- Health: https://YOUR_USERNAME-todo-backend.hf.space/health
- API Docs: https://YOUR_USERNAME-todo-backend.hf.space/docs
```

---

## Step 5: Configure Secrets (5 minutes)

1. Go to your Space page
2. Click **Settings** → **Repository secrets**
3. Add these 8 secrets (click "Add a new secret" for each):

| Secret Name | Value | Notes |
|-------------|-------|-------|
| `DATABASE_URL` | Your Neon PostgreSQL URL | Get from https://console.neon.tech |
| `SECRET_KEY` | Output from Step 1 | 64-character hex string |
| `ALGORITHM` | `HS256` | Exactly as shown |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Number only |
| `BETTER_AUTH_SECRET` | Output from Step 1 | 64-character hex string |
| `BETTER_AUTH_URL` | `https://YOUR_USERNAME-todo-backend.hf.space` | Replace YOUR_USERNAME |
| `BACKEND_URL` | `https://YOUR_USERNAME-todo-backend.hf.space` | Replace YOUR_USERNAME |
| `FRONTEND_URL` | `http://localhost:3000` | Update after Vercel deploy |

**⚠️ Replace `YOUR_USERNAME` with your actual Hugging Face username!**

---

## Step 6: Deploy (3 minutes)

```bash
# Add all files
git add .

# Commit
git commit -m "Deploy Todo Backend"

# Push to Hugging Face
git push
```

---

## Step 7: Verify (2 minutes)

Wait 2-5 minutes for build, then test:

```bash
# Replace YOUR_USERNAME with your actual username
curl https://YOUR_USERNAME-todo-backend.hf.space/health
```

**Expected response:**
```json
{"status": "healthy", "version": "1.0.0"}
```

**Your backend is live!** 🎉

---

## 🔗 Your URLs

**Backend API**: `https://YOUR_USERNAME-todo-backend.hf.space`
**API Docs**: `https://YOUR_USERNAME-todo-backend.hf.space/docs`
**Health Check**: `https://YOUR_USERNAME-todo-backend.hf.space/health`

**Save these URLs** - you'll need them for Vercel frontend deployment!

---

## 🐛 Troubleshooting

### Build fails
- Check **Logs** tab in your Space
- Verify `Dockerfile` is in root directory
- Ensure all files copied correctly

### Database connection error
- Verify `DATABASE_URL` is correct in secrets
- Check Neon database allows external connections
- Go to https://console.neon.tech → Settings → Allow connections from anywhere

### Space shows "Building" forever
- Refresh the page
- Check Logs tab for errors
- Verify Docker SDK was selected (not Gradio or Streamlit)

### Can't access API
- Wait 5 minutes for build to complete
- Check Space status shows "Running"
- Verify URL format: `https://username-space-name.hf.space`

---

## 📝 Next Steps

1. ✅ Backend deployed to Hugging Face
2. ⏳ Deploy frontend to Vercel (see Vercel guide)
3. ⏳ Update `FRONTEND_URL` secret with Vercel URL
4. ⏳ Test the full application

---

## 🆘 Need Help?

- **Detailed guide**: `docs/deployment/README_HF_DEPLOYMENT.md`
- **Hugging Face Discord**: https://hf.co/join/discord
- **Check logs**: Space page → Logs tab

---

**Deployment complete!** Your backend is now live on Hugging Face Spaces. 🚀
