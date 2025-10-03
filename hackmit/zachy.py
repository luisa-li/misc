import random
from datetime import datetime, timedelta

import pandas as pd

# 100 Zachy notes
zachy_notes = [
    "I am the best trumpet player.",
    "Ugh, why does Alan always pick on the trumpet section?",
    "I can nail this distributed systems assignment.",
    "If only rehearsals were shorter… my lips are dying.",
    "Snowboarding this weekend is going to be epic.",
    "Seriously, Alan, did you even check the tempo?",
    "Math can be cool sometimes, like, when I actually get it.",
    "Another long rehearsal… my brain hurts.",
    "I’m a natural leader in the trumpet section.",
    "Why do people clap at the wrong moments?",
    "I love the sound of a perfectly tuned trumpet.",
    "Alan’s feedback is so passive-aggressive…",
    "I can finally solve this concurrency bug.",
    "Wind ensemble is actually kinda fun today.",
    "My chops are stronger than ever.",
    "Why does Alan always ignore my solo cues?",
    "I’m improving at every performance.",
    "Rewriting this code for the third time… ugh.",
    "I am a math ninja when I focus.",
    "If only Alan would take a chill pill.",
    "Snowboarding resets my brain.",
    "My trumpet tone is immaculate.",
    "Another wrong note from the cellos, wow.",
    "I can explain this distributed hash table to anyone.",
    "I hate when people chew during rehearsal.",
    "I am confident in my trumpet skills.",
    "Seriously, Alan, you literally never smile.",
    "I can debug this networking code in record time.",
    "Orchestra nights are exhausting but worth it.",
    "I wish Alan knew what a good tempo is.",
    "I hit all my high notes today.",
    "Why is the woodwind section always late?",
    "I am focused and ready for the next solo.",
    "CS assignments are way easier than people make them.",
    "Alan’s face when I play forte… priceless.",
    "I can shred this trumpet solo.",
    "Another math problem that’s actually kind of cool.",
    "I hate how slow the rehearsals drag.",
    "I am proud of my practice routine.",
    "If Alan moves the music stand one more time…",
    "I can crush this snowboarding trick.",
    "My articulation is perfect today.",
    "Everyone else sounds off, but I’m solid.",
    "I understand distributed consensus… sometimes.",
    "Alan’s critique makes me want to quit.",
    "I am resilient under rehearsal pressure.",
    "Math sometimes feels like a puzzle I enjoy.",
    "My lips feel like steel.",
    "Why is the woodwind section always late?",
    "I am the best trumpet player in this room.",
    "Alan just sighed… probably at me.",
    "I can optimize this code like a pro.",
    "My snowboarding balance is perfect.",
    "Another trumpet solo? Bring it.",
    "I hate the sound of squeaky chairs in rehearsal.",
    "I am proud of my improvisation skills.",
    "Why does Alan think vibrato is optional?",
    "I can master this distributed locking problem.",
    "The mountains are calling me this weekend.",
    "My tone quality is unmatched.",
    "Another rehearsal, another nap I didn’t take.",
    "I am strong enough to carry this ensemble.",
    "Alan’s timing is questionable at best.",
    "I can calculate these probabilities in my sleep.",
    "I love hitting that perfect trumpet fortissimo.",
    "Why do people clap offbeat? Seriously.",
    "I am unstoppable on my instrument.",
    "Alan, maybe listen to the trumpet section once in a while.",
    "I can snowboard down black diamonds like a champ.",
    "My fingers are fast and precise.",
    "Another math theorem to memorize… yay.",
    "I am confident I’ll ace this CS exam.",
    "Alan’s facial expressions are a hazard to focus.",
    "I can compose a melody in my head instantly.",
    "Why does rehearsal always feel like a full day?",
    "I am proud of my practice ethic.",
    "Snowboarding boots are the best invention.",
    "I can hit those double high Cs.",
    "Alan’s directions are always vague.",
    "I am learning new techniques every day.",
    "Another bug in my code… sigh.",
    "I love my trumpet solos, even if Alan doesn’t.",
    "Why does everyone play the same wrong dynamics?",
    "I am a math problem-solving machine.",
    "My endurance during long rehearsals is insane.",
    "Alan probably doesn’t know how hard we try.",
    "I can visualize complex distributed systems.",
    "Snowboarding keeps me sane.",
    "My tone is smooth like butter.",
    "Another day, another trumpet warm-up.",
    "I am the definition of a committed musician.",
    "Alan’s critiques are unnecessary and mean.",
    "I can implement this algorithm efficiently.",
    "I love landing clean tricks on the slopes.",
    "My range is expanding every week.",
    "Everyone else sounds tired, but I’m energized.",
    "I am in control of my music and my life.",
    "Why does Alan never appreciate small victories?",
    "I can solve these CS problems faster than anyone.",
    "I am the best trumpet player, and no one can tell me otherwise."
]

locations = [
    "New York, USA", "Tokyo, Japan", "Paris, France", "Sydney, Australia",
    "Rio de Janeiro, Brazil", "Berlin, Germany", "Cape Town, South Africa",
    "Toronto, Canada", "Mumbai, India", "Moscow, Russia"
]


def random_datetime():
    start = datetime.now() - timedelta(days=365)
    end = datetime.now()
    return (start + (end - start) * random.random()).strftime("%Y-%m-%d %H:%M:%S")


df = pd.DataFrame({
    "content": zachy_notes,
    "author": ["Zachie"] * len(zachy_notes),
    "location_from": [random.choice(locations) for _ in range(len(zachy_notes))],
    "created_at": [random_datetime() for _ in range(len(zachy_notes))],
    "tag": [9] * len(zachy_notes)
})

df.to_csv("zachy_notes.csv", index=False)
print("CSV file 'zachy_notes.csv' created successfully!")
