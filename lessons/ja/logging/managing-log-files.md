---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "ja"
order_index: 6
title: "ログファイルの管理"
description: "logrotate で安全なテキストログ rotation を設定、テスト、検証する方法を学びます。"
meta_title: "ログファイルの管理 - ロギング"
meta_description: "logrotate の初心者向けガイドで Linux ログ管理をマスターしましょう。ログローテーションがディスク容量を節約する方法、設定方法、システムのログを整理する方法を学びます。"
meta_keywords: "logrotate, Linux ログ，ログ管理，ログローテーション，Linux チュートリアル，初心者，ガイド，ディスク容量"
---

上限のないテキストログはファイルシステムを使い切る可能性があり、削除が積極的すぎると運用や compliance に必要な証拠を失います。`logrotate` は、設定済みの size、time、compression、ownership、retention policy をファイルベースのログへ適用します。

## Rotation を理解する

一般的な rotation は、有効ファイルを rename し、代わりを作り、必要に応じてアプリケーションへ reopen を要求し、古い世代を圧縮し、retention を超えたファイルを削除します。これらの手順は設定に依存します。保持コピーも削除・破損し、同じホストとともに失われるため、rotation は backup ではありません。

:::single-choice{#logrotate-not-backup} log rotation が backup や archival の代わりにならないのはなぜですか？

::option[rotation 済みファイルもローカル retention とホスト障害の影響を受けるから。]{#logrotate-local-retention .correct explanation="rotation は作業ログの世代を制御しますが、独立した永続コピーは作りません。"}
::option[rotation が image file しか処理できないから。]{#logrotate-images explanation="この utility は主に log file を対象に設計されています。"}
::option[すべての rotation が全世代を永久に保持するから。]{#logrotate-forever explanation="retention rule は通常、古い世代を削除します。"}
:::

## 設定を見つける

main file は通常 `/etc/logrotate.conf` で、package または application snippet は `/etc/logrotate.d/` 以下にあります。単純化した policy は次のようになります。

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

これは daily evaluation、7 世代の retention、1 世代遅らせた compression、log が存在しないまたは空の場合の許容、明示的な mode と ownership の新規ファイルを要求します。実際の rotation は、記録された state と scheduler が logrotate を呼び出す方法にも依存します。

:::single-choice{#logrotate-rotate-seven} `rotate 7` は何を指定しますか？

::option[policy の下で最大 7 世代の rotation 済みファイルを保持する。]{#logrotate-seven-generations .correct explanation="設定された retention を超えると、古い世代が削除されます。"}
::option[アプリケーションを一日 7 回実行する。]{#logrotate-run-seven explanation="この directive が制御するのは保持世代であり、アプリケーションの実行ではありません。"}
::option[全 rotation 済みファイルの権限を mode 0007 にする。]{#logrotate-mode-seven explanation="file mode は `create` などの directive で制御します。"}
:::

## 書き込み側と調整する

ログを rename した後も、daemon が開いたままの file descriptor を通じて旧ファイルへ書き続ける場合があります。`postrotate` script は、文書化された reload または reopen signal を送ることがよくあります。正確なアプリケーション動作を確認し、script の範囲を限定してください。

`copytruncate` はログを reopen できないアプリケーション向けに、ファイルをコピーして元ファイルをその場で truncate します。copy と truncate の間に write が失われたり重複したりする可能性があるため、普遍的に安全な default ではなく妥協策です。

:::single-choice{#logrotate-open-descriptor} rotation 後にアプリケーションへ reopen signal が必要な場合があるのはなぜですか？

::option[開いている descriptor が rename 済みファイルを参照し続けるから。]{#logrotate-descriptor-renamed .correct explanation="reopen すると、以後の write が新しく作られた有効パスを使います。"}
::option[compression が自動的に全アプリケーションプロセスを停止するから。]{#logrotate-compression-stops explanation="compression は writer の process lifecycle を自動管理しません。"}
::option[カーネルが二つ目のログファイル作成を禁止するから。]{#logrotate-kernel-forbids explanation="複数のログファイルは存在できます。問題は writer がどの inode を開いているかです。"}
:::

## 有効化前にテストする

debug mode を使い、ファイルを rotation せず判断を調べます。

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

debug 出力は、本番実行時に permission、script、free space、application reopen が成功することを証明しません。新しい rule は管理された環境でテストし、実行後に active file、rotated generation、ownership、compression、application output、logrotate status を確認します。`-f` は rotation を強制する状態変更オプションで、dry run と取り違えないでください。

:::single-choice{#logrotate-debug-mode} `logrotate -d` から何が得られますか？

::option[期限切れログすべての恒久的な削除。]{#logrotate-debug-delete explanation="debug mode は rotation を行わず、予定する判断を報告します。"}
::option[policy を無視した強制 production rotation。]{#logrotate-debug-force explanation="force option は状態を変更する `-f` です。"}
::option[log file と state を変更しない診断評価。]{#logrotate-debug-dry .correct explanation="構文と判断を最初に確認する適切な方法で、その後に管理された実動検証を行います。"}
:::

## ほかの Store を考慮する

logrotate が管理するのは policy で指定した file です。systemd journal は独自の size と retention 設定を持ち、database と remote logging service にも別の lifecycle control があります。filesystem capacity と logging health を監視し、停止した writer や失敗した rotation を容量枯渇前に検出してください。

:::single-choice{#logrotate-journal-retention} logrotate rule は systemd journal の retention も自動的に強制しますか？

::option[いいえ。journal storage には独自の設定と上限があります。]{#logrotate-journal-separate .correct explanation="logrotate が管理するのは、file policy で選択したパスだけです。"}
::option[はい。全ログが一つの retention engine を共有するからです。]{#logrotate-all-logs explanation="file rotation と journal retention は別の仕組みです。"}
::option[はい。ただしテキストログがない場合だけです。]{#logrotate-journal-fallback explanation="テキストログの有無で二つの retention system が統合されることはありません。"}
:::

## まとめ

これで、archival と取り違えずに file-log rotation policy を設計・検証できます。

1. 容量、運用、retention の要件を釣り合わせる。
2. 世代、compression、ownership、空ファイルの動作を定義する。
3. descriptor を開いたままにするアプリケーションと安全に調整する。
4. 管理された実動 rotation 前に設定を debug する。
5. journal と外部 store の retention を別々に管理する。
