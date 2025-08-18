---
lang: "ja"
title: "netstat"
meta_description: "Linux ネットワーク分析のための netstat コマンドを学びます。この初心者向けガイドで、ネットワーク接続、ポート、ソケットを理解しましょう。"
meta_keywords: "netstat, netstat コマンド，Linux ネットワーキング，ネットワーク接続，Linux チュートリアル，初心者，ガイド"
---

## Lesson Content

### Well-Known Ports

マシン上のポートを介したデータ転送について説明しました。ここでは、いくつかのよく知られたポートを見てみましょう。

よく知られたポートのリストは、ファイル **/etc/services** を見ると取得できます。

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

最初の列はサービスの名前、次にポート番号、そしてそれが使用するトランスポート層プロトコルです。

### netstat

ネットワークに関する詳細な情報を取得するための非常に便利なツールが **netstat** です。Netstat は、ネットワーク接続、ルーティングテーブル、ネットワークインターフェースに関する情報など、さまざまなネットワーク関連情報を表示します。これは、ネットワークツールのスイスアーミーナイフです。ここでは、netstat が持つ機能の 1 つ、つまりネットワーク接続の状態に主に焦点を当てます。例を見る前に、まずソケットとポートについて説明しましょう。ソケットはプログラムがデータを送受信できるようにするインターフェースであり、ポートはどのアプリケーションがデータを送受信すべきかを識別するために使用されます。ソケットアドレスは、IP アドレスとポートの組み合わせです。ホストと宛先間のすべての接続には、一意のソケットが必要です。たとえば、HTTP はポート 80 で実行されるサービスですが、多くの HTTP 接続を持つことができ、各接続を維持するために、接続ごとにソケットが作成されます。

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

`netstat -a` コマンドは、ネットワーク接続のリスニングソケットと非リスニングソケットを表示します。`-t` フラグは TCP 接続のみを表示します。

列は左から右へ以下の通りです。

- **Proto**: 使用されるプロトコル、TCP または UDP。
- **Recv-Q**: 受信待ちのデータ。
- **Send-Q**: 送信待ちのデータ。
- **Local Address**: ローカルに接続されたホスト。
- **Foreign Address**: リモートに接続されたホスト。
- **State**: ソケットの状態。

ソケットの状態のリストについては manpage を参照してください。いくつか例を挙げます。

- **LISTENING**: ソケットは着信接続を待機しています。TCP 接続を行う際、接続する前に宛先が待機している必要があることを覚えておいてください。
- **SYN_SENT**: ソケットは積極的に接続を確立しようとしています。
- **ESTABLISHED**: ソケットは接続が確立されています。
- **CLOSE_WAIT**: リモートホストがシャットダウンし、ソケットが閉じるのを待っています。
- **TIME_WAIT**: ソケットは、ネットワークに残っているパケットを処理するために、クローズ後に待機しています。

## Exercise

`netstat` の manpage を見て、それが提供するすべての機能を学びましょう。

## Quiz Question

HTTPS に使用されるポートは何ですか？

## Quiz Answer

443
