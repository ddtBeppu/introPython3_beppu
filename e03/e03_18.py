# 復習課題 3-18
# life['animals']['cats']の値を表示しよう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> cats = ['Henri', 'Grumpy', 'Lucy']   #  リストを作成
>>> octopi = {}   #  空集合を作成
>>> emus = {}   #  空集合を作成
>>> animals = {'cats': cats, 'octopi': octopi, 'emus': emus}   #  上記のリスト、空集合を値に持つ辞書を作成
>>> plants = {}   #  空集合を作成
>>> other = {}   #  空集合を作成
>>> Life = {'animals': animals, 'plants': plants, 'other': other}   # 辞書を値に持つ辞書を作成
>>> Life    #  辞書の内容を表示
{'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
>>> Life.keys()   #  最上位のキーを表示
dict_keys(['animals', 'plants', 'other'])
>>> Life['animals'].keys()   # life['animals']のキーを表示
dict_keys(['cats', 'octopi', 'emus'])
>>> Life['animals']['cats']   ###  life['animals']['cats']の値を表示
['Henri', 'Grumpy', 'Lucy']
>>> 


"""