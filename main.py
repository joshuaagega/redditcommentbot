import praw
import time
import os

reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    username=os.environ["USERNAME"],
    password=os.environ["PASSWORD"],
    user_agent="comment_app by u/" + os.environ["USERNAME"]
)

subreddits = ["example_subreddit"]  # Replace with your actual subreddit(s)
comment_text = "🔥 Thanks for posting! Check this out: https://your-affiliate-link.com"

already_commented = set()

while True:
    for sub in subreddits:
        for post in reddit.subreddit(sub).new(limit=10):
            if post.id not in already_commented:
                try:
                    post.reply(comment_text)
                    already_commented.add(post.id)
                    print(f"✅ Replied to post: {post.title}")
                    time.sleep(10)
                except Exception as e:
                    print(f"❌ Error: {e}")
    time.sleep(60)