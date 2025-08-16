---
lang: "ja"
title: "route"
description: "Linux の route コマンドと ip コマンドを使用して、ネットワークルートを追加および削除する方法を学びます。初心者から中級者向けのルーティングテーブル管理を理解します。"
keywords: "route command, ip route, add route, delete route, Linux networking, routing table, Linux tutorial, beginner guide"
---

## Lesson Content

ルーティングテーブルを `route` コマンドで表示する方法については、すでに説明しました。ルートを追加または削除したい場合は、手動で行うことができます。

### Add a new route

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Delete a route

```bash
sudo route del -net 192.168.2.1/23
```

これらの変更は、**ip** コマンドでも実行できます。

### To add a route

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### To delete a route

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

このレッスンには演習はありませんが、ここで説明したコマンドの詳細については、man ページで確認できます。

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

ルートを削除するためのコマンドフラグは何ですか？

## Quiz Answer

del
