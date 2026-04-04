import pandas as pd
import numpy as np

# 1. 【Before】わざと「汚いデータ」を作成
data = {
    '日付': ['2023/01/01', '2023-01-02', '2023.01.03', '2023/01/04', '2023/01/01'], # 形式バラバラ + 重複
    '顧客名': [' 山田 太郎', '田中　次郎', '山田太郎', '佐藤 花子', ' 山田 太郎'], # 空白 + 表記揺れ + 重複
    '売上額': ['1,500', '2000', None, '3500', '1,500'], # カンマあり + 欠損値
}
df = pd.DataFrame(data)

# --- 2. データ加工プロセスの開始 ---

# ① 重複データの削除
df = df.drop_duplicates()

# ② 日付形式の統一（バラバラな区切り文字を修正して変換）
# df['日付'] = pd.to_datetime(df['日付'].str.replace('.', '/', regex=False))
df['日付'] = pd.to_datetime(df['日付'], format='mixed')

# ③ 文字列のクレンジング（前後空白の削除、全角スペースの除去、氏名の結合）
df['顧客名'] = df['顧客名'].str.strip().str.replace('　', '', regex=False).str.replace(' ', '', regex=False)

# ④ 数値データの整形（カンマ除去と数値型への変換）
df['売上額'] = df['売上額'].str.replace(',', '', regex=False).astype(float)

# ⑤ 欠損値の補完（例：全体の平均値で埋める）
df['売上額'] = df['売上額'].fillna(df['売上額'].mean())

# ⑥ 曜日情報を追加
df['曜日'] = df['日付'].dt.day_name()

# 3. 【After】結果の出力
print("--- 加工済みのデータ ---")
print(df)