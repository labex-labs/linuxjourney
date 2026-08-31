---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "ja"
order_index: 5
title: "認証ログ"
description: "Linux の認証レコードを見つけ、解釈し、安全に相関する方法を学びます。"
meta_title: "認証ログ - ログ記録"
meta_description: "/var/log/auth.log ファイルを調べて Linux の認証ログを探索します。このガイドは、初心者向けにユーザーログインイベント、認証方法、アクセス問題のトラブルシューティング方法を解説し、Linux セキュリティの向上を支援します。"
meta_keywords: "Linux 認証，auth.log, Linux ログ，ユーザーログイン，Linux セキュリティ，システム認証，ログイントラブルシューティング，認証方法，初心者，チュートリアル，ガイド，セキュアログ"
---

認証ログは、ログイン試行、権限変更、session activity を説明する助けになります。セキュリティ上重要な証拠ですが、一行だけでユーザーの意図を確定したり、アカウント侵害を証明したりすることはほとんどできません。

## 認証レコードを見つける

Debian 系の syslog 設定は認証イベントを `/var/log/auth.log` へ、Red Hat 系は `/var/log/secure` へ route するのが一般的です。systemd journal が同じイベントを unit・process metadata とともに保持する場合や、集中ログが authoritative copy を持つ場合もあります。

ローカルの宛先を見つけ、関連サービスを問い合わせます。

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

SSH unit は `ssh.service` または `sshd.service` の場合があります。アカウントとアクセスの詳細が含まれるため、通常レコードの権限は制限されています。

:::single-choice{#auth-logs-file-location}
Linux の認証イベントは、必ずどこに保存されますか？

::option[ローカルのロギングポリシーが選んだ宛先。]{#auth-logs-local-policy .correct explanation="file、journal、集中 collector はディストリビューションと設定によって異なります。"}
::option[すべてのディストリビューションの `/var/log/auth.log`。]{#auth-logs-auth-only explanation="このパスは Debian 系では一般的ですが、普遍的ではありません。"}
::option[各ユーザーの shell history file 内。]{#auth-logs-shell-history explanation="shell history はユーザーコマンド履歴であり、システムの認証イベント保存先ではありません。"}
:::

## イベントを解釈する

従来形式のレコード例です。

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

時刻、host、発信 program、PAM module と service、要求された session user、発信元 UID を識別できます。これだけでは UID 1000 の背後にいる人物を特定できず、悪意ある操作とも証明できません。障害時点で有効な account record から UID を解決し、terminal、remote address、session、周辺イベントと相関させます。

:::single-choice{#auth-logs-uid-inference}
このレコードの `uid=1000` から何が分かりますか？

::option[root password が 1,000 回間違って入力された。]{#auth-logs-thousand-passwords explanation="この値は identity number であり、試行回数ではありません。"}
::option[開始プロセスに関連付けられた数値 account identity。]{#auth-logs-numeric-identity .correct explanation="操作を人へ帰属させるには、追加の session と account の証拠が必要です。"}
::option[イベントが TCP port 1000 から発生した。]{#auth-logs-port explanation="UID はネットワークポートの field ではありません。"}
:::

## 成功と失敗を調査する

限定した時間範囲で、accepted と rejected の試行をどちらも検索します。SSH では connection source、authentication method、target account、session open/close、service restart も調べます。失敗の繰り返しは、ユーザーの誤り、古い認証情報を持つ自動処理、scan、attack のいずれでも起こります。頻度だけで一つに決めることはできません。

`last` と `lastb` は、維持されていれば `wtmp` と `btmp` のレコードを要約できますが、これらの binary database にも retention と integrity の限界があります。journal、syslog、集中ログと照合してください。

:::single-choice{#auth-logs-failed-attempts}
失敗ログインの繰り返しは何と相関させるべきですか？

::option[ディスクの空き容量だけ。]{#auth-logs-disk-space explanation="容量から、認証試行の source、target、method は特定できません。"}
::option[source、target account、method、timing、成功 session。]{#auth-logs-correlated-fields .correct explanation="これらの詳細は、設定誤り、ユーザー操作ミス、scan、不正アクセスの区別に役立ちます。"}
::option[アカウントが確実に侵害されたという結論。]{#auth-logs-certain-compromise explanation="失敗には善意・悪意の複数原因が考えられます。"}
:::

## 保存して対応する

incident が疑われる場合、host time と timezone を記録し、元ログと metadata を保持し、export copy を安全に保護します。証拠をその場で編集してはいけません。account lock、firewall change、session termination は正当なアクセスを中断したり、攻撃者へ気付かせたりする可能性があるため、incident-response process に従い、復旧経路を維持します。

:::single-choice{#auth-logs-preservation}
調査中の認証証拠はどのように扱うべきですか？

::option[分かりやすくするため、元ファイルの疑わしい行を編集する。]{#auth-logs-edit-original explanation="発生元を変更すると証拠の integrity が損なわれます。"}
::option[誰でもユーザーを特定できるよう、完全なログを公開する。]{#auth-logs-publish explanation="認証レコードは機密性の高い identity と infrastructure の詳細を露出する場合があります。"}
::option[原本を保持し、export copy を保護する。]{#auth-logs-preserve .correct explanation="セキュリティログには integrity と confidentiality の両方が重要です。"}
:::

## まとめ

これで、一つのレコードから分かることを過大評価せず、認証イベントを調べられます。

1. ローカルで設定された認証ログの宛先を見つける。
2. identity、service、method、session field を文脈の中で解釈する。
3. 保存された複数情報源で、失敗・成功 activity を相関させる。
4. 証拠を保持し、中断を伴う対応操作を調整する。
