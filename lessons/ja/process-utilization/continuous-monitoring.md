---
lang: "ja"
title: "継続的な監視"
meta_title: "継続的な監視 - プロセス利用率"
meta_description: "sar を使用した継続的な Linux システム監視について学びます。インストール、データ収集、およびパフォーマンスのための履歴リソース使用量の分析方法を理解します。始めましょう！"
meta_keywords: "sar, sysstat, Linux monitoring, system performance, continuous monitoring, beginner, tutorial, guide"
---

## Lesson Content

これらの監視ツールは、マシンに問題が発生しているときに確認するのに適していますが、見ていないときに問題が発生しているマシンについてはどうでしょうか？そのような場合は、継続的な監視ツール、つまりシステムアクティビティ情報を収集、報告、保存するツールを使用する必要があります。このレッスンでは、使用するのに最適なツールである **sar** について説明します。

### Installing sar

sar は、システムの履歴分析に使用されるツールです。まず、`sysstat` パッケージをインストールして、インストールされていることを確認します：`sudo apt install sysstat`。

### Setting up data collection

通常、`sysstat` をインストールすると、システムは自動的にデータの収集を開始します。開始しない場合は、`/etc/default/sysstat` の `ENABLED` フィールドを変更することで有効にできます。

### Using sar

```bash
sudo sar -q
```

このコマンドは、その日の初めからの詳細を一覧表示します。

```bash
sudo sar -r
```

これは、その日の初めからのメモリ使用量の詳細を一覧表示します。

```bash
sudo sar -P
```

これは、CPU 使用量の詳細を一覧表示します。

別の日付の表示を見るには、`/var/log/sysstat/saXX` に移動します。ここで `XX` は表示したい日付です。

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

システムに sar をインストールし、システムリソースの使用率の収集と分析を開始します。

## Quiz Question

システムリソースの監視に最適なツールは何ですか？

## Quiz Answer

sar
