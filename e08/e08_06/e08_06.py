# 復習課題 8-6
# sqlite3モジュールを使って、books.dbというSQLiteデータベースを作り、
# その中にtitle(文字列)、'author'(整数)というフィールドを持つbookというテーブルを作ろう。

import sqlite3

# books.dbの作成
conn = sqlite3.connect('books.db')
# カーソルオブジェクトを作成
cursor = conn.cursor()

# dbにテーブルbookを作成するsql文を定義
insert_sql = 'CREATE TABLE book (title VARCHAR(20), author INT)'
# 実行する
cursor.execute(insert_sql)

# テーブルの内容を行ごとに抽出
rows = cursor.fetchall()
# 表示 → まだ値を追加していないため、空
print(rows)
