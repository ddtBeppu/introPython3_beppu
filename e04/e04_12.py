# 復習課題 4-12
# zip()を使ってmoviesという辞書を作ろう。辞書は、titles = ['Creature of Habit', 'Crewel Fate']というリストと
# plots = ['A nun turns into a monster', 'A Haunted yarn shop']というリストを組み合わせて作るものとする。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。


"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

###  映画タイトルを値にもつtitlesリストを作成
>>> titles = ['Creature of Habit', 'Crewel Fate']
###  映画の短いあらすじを値にもつplotsリストを作成
>>> plots = ['A nun turns into a monster', 'A Haunted yarn shop']
###  辞書を生成
>>> movies = dict(zip(titles,plots))
###  辞書の値を表示
>>> movies
{'Creature of Habit': 'A nun turns into a monster', 'Crewel Fate': 'A Haunted yarn shop'}
>>> 

"""