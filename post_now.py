import os
import random
from datetime import datetime
from mastodon import Mastodon
from dotenv import load_dotenv
from openai import OpenAI

# ✅ 環境変数の読み込み
load_dotenv()

# ✅ OpenAIクライアントの初期化（gpt-4o-miniなど有効なモデルを使用）
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ✅ 各候補データ
muscles = ["胸", "背中", "体幹", "下半身", "腕", "肩", "ふくらはぎ", "お腹", "太もも", "広背筋"]
stretches = ["肩甲骨ストレッチを1分", "股関節を回す", "太もも裏を伸ばす"]
nutritions = ["朝にタンパク質を取ろう", "水を1.5L飲もう", "夕食はビタミン意識"]
habits = ["深呼吸3回してみよう", "スマホを寝る1時間前に手放す", "朝に日光を浴びよう"]
emojis = ["💪", "🌿", "🔥", "🌞", "✨"]

# ✅ ランダムでセルフケアメッセージを作成
def generate_care_message():
    today = datetime.now().strftime("%Y/%m/%d")
    emoji = random.choice(emojis)
    return f"""🗓 {today} のセルフケアメニュー {emoji}

🏋️‍♀️ 筋トレ部位：{random.choice(muscles)}
🤸‍♂️ ストレッチ：{random.choice(stretches)}
🍽 栄養ワンポイント：{random.choice(nutritions)}
📌 習慣のヒント：{random.choice(habits)}

#ストレッチ #健康習慣 #自動投稿
"""

# ✅ Mastodonへ投稿
def post_to_mastodon(text: str):
    mastodon = Mastodon(
        access_token=os.environ.get("MASTODON_ACCESS_TOKEN"),
        api_base_url="https://mstdn.jp"
    )
    mastodon.toot(text)
    print(f"✅ 投稿完了: {text.splitlines()[0]}")  # 1行目だけ表示

# ✅ 実行（セルフケアメニュー投稿）
if __name__ == "__main__":
    try:
        message = generate_care_message()
        if message.strip():
            post_to_mastodon(message)
        else:
            print("⚠️ メッセージが空だったため投稿スキップ")
    except Exception as e:
        print("❌ 投稿失敗:", e)
