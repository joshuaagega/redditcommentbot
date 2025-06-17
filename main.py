import os
import time
import random
from threading import Thread
from flask import Flask
import praw

app = Flask(__name__)
@app.route("/")
def home():
    return "Bot is running."

def run_web():
    # Railway sets the port number in the env var PORT
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()

reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    username=os.environ["REDDIT_USER"],
    password=os.environ["REDDIT_PASS"],
    user_agent="comment_app by u/" + os.environ["REDDIT_USER"]
)

subreddits = ["ebonynut", "CamgirlsPics", "hentaihubx", "contenusexyfrancaise", "tattedphysique", "Deutschehentai"] # Replace with your actual subreddit(s)

comments = ["""🔥 Here are a few crazier options ...
🌙 **Late Night Chat (Tested & Real)**

- THOTs who flirt and send nudes: [Mature Flirts Nearby](https://ebonynut.click/MatureFlirtsNearby)
- Into trans girls? This one’s solid: [Transgender Flirters](https://ebonynut.click/TransgenderFlirters)
- Freaky Latina girls going all out: [Flirt With Me Now](https://ebonynut.click/FlirtWithMeNow)
- Dirty dating, straight to the point: [MatureFlirtsNearby](ebonynut.click/MatureFlirtsNearby2)
- Straight-to-the-point dirty dating: [Your Online Matches](https://ebonynut.click/YourOnlineMatches)
- For the real sexting lovers: [Flirt With Me Now D](https://ebonynut.click/FlirtWithMeNowD)
- Strictly for nasty hookups: [Mature Flirts Near](https://ebonynut.click/MatureFlirtsNear)"""]
rate_sleep = 10   
already_commented = set()

while True:
    for sub in subreddits:
        for post in reddit.subreddit(sub).new(limit=10):
            if post.id not in already_commented:
                try:
                    post.reply(random.choice(comments))
                    already_commented.add(post.id)
                    print(f"✅ Replied to: {post.title}")
                    time.sleep(rate_sleep)
                except Exception as e:
                    print(f"❌ Error on {post.id}: {e}")
    time.sleep(60)   # wait 1 min before checking the subs again
