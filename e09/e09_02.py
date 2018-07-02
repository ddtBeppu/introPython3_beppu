# 復習課題 9-2
# Flaskのデバッグ/再ロードできる開発用ウェブサーバーを使って骨組みだけのウェブサイトを作ろう。
# サーバーはホスト名localhost、ポート5000を使って起動すること。
# 手持ちのマシンがすでにポート5000をほかの目的に使っている場合には、別のポート番号を使ってもよい。

from flask import Flask

# ウェブサイトの骨組み作成
app = Flask(__name__, static_folder='.', static_url_path='')

# 実行
app.run(port=5000, debug=True)

# 実行結果
"""
NaotonoMacBook-puro:e09 naotobeppu$ python e09_02.py 
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 305-886-912
 """