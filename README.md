# nikoha（にこは）

[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/42997991/98469505-6e9e4d00-2223-11eb-8e53-bad8a8e93a8e.png)](https://youtu.be/sKh3GzVOxkY)

## 製品概要

### 2人の笑顔ではんこを押せる、オンライン提出用の婚姻届作成サービス「nikoha（にこは）」
<img src="https://user-images.githubusercontent.com/42997991/98469508-7100a700-2223-11eb-889d-583894d0046b.png" width="750px">

### デモ

https://nikoha.herokuapp.com/

<br>

## 製品開発のきっかけ、課題

先月、行政手続きでの文書のデジタル化や押印廃止についてのニュースが盛り上がりました。
面倒な「この書類にはんこ下さい」といったやり取りから今後解放されることに喜んだ人はかなり多かったのではないかと思います。

しかし、あらゆる文書がデジタル化されはんこを押す必要がなくなることを、すべての国民が望んでいるのでしょうか？<br>
手続きの簡素化と引き換えに、何か大切な価値が失われてしまう文書はないでしょうか？

私たちは「婚姻届」に着目しました。<br>
婚姻届は、これから夫婦になる2人が署名・押印することで役場に自分の意思を示すという機能と、押印することで結婚の幸せを実感できるという価値、人生の節目に決意を新たにできるという価値を持ちます。
デジタル化と押印廃止によってこれらの価値が失われてしまうと、悲しい思いをする人も少なくないはずです。<br>
実際に様々なメディアが行なったアンケートでは、「婚姻届も結婚のセレモニーの一つなので悲しい」「オンライン提出になると楽だけど、手軽すぎると結婚が軽いものになる」といった反対意見が見られます。

この、「本人の意思確認をしつつ文書のデジタル化を進めたい」「婚姻届にはんこを押すことの価値はそのまま残したい」というコンフリクトを解消すべく、私たちは婚姻届作成サービス「nikoha（にこは）」を開発することにしました。

<img src="https://user-images.githubusercontent.com/42997991/98469511-7231d400-2223-11eb-8689-36d237db95be.png" width="750px">
<br>

## 製品説明

「nikoha」は、新郎新婦がカメラに向かって笑顔でポーズをとることで、デジタル婚姻届にハンコを押すことができるウェブアプリです。

まず、ユーザーが必要事項をフォームで記入すると、その内容が書き込まれた婚姻届のpdfファイルを発行します。

次に、ユーザーがカメラを起動し2人で笑顔でカメラに映ると、笑顔=本人の意思を確認し、はんこを押すアニメーションと同時に指定したはんこの画像を婚姻届pdfの上に追加します。

さらに、希望すればユーザーがカメラに映った時の写真を婚姻届の空きスペースに載せることもでき、世界に一つだけの特別な婚姻届を完成させることも可能です。

このようにして、ユーザーは完成したpdfをすぐに役場に提出することができます。

<img src="https://user-images.githubusercontent.com/42997991/98469501-680fd580-2223-11eb-9b00-397bcc71788e.png" width="750px">
<img width="750px" alt="カメラ" src="https://user-images.githubusercontent.com/42997991/98470046-875c3200-2226-11eb-90c0-4ca6d6fd51df.png">

<br>

## 特長

#### 1. ただ顔を認識するのではなく、笑顔を認識することではんこが押される！

人の顔がカメラに映ったら押印する、だけでは不正届出の懸念もあります。
nikohaでは、ただ顔を認識するのではなく、笑顔をカメラに向けるというユーザーの能動的な行動を押印のトリガーとしているため、「本人の意思確認」という行政上のはんこの役割を再現しています。

#### 2. 最高の笑顔を記念に残せる！

笑顔が認識されるとその瞬間の画像を保存。
画像は婚姻届にも添付することができるので、2人だけの婚姻届を完成させて結婚の幸せを感じることができます。
また、単にウェブ上のフォームから文書を提出するのではなく、笑顔の写真を撮るというイベントを経ることで、婚姻届の提出を機械的な手続きにせず、入籍日を思い出に残るものにしています。  


#### 3. 婚姻届作成から押印までワンストップで完了できる！

現在のところ、デジタル文書の上にはんこを押すには、まず文書のデータを作成し、別途はんこの画像データを用意する必要があります。
これは、PCや文書作成ソフトに使い慣れていないユーザーにとってはハードルの高いことです。
nikohaなら、必要事項の記入から押印まで、全てnikohaだけで完結させられます。

<br>
  

## 解決出来ること

<img src="https://user-images.githubusercontent.com/42997991/98469509-71993d80-2223-11eb-8a7f-2047d3161d93.png" width="750px">

#### 本人の意思確認ができる機能を持たせて文書のデジタル化を進める
特徴1でも述べましたが、笑顔をカメラに向けるというユーザーの能動的な行動を押印のトリガーとしているため、「本人の意思確認」という行政上のはんこの役割を再現しています。

#### 婚姻届にはんこを押すことの価値はそのまま残す
フォームに必要事項を記入しマイナンバーで本人確認…のように誰にでもできる操作ではなく、カップルが二人でカメラに映るという情緒的なステップを盛り込むことで、心を込めてはんこを押した時のような雰囲気を疑似体験できるようにしました。
これにより、特徴2でも述べましたが、婚姻届の提出を機械的な手続きにせず、入籍日を思い出に残るものにしています。

<br>

## 今後の展望

* なりすまし防止のため、身分証明書の写真と照らし合わせた顔認証を実装すれば、より「本人の意思確認」としての本プロダクトの機能を強められます。

* フォーム入力による文書作成システムと、顔認証による押印システムは、婚姻届以外のデジタル文書にも応用できます。

* 現在はフォームに入力された苗字からはんこの画像を生成していますが、自分ではんこの画像をアップロードできるようにすれば、はんこの画像データが現在のはんこに変わる商材となり、印章業界のピンチも救えるのではないかと考えています。

* 婚姻届pdfに、ユーザーが描いた好きな絵をcanvasで貼り付けられる機能を実装して、より自分たちオリジナルの婚姻届を作れる体験を提供したいと考えています。

<br>

## 注力したこと（こだわり等）

* アプリケーションのUIとロゴのデザイン。「はんこ」は日本独自の文化なので、和婚をイメージした配色で画面を構成しています。婚姻届の入力フォームは、無機的にならないよう本物の婚姻届に近い見た目になるようにしました。

* 笑顔が100%になったとき再生される、はんこを押すアニメーション。ユーザー側から画面の中の婚姻届に向けてはんこを押したように見せるため、はんこの画像が手前から画面奥に向かってアニメーションするようにしました。

* 笑顔の程度がリアルタイムで横のメーターに表示される。顔のマークが動いて笑顔の程度を表すようにし、はんこを押す前に楽しい雰囲気を演出できるようにしました。

* どんな名字でも印鑑を生成することが可能です。ユーザーが入力した名字を自動で円の中心に配置し、印鑑の画像を生成するジェネレーターを1から開発しました。

<br>

## 開発技術
### 活用した技術
#### フレームワーク・ライブラリ・モジュール
* flask
* opencv
* jquery
* javascript

#### API・データ
* [face-api.js](https://github.com/justadudewhohacks/face-api.js)

#### デバイス
* Webカメラ

### 独自技術
#### ハッカソンで開発した独自機能・技術
* アプリケーションのデザイン
* [リアルタイム笑顔判定](https://github.com/jphacks/C_2012/blob/develop/static/js/smilecamera.js)
  * リアルタイムで笑顔の状態を測定。
  * 横のメーターに表示。
* [印鑑ジェネレーター](https://github.com/jphacks/C_2012/blob/develop/create_stamps.py)
  * 入力された名字から自動で印鑑を生成。
* [婚姻届(png)に必要事項、印鑑、写真を合成](https://github.com/jphacks/C_2012/blob/develop/create_pdf.py)
