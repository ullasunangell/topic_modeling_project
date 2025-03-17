import time
import pandas as pd
import praw
import config

# Reddit API authentication
reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD,
    user_agent=config.REDDIT_USER_AGENT
)

def scrape_reddit(subreddit_name, limit=500):
    """Scrape posts from a subreddit using multiple sorting methods."""
    subreddit = reddit.subreddit(subreddit_name)
    posts = set()  # Use a set to avoid duplicates

    # Fetch from different categories
    for category in ["hot", "new", "top"]:
        for post in getattr(subreddit, category)(limit=limit // 3):  # Divide limit across categories
            posts.add((post.title, post.selftext, post.score, post.num_comments, post.created_utc, post.url))

        time.sleep(2)  # Prevent hitting API rate limits

    df = pd.DataFrame(posts, columns=["Title", "Text", "Upvotes", "Comments", "Timestamp", "URL"])
    df.to_csv(f"data/{subreddit_name}_raw_{len(df)}_posts.csv", index=False)
    print(f"✅ Saved {len(df)} posts from r/{subreddit_name}")

# Run the scraper
scrape_reddit("stocks", limit=500)
