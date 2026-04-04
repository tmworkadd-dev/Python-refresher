import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. サンプルデータの作成（100人の年収データ）
# 大部分は400~800万円だが、入力ミスで「5億円(50000)」が混じっている想定
np.random.seed(0)
income = np.random.normal(600, 100, 99).tolist() # 通常のデータ
income.append(50000) # 1つだけ極端な外れ値を追加
df = pd.DataFrame({'年収': income})

# 2. グラフ表示の設定
plt.figure(figsize=(12, 5))

# --- 【加工前】のヒストグラム ---
plt.subplot(1, 2, 1)
plt.hist(df['年収'], bins=30, color='skyblue', edgecolor='black')
plt.title('Before: With Outlier')
plt.xlabel('Income (10k yen)')
plt.ylabel('Count')

# --- データ加工（外れ値の除外） ---
# 3. 3標準偏差(3sigma)を超えるデータ、または現実的な範囲（例: 2000万以上）を除外
upper_limit = 2000 
df_cleaned = df[df['年収'] < upper_limit]

# --- 【加工後】のヒストグラム ---
plt.subplot(1, 2, 2)
plt.hist(df_cleaned['年収'], bins=15, color='orange', edgecolor='black')
plt.title('After: Removed Outlier')
plt.xlabel('Income (10k yen)')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

# 4. 統計量の比較
print("--- 統計量の比較 ---")
print(f"加工前 平均値: {df['年収'].mean():.1f} 万円")
print(f"加工後 平均値: {df_cleaned['年収'].mean():.1f} 万円")