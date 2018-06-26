# 復習課題 8-3
# 次のテキストをbooks.csvというファイルに保存しよう。
# フィールドがカンマで区切られている場合、カンマを含むフィールドはクォートで囲まなければならないことに注意しよう。

# author, book
# J R R Tolkin,The Hobbit
# Lynne Truss, "Eats, Shoots & Leaves"

import csv

# CSVに書き込むテキストを設定
books = [
    ['author', 'book'],
    ['J R R Tolkin','The Hobbit'],
    ['Lynne Truss', "Eats, Shoots & Leaves"],
    ]

# CSVに書き込む処理
with open('books', 'wt') as fout:
    # 書き込むテキストを格納
    csvout = csv.writer(fout)
    # 1行ずつ書き込み
    csvout.writerows(books)