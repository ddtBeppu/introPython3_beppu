# 復習課題 8-10
# sqlalchemyモジュールを使って、8-6で作ったsqlite3のbooks.dbデータベースに接続しよう。
# そして、8-8と同じように、bookテーブルのtitle列を選択してアルファベット順に表示しよう。

import csv
import sqlite3
from pprint import pprint
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# books.dbのパスを定義しておく
path_db = '../e08_06/books.db'
# データベースに接続
conn = sa.create_engine('sqlite:///'+path_db)

# データベースの元を定義
Base = declarative_base()
# Booksクラスを定義
class Books(Base):
    # テーブル名を明示
    __tablename__ = 'book'
    # title列を定義
    title = sa.Column('title', sa.String, primary_key=True)
    # author列を定義
    author = sa.Column('author', sa.String)
    # year列を定義
    year = sa.Column('year', sa.Integer)

    # コンストラクタ
    def __init__(self, title, author, year):
        # 変数titleを定義
        self.title = title
        # 変数authorを定義
        self.author = author
        # 変数yearを定義
        self.year = year

    # 表示形式を設定
    def __repr__(self):
        # 列ごとにフォーマットを指定する
        return "<books({}, {}, {})>".format(self.title, self.author, self.year)

# データベースとテーブルを作成
Base.metadata.create_all(conn)
# セッションの作成
Session = sessionmaker(bind=conn)
# セッション開始
sess = Session()

# books.csvを開き、処理を行う
with open('../e08_05/books.csv', 'rt') as fin:
    # 内容を抽出できる行を作成
    cin = csv.reader(fin)
    # 行ごとに値を格納するため、リストを定義
    rows = []
    # 行ごとに値を抽出
    for row in cin:
        # １行ずつ値を変数に格納
        a_row = Books(row[0], row[1], row[2])
        # リストに挿入
        rows.append(a_row)

    # 全ての値をデータベースに書き込み
    sess.add_all(rows)
    # 処理を完了させる
    sess.commit()

# 実行結果
# sqlite3にてコマンドを実行して、確認
"""
sqlite> SELECT * FROM book ORDER BY title;
Perdido Street Station|china Mieville|2000
Small Gods|Terry Pratchett|1992
The Spellman Files|Lisa Lutz|2007
The Weirdstone of Brisingamen|Alan Garner|1960
Thud!|Terry Pratchett|2005
title|author|year
"""