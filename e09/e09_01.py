# 復習課題 9-1
# まだflaskをインストールしていないなら、今すぐインストールしよう。
# そうすれば、werkzeug、jinja2などのパッケージもインストールされる。

# 結果
# インストール済み

NaotonoMacBook-puro:e08_12 naotobeppu$ pip install flask
Requirement already satisfied: flask in /anaconda3/lib/python3.6/site-packages (0.12.2)
Requirement already satisfied: Werkzeug>=0.7 in /anaconda3/lib/python3.6/site-packages (from flask) (0.14.1)
Requirement already satisfied: Jinja2>=2.4 in /anaconda3/lib/python3.6/site-packages (from flask) (2.10)
Requirement already satisfied: itsdangerous>=0.21 in /anaconda3/lib/python3.6/site-packages (from flask) (0.24)
Requirement already satisfied: click>=2.0 in /anaconda3/lib/python3.6/site-packages (from flask) (6.7)
Requirement already satisfied: MarkupSafe>=0.23 in /anaconda3/lib/python3.6/site-packages (from Jinja2>=2.4->flask) (1.0)