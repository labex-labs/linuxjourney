---
lang: "ja"
title: "System V サービス"
meta_description: "コマンドラインツールを使用して System V サービスを管理する方法を学びます。この初心者向けの Linux チュートリアルで、サービスのリスト表示、開始、停止、再起動の方法を発見してください。"
meta_keywords: "System V サービス，Linux サービス，service コマンド，SysV init, Linux チュートリアル，初心者 Linux, サービス管理，Linux ガイド"
---

## Lesson Content

Sys V サービスを管理するために使用できるコマンドラインツールはたくさんあります。

### List services

```bash
service --status-all
```

### Start a service

```bash
sudo service networking start
```

### Stop a service

```bash
sudo service networking stop
```

### Restart a service

```bash
sudo service networking restart
```

これらのコマンドは Sys V init システムに固有のものではありません。Upstart サービスを管理するためにも使用できます。Linux は従来の Sys V init スクリプトから移行しようとしているため、その移行を助けるための仕組みがまだ残っています。

## Exercise

いくつかのサービスを管理し、その状態を変更してください。何を観察しますか？

## Quiz Question

Sys V で`peanut`という名前のサービスを停止するコマンドは何ですか？

## Quiz Answer

sudo service peanut stop
