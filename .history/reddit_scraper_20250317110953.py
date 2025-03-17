import praw
import config
import pandas as pd

# auth for reddit api
reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD,
    user_agent=config.REDDIT_USER_AGENT
)

# # test for successful autho
# print(f"✅ Authenticated as: {reddit.user.me()}")

def scrape_reddit(subreddit_name, limit=500):
    """Scrape posts from a specific subreddit."""
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):  # get top 100 hot posts
        posts.append([post.title, post.selftext, post.score, post.num_comments, post.created_utc, post.url])

    df = pd.DataFrame(posts, columns=["Title", "Text", "Upvotes", "Comments", "Timestamp", "URL"])
    df.to_csv(f"data/{subreddit_name}_raw_500_posts.csv", index=False)
    print(f"✅ Saved {len(df)} posts from r/{subreddit_name}")

# test: scrape 100 posts from r/stocks
scrape_reddit("stocks", limit=500)
