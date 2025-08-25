---
index: 4
lang: "ja"
title: "netstat"
meta_title: "netstat - トラブルシューティング"
meta_description: "Linux ネットワーク分析のための netstat コマンドを学びましょう。この初心者向けのガイドで、ネットワーク接続、ポート、ソケットを理解しましょう。"
meta_keywords: "netstat, netstat コマンド，Linux ネットワーキング，ネットワーク接続，Linux チュートリアル，初心者，ガイド"
---

## Lesson Content

### よく知られているポート

マシン上のポートを介したデータ送信について説明しました。いくつかのよく知られているポートを見てみましょう。

よく知られているポートのリストは、ファイル **/etc/services** を見ると取得できます。

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

最初の列はサービス名、次にポート番号、そしてそれが使用するトランスポート層プロトコルです。

### netstat

ネットワークに関する詳細な情報を取得するための非常に便利なツールが **netstat** です。Netstat は、ネットワーク接続、ルーティングテーブル、ネットワークインターフェースに関する情報など、さまざまなネットワーク関連情報を表示します。これは、ネットワークツールのスイスアーミーナイフです。netstat が持つ機能の 1 つ、つまりネットワーク接続の状態に主に焦点を当てます。例を見る前に、まずソケットとポートについて話しましょう。ソケットはプログラムがデータを送受信できるようにするインターフェースであり、ポートはどのアプリケーションがデータを送受信すべきかを識別するために使用されます。ソケットアドレスは、IP アドレスとポートの組み合わせです。ホストと宛先間のすべての接続には、一意のソケットが必要です。たとえば、HTTP はポート 80 で実行されるサービスですが、多くの HTTP 接続を持つことができ、各接続を維持するために、接続ごとにソケットが作成されます。

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                     LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

`netstat -a` コマンドは、ネットワーク接続のリスニングソケットと非リスニングソケットを表示します。`-t` フラグは TCP 接続のみを表示します。

列は左から右へ次のとおりです。

- **Proto**: 使用されるプロトコル、TCP または UDP。
- **Recv-Q**: 受信待ちのデータ。
- **Send-Q**: 送信待ちのデータ。
- **Local Address**: ローカルに接続されたホスト。
- **Foreign Address**: リモートに接続されたホスト。
- **State**: ソケットの状態。

ソケットの状態のリストについては man ページを参照してください。いくつか例を挙げます。

- **LISTENING**: ソケットは着信接続を待機しています。TCP 接続を行う際、接続する前に宛先が待機している必要があることを覚えておいてください。
- **SYN_SENT**: ソケットは接続を確立しようと積極的に試みています。
- **ESTABLISHED**: ソケットは接続が確立されています。
- **CLOSE_WAIT**: リモートホストがシャットダウンし、ソケットが閉じるのを待っています。
- **TIME_WAIT**: ソケットは、ネットワークに残っているパケットを処理するために、クローズ後に待機しています。

## Exercise

練習は完璧をもたらします！ネットワークインターフェース設定の理解を深めるための実践的なラボです。

1. **[Linux で ethtool を使用してネットワークインターフェース設定を調べる](https://labex.io/ja/labs/linux-examine-network-interface-settings-with-ethtool-in-linux-592759)** - `ethtool` コマンドを使用して、ネットワークインターフェース設定の調査と管理（インターフェース速度とデュプレックスの表示と設定、物理層のネットワーク問題をトラブルシューティングするためのリンクモードの分析など）を学びます。

このラボは、実際のシナリオで概念を適用し、ネットワークインターフェースの管理に自信を持つのに役立ちます。

## Quiz Question

HTTPS にはどのポートが使用されますか？

## Quiz Answer

443
