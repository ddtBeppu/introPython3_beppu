# 復習課題 6-10
# Laser, Claw, SmartPhoneクラスを定義しよう。3つのクラスは唯一のメソッドとしてdoes()を持っている。
# does()は、'disintegrate'(Laser)、'crush'(Claw)、'ring'(SmartPhone)を返す。
# 次に、これらのインスタンス（オブジェクト）を一つづつ持つRobotクラスを定義する。Robotクラスのために、
# コンポーネントオブジェクトがすることを表示するdoes()メソッドを定義しよう。

# Laserクラスを定義
class Laser():
    # doesメソッドを定義
    def does(self):
        # 動作を表す値を返す
        return 'disintegrate'

# Clawクラスを定義 
class Claw():
    # doesメソッドを定義
    def does(self):
        # 動作を表す値を返す
        return 'crush'

# SmartPhoneクラスを定義
class SmartPhone():
    # doesメソッドを定義
    def does(self):
        # 動作を表す値を返す
        return 'ring'

# Robotクラスを返す
class Robot():
    # doesメソッドを定義
    def does(self):
        # laserオブジェクトを作成
        laser = Laser()
        # clawオブジェクトを作成
        claw = Claw()
        # smartPhoneオブジェクトを作成
        smartPhone = SmartPhone()
        
        # それぞれのオブジェクトの動作を、does()メソッドを実行ことにより表示
        # laser
        print(laser.does())
        # claw
        print(claw.does())
        # smartPhone
        print(smartPhone.does())

# robotオブジェクトを作成
robot = Robot()
# robotクラスの動作を表示
robot.does()