# codefamily-serverless
## Refferemce article
Zennに投稿した、「CodePipelineとCloudformationで、API Gatewayをビルド【CodeFamily Practices 5/7】」に掲載したコードを収録したリポジトリ。

<a href="https://zenn.dev/lifewithpiano/articles/codefamily_cloudformation"><img src="images/codefamily_cloudformation_zenn.png" width="50%">
## Summary
API GatewayとLambdaの挙動を確認するための、シンプルな構成。

* ソースステージをCodeCommit、ビルドステージをCodeBuildに設定したCodePipelineを構築。
* ビルドはCloudeFormation(SAM)を使用。
* API Gatewayへメールのタイトルと本文を指定してアクセスをすると、SNSトピックのサブスクリプションへメールを送信
* 送信に成功すると、サブジェクトとメッセージの値をレスポンス。

<img src="images/api-cf.drawio.png" width="50%">

* __コマンド__

```
curl -X POST \
'https://Your-domain-name' \
-d $'{"sub": "テスト", "mes": "動作異常なし。"}'
```
* __メール__

<img src="images/apicf16.png" width="50%">