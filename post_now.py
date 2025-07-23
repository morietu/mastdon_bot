import os
from mastodon import Mastodon
import openai

# OpenAI API Key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 🔮 GPTからメッセージ生成
def generate_daily_message():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": "あなたは親しみやすくポジティブなSNS投稿Botです。" },
            { "role": "user", "content": "朝のSNS投稿メッセージを120文字以内で作ってください。" }
        ],
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# 🐘 Mastodon API設定
mastodon = Mastodon(
    access_token=os.environ.get("MASTODON_ACCESS_TOKEN"),
    api_base_url=os.environ.get("MASTODON_API_BASE_URL")
)

# 投稿メッセージ生成と投稿
if __name__ == "__main__":
    try:
        message = generate_daily_message()
        mastodon.toot(message)
        print("✅ 投稿完了:", message)
    except Exception as e:
        print("❌ 投稿失敗:", e)
