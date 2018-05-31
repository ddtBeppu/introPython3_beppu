# 復習課題 7-3
# UTF-8を使ってpop_bytesを文字列変数pop_stringにデコードし、pop_stringを表示しよう。pop_stringはmysteryと等しいか？

# 実行結果
NaotonoMacBook-puro:~ naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

# mysteryに値を代入
>>> mystery = '\U0001f4a9'
# mysteryの値を確認
>>> mystery
'💩'   ### <--
# エンコード
>>> pop_bytes = mystery.encode('utf-8')
# 値の確認
>>> pop_bytes
b'\xf0\x9f\x92\xa9'
### デコード
>>> pop_string = pop_bytes.decode('utf-8')
### 値の確認
>>> pop_string
'💩'  ### mysteryと等しい値であることが確認できる
>>> 
