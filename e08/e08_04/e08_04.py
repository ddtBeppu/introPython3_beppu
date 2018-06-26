# 復習課題 8-4
# csvモジュールとそのDictReaderメソッドを使って、books.csvの内容をbooks変数に読み込み、booksの内容を表示しよう。
# DictReaderはクォートと第２の本のタイトルに含まれるカンマを正しく処理出来ているか。

import csv

# ファイルを開いて処理を行う
with open('../e08_03/books', 'rt') as fin:
    # csvの内容を読み込み
    cin = csv.DictReader(fin, fieldnames=['author', 'book'])
    # 1行ずつ読み込み、books変数に格納
    books = [row for row in cin]
    # 内容の表示
    print(books)


# 実行結果
"""
NaotonoMacBook-puro:e08_04 naotobeppu$ python e08_04.py 
[OrderedDict([('author', 'author'), ('book', 'book')]), 
OrderedDict([('author', 'J R R Tolkin'), ('book', 'The Hobbit')]), 
OrderedDict([('author', 'Lynne Truss'), ('book', 'Eats, Shoots & Leaves')])]
"""