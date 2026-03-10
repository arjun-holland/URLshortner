import os
import string
import random
from pymongo import MongoClient
from redis import Redis
from django.conf import settings
from datetime import datetime, timezone

# Initialize MongoDB Client
try:
    mongo_client = MongoClient(settings.MONGO_URI, serverSelectionTimeoutMS=5000)
    db = mongo_client.get_default_database() if mongo_client.get_default_database().name else mongo_client['urlshortener']
    urls_collection = db['urls']
    # Ensure indexes (creates them if they don't exist)
    urls_collection.create_index("short_code", unique=True)
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    db = None
    urls_collection = None

# Initialize Redis Client
try:
    redis_client = Redis.from_url(settings.REDIS_URL, decode_responses=True)
except Exception as e:
    print(f"Failed to connect to Redis: {e}")
    redis_client = None

def generate_short_code(length=6):
    """Generate a random alphanumeric string of given length."""
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        # Check if code already exists in DB
        if urls_collection is not None and not urls_collection.find_one({"short_code": code}):
            return code
        elif urls_collection is None:
            # Fallback if DB is not connected yet
            return code

def create_short_url(long_url, custom_code=None):
    if custom_code:
        if urls_collection.find_one({"short_code": custom_code}):
            raise ValueError("Custom code already exists")
        short_code = custom_code
    else:
        short_code = generate_short_code()
    
    url_document = {
        "long_url": long_url,
        "short_code": short_code,
        "created_at": datetime.now(timezone.utc),
        "clicks": 0
    }
    
    if urls_collection is not None:
        urls_collection.insert_one(url_document)
    
    # Store in Redis cache
    if redis_client:
        redis_client.set(short_code, long_url)

    return short_code

def get_long_url(short_code):
    # Try cache first
    if redis_client:
        cached_url = redis_client.get(short_code)
        if cached_url:
            return cached_url
            
    # Try DB
    if urls_collection is not None:
        url_doc = urls_collection.find_one({"short_code": short_code})
        if url_doc:
            long_url = url_doc.get("long_url")
            # Update cache for future
            if redis_client:
                redis_client.set(short_code, long_url)
            return long_url
    return None


