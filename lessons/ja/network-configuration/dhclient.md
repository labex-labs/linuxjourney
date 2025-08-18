---
lang: "ja"
title: "dhclient"
meta_title: "dhclient - ネットワーク設定"
meta_description: "dhclient、DHCP を使用して IP アドレスを取得し、ネットワークリースを管理する方法について学びます。dhclient.conf および dhclient.leases ファイルについて理解します。Linux 初心者向けガイド。"
meta_keywords: "dhclient, DHCP, Linux networking, IP address, network configuration, Linux tutorial, beginner guide"
---

## Lesson Content

以前にも DHCP について説明しましたが、ほとんどの場合、IP アドレスやサブネットマスクなどを静的に設定する必要はありません。代わりに、DHCP を使用することになります。`dhclient`は起動時に起動し、`dhclient.conf`ファイルからネットワークインターフェースのリストを取得します。リストされた各インターフェースについて、DHCP プロトコルを使用してインターフェースを構成しようとします。

`dhclient.leases`ファイルでは、`dhclient`はシステム再起動をまたいでリース（lease）のリストを追跡します。`dhclient.conf`を読み込んだ後、`dhclient.leases`ファイルが読み込まれ、すでに割り当てられているリースを`dhclient`に知らせます。

### To obtain a fresh IP

```bash
sudo dhclient
```

## Exercise

No exercises for this lesson.

## Quiz Question

DHCP プロトコルで IP アドレスを割り当てようとするものは何ですか？

## Quiz Answer

dhclient
