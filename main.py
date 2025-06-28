import os
import time
import random
from threading import Thread
from flask import Flask
import praw
from datetime import datetime
import pytz

# Flask app setup for Railway
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running."

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()

# Reddit auth
reddit = praw.Reddit(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    username=os.environ["REDDIT_USER"],
    password=os.environ["REDDIT_PASS"],
    user_agent="comment_app by u/" + os.environ["REDDIT_USER"]
)

# Target subreddits
subreddits = ["ebonynut", "CamgirlsPics", "hentaihubx", "contenusexyfrancaise", "tattedphysique", "Deutschehentai"]

# Timezone
timezone = pytz.timezone("Africa/Nairobi")

# Comment sets
morning_comments = [
    "☀️ Start your day off spicy: [Lit Latinas](https://ebonynut.click/SearchingForDatesCA)",
    "🌄 Wake up with local MILFs: [MilfDatersAU](https://ebonynut.click/SearchingForDatesCA)",
    "🚿 Morning shower thoughts? [Transgender Flirters](https://ebonynut.click/SearchingForDatesCA)"
]

afternoon_comments = [
   "Tired of boring chats? 🔥 Talk dirty with real people who are actually online now: https://ebonynut.click/MilfDatersCA",
    "Just found this wild cam site – these girls don't hold back 😳 hhttps://ebonynut.click/MilfDatersCA",
    "No games, just hookups. Locals are literally waiting right now 👇 https://ebonynut.click/MilfDatersCA",
    "Into MILFs? This place is packed with hot moms ready to meet 👀 https://ebonynut.click/MilfDaters",
    "If you’re just here to smash, this is where it’s at: https://ebonynut.click/Instabang",
    "Swipe, match, and go crazy tonight. Fling is full of real hookups 🔞 https://ebonynut.click/Fling"
]

evening_comments = [
    """🌙 **Lonely Night? This Worked for Me 👇**

- 🍪 THOTs who flirt and send nudes: [Mature Flirts Nearby](https://ebonynut.click/MilfDatersCA)
- 👏🏿 Into trans girls? This one’s solid: [Transgender Flirters](https://ebonynut.click/SearchingForDatesCA)
- 🍑 Freaky Latina girls going all out: [Lit Latinas](https://ebonynut.click/MilfDatersCA)
- 💯 Dirty dating, straight to the point: [MatureFlirtsNearby](https://ebonynut.click/SearchingForDatesCA)
- 💋 Swipe, match, and meet MILFs: [Cupidfeel](https://ebonynut.click/Cupidfeel)
- 🚨 No sign-up games: [MeetNHook](https://ebonynut.click/SearchingForDatesCA)
- 👀 Scroll if you're taken. If not: [OzzieFlirtZone2](https://ebonynut.click/MilfDatersCA)
- 💦 Late-night craving? [SearchingForDates](https://ebonynut.click/SearchingForDatesCA)
- 🔞 Sexting lovers only: [Flirt With Me Now D](https://ebonynut.click/SearchingForDatesCA)"""
]

# Determine which comment set to use
def get_comment_set():
    current_hour = datetime.now(timezone).hour
    if 5 <= current_hour < 12:
        return morning_comments
    elif 12 <= current_hour < 18:
        return afternoon_comments
    else:
        return evening_comments

rate_sleep = 10
already_commented = set()

# Main loop
while True:
    for sub in subreddits:
        for post in reddit.subreddit(sub).new(limit=10):
            if post.id not in already_commented:
                try:
                    selected_comment = random.choice(get_comment_set())
                    post.reply(selected_comment)
                    already_commented.add(post.id)
                    print(f"✅ Replied to: {post.title}")
                    time.sleep(rate_sleep)
                except Exception as e:
                    print(f"❌ Error on {post.id}: {e}")
    time.sleep(60)  # Re-check after 1 min
