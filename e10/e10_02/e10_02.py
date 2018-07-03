# 復習課題 10-2
# テキストファイルtoday.txtの内容をtoday_stringという文字列変数に読み込もう。

from datetime import date
import time

# テキストファイルに書き込む準備
fout = open('today.txt', 'rt')

# today.txtの内容をtoday_string変数に読み込み
today_string = fout.readline()
# 確認のため表示
print(today_string)

# ファイルを閉じる
fout.close()