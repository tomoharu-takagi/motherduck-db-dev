#!/bin/python

import duckdb
import pandas as pd

# DuckDBに接続（データベースファイルはローカルに保存されます）
con = duckdb.connect('/data/motherduck.db')

# サンプルデータを作成してテーブルに挿入
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

# データをDuckDBに保存
con.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name VARCHAR, age INTEGER)')
con.execute('INSERT INTO users SELECT * FROM df')

# クエリを実行して結果を取得
result = con.execute('SELECT * FROM users').fetchdf()

# 結果を表示
print(result)

# コネクションをクローズ
con.close()
