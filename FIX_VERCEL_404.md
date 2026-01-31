# 🔧 FIX: Vercel 404 NOT_FOUND Error

**Error**: 404: NOT_FOUND when accessing http://todo-web-phase2.vercel.app/

---

## 🎯 Most Likely Cause

The **root directory** is not set to `frontend`. Vercel is trying to build from the project root instead of the frontend folder.

---

## ✅ SOLUTION - Fix Root Directory

### Step 1: Go to Project Settings

1. Go to: https://vercel.com/dashboard
2. Click on your project: `todo-web-phase2`
3. Click **"Settings"** tab

### Step 2: Update Root Directory

1. In Settings, click **"General"** (left sidebar)
2. Scroll down to **"Root Directory"**
3. Click **"Edit"**
4. Type: `frontend`
5. Click **"Save"**

### Step 3: Redeploy

1. Go to **"Deployments"** tab
2. Click on the latest deployment
3. Click the **"..."** menu (three dots)
4. Click **"Redeploy"**
5. Wait 2-5 minutes for new build

---

## 🔍 Verify Root Directory is Correct

Before redeploying, check:

1. Go to Project Settings → General
2. Look for **"Root Directory"** section
3. Should show: `frontend`
4. If it shows: `.` or is empty → **This is the problem!**

---

## 📊 Alternative: Check Build Logs

If root directory is already set correctly:

1. Go to **"Deployments"** tab
2. Click on the failed deployment
3. Click **"Building"** to see build logs
4. Look for errors like:
   - `Error: Cannot find module 'next'`
   - `Error: No such file or directory`
   - `package.json not found`

**If you see these errors**: Root directory is wrong.

---

## 🚀 Complete Fix Steps

### Option A: Fix via Dashboard (Recommended)

```
1. Vercel Dashboard → Your Project
2. Settings → General → Root Directory
3. Edit → Type "frontend" → Save
4. Deployments → Latest → ... → Redeploy
```

### Option B: Redeploy from Scratch

If Option A doesn't work:

1. Go to Project Settings
2. Scroll to bottom → **"Delete Project"**
3. Confirm deletion
4. Go to https://vercel.com/new
5. Import `mnusrullah104/todo_web_phase2` again
6. **IMPORTANT**: Set Root Directory to `frontend` BEFORE deploying
7. Add environment variables
8. Deploy

---

## ✅ After Fix - Verify

Once redeployed, test:

1. Visit: http://todo-web-phase2.vercel.app/
2. Should see the landing page (not 404)
3. Check browser console (F12) - no errors
4. Try signing up

---

## 🐛 If Still Getting 404

### Check 1: Verify Frontend Files Exist

```bash
# In your project directory
cd D:\mna\hackathon_2
ls frontend/

# Should see:
# - package.json
# - next.config.js
# - src/
# - public/
```

### Check 2: Verify package.json

```bash
cat frontend/package.json
```

Should contain:
```json
{
  "name": "todo-frontend",
  "scripts": {
    "dev": "next dev -p 3000",
    "build": "next build",
    "start": "next start -p 3000"
  }
}
```

### Check 3: Test Local Build

```bash
cd frontend
npm install
npm run build
```

If this fails locally, fix the errors before deploying to Vercel.

---

## 📝 Correct Vercel Configuration

Your project should have:

**Root Directory**: `frontend`
**Framework Preset**: Next.js
**Build Command**: `npm run build`
**Output Directory**: `.next`
**Install Command**: `npm install`

**Environment Variables**:
- `NEXT_PUBLIC_API_BASE_URL` = `https://mnusrulah104-todo-backend.hf.space`
- `NEXT_PUBLIC_BETTER_AUTH_URL` = `https://mnusrulah104-todo-backend.hf.space`

---

## 🎯 Quick Fix Checklist

- [ ] Root directory set to `frontend`
- [ ] Environment variables added (2 variables)
- [ ] Redeployed after changing settings
- [ ] Build completed successfully (check logs)
- [ ] Landing page loads (not 404)

---

## 📞 Still Having Issues?

### Get Build Logs

1. Vercel Dashboard → Deployments
2. Click failed deployment
3. Copy build logs
4. Look for specific error messages

### Common Error Messages

**"Cannot find module 'next'"**
→ Root directory is wrong

**"package.json not found"**
→ Root directory is wrong

**"Build failed"**
→ Check build logs for specific error

---

## ✅ Expected Result

After fix:
- ✅ http://todo-web-phase2.vercel.app/ shows landing page
- ✅ No 404 error
- ✅ Build logs show "Build Completed"
- ✅ Deployment status shows "Ready"

---

**Most likely fix**: Set Root Directory to `frontend` and redeploy.

Let me know if you need help with any of these steps!
