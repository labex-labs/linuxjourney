---
lesson_id: "system-logging"
course_id: "logging"
lang: "ja"
order_index: 1
title: "システムロギング"
description: "Linux のログ発生元、collector、保存先、閲覧ツールが連携する仕組みを学びます。"
meta_title: "システムロギング - ログ記録"
meta_description: "システムロギングを理解することで、Linux を学ぶ最良の方法を見つけましょう。このガイドでは、syslog、rsyslogd、および/var/log 内のログファイルの見つけ方と読み方について説明します。無料のオンライン Linux コースの重要な要素です。"
meta_keywords: "linux を学ぶ方法，linux を学ぶ最良の方法，linux システムロギング，syslog, rsyslogd, var log, システムログ，linux コマンドラインを学ぶ，linux を学ぶための最良のリソース"
---

ログは、カーネル、サービス、アプリケーション、セキュリティコンポーネントが発したイベントを記録します。トラブルシューティングや監査に役立ちますが、それは収集が機能し、時刻を正しく理解し、必要な情報源が含まれている場合に限ります。

## ログメッセージの流れを追う

ロギングの経路には、いくつかの異なる部分があります。

1. 発生元がイベントを出力する。
2. collector が受信し、情報を付加する。
3. routing と retention の規則が保存先または転送先を選ぶ。
4. viewer が保存済みレコードを問い合わせる。

systemd ホストでは、`systemd-journald` がサービスの標準出力、カーネルメッセージ、journal-native または syslog メッセージを収集するのが一般的です。rsyslog などの syslog daemon もメッセージを受け取り、従来のテキストファイルへ書いたり転送したりできます。アプリケーションが独自ファイルや外部 telemetry を管理する場合もあります。

:::single-choice{#system-logging-distinct-roles} 受信したメッセージをどこへ保存または転送するか決めるものはどれですか？

::option[端末の現在の作業ディレクトリ。]{#system-logging-cwd explanation="シェルのディレクトリは、システム全体のロギング経路を定義しません。"}
::option[動作中カーネルイメージのファイル名。]{#system-logging-kernel-file explanation="カーネルはメッセージを発信できますが、イメージのファイル名は routing policy ではありません。"}
::option[routing と retention の設定。]{#system-logging-routing .correct explanation="収集から保存までの規則が、宛先と保持動作を決めます。"}
:::

## 利用可能なログを見つける

すべてのホストに同じファイルがあると想定せず、稼働中のロギングサービスとローカル設定を調べます。

```bash
$ systemctl --type=service --state=running | grep -E 'journal|syslog'
$ ls -la /var/log
$ journalctl --disk-usage
```

互換性のある routing を使う Debian 系では `/var/log/syslog` が一般的で、ほかの環境では `/var/log/messages` がよく使われます。journal-only ホストではどちらもない場合があります。アプリケーション文書と unit 設定から、追加の宛先を特定できます。

:::single-choice{#system-logging-file-absence} `/var/log/syslog` がない場合、必ず何を意味しますか？

::option[ホストが別の設定済みロギング先を使っている可能性がある。]{#system-logging-other-destination .correct explanation="journal-only system や別の syslog policy では、このファイルを作る必要がありません。"}
::option[カーネルが一度もメッセージを出していない。]{#system-logging-no-kernel explanation="カーネルのレコードは journal や別の宛先に存在する場合があります。"}
::option[すべてのアプリケーションが停止している。]{#system-logging-apps-stopped explanation="一つのパスがないだけで、アプリケーション状態は判断できません。"}
:::

## Journal を問い合わせる

journal 全体を出力せず、範囲を限定した問い合わせから始めます。

```bash
$ journalctl -b -p warning
$ journalctl -u ssh.service --since '1 hour ago'
```

`-b` は現在の boot、`-p` は priority、`-u` は unit で絞り込みます。unit 名と保存済み boot はホストごとに異なります。`journalctl --list-boots` で利用可能な boot を確認し、問題を再現しながら `journalctl -f` で新しいレコードを追います。

:::single-choice{#system-logging-current-boot} `journalctl` の問い合わせを現在の boot に限定するオプションはどれですか？

::option[`-b`]{#system-logging-boot-option .correct explanation="引数なしの boot selector は現在の boot を選びます。"}
::option[`-u`]{#system-logging-unit-option explanation="これは systemd unit で絞り込みます。"}
::option[`-f`]{#system-logging-follow-option explanation="これは新しく追加されるレコードを追跡します。"}
:::

## 文脈の中でレコードを読む

従来の syslog 形式の行は次のようになります。

```text
Jan 27 07:41:32 icebox anacron[4650]: Job `cron.weekly' started
```

timestamp、host、program と PID、その後に message が続きます。message text はアプリケーション出力であり、保証された構造化事実として扱わないでください。timezone、時計同期、boot ID、PID の再利用、イベント直前直後のレコードを確認します。journal field は、表示テキストだけより強い識別情報を提供できる場合があります。

ログにはユーザー名、アドレス、パス、token などの機密データが含まれる可能性があります。最小権限でアクセスし、export は redact し、調査中は原本と timestamp を保持してください。

:::single-choice{#system-logging-export-safety} ログの抜粋を外部共有する前に何をすべきですか？

::option[すべての timestamp を無作為な値へ置き換える。]{#system-logging-random-time explanation="時間情報を壊すと相関分析ができなくなり、適切な redaction にはなりません。"}
::option[秘密情報と機密性の高い識別情報がないか確認する。]{#system-logging-review-sensitive .correct explanation="ログには運用情報や個人データが含まれることが多く、管理された redaction が必要です。"}
::option[元のログを誰でも書き込み可能にする。]{#system-logging-world-writable explanation="アクセス制御を弱めると、完全性を損ない、追加データを露出する可能性があります。"}
:::

## まとめ

これで、普遍的な一つの保存パスを想定せず、Linux のログを見つけて問い合わせられます。

1. イベント発生元、collector、routing、storage、viewer を区別する。
2. ホストで稼働中のロギング設定を調べる。
3. unit、boot、time、priority で範囲を絞った journal 問い合わせを使う。
4. 文脈の中でレコードを相関させ、機密ログデータを保護する。
