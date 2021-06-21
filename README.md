
### sicence_literature_twitter_bot

## コンセプト

<img width="588" alt="Screen Shot 2021-06-20 at 23 55 23" src="https://user-images.githubusercontent.com/17135389/122705352-8612cf00-d223-11eb-88fb-426f01b0dde3.png">

## 説明

これはツィッタでCell誌のlatest articleを取得し、twitterに自動投稿するpythonプログラム(cell_twitter.py)です。

seleniumで最新のarticleのサイトを立ち上げて、タイトルと論文のurl取ってきて、twitter APIのtweepyツィートするようになっています。

Macで運用していましたので、croncで一定の時間にプログラムが稼働するようにし、botとしていました。

## 準備

1. Python 3.8, anaconda 3で動作確認しており、botはダイレクトにpythonのプログラムで動かしています。

2. twitter development accountを申請し、

CONSUMER_KEY

CONSUMER_SECRET

ACCESS_TOKEN 

ACCESS_TOKEN_SECRET 

を事前に取得しておいてください（https://koleoblog.info/how_to_make_tweetbot/）。

3. Chromedriver （https://sites.google.com/chromium.org/driver/home?authuser=0）

を事前にダウンロードして適当な場所にフォルダーを作って入れておいてください（プログラムの中で指定）

## 実際のtwitter bot

<img width="600" alt="Screen Shot 2021-06-20 at 23 55 36" src="https://user-images.githubusercontent.com/17135389/122705398-a3e03400-d223-11eb-81b3-bb701ba06ef7.png">

## 参考サイト＆文献

1. Cronについて：https://note.com/tokitky/n/nf99ffa77aae2

2. スクレイピングについて：https://www.amazon.co.jp/%E5%A2%97%E8%A3%9C%E6%94%B9%E8%A8%82Python%E3%81%AB%E3%82%88%E3%82%8B%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0-%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92-%E9%96%8B%E7%99%BA%E3%83%86%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF-%E3%82%AF%E3%82%B8%E3%83%A9%E9%A3%9B%E8%A1%8C%E6%9C%BA/dp/4802611927

3. スクレイピングについて（ちょいアングラですが色々書いてあります笑）:
https://review-of-my-life.blogspot.com/search/label/Python%2F%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0

4. twitter botについて：
https://aidemy.net/magazine/712/

## お問い合わせ
なにかありましたら、toshihiko.oki(at)gmail.com
までおしらせください((at)の部分を＠マークに変えてください)。


