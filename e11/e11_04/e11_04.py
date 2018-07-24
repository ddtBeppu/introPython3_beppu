# 復習課題 11-4
# テレビ番組「アイ・ラブ・ルーシー」で、ルーシーとエセルがチョコレート工場で働いていたシーンを覚えているだろうか。
# 紙で包むチョコが送られてくるベルトコンベアがスピードアップすると、彼女たちはついていけなくなる。
# Redisリストに様々なタイプのチョコをプッシュすると、ルーシーがこのリストに対してブロックを起こすポップを行うという
# シミュレーションを書いてみよう。彼女がチョコを1個包むのに0.5秒かかる。ルーシーがポップするたびに時刻とチョコのタイプと
# 残っているチョコが何個あるかを表示しよう。

###
# 以下のように、サーバーとクライアントを用意して処理を行った

# push_chocolate.py
NaotonoMacBook-puro:e11_04 naotobeppu$ python push_chocolates.py 
start pushing chocolates!!

# pop_by_lucy.py
NaotonoMacBook-puro:e11_04 naotobeppu$ python pop_by_lucy.py &
[1] 1475
NaotonoMacBook-puro:e11_04 naotobeppu$ start!
Got  b'dark' chocolate
0 remains.
It's  2018-07-24 10:41:12.384657
Got  b'regular' chocolate
0 remains.
It's  2018-07-24 10:41:12.886874
Got  b'quality handcrafted gourmet' chocolate
0 remains.
It's  2018-07-24 10:41:13.389005
Got  b'milk' chocolate
0 remains.
It's  2018-07-24 10:41:13.891169
Got  b'regular' chocolate
0 remains.
It's  2018-07-24 10:41:14.603943
Got  b'dark' chocolate
0 remains.
It's  2018-07-24 10:41:15.106103
Got  b'ultra couverture' chocolate
0 remains.
It's  2018-07-24 10:41:15.720296
Got  b'couverture' chocolate
0 remains.
It's  2018-07-24 10:41:16.225322
Got  b'quality handcrafted gourmet' chocolate
0 remains.
It's  2018-07-24 10:41:16.727540
Got  b'dark' chocolate
1 remains.
It's  2018-07-24 10:41:17.229705
Got  b'milk' chocolate
2 remains.
It's  2018-07-24 10:41:17.731069
Got  b'white' chocolate
1 remains.
It's  2018-07-24 10:41:18.233215
Got  b'milk' chocolate
1 remains.
It's  2018-07-24 10:41:18.735405
Got  b'quality handcrafted gourmet' chocolate
1 remains.
It's  2018-07-24 10:41:19.237567
Got  b'ultra couverture' chocolate
1 remains.
It's  2018-07-24 10:41:19.741123
Got  b'couverture' chocolate
2 remains.
It's  2018-07-24 10:41:20.243267
Got  b'quality handcrafted gourmet' chocolate
1 remains.
It's  2018-07-24 10:41:20.744991
Got  b'quality handcrafted gourmet' chocolate
1 remains.
It's  2018-07-24 10:41:21.247015
Got  b'ultra couverture' chocolate
1 remains.
It's  2018-07-24 10:41:21.748922
Got  b'white' chocolate
3 remains.
It's  2018-07-24 10:41:22.250997
Got  b'white' chocolate
4 remains.
It's  2018-07-24 10:41:22.753085
Got  b'regular' chocolate
3 remains.
It's  2018-07-24 10:41:23.254730
Got  b'regular' chocolate
5 remains.
It's  2018-07-24 10:41:23.756843
Got  b'regular' chocolate
6 remains.
It's  2018-07-24 10:41:24.258869
Got  b'dark' chocolate
5 remains.
It's  2018-07-24 10:41:24.760823
Got  b'quality handcrafted gourmet' chocolate
5 remains.
It's  2018-07-24 10:41:25.262403
Got  b'quality handcrafted gourmet' chocolate
6 remains.
It's  2018-07-24 10:41:25.764498
Got  b'couverture' chocolate
6 remains.
It's  2018-07-24 10:41:26.267994
Got  b'dark' chocolate
6 remains.
It's  2018-07-24 10:41:26.770784
Got  b'regular' chocolate
6 remains.
It's  2018-07-24 10:41:27.273642
Got  b'white' chocolate
7 remains.
It's  2018-07-24 10:41:27.775734
Got  b'dark' chocolate
8 remains.
It's  2018-07-24 10:41:28.277746
Got  b'milk' chocolate
9 remains.
It's  2018-07-24 10:41:28.783002
Got  b'milk' chocolate
10 remains.
It's  2018-07-24 10:41:29.284138
Got  b'ultra couverture' chocolate
10 remains.
It's  2018-07-24 10:41:29.786402
Got  b'regular' chocolate
10 remains.
It's  2018-07-24 10:41:30.288842
Got  b'ultra couverture' chocolate
10 remains.
It's  2018-07-24 10:41:30.790932
Got  b'ultra couverture' chocolate
9 remains.
It's  2018-07-24 10:41:31.292936
Got  b'quality handcrafted gourmet' chocolate
9 remains.
It's  2018-07-24 10:41:31.796809
Got  b'ultra couverture' chocolate
9 remains.
It's  2018-07-24 10:41:32.298923
Got  b'ultra couverture' chocolate
10 remains.
It's  2018-07-24 10:41:32.801052
Got  b'quality handcrafted gourmet' chocolate
9 remains.
It's  2018-07-24 10:41:33.305592
Got  b'couverture' chocolate
9 remains.
It's  2018-07-24 10:41:33.810583
Got  b'ultra couverture' chocolate
8 remains.
It's  2018-07-24 10:41:34.312654
Got  b'quality handcrafted gourmet' chocolate