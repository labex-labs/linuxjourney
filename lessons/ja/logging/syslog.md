---
lesson_id: "syslog"
course_id: "logging"
lang: "ja"
order_index: 2
title: "syslog"
description: "syslog の facility、severity、routing rule、logger コマンドの仕組みを学びます。"
meta_title: "syslog - ロギング"
meta_description: "Linux の syslog と rsyslog について学び、システムログの管理方法、および logger コマンドの使用方法を習得します。この初心者向けのチュートリアルを始めましょう！"
meta_keywords: "syslog, rsyslog, Linux ログ，logger コマンド，/var/log/syslog, Linux チュートリアル，初心者 Linux, システムロギング"
---

syslog は、多くの Unix 系システムで使われるメッセージモデルとトランスポートの規約を定義します。rsyslog はその実装の一つで、メッセージの受信、filter、変換、保存、転送を行えます。`systemd-journald` と共存する場合があり、どちらの名前も、全アプリケーションがその経路を使うことを意味しません。

## Facility と Severity

syslog メッセージは、発生元の大まかな分類を表す facility と、emergency から debug までの severity を持ちます。代表的な facility には `auth`、`cron`、`daemon`、`kern`、`mail`、`user`、`local0` から `local7` があります。

severity には順序があります。従来の selector 構文では、`daemon.warning` は通常 warning だけでなく、それ以上に重大な daemon メッセージすべてに一致します。従来構文に対応する実装では、`daemon.=warning` のように equals modifier を使うと完全一致になります。

:::single-choice{#syslog-warning-selector}
従来の `daemon.warning` という selector は通常何に一致しますか？

::option[テキストに daemon という単語を含むメッセージだけ。]{#syslog-text-daemon explanation="この selector を動かすのは message text の検索ではなく、facility metadata です。"}
::option[全 facility のすべての debug メッセージ。]{#syslog-all-debug explanation="selector は daemon facility と severity threshold に限定されます。"}
::option[warning および、それより重大な daemon メッセージ。]{#syslog-warning-or-higher .correct explanation="priority selector は指定 severity と、それより緊急度の高い level を含みます。"}
:::

## rsyslog のルールを読む

rsyslog は一般に、main file と `/etc/rsyslog.d/` 以下の snippet を読み込みます。従来の rule は selector の後に action が続きます。

```text
auth,authpriv.*          /var/log/auth.log
*.*;auth,authpriv.none  -/var/log/syslog
kern.*                  /var/log/kern.log
```

最初の行は二つの authentication facility の全 priority を route します。二番目は広くメッセージを選択し、それらの facility を除外します。三番目は kernel facility のメッセージを route します。file action の先頭 `-` は通常 asynchronous write を要求し、除外を意味しません。

production routing を変える前に、include される全ファイルを確認し、インストール済みバージョンが使う正確な構文を検証してください。

:::single-choice{#syslog-selector-action}
従来の rsyslog rule で action に当たるのはどれですか？

::option[左側の facility と severity の式。]{#syslog-left-selector explanation="その部分はメッセージを選択します。"}
::option[右側の宛先または操作。]{#syslog-right-action .correct explanation="action は、選択済みレコードを file、remote target などのどの出力へ送るか決めます。"}
::option[パッケージバージョンを説明するコメント。]{#syslog-comment-version explanation="コメントはメッセージを route しません。"}
:::

## テストメッセージを送る

`logger` を使い、識別可能な tag と priority を持つ管理されたテストを送ります。

```bash
$ logger -p user.notice -t lesson-test 'routing check 2026-08-31T10:00'
```

次に、想定する宛先を問い合わせます。

```bash
$ journalctl -t lesson-test --since '5 minutes ago'
```

forwarding と routing の設定によっては、同じイベントが journal と text file の両方に現れます。`logger -s` はメッセージを標準エラーにもコピーしますが、永続保存の証明にはなりません。

:::single-choice{#syslog-logger-tag}
`logger -t lesson-test` は送信メッセージへ何を追加しますか？

::option[古いテストレコードを削除する要求。]{#syslog-tag-delete explanation="このオプションは識別 tag を設定し、retention は管理しません。"}
::option[`lesson-test` というメッセージ tag。]{#syslog-tag-identifier .correct explanation="固有 tag によって、設定済み宛先内の管理されたイベントを見つけやすくなります。"}
::option[5 分間の配送遅延。]{#syslog-tag-delay explanation="tag option に配送間隔は含まれません。"}
:::

## Routing を変更して検証する

変更前に現在の設定を保存し、下流の consumer を特定します。実装の configuration-check mode で構文を検証します。一般的な例は次のとおりです。

```bash
$ sudo rsyslogd -N1
```

検証後にだけ、service manager からサービスを reload します。新しい tag 付きメッセージを送り、必要な全宛先を確認し、サービス状態と内部エラーログを調べます。構文上有効でも、広すぎる route、レコード重複、機密データ露出を起こす rule はあります。

信頼できないネットワークをログが横断する場合、remote forwarding には認証・暗号化された transport を使います。UDP 配送にはエンドツーエンドの acknowledgement がありません。重要な audit 要件には、queue、loss、integrity、access control、receiver outage を考慮した設計が必要です。

:::single-choice{#syslog-change-verification}
新しい routing rule が機能する十分な証拠はどれですか？

::option[設定ファイルの更新時刻が新しい。]{#syslog-mtime explanation="timestamp から有効な構文や配送は証明できません。"}
::option[送信側から受信側へ ping が届く。]{#syslog-ping explanation="ネットワーク到達性だけでは、ロギングプロトコルや保存経路を検証できません。"}
::option[検証に合格し、tag 付きテストが全予定宛先へ届く。]{#syslog-validate-and-test .correct explanation="静的検証と、観測できるエンドツーエンドのイベントの両方が必要です。"}
:::

## まとめ

これで、メッセージ metadata から設定済み宛先まで、syslog routing をテストできます。

1. facility と順序付き severity level を区別する。
2. selector と action を分けて読む。
3. `logger` で tag と priority を持つイベントを送る。
4. 設定を検証し、配送をエンドツーエンドで確認する。
