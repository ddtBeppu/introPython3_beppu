# 復習課題 5-6
# 5-5と同じペアからfancyという名前のOrderedDictを作り、内容を表示しよう。plainと同じ順序で表示されただろうか。

from collections import OrderedDict
# 辞書の作成
plain = {'a': 1, 'b': 2, 'c': 3}
# orderedDictの生成
fancy = OrderedDict([
    ('a', 1), # キー/値ペア1
    ('b', 2), # キー/値ペア2
    ('c', 3)  # キー/値ペア3
])
### 値の表示
print("fancy = ", fancy)


# 実行結果
# 以下の通り、plainと同様の順序で表示された。
"""

NaotonoMacBook-puro:e05 naotobeppu$ python e05_06.py 
fancy =  OrderedDict([('a', 1), ('b', 2), ('c', 3)])

"""