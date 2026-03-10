# Python復習：リストと繰り返し処理
data_fields = ["日付", "気温", "湿度", "天気"]

print("--- 取得予定のデータ項目一覧 ---")

# リストの中身を順番に表示
for i, field in enumerate(data_fields, start=1):
    print(f"{i}番目の項目: {field}")

# データの件数を表示
print(f"\n合計 {len(data_fields)} 項目のデータを扱う予定です。")