---
index: 9
lang: "ja"
title: "tail"
meta_title: "tail - テキスト操作"
meta_description: "`tail`コマンドを使って Linux でファイルの末尾を表示し、ログを監視する方法を学びます。リアルタイム更新のための`tail -f`を発見しましょう。Linux の旅を始めましょう！"
meta_keywords: "tail コマンド，Linux tail, tail -f, ログ表示，Linux チュートリアル，Linux 初心者，Linux ガイド"
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

もう一つの便利なオプションとして、`-f` (follow) フラグがあります。これはファイルが成長するにつれて追跡します。試してみて、何が起こるか見てみましょう。

```bash
tail -f /var/log/syslog
```

システムを操作している間、`syslog`ファイルは継続的に変化し、`tail -f`を使用すると、そのファイルに追加されるすべてを見ることができます。

## Exercise

`tail`の man ページを見て、私たちが議論しなかった他のコマンドをいくつか読んでみましょう。

```bash
man tail
```

## Quiz Question

`tail`でファイルを追跡するために使用されるフラグは何ですか？

## Quiz Answer

-f
