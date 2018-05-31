# 復習課題 7-4
# 古いスタイルの書式指定を使って次の詩を表示し、置換部分に'roast beef', 'ham', 'head', 'clam'を挿入しよう。
#
# My kitty cat likes %s,
# My kitty cat likes %s,
# My kitty cat fell on his %s,
# And now thinks he's a %s.

# 古いスタイルの書式指定にて文字列を表示
print("My kitty cat likes %s,\
    \nMy kitty cat likes %s,\
    \nMy kitty cat fell on his %s,\
    \nAnd now thinks he's a %s."
    % ('roast beef', 'ham', 'head', 'clam')) # 置換部分を入力


# 実行結果
"""
NaotonoMacBook-puro:e07 naotobeppu$ python e07_04.py 
My kitty cat likes roast beef,    
My kitty cat likes ham,    
My kitty cat fell on his head,    
And now thinks he's a clam.

"""