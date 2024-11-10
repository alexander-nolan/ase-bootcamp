# Python API Requests Lab Guide

### Prerequisites:
1. **Install Python**  
   Python 3.x is required. Download from the official [Python website](https://www.python.org/downloads/).

2. **Install Required Packages**  
   ```bash
   pip install requests
   ```

### Step 1: Basic GET Request
Let's start with a simple GET request to retrieve data from an API.

```python
import requests

# Make a GET request to a public API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### Step 2: Making POST Requests
Create new resources using POST requests.

```python
import requests

# Data to send in the POST request
new_post = {
    'title': 'My New Post',
    'body': 'This is the content of my post',
    'userId': 1
}

# Make a POST request
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=new_post
)

# Check response
if response.status_code == 201:
    created_post = response.json()
    print("Created post:", created_post)
else:
    print(f"Error: {response.status_code}")
```

### Step 3: Adding Headers
Learn how to add custom headers to your requests.

```python
import requests

# Define headers
headers = {
    'User-Agent': 'Python API Lab Client',
    'Accept': 'application/json',
    'Authorization': 'Bearer your-token-here'
}

# Make request with headers
response = requests.get(
    'https://api.github.com/user',
    headers=headers
)

print(f"Status Code: {response.status_code}")
print(f"Headers: {response.headers}")
```

### Step 4: Handling Query Parameters
Add query parameters to your requests for filtering and pagination.

```python
import requests

# Parameters as a dictionary
params = {
    'page': 1,
    'limit': 10,
    'sort': 'desc'
}

# Make GET request with parameters
response = requests.get(
    'https://jsonplaceholder.typicode.com/posts',
    params=params
)

# URL with parameters will be printed
print(f"Request URL: {response.url}")
print(f"Results: {response.json()[:2]}")  # Print first 2 results
```

### Step 5: PUT and PATCH Requests
Update existing resources using PUT and PATCH.

```python
import requests

# PUT request (full update)
put_data = {
    'id': 1,
    'title': 'Updated Title',
    'body': 'Updated body content',
    'userId': 1
}

put_response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    json=put_data
)

# PATCH request (partial update)
patch_data = {
    'title': 'Only Update Title'
}

patch_response = requests.patch(
    'https://jsonplaceholder.typicode.com/posts/1',
    json=patch_data
)
```

### Step 6: DELETE Requests
Remove resources using DELETE requests.

```python
import requests

# Make DELETE request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

# Check if deletion was successful
if response.status_code == 200:
    print("Resource deleted successfully")
else:
    print(f"Error deleting resource: {response.status_code}")
```

### Step 7: Error Handling
Implement proper error handling for your API requests.

```python
import requests
from requests.exceptions import RequestException

def make_api_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting to server: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    
    return None

# Test the function
result = make_api_request('https://jsonplaceholder.typicode.com/posts/1')
if result:
    print("Data retrieved successfully:", result)
```

### Step 8: Working with Sessions
Use sessions to maintain cookies and connection pools.

```python
import requests

# Create a session
session = requests.Session()

# Set default headers for all requests in this session
session.headers.update({
    'User-Agent': 'Python API Lab Client',
    'Accept': 'application/json'
})

# Make multiple requests using the session
response1 = session.get('https://jsonplaceholder.typicode.com/posts/1')
response2 = session.get('https://jsonplaceholder.typicode.com/posts/2')

# Close the session when done
session.close()
```

### Practice Exercises:
1. Create a function that fetches and displays user data from the JSONPlaceholder API
2. Build a script that creates a new post and then updates it
3. Implement pagination to fetch multiple pages of data
4. Create a function that handles both successful and failed API requests
5. Build a simple CLI tool that allows users to perform CRUD operations on the JSONPlaceholder API

### Additional Resources:
- [Requests Library Documentation](https://docs.python-requests.org/)
- [JSONPlaceholder API Documentation](https://jsonplaceholder.typicode.com/)
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)