# 復習課題 8-8
# bookテーブルのtitle列を選択し、アルファベット順に表示しよう。

import csv
import sqlite3
from pprint import pprint

path_db = '../e08_06/books.db'

# books.csvの内容を読み出し、テーブルに格納する
with open('../e08_05/books', 'rt') as fin:
    # 内容を抽出できる行を作成
    cin = csv.reader(fin)

    # dbに接続
    conn = sqlite3.connect(path_db)
    # カーソルオブジェクトを作成
    cursor = conn.cursor()

    # books.csvの内容を1行ずつ参照
    for row in cin:
        # 内容をテーブルbookに挿入するSQL文を作成
        insert_sql = 'INSERT INTO book (title, author, year) VALUES(?, ?, ?)'
        # 実行
        cursor.execute(insert_sql, row)
    
    # テーブルに内容が挿入されたことを確認する。
    # SQL文を作成
    select = 'SELECT * FROM book ORDER BY title'
    # テーブルから値を抽出
    rows = cursor.execute(select)
    # 全ての行の内容を格納する変数を定義
    output = [row for row in rows]

    # タイトルの行を選択
    select_title = 'SELECT title FROM book ORDER BY title'
    # 検索結果を格納
    rows_title = cursor.execute(select_title)
    # 検索した値の確認
    pprint([row for row in rows_title])

    # カーソルオブジェクトを閉じる
    cursor.close()
    # dbを閉じる
    conn.close()