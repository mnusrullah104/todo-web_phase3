"""
Deployment verification script for Hugging Face Space.
Run this script to verify the backend is working correctly.
"""
import requests
import sys
import json

# Configuration
BASE_URL = "https://mnusrulah104-todo-app.hf.space"
TEST_EMAIL = "test_user@example.com"
TEST_PASSWORD = "testpass123"

def print_status(message, success=True):
    """Print colored status message"""
    symbol = "✅" if success else "❌"
    print(f"{symbol} {message}")

def test_health_check():
    """Test the health endpoint"""
    print("\n1. Testing Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print_status(f"Health check passed: {data}")
            return True
        else:
            print_status(f"Health check failed with status {response.status_code}", False)
            return False
    except Exception as e:
        print_status(f"Health check error: {str(e)}", False)
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    print("\n2. Testing Root Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print_status(f"Root endpoint passed: {data}")
            return True
        else:
            print_status(f"Root endpoint failed with status {response.status_code}", False)
            return False
    except Exception as e:
        print_status(f"Root endpoint error: {str(e)}", False)
        return False

def test_api_docs():
    """Test API documentation endpoint"""
    print("\n3. Testing API Documentation...")
    try:
        response = requests.get(f"{BASE_URL}/docs", timeout=10)
        if response.status_code == 200:
            print_status("API documentation is accessible")
            print(f"   Visit: {BASE_URL}/docs")
            return True
        else:
            print_status(f"API docs failed with status {response.status_code}", False)
            return False
    except Exception as e:
        print_status(f"API docs error: {str(e)}", False)
        return False

def test_registration():
    """Test user registration"""
    print("\n4. Testing User Registration...")
    try:
        payload = {
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
        response = requests.post(
            f"{BASE_URL}/api/auth/register",
            json=payload,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            print_status("Registration successful")
            print(f"   User ID: {data.get('user', {}).get('id')}")
            print(f"   Email: {data.get('user', {}).get('email')}")
            print(f"   Token received: {data.get('access_token')[:20]}...")
            return True, data.get('access_token')
        elif response.status_code == 400:
            # User might already exist
            print_status("User already exists (expected if running multiple times)")
            return True, None
        else:
            print_status(f"Registration failed with status {response.status_code}", False)
            print(f"   Response: {response.text}")
            return False, None
    except Exception as e:
        print_status(f"Registration error: {str(e)}", False)
        return False, None

def test_login():
    """Test user login"""
    print("\n5. Testing User Login...")
    try:
        payload = {
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
        response = requests.post(
            f"{BASE_URL}/api/auth/login",
            json=payload,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            print_status("Login successful")
            print(f"   User ID: {data.get('user', {}).get('id')}")
            print(f"   Email: {data.get('user', {}).get('email')}")
            print(f"   Token received: {data.get('access_token')[:20]}...")
            return True, data.get('access_token')
        else:
            print_status(f"Login failed with status {response.status_code}", False)
            print(f"   Response: {response.text}")
            return False, None
    except Exception as e:
        print_status(f"Login error: {str(e)}", False)
        return False, None

def test_authenticated_request(token):
    """Test an authenticated request"""
    print("\n6. Testing Authenticated Request...")
    if not token:
        print_status("Skipping authenticated request (no token)", False)
        return False

    try:
        headers = {
            "Authorization": f"Bearer {token}"
        }
        # Try to get tasks for the user
        response = requests.get(
            f"{BASE_URL}/api/tasks",
            headers=headers,
            timeout=10
        )

        if response.status_code in [200, 404]:
            print_status("Authenticated request successful")
            return True
        else:
            print_status(f"Authenticated request failed with status {response.status_code}", False)
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print_status(f"Authenticated request error: {str(e)}", False)
        return False

def main():
    """Run all verification tests"""
    print("=" * 60)
    print("🚀 Hugging Face Deployment Verification")
    print(f"   Backend URL: {BASE_URL}")
    print("=" * 60)

    results = []

    # Run tests
    results.append(("Health Check", test_health_check()))
    results.append(("Root Endpoint", test_root_endpoint()))
    results.append(("API Documentation", test_api_docs()))

    reg_success, reg_token = test_registration()
    results.append(("User Registration", reg_success))

    login_success, login_token = test_login()
    results.append(("User Login", login_success))

    token = login_token or reg_token
    if token:
        results.append(("Authenticated Request", test_authenticated_request(token)))

    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)

    passed = sum(1 for _, success in results if success)
    total = len(results)

    for test_name, success in results:
        print_status(f"{test_name}", success)

    print("\n" + "=" * 60)
    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print_status("All tests passed! Deployment is working correctly. 🎉")
        return 0
    else:
        print_status(f"{total - passed} test(s) failed. Check the logs above.", False)
        return 1

if __name__ == "__main__":
    sys.exit(main())
