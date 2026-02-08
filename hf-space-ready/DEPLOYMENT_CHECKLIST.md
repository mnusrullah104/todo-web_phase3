# Hugging Face Deployment Checklist

## ✅ Pre-Deployment Steps

### 1. Environment Variables Configuration
Set these in Hugging Face Space Settings → Repository secrets:

```bash
DATABASE_URL=postgresql://user:password@host:port/database?sslmode=require
SECRET_KEY=your-super-secret-key-min-32-characters
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
BETTER_AUTH_SECRET=your-better-auth-secret
BETTER_AUTH_URL=https://your-space.hf.space
BACKEND_URL=https://your-space.hf.space
FRONTEND_URL=https://your-frontend-url.vercel.app,http://localhost:3000
```

**CRITICAL**: Make sure `DATABASE_URL` is correct and accessible from Hugging Face servers.

### 2. Database Setup
The application will automatically create tables on startup, but verify:
- PostgreSQL database is accessible
- Database credentials are correct
- SSL mode is properly configured
- Connection pooling settings are appropriate

### 3. CORS Configuration
Ensure `FRONTEND_URL` includes:
- Production frontend URL (e.g., Vercel deployment)
- Local development URLs for testing
- Multiple URLs separated by commas

### 4. Frontend Configuration
Update frontend `.env.local`:
```bash
NEXT_PUBLIC_API_BASE_URL=https://mnusrulah104-todo-app.hf.space
```

## 🔍 Post-Deployment Verification

### 1. Health Check
```bash
curl https://your-space.hf.space/health
```
Expected response:
```json
{"status": "healthy", "version": "1.0.0"}
```

### 2. API Documentation
Visit: `https://your-space.hf.space/docs`
- Verify all endpoints are listed
- Test authentication endpoints

### 3. Database Connection
Check logs for:
```
INFO: Connecting to database...
INFO: Database engine created successfully
INFO: Creating database tables...
INFO: Database tables created successfully!
```

### 4. Test Authentication Flow

#### Register a new user:
```bash
curl -X POST https://your-space.hf.space/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "testpass123"}'
```

Expected response:
```json
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "user": {"id": "...", "email": "test@example.com"}
}
```

#### Login:
```bash
curl -X POST https://your-space.hf.space/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "testpass123"}'
```

## 🐛 Troubleshooting

### 500 Internal Server Error

**Check logs for:**
1. Database connection errors
   - Solution: Verify `DATABASE_URL` is correct
   - Ensure database is accessible from Hugging Face IPs

2. Missing environment variables
   - Solution: Set all required variables in Space settings

3. Table creation failures
   - Solution: Check database permissions
   - Manually run `init_db.py` if needed

4. Password hashing errors
   - Solution: Verify `passlib[bcrypt]` is installed

### CORS Errors

**Symptoms:** Frontend can't connect to backend

**Solutions:**
1. Add frontend URL to `FRONTEND_URL` environment variable
2. Verify CORS middleware is configured correctly
3. Check browser console for specific CORS error messages

### Authentication Failures

**Check:**
1. JWT secret key is set correctly
2. Token expiration settings
3. Password hashing is working (check logs)

## 📊 Monitoring

### Key Metrics to Watch
1. Response times for auth endpoints
2. Database connection pool usage
3. Error rates in logs
4. Token generation/validation success rates

### Log Patterns to Monitor
- `Login attempt for email:` - Track login attempts
- `User logged in successfully:` - Successful logins
- `Login failed:` - Failed login attempts
- `Registration attempt for email:` - New user registrations
- `Database session error:` - Database issues

## 🔒 Security Checklist

- [ ] `SECRET_KEY` is strong and unique (min 32 characters)
- [ ] `DATABASE_URL` contains credentials - stored as secret
- [ ] CORS is configured with specific origins (not `*`)
- [ ] Password minimum length enforced (6+ characters)
- [ ] JWT tokens have reasonable expiration time
- [ ] Database uses SSL connection
- [ ] No sensitive data in logs

## 🚀 Deployment Commands

### Deploy to Hugging Face
```bash
# From project root
cd hf-space-ready

# Verify all files are present
ls -la

# Push to Hugging Face Space repository
git add .
git commit -m "Deploy backend with auth fixes"
git push
```

### Monitor Deployment
1. Go to Space settings
2. Check "Logs" tab for startup messages
3. Verify no errors during initialization
4. Test health endpoint

## 📝 Common Issues and Solutions

### Issue: "Table does not exist"
**Solution:** Database tables are now created automatically on startup. Check logs for table creation messages.

### Issue: "Could not validate credentials"
**Solution:**
1. Verify JWT secret key matches between registration and login
2. Check token format in Authorization header: `Bearer <token>`
3. Ensure token hasn't expired

### Issue: "Email already registered"
**Solution:** This is expected behavior. Use a different email or login with existing credentials.

### Issue: Database connection timeout
**Solution:**
1. Verify database is running and accessible
2. Check connection string format
3. Ensure SSL mode is correct for your database provider
4. Check if database allows connections from Hugging Face IPs
