<img src="https://raw.githubusercontent.com/amaotone/kotatsu/img/icon.png" width="200">

# こたつちゃん
herokuにデプロイして動かしているslack botです。

## 依存関係
- python 3.5.2
- slackbot 0.4.1 `pip install slackbot`

## 機能追加
`kotatsu/`以下にプラグインファイルを作ってください。

__動作確認方法__

1. [slack botを作成](https://slack.com/apps/new/A0F7YS25R-bots)
2. 作成したbotのAPI_TOKENをコピー
3. `$ export SLACK_API_TOKEN=【コピーしたAPI_TOKEN】`
4. `$ python run.py`
