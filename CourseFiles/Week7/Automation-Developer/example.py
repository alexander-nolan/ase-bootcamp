import asyncio
import aiohttp
import requests
import time

async def fetch_post(session, post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    async with session.get(url) as response:
        return await response.json()

async def fetch_user(session, user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    async with session.get(url) as response:
        return await response.json()

async def main():
    # Start timing
    start_time = time.time()
    
    # Create a session
    async with aiohttp.ClientSession() as session:
        # Create tasks for multiple API calls
        post_tasks = [fetch_post(session, i) for i in range(1, 6)]
        user_tasks = [fetch_user(session, i) for i in range(1, 4)]
        
        # Execute all tasks concurrently
        posts, users = await asyncio.gather(
            asyncio.gather(*post_tasks),
            asyncio.gather(*user_tasks)
        )
        
        # Calculate execution time
        execution_time = time.time() - start_time
        
        # Print results
        print(f"\nFetched {len(posts)} posts and {len(users)} users in {execution_time:.2f} seconds")
        
        print("\nPosts:")
        for post in posts:
            print(f"- Post {post['id']}: {post['title'][:30]}...")
        
        print("\nUsers:")
        for user in users:
            print(f"- User {user['id']}: {user['name']}")

# Compare with synchronous version
def sync_version():
    start_time = time.time()
    
    # Make the same requests synchronously
    posts = []
    users = []
    
    for i in range(1, 6):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
        posts.append(response.json())
    
    for i in range(1, 4):
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{i}')
        users.append(response.json())
    
    execution_time = time.time() - start_time
    print(f"\nSynchronous version took {execution_time:.2f} seconds")

if __name__ == "__main__":
    print("Running async version...")
    asyncio.run(main())
    
    print("\nRunning sync version...")
    sync_version()