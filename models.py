import hashlib
# Basic model simulation
def get_greeting():
    """Return a greeting message."""
    return "Hello, World!"

# Function to generate a unique short URL
def generate_short_url(long_url):
    # Using a hash of the URL to generate a unique ID
    hash_object = hashlib.md5(long_url.encode())
    short_id = hash_object.hexdigest()[:6]  # Taking first 6 characters
    return short_id