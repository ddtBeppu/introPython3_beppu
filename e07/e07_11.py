# 復習課題 7-11
# ３個の連続した母音を含む全ての単語を見つけよう。

import re

mammoth = '''We have seen the Queen of cheese,
            Laying quietly at your ease,
            Gently fanned by evening breeze –
            Thy fair form no flies dare seize.
            All gaily dressed soon you'll go
            To the great Provincial Show,
            To be admired by many a beau
            In the city of Toronto.
            Cows numerous as a swarm of bees –
            Or as the leaves upon the trees –
            It did require to make thee please,
            And stand unrivalled Queen of Cheese.
            May you not receive a scar as
            We have heard that Mr. Harris
            Intends to send you off as far as
            The great World's show at Paris.
            Of the youth – beware of these -
            For some of them might rudely squeeze
            And bite your cheek; then songs or glees
            We could not sing o' Queen of Cheese.
            We'rt thou suspended from baloon,
            You'd caste a shade, even at noon;
            Folks would think it was the moon
            About to fall and crush them soon.'''


# r３個の連続した母音を含む全ての単語を検索
cs = re.findall(r'\W\w*[aeiou]{3}\w*', mammoth)
# 結果表示
print(cs)