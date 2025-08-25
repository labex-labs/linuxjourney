---
index: 9
lang: "ja"
title: "tail"
meta_title: "tail - テキスト操作の達人"
meta_description: "Linux で`tail`コマンドを使用してファイルの末尾を表示し、ログを監視する方法を学びます。リアルタイム更新のための`tail -f`を発見してください。Linux の旅を始めましょう！"
meta_keywords: "tail コマンド，Linux tail, tail -f, ログ表示，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

## Lesson Content

`head`コマンドと同様に、`tail`コマンドはデフォルトでファイルの最後の 10 行を表示します。

```bash
tail /var/log/syslog
```

`head`と同様に、表示したい行数を変更できます。

```bash
tail -n 10 /var/log/syslog
```

もう 1 つの便利なオプションとして、`-f` (follow) フラグがあります。これは、ファイルが成長するにつれてファイルを追跡します。試してみて、何が起こるか見てみましょう。

```bash
tail -f /var/log/syslog
```

システムを操作している間、`syslog`ファイルは継続的に変化し、`tail -f`を使用すると、そのファイルに追加されるすべてを見ることができます。

## Exercise

練習は完璧をもたらします！`tail`コマンドとそのアプリケーションの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux tail コマンド：ファイル末尾の表示](https://labex.io/ja/labs/linux-linux-tail-command-file-end-display-214303)** - テキストファイルの末尾を表示および監視するための Linux `tail`コマンド（リアルタイム更新用の`-f`オプションを含む）を学びます。
2. **[Linux でのログファイルと設定ファイルの表示](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `tail`（`cat`や`more`と合わせて）を使用して、ログファイルと設定ファイルを効率的に表示およびナビゲートする練習をします。これはシステム監視に不可欠です。
3. **[迅速な脅威検出](https://labex.io/ja/labs/linux-rapid-threat-detection-387930)** - `tail`の知識を応用して、最近のログエントリを迅速に抽出し分析し、サイバーセキュリティの文脈での迅速な脅威検出をシミュレートします。

これらのラボは、実際のシナリオでファイルコンテンツの表示と監視の概念を適用し、`tail`コマンドに自信を持つのに役立ちます。

## Quiz Question

`tail`でファイルを追跡するために使用されるフラグは何ですか？

## Quiz Answer

-f
