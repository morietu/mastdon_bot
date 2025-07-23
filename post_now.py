import os
from mastodon import Mastodon
import openai

# OpenAI API Key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 🔮 GPTからメッセージ生成
def generate_daily_message():
    prompt = "元気が出る、キャッチーで短いSNS用メッセージを40文字以内で1つ作って"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            { "role": "system", "content": "あなたは親しみやすくポジティブなSNS投稿Botです。" },
            { "role": "user", "content": prompt }
        ],
        max_tokens=100,
        temperature=0.8
    )
    return response.choices[0].message.content.strip()

# 🐘 Mastodon API設定
mastodon = Mastodon(
    access_token=os.environ.get("MASTODON_ACCESS_TOKEN"),
    api_base_url="https://mstdn.jp"
)

# 投稿メッセージ生成と投稿
if __name__ == "__main__":
    try:
        message = generate_daily_message()
        mastodon.toot(message)
        print("✅ 投稿完了:", message)
    except Exception as e:
        print("❌ 投稿失敗:", e)
