# 復習課題 7-7
# テキストを操作するとき、正規表現はとても役に立つ。少し大きいテキストを用意して、正規表現の使い方をさまざまな角度から見ていこう。
# テキストは、James McIntyreが1866年に書いた「Ode on the Mammoth Cheese」で、オンタリオ州で作られ、世界ツアーに送り出された
# 7,000ポンドのチーズに対する歌である。これを全部入力するのはいやだと思うなら、サーチエンジンでテキストを探し出し、
# Pythonプログラムにカットアンドペーストすればよい。Project Gutenbergから直接入手する方法もある。テキストには、mammothという
# 名前を付けよう。

mammoth = "We have seen the Queen of cheese, \
            Laying quietly at your ease, \
            Gently fanned by evening breeze – \
            Thy fair form no flies dare seize. \
            All gaily dressed soon you'll go \
            To the great Provincial Show, \
            To be admired by many a beau \
            In the city of Toronto. \
            Cows numerous as a swarm of bees – \
            Or as the leaves upon the trees – \
            It did require to make thee please, \
            And stand unrivalled Queen of Cheese. \
            May you not receive a scar as \
            We have heard that Mr. Harris \
            Intends to send you off as far as \
            The great World's show at Paris. \
            Of the youth – beware of these - \
            For some of them might rudely squeeze \
            And bite your cheek; then songs or glees \
            We could not sing o' Queen of Cheese. \
            We'rt thou suspended from baloon, \
            You'd caste a shade, even at noon; \
            Folks would think it was the moon \
            About to fall and crush them soon."

