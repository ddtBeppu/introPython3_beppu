# 復習課題 3-9
# surpriseリストの最後の要素を小文字にして、逆順にしてから、先頭文字を大文字に戻そう。

# 解答：
# インタープリタにて計算を行いました。
# コメントは、後からエディタにて追加しました。

"""

NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> surprise = ["Groucho", "Chico", "Harpo"]   # リストsurpriseを作成
>>> surprise    ###  surpriseリストを表示
['Groucho', 'Chico', 'Harpo']
>>> surprise[-1] = surprise[-1].lower()   ### リストの最後の要素を小文字にする。
>>> surprise   ###  surpriseリストを表示
['Groucho', 'Chico', 'harpo']
>>> surprise_copy = surprise.copy()    ###  リストのコピーを作成
>>> surprise[0] = surprise_copy[-1]   ### コピーしたリストの末尾の要素を元のリストの先頭に代入
>>> surprise[1] = surprise_copy[-2]   ### コピーしたリストの末尾より一つ前の要素を、元のリストの二番目の要素に代入
>>> surprise[2] = surprise_copy[-3]   ### コピーしたリストの先頭の要素を、元のリストの末尾の要素に代入
>>> surprise   ###  surpriseリストを表示
['harpo', 'Chico', 'Groucho']
>>> surprise[0] = surprise[0].capitalize()   ###  先頭の要素を大文字に戻す
>>> surprise   ###  surpriseリストを表示
['Harpo', 'Chico', 'Groucho']
>>> 


"""