# 復習課題 10-5
# 親ディレクトリのファイルのリストを作ろう。

import os

# 親ディレクトリに含まれるもののリスト
par_lists = os.listdir('..')
# 値の確認
print("親ディレクトリ: ", par_lists)

# 親ディレクトリに含まれるもののリスト
cur_lists = os.listdir('.')
# 値の確認
print("カレントディレクトリ: ", cur_lists)

# ファイルのみを選択して、リストに追加する
file_list = [file for file in par_lists if os.path.isfile(file)]
# 結果の確認
print("ファイルのみ: ", file_list)


# 実行結果
"""
NaotonoMacBook-puro:e10 naotobeppu$ python e10_05.py 
親ディレクトリ:  ['e03', 'e04', '.DS_Store', 'e05', 'e02', 'e10', '.gitignore', 'e07', 'e09', 'e08', 'e01', 'e06', '.git']
カレントディレクトリ:  ['.DS_Store', 'e10_03.py', 'today.txt', 'e10_04.py', 'e10_01.py', 'e10_05.py', 'e10_02']
ファイルのみ:  ['.DS_Store']
"""