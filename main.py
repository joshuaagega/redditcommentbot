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

comments = ["""🔥 Craving something wild? These are 100% active:
🌙 **Lonely Night? This Worked for Me 👇**

- 🍪 THOTs who flirt and send nudes: [Mature Flirts Nearby](https://ebonynut.click/MatureFlirtsNearby)
- 👏🏿 Into trans girls? This one’s solid: [Transgender Flirters](https://ebonynut.click/TransgenderFlirters)
- 🍑 Freaky Latina girls going all out: [Lit Latinas](https://ebonynut.click/LitLatinz)
- 💯 Dirty dating, straight to the point: [MatureFlirtsNearby](https://ebonynut.click/Cupidfeel)
- 💦 Straight-to-the-point dirty dating: [Your Online Matches](https://ebonynut.click/YourOnlineMatches)
- 🔥 Tired of fake chats? These girls are 100% real and local: [MilfDatersAU](https://ebonynut.click/MilfDatersAU)
- 💋 Swipe, match, and meet MILFs who are online now 👇 [Cupidfeel](https://ebonynut.click/Cupidfeel)
- 🚨 No sign-up games. Just real girls ready to hook up nearby: [MeetNHook](https://ebonynut.click/MeetNHook)
- 👀 Scroll if you're taken. Single? She's already waiting: [OzzieFlirtZone2](https://ebonynut.click/OzzieFlirtZone2)
- 💦 Late-night cravings? She's online and wants to chat now: [SearchingForDates](https://ebonynut.click/SearchingForDates)
- 📍 Girls near you are posting spicy invites here: [YourLocalDate](https://ebonynut.click/YourLocalDate)
- For the real sexting lovers: [Flirt With Me Now D](https://ebonynut.click/FlirtWeMe)
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
