# 復習課題 5-7
# dict_of_listsという名前のdefaultdictを作り、list引数を渡そう。
# 次に、一度の操作で、dict_of_lists['a']というリストを作り、'something for a'という値を追加しよう。
# 最後に、dict_of_lists['a']を表示しよう。

from collections import defaultdict
dict_of_lists = defaultdict(list) # defaultdictを作り、list引数を渡す

dict_of_lists['a'] = 'somthing for a' # dict_of_lists['a']というリストを作り、'something for a'という値を追加
# 値を表示
print(dict_of_lists['a'])


# 実行結果
"""
NaotonoMacBook-puro:e05 naotobeppu$ python e05_07.py 
somthing for a
"""