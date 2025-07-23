# main.py
import os
import random
import schedule
import time
from mastodon import Mastodon
from dotenv import load_dotenv
from datetime import datetime

# ✅ ランダムの種（同じになりにくくする）
random.seed(datetime.now().timestamp())

# .env 読み込み
load_dotenv()

# 投稿データ候補
muscles = ["胸", "背中", "体幹", "下半身", "腕", "肩", "ふくらはぎ", "お腹", "太もも", "広背筋"]
stretches = ["肩甲骨ストレッチを1分", "股関節を回す", "太もも裏を伸ばす"]
nutritions = ["朝にタンパク質を取ろう", "水を1.5L飲もう", "夕食はビタミン意識"]
habits = ["深呼吸3回してみよう", "スマホを寝る1時間前に手放す", "朝に日光を浴びよう"]
emojis = ["💪", "🌿", "🔥", "🌞", "✨"]

# 投稿内容を組み立てて送信
def post_to_mastodon():
    today = datetime.now().strftime("%Y/%m/%d")
    emoji = random.choice(emojis)

    text = f"""🗓 {today} のセルフケアメニュー {emoji}

🏋️‍♀️ 筋トレ部位：{random.choice(muscles)}
🤸‍♂️ ストレッチ：{random.choice(stretches)}
🍽 栄養ワンポイント：{random.choice(nutritions)}
📌 習慣のヒント：{random.choice(habits)}

#ストレッチ #健康習慣 #自動投稿
"""

    mastodon = Mastodon(
        access_token=os.getenv("MASTODON_ACCESS_TOKEN"),
        api_base_url="https://mstdn.jp"
    )

    mastodon.toot(text)
    print(f"✅ {today} に投稿しました")

# テスト用：1分ごとに投稿（本番は 08:00 に変更）
schedule.every().day.at("08:00").do(post_to_mastodon)

print("Botは毎朝8時の投稿を待機中です...")

while True:
    schedule.run_pending()
    time.sleep(60)
