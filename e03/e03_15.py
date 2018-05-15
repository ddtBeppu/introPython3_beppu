# 復習課題 3-15
# lifeという多重レベルの辞書を作ろう。最上位のキーとしては、'animals', 'plants', 'other'という文字列を使う。
# animalsキーは、'cats', 'octopi', 'emus'というキーを持つ他の辞書を参照するようにする。
# catsキーは、'Henri', 'Grumpy', 'Lucy'という文字列のリストを参照するようにする。他のキーは全て空辞書を参照するようにする。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> cats = ['Henri', 'Grumpy', 'Lucy']
>>> octopi = {}
>>> emus = {}
>>> animals = {'cats': cats, 'octopi': octopi, 'emus': emus}
>>> plants = {}
>>> other = {}
>>> Life = {'animals': animals, 'plants': plants, 'other': other}
>>> Life
{'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
>>> 


"""