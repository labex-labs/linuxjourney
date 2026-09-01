---
lesson_id: "general-logging"
course_id: "logging"
lang: "ja"
order_index: 3
title: "一般的なロギング"
description: "Linux の一般的なシステムログを見つけ、絞り込み、追跡、相関する方法を学びます。"
meta_title: "一般的なロギング - ロギング"
meta_description: "一般的な Linux ログの初心者向けガイド。効果的なシステム監視、ログ分析、Linux トラブルシューティングのための/var/log/messages と syslog について学びます。"
meta_keywords: "Linux ログ，syslog, var/log/messages, Linux トラブルシューティング，システムログ，ログ分析，システム監視，Linux ガイド，Linux 初心者，/var/log"
---

一般的なシステムログには、複数の発生元からの通常通知、warning、error が集まります。調査の出発点として便利ですが、ファイル名と内容は routing policy による選択であり、すべての Linux に共通する保証ではありません。

## 関係する情報源を見つける

ディストリビューションと設定によって、一般メッセージは `/var/log/syslog`、`/var/log/messages`、systemd journal、または複数の宛先に現れます。最初にホストと障害時間帯を特定し、利用可能な情報源を調べます。

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

アプリケーションログは独自のサブディレクトリや外部サービスにある場合があります。authentication、audit、package、database、web-server のレコードは、一般ストリームから意図的に分離されていることもあります。

:::single-choice{#general-logs-universal-file} すべての Linux ホストに `/var/log/messages` があると想定すべきでないのはなぜですか？

::option[一般ログの宛先は、ローカルの collector と routing policy に依存するから。]{#general-logs-local-routing .correct explanation="journal-only system や異なる syslog 設定では、別の宛先を使います。"}
::option[Linux では各ディスクに一つのログファイルしか置けないから。]{#general-logs-one-file explanation="システムは通常、多数のログファイルと journal store を維持します。"}
::option[そのパスがユーザー文書専用に予約されているから。]{#general-logs-user-documents explanation="`/var/log` 階層は慣例上ログに使われます。"}
:::

## テキストログを調べる

制御しながら移動するには `less`、最新レコードには `tail` を使います。

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

範囲を限定した再現中に新しい行を追うには、`tail -F FILE` を使います。単純な snapshot と異なり、`-F` は rotation でファイルが置き換わっても再試行します。`Ctrl-C` で追跡を止め、広い権限の session を開いたままにしないでください。

:::single-choice{#general-logs-tail-f-capability} 制御された再現中、`tail -F` は何に役立ちますか？

::option[通常の rotation で置き換わった後も、名前付きファイルを追うこと。]{#general-logs-tail-follow .correct explanation="名前による再試行動作により、有効ファイルが rename・再作成された後も追跡を続けやすくなります。"}
::option[すべてのログ severity を debug へ変更すること。]{#general-logs-tail-debug explanation="tail はファイル内容を読み、発生元の設定は変更しません。"}
::option[別プログラムなしで圧縮 archive を復号すること。]{#general-logs-tail-decrypt explanation="一般的な archive 展開や復号機能はありません。"}
:::

## 文脈を失わず絞り込む

無制限の live stream をすぐ pipe するのではなく、範囲を限定した file または journal interval を検索します。

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

大文字小文字、表現、rate limit、localization によって literal search は不完全になる場合があります。成功・失敗イベントの両方を記録し、目に見える error より前に原因がある可能性を考え、前後の行を保持します。

:::single-choice{#general-logs-context-lines} 一致した error の周辺行を含めるのはなぜですか？

::option[先行イベントが後の失敗を説明する可能性があるから。]{#general-logs-preceding-context .correct explanation="時間的な文脈により、一つの文字列を障害全体とみなさず、事象の順序を再構築できます。"}
::option[文脈があれば最初の一致が root cause だと保証されるから。]{#general-logs-guaranteed-cause explanation="追加証拠との相関が必要で、文脈だけでは因果関係を証明できません。"}
::option[サービス設定が自動的に変更されるから。]{#general-logs-context-config explanation="検索出力は読み取り専用で、サービス設定を更新しません。"}
:::

## Rotation 済み Archive を含める

障害が rotation の境界をまたぐ場合があります。有効ファイル、番号付き archive、圧縮ファイルに、同じ一連の事象の別部分が入ることがあります。`zgrep` や `zless` は gzip 圧縮 archive を読みます。

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

suffix だけでなく、実際の timestamp で結果を並べます。証拠をコピーする前に metadata を保持し、ログに個人データや認証情報が含まれる可能性を考えてアクセスを制限してください。

:::single-choice{#general-logs-rotation-boundary} 障害が log rotation をまたぐ場合、何を確認すべきですか？

::option[新しく作られた空の有効ファイルだけ。]{#general-logs-active-only explanation="以前のレコードは rotated archive へ移動している可能性があります。"}
::option[イベント時刻順に並べた有効ログと archive ログ。]{#general-logs-all-intervals .correct explanation="関係する一連の事象が、現在と rotation 済みファイルに分割されている場合があります。"}
::option[レコード timestamp を無視したファイル名だけ。]{#general-logs-filenames-only explanation="suffix 順とイベント時刻は必ずしも一致しません。"}
:::

## まとめ

これで、file、journal、rotation の境界をまたいで一般ログを調査できます。

1. 普遍的なファイル名を想定せず、宛先を見つける。
2. 限定した時間帯を読み、再現中だけ追跡する。
3. 一致レコードの周辺にある時間的文脈を保持する。
4. rotation 済み archive を含め、機密性の高い証拠を保護する。
