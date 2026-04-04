import requests
from bs4 import BeautifulSoup
import time

# 1. 取得したいWebサイトのURLを指定
url = "https://oretsuri.com/"

# 2. Webページを取得
response = requests.get(url)

# 3. 取得が成功したかチェック（200番台ならOK）
if response.status_code == 200:
    # 4. HTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 5. データの抽出
    # ページのタイトルを取得
    page_title = soup.title.string
    print(f"ページタイトル: {page_title}")

    # ページ内のすべてのリンクを取得
    print("\n--- ページ内のリンク一覧 ---")
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        text = link.get_text()
        print(f"テキスト: {text}, URL: {href}")

    # サーバーへの負荷軽減のため、次のアクセスまで1秒待機（ループ時などは必須）
    time.sleep(1)
else:
    print(f"エラーが発生しました。ステータスコード: {response.status_code}")