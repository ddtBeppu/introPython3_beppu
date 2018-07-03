# 復習課題 10-8
# あなたの誕生日は何曜日だったか。

from datetime import date

# 誕生日のdateオブジェクトを作成
birthday = date(1993, 2, 14)

# 曜日を表示するために、フォーマットを設定
fmt = "It was %A"
# 結果を表示
print(birthday.strftime(fmt))


# 実行結果
"""
NaotonoMacBook-puro:e10 naotobeppu$ python e10_08.py 
It was Sunday
"""