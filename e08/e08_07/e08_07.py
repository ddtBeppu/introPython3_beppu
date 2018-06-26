# 復習課題 8-7
# books.csvを読み出し、そのデータをbookデーブルに格納しよう。

import csv
import sqlite3
from pprint import pprint

# books.csvの内容を読み出し、テーブルに格納する
with open('../e08_05/books', 'rt') as fin:
    # 内容を抽出できる行を作成
    cin = csv.reader(fin)

    # dbに接続
    conn = sqlite3.connect('../e08_06/books.db')
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
    select = 'SELECT * FROM book'
    # テーブルから値を抽出
    rows = cursor.execute(select)
    # 全ての行の内容を格納する変数を定義
    output = [row for row in rows]

    print("テーブルの内容")
    # テーブルの値の確認
    pprint(output)

    # カーソルオブジェクトを閉じる
    cursor.close()
    # dbを閉じる
    conn.close()

# 実行結果
"""
NaotonoMacBook-puro:e08_07 naotobeppu$ python e08_07.py 
テーブルの内容
[('title', 'author', 'year'),
 ('The Weirdstone of Brisingamen', 'Alan Garner', 1960),
 ('Perdido Street Station', 'china Mieville', 2000),
 ('Thud!', 'Terry Pratchett', 2005),
 ('The Spellman Files', 'Lisa Lutz', 2007),
 ('Small Gods', 'Terry Pratchett', 1992)]
 """