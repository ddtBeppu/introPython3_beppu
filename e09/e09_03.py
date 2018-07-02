# 復習課題 9-3
# ホームページに対する要求を処理するhome()関数を追加しよう。
# It's aliveという文字列を返すようにセットアップしていただきたい。

from flask import Flask

# ウェブサイトの骨組み作成
app = Flask(__name__, static_folder='.', static_url_path='')

# '/'の後ろに、次の処理を追加
@app.route('/')
# ホームページに対する要求
def home():
    # 以下を表示
    return "It's alive"

# 実行
app.run(port=5000, debug=True)