# 復習課題 6-3
# さらにもう一つクラスを作ろう。名前はもちろんThing3だ。
# 今度は、lettersというインスタンス(オブジェクト)属性に'xyz'という値を代入し、lettersを表示しよう。
# これを行うためには、クラスからオブジェクトを作ることが必要か。

# クラスの作成
class Thing3():
    # 中身のないクラスとする
    pass

# インスタンスの生成
letters = Thing3()
# インスタンスに値を代入
letters = 'xyz'

#Thing3 = 'xyz'

# 値を表示
print(letters)
#print(Thing3)


# 実行結果
# クラスからオブジェクトを作らなくても同じ結果となった。
"""

NaotonoMacBook-puro:e06 naotobeppu$ python e06_03.py 
xyz


"""