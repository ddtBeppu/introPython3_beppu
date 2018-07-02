# 復習課題 10-1
# 現在の日付をtoday.txtというテキストファイルに文字列の形で書き込もう。

from datetime import date
import time

# テキストファイルに書き込む準備
fout = open('today.txt', 'wt')
# 文字列のフォーマットを設定
fmt = "It's %Y/%m/%d"
# 今日の日付を指定
now = date(2018, 7, 3)
# ファイルに書き込み
print(now.strftime(fmt), file=fout)
# ファイルを閉じる
fout.close()