# 🚀 Deploy Frontend to Vercel

**Backend URL**: https://mnusrulah104-todo-backend.hf.space
**Repository**: https://github.com/mnusrullah104/todo_web_phase2

---

## Step 1: Create Vercel Account (2 minutes)

1. Go to: https://vercel.com/signup
2. Click **"Continue with GitHub"**
3. Authorize Vercel to access your repositories
4. Complete account setup

---

## Step 2: Import Your Repository (3 minutes)

1. Go to: https://vercel.com/new
2. Click **"Import Git Repository"**
3. Find: `mnusrullah104/todo_web_phase2`
4. Click **"Import"**

---

## Step 3: Configure Project Settings (5 minutes)

### Root Directory (IMPORTANT!)
1. Click **"Edit"** next to "Root Directory"
2. Type: `frontend`
3. Click **"Continue"**

### Framework Preset
- Should auto-detect as **"Next.js"**
- Leave as default

### Build Settings
- **Build Command**: `npm run build` (default - leave as is)
- **Output Directory**: `.next` (default - leave as is)
- **Install Command**: `npm install` (default - leave as is)

---

## Step 4: Add Environment Variables (3 minutes)

Click **"Environment Variables"** section and add these **2 variables**:

### Variable 1:
- **Name**: `NEXT_PUBLIC_API_BASE_URL`
- **Value**: `https://mnusrulah104-todo-backend.hf.space`
- **Environments**: Select all (Production, Preview, Development)

### Variable 2:
- **Name**: `NEXT_PUBLIC_BETTER_AUTH_URL`
- **Value**: `https://mnusrulah104-todo-backend.hf.space`
- **Environments**: Select all (Production, Preview, Development)

**⚠️ IMPORTANT**: Both variables use the SAME value (your backend URL)

---

## Step 5: Deploy (2 minutes)

1. Click **"Deploy"**
2. Wait 2-5 minutes for build
3. Vercel will show build progress
4. You'll get a URL like: `https://todo-web-phase2.vercel.app`

**Save your Vercel URL!** You'll need it for the next step.

---

## Step 6: Update Backend CORS (3 minutes)

Now connect your frontend to backend:

1. Go to: https://huggingface.co/spaces/mnusrulah104/todo-backend/settings
2. Scroll to **"Repository secrets"**
3. Find the `FRONTEND_URL` secret
4. Click **"Edit"**
5. Change value from `http://localhost:3000` to your Vercel URL
   - Example: `https://todo-web-phase2.vercel.app`
6. Click **"Update secret"**
7. Wait ~1 minute for HF Space to restart

---

## Step 7: Verify Deployment (2 minutes)

### Test Frontend
1. Visit your Vercel URL
2. You should see the landing page
3. Open browser DevTools (F12) → Console tab
4. Should see NO CORS errors

### Test Full Flow
1. Click **"Sign Up"**
2. Create a test account (email: test@example.com, password: Test123!)
3. Should redirect to dashboard
4. Try creating a task
5. Task should appear in the list

---

## ✅ Success Checklist

- [ ] Vercel account created
- [ ] Repository imported
- [ ] Root directory set to `frontend`
- [ ] 2 environment variables configured
- [ ] Deployment successful
- [ ] Frontend loads without errors
- [ ] Backend CORS updated with Vercel URL
- [ ] Sign up works
- [ ] Login works
- [ ] Tasks can be created
- [ ] No CORS errors in console

---

## 🔗 Your Live URLs

After deployment:

**Frontend**: `https://your-project-name.vercel.app`
**Backend**: `https://mnusrulah104-todo-backend.hf.space`
**API Docs**: `https://mnusrulah104-todo-backend.hf.space/docs`

---

## 🐛 Troubleshooting

### Build fails on Vercel
**Check:**
- Root directory is set to `frontend`
- `package.json` exists in frontend folder
- View build logs for specific error

**Fix:**
- Go to Project Settings → General → Root Directory
- Ensure it says `frontend`
- Redeploy

### CORS errors in browser console
```
Access to fetch at 'https://mnusrulah104-todo-backend.hf.space/api/...'
from origin 'https://your-app.vercel.app' has been blocked by CORS policy
```

**Fix:**
1. Verify `FRONTEND_URL` in HF Space matches Vercel URL exactly
2. Include `https://` in the URL
3. Wait for HF Space to restart (check Logs tab)
4. Refresh your Vercel app

### Environment variables not working
**Fix:**
1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Verify both variables are set correctly
3. Go to Deployments tab
4. Click latest deployment → "..." menu → "Redeploy"
5. Environment variables only take effect after redeployment

### Can't sign up or login
**Check:**
1. Browser console for errors
2. Network tab in DevTools for failed requests
3. Backend health: https://mnusrulah104-todo-backend.hf.space/health
4. Backend is running (HF Space shows "Running")

**Fix:**
- Verify environment variables are correct
- Check backend logs in HF Space
- Test backend API directly in browser

### Authentication not persisting
**Check:**
- Browser localStorage (DevTools → Application → Local Storage)
- Should see `token` key with JWT value

**Fix:**
- Clear browser cache and cookies
- Try in incognito/private window
- Check browser console for errors

---

## 🔄 Automatic Deployments

Vercel automatically deploys when you push to GitHub:

- **Push to `main` branch** → Production deployment
- **Push to other branches** → Preview deployment
- **Pull requests** → Preview deployment with unique URL

---

## 🎨 Optional: Custom Domain

After deployment, you can add a custom domain:

1. Go to Project Settings → Domains
2. Click **"Add"**
3. Enter your domain (e.g., `todo.yourdomain.com`)
4. Follow DNS configuration instructions
5. Vercel provides free SSL certificate

**After adding custom domain:**
- Update `FRONTEND_URL` in HF Space to include custom domain
- Can have multiple URLs: `https://your-app.vercel.app,https://todo.yourdomain.com`

---

## 📊 Optional: Enable Analytics

1. Go to Project Settings → Analytics
2. Enable **Vercel Analytics** (free)
3. View real-time visitor data
4. Track Web Vitals (performance metrics)

---

## 🎉 Deployment Complete!

Your full-stack Todo application is now live:

- ✅ **Backend**: Hugging Face Spaces
- ✅ **Frontend**: Vercel
- ✅ **Database**: Neon PostgreSQL
- ✅ **CORS**: Configured
- ✅ **HTTPS**: Automatic (both platforms)

**Share your app**: Send your Vercel URL to users!

---

## 📝 Next Steps

1. Test all features thoroughly
2. Share your app URL
3. Monitor logs and analytics
4. Consider adding custom domain
5. Set up error tracking (optional - Sentry)

---

**Your frontend URL**: `https://your-project-name.vercel.app`
**Your backend URL**: `https://mnusrulah104-todo-backend.hf.space`
