# 復習課題 7-1
# mysteryというUnicode文字列を作り、'\U0001f4a9'という値を代入して、mysteryを表示してみよう。
# またmysteryのUnicode名を調べよう。


# 実行結果
NaotonoMacBook-puro:e06 naotobeppu$ python3
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 12:04:33) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

# mysteryに値をだいにゅう
>>> mystery = '\U0001f4a9'
# mysteryを表示
>>> mystery
'💩'
# モジュールをインポート
>>> import unicodedata
# mysteryのUnicode名を設定
>>> name = unicodedata.name(mystery)
# Unicode名を返す
>>> name
'PILE OF POO'
>>> 
