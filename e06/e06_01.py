# 復習課題 6-1
# 中身のないThingクラスを作り、表示しよう。次に、このクラスからexampleというオブジェクトを作り、これも表示しよう。
# 表示される値は同じか、それとも異なるか。

# Thingクラスの作成
class Thing():
    # 中身を持たないクラスとする
    pass

# Thing()クラスを表示
print("class Thing() = ", Thing())

# exampleオブジェクトを作成
example = Thing()
# exampleオブジェクトを表示
print("example = ", example)


# 実行結果
# 表示される値は等しいことがわかる
"""

NaotonoMacBook-puro:e06 naotobeppu$ python e06_01.py 
class Thing() =  <__main__.Thing object at 0x102ad4128>
example =  <__main__.Thing object at 0x102ad4128>

"""