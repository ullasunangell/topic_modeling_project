import praw
import config  # Import the credentials from config.py

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD,
    user_agent=config.REDDIT_USER_AGENT
)

# test for successful autho
print(f"✅ Authenticated as: {reddit.user.me()}")
