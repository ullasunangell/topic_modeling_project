import time
import pandas as pd
import praw
import config



reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    username=config.REDDIT_USERNAME,
    password=config.REDDIT_PASSWORD,
    user_agent=config.REDDIT_USER_AGENT
)


def scrape_reddit(subreddits, limit=1000):
    """Scrape posts from multiple subreddits using different sorting methods."""
    
    all_data = []

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        posts = set()  # avoid duplicates

        # scrape from hot, new, and top
        for category in ["hot", "new", "top"]:
            for post in getattr(subreddit, category)(limit=limit // 3):  # divide limit across categories
                posts.add((subreddit_name, post.title, post.selftext, post.score, post.num_comments, post.created_utc, post.url))
            
            time.sleep(2)  # prevent hitting api rate limits

        df = pd.DataFrame(posts, columns=["Subreddit", "Title", "Text", "Upvotes", "Comments", "Timestamp", "URL"])
        all_data.append(df)

        print(f"saved {len(df)} posts from r/{subreddit_name}")

    # combine all into one df and save
    final_df = pd.concat(all_data, ignore_index=True)
    final_df.to_csv(f"data/multiple_subreddits_{len(final_df)}_posts.csv", index=False)
    print(f"scraped a total of {len(final_df)} posts from {len(subreddits)} subreddits!")

# list of subreddits to scrape
subreddits = ["stocks", "investing", "wallstreetbets", "finance"]
scrape_reddit(subreddits, limit=1000)