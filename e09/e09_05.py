# 復習課題 9-5
# home.htmlテンプレートを使うようにサーバーのhome()関数を書き換えよう。
# home()関数には、thing, height, colorの３個のGET引数を渡すこと。

from flask import Flask, render_template, request

# ウェブサイトの骨組み作成
app = Flask(__name__) 

# '/'以下を開始として、処理を行う
@app.route('/')
# サーバーに要求を送る
def home():
    # GET引数thingを定義
    thing = request.values.get('thing')
    # GET引数heightを定義
    height = request.values.get('height')
    # GET引数colorを定義
    color = request.values.get('color')
    # 要求を送信
    return render_template('home.html', thing=thing, height=height, color=color)

# 実行
app.run(debug=True)