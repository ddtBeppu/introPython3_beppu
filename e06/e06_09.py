# 復習課題 6-9
# Bear, Rabbit, Octothropeの3つのクラスを定義しよう。それぞれについて唯一のメソッド、eats()を定義する。
# eats()は、'berries'(Bear)、'clover'(Rabbit)、'campers'(Octothrope)を返すものとする。
# それぞれのクラスからオブジェクトを作り、何を食べるのかを表示しよう。

# クラスBearを定義
class Bear():
    # eatsメソッドを定義
    def eats(self):
        # 何を食べるか、の値を返す
        return 'berries'

# クラスRabbitを定義
class Rabbit():
    # eatsメソッドを定義
    def eats(self):
        # 何を食べるか、の値を返す
        return 'clover'

# クラスOctothropeを定義
class Octothrope():
    # eatsメソッドを定義
    def eats(self):
        # 何を食べるか、の値を返す
        return 'campers'

# オブジェクトの作成
bear = Bear()
# オブジェクトの作成
rabbit = Rabbit()
# オブジェクトの作成
octothrope = Octothrope()

# メソッドを呼び出し、何を食べるかを表示
print(bear.eats())
# メソッドを呼び出し、何を食べるかを表示
print(rabbit.eats())
# メソッドを呼び出し、何を食べるかを表示
print(octothrope.eats())