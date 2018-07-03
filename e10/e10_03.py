# 復習課題 10-3
# today_stringから日付を解析して取り出そう。

import time

# テキストファイルに書き込む準備
fout = open('today.txt', 'rt')

# today.txtの内容をtoday_string変数に読み込み
today_string = fout.readline()
print("today_string: ", today_string)

# 文字列解析のためにフォーマットを定義
fmt = "It's %Y/%m/%d\n"
# today_stringとフォーマットを照合して、日付を取り出す
today = time.strptime(today_string, fmt)
# 結果の表示
print(today)

# ファイルを閉じる
fout.close()

# 実行結果
"""
NaotonoMacBook-puro:e10 naotobeppu$ python e10_03.py 
today_string:  It's 2018/07/03

time.struct_time(tm_year=2018, tm_mon=7, tm_mday=3, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=184, tm_isdst=-1)
"""