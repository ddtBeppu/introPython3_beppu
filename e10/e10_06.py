# 復習課題 10-6
# multiprocessingを使って3個の別々のプロセスを作ろう。
# それぞれを1秒から5秒までのランダムな秒数だけ眠らせよう。

import numpy as np
import os
import multiprocessing
import time

# プロセスごとに実行
def do_this(what):
    # 今動いているプロセスがメッセージを表示する
    whoami(what)

def whoami(what):
    # 時刻表示のフォーマットを定義
    fmt = "%H:%M:%S"
    # システム標準時を取得
    t = time.localtime()
    # メッセージを表示
    print("I'm %s, in process %s, It's %s"  % (os.getpid(), what, time.strftime(fmt, t)))

# コマンドプロンプトからの実行
if __name__ == "__main__":
    # メッセージを表示。今動いているプロセスが何かを知らせる。
    whoami("I'm the main program.")
    for n in range(3):
        # プロセスを眠らせるランダムな秒数(1~5秒)を生成
        time_sleep = np.random.random() * 10 / 2

        # メッセージを表示。今動いているプロセスが何かを知らせる。
        p = multiprocessing.Process(target=do_this, args=("I'm function %s" % n,))
        # プロセス開始
        p.start()
        # プロセスを眠らせる
        time.sleep(time_sleep)
        # プロセスを終了する
        p.terminate()


# 実行結果
"""
NaotonoMacBook-puro:e10 naotobeppu$ python e10_06.py 
I'm 675, in process I'm the main program., It's 01:10:20
I'm 676, in process I'm function 0, It's 01:10:20
I'm 677, in process I'm function 1, It's 01:10:24
I'm 678, in process I'm function 2, It's 01:10:26
"""