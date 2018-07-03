# 復習課題 10-4
# カレントディレクトリのファイルのリストを作ろう。

import os

# カレントディレクトリに含まれるもののリスト
lists = os.listdir('.')
# 値の確認
print("全て: ", lists)

# ファイルのみを選択して、リストに追加する
file_list = [file for file in lists if os.path.isfile(file)]
# 結果の確認
print("ファイルのみ: ", file_list)

# 実行結果
"""
NaotonoMacBook-puro:e10 naotobeppu$ python e10_04.py 
全て:  ['.DS_Store', 'e10_03.py', 'today.txt', 'e10_04.py', 'e10_01.py', 'e10_02']
ファイルのみ:  ['.DS_Store', 'e10_03.py', 'today.txt', 'e10_04.py', 'e10_01.py']
"""
