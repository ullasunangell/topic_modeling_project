REDDIT_CLIENT_ID = "7t-zD_YzmiwGV91w7R_AOg"
REDDIT_CLIENT_SECRET = "LKqEpLkVeT2GTq2Lx5uWOOlb-SIIPg"
REDDIT_USERNAME = "ullaangell"
REDDIT_PASSWORD = "rymcy8-poxtyx-hinNeg"
REDDIT_USER_AGENT = "MarketTrendsScraper v1.0"

import praw
import config  # Import credentials from config.py

# Authenticate with Reddit
reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD,
    user_agent=config.REDDIT_USER_AGENT
)

print(f"Authenticated as: {reddit.user.me()}")
