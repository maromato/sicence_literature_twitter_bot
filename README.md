
### sicence_literature_twitter_bot

## コンセプト

<img width="588" alt="Screen Shot 2021-06-20 at 23 55 23" src="https://user-images.githubusercontent.com/17135389/122705352-8612cf00-d223-11eb-88fb-426f01b0dde3.png">

## 説明

これはツィッタでCell誌のlatest articleを取得し、twitterに自動投稿するpythonプログラム(cell_twitter.py)です。
seleniumで最新のarticleのサイトを立ち上げて、タイトルと論文のurl取ってきて、twitter APIのtweepyツィートするようになっています。
Macで運用していましたので、croncで一定の時間にプログラムが稼働するようにし、botとしていました。

## 準備

Python 3.8, anaconda 3で動作確認しており、botはダイレクトにpythonのプログラムで動かしています。
twitterのオーソライゼーション、アクセストークンを事前に申請しておいてください。
Chromedriver https://sites.google.com/chromium.org/driver/　
を事前にダウンロードして適当な場所にフォルダーを作って入れておいてください（プログラムの中で指定）

## 実際のtwitter bot

<img width="600" alt="Screen Shot 2021-06-20 at 23 55 36" src="https://user-images.githubusercontent.com/17135389/122705398-a3e03400-d223-11eb-81b3-bb701ba06ef7.png">



