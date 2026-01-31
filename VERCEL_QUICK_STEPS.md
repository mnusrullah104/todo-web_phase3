# ⚡ Quick Vercel Deployment - Copy & Paste Guide

**Backend URL**: https://mnusrulah104-todo-backend.hf.space

---

## 🚀 Deploy in 7 Steps

### Step 1: Create Account
Go to: https://vercel.com/signup
Click: **"Continue with GitHub"**

---

### Step 2: Import Repository
Go to: https://vercel.com/new
Select: `mnusrullah104/todo_web_phase2`
Click: **"Import"**

---

### Step 3: Set Root Directory
Click: **"Edit"** next to Root Directory
Type: `frontend`
Click: **"Continue"**

---

### Step 4: Add Environment Variables

Add these 2 variables:

**Variable 1:**
```
Name: NEXT_PUBLIC_API_BASE_URL
Value: https://mnusrulah104-todo-backend.hf.space
Environments: All (Production, Preview, Development)
```

**Variable 2:**
```
Name: NEXT_PUBLIC_BETTER_AUTH_URL
Value: https://mnusrulah104-todo-backend.hf.space
Environments: All (Production, Preview, Development)
```

---

### Step 5: Deploy
Click: **"Deploy"**
Wait: 2-5 minutes

---

### Step 6: Update Backend CORS

1. Go to: https://huggingface.co/spaces/mnusrulah104/todo-backend/settings
2. Find: `FRONTEND_URL` secret
3. Click: **"Edit"**
4. Change to: Your Vercel URL (e.g., `https://todo-web-phase2.vercel.app`)
5. Click: **"Update secret"**

---

### Step 7: Test

Visit your Vercel URL and test:
- [ ] Landing page loads
- [ ] Sign up works
- [ ] Login works
- [ ] Create task works
- [ ] No CORS errors in console (F12)

---

## ✅ Done!

**Frontend**: Your Vercel URL
**Backend**: https://mnusrulah104-todo-backend.hf.space

---

## 🐛 Quick Fixes

**CORS errors?**
- Update `FRONTEND_URL` in HF Space settings
- Wait 1 minute for restart

**Build fails?**
- Check root directory is `frontend`
- View build logs in Vercel

**Env vars not working?**
- Redeploy from Vercel dashboard

---

**Need detailed help?** See `DEPLOY_VERCEL_NOW.md`
