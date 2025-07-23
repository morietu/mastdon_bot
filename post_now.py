from mastodon import Mastodon
import os

mastodon = Mastodon(
    access_token=os.environ["MASTODON_ACCESS_TOKEN"],
    api_base_url="https://mstdn.jp"
)

mastodon.toot("✅ GitHub Actions から即投稿できました！")
