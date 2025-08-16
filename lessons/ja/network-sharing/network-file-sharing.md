---
lang: "ja"
title: "ファイル共有の概要"
description: "Linux のファイル共有とセキュアコピー（scp）コマンドについて学びましょう。ネットワーク上のホスト間でファイルを転送します。この初心者向けガイドで始めましょう！"
keywords: "Linux ファイル共有，scp コマンド，セキュアコピー, ネットワークファイル転送，Linux チュートリアル，初心者向け Linux, Linux ガイド"
---

## Lesson Content

特に商用環境で作業している場合、通常、ネットワーク上にはあなた以外のコンピューターも存在します。あるマシンから別のマシンへデータを転送したい場合、USB ドライブを接続して手動でコピーする方が簡単なこともあります。しかし、ほとんどの場合、同じネットワーク上のマシンで作業している場合は、ネットワークファイル共有を介してデータを転送します。

このコースでは、ネットワーク上の異なるマシン間でデータをコピーするいくつかの異なる方法について説明します。簡単なファイルコピーについて議論し、その後、別のドライブとして機能するディレクトリ全体をマシンにマウントすることについて話します。

シンプルなファイル共有ツールの 1 つに **scp** コマンドがあります。scp コマンドは secure copy の略で、cp コマンドとまったく同じように機能しますが、同じネットワーク上の 1 つのホストから別のホストへコピーすることができます。ssh を介して動作するため、すべてのアクションは ssh と同じ認証とセキュリティを使用します。

### To copy a file from a local host to a remote host

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### To copy a file from a remote host to your local host

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### To copy a directory from your local host to a remote host

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

scp を使って、あるマシンから別のマシンへファイルをコピーしてみてください。

## Quiz Question

あるホストから別のホストへファイルを安全にコピーするために使用できるコマンドは何ですか？

## Quiz Answer

scp
