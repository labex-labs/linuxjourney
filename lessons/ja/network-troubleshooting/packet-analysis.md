---
index: 5
lang: "ja"
title: "パケット解析"
meta_title: "パケット解析 - トラブルシューティング"
meta_description: "tcpdump を使ったパケット解析の基本を学びましょう。この初心者向けの Linux ガイドで、ネットワークトラフィックを理解し、データをキャプチャし、出力を解釈する方法を学びます。"
meta_keywords: "tcpdump, パケット解析，ネットワーク解析，Linux ネットワーク，初心者向けチュートリアル，Wireshark, Linux コマンド，ネットワークトラフィック"
---

## Lesson Content

パケット解析の主題は、それだけでコース全体を埋めることができ、パケット解析について書かれた本もたくさんあります。しかし、今日はその基本を学ぶだけです。非常に人気のあるパケットアナライザーが 2 つあります。Wireshark と tcpdump です。これらのツールは、ネットワークインターフェースをスキャンし、パケットアクティビティをキャプチャし、パケットを解析し、その情報を私たちが見られるように出力します。これらにより、ネットワーク解析の核心に入り込み、低レベルの事柄を深く掘り下げることができます。今回は tcpdump を使用します。なぜなら、よりシンプルなインターフェースを持っているからです。しかし、もしパケット解析をあなたのツールベルトに加えるのであれば、Wireshark を調べることをお勧めします。

### tcpdump をインストールする

```bash
sudo apt install tcpdump
```

### インターフェースでパケットデータをキャプチャする

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
```

パケットキャプチャを実行すると、多くのことが起こっていることに気づくでしょう。それは当然のことです。バックグラウンドでは多くのネットワークアクティビティが発生しています。上記の例では、私が`www.google.com`に ping を打つことにした特定の時間のキャプチャの一部のみを抜粋しました。

### 出力を理解する

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- 最初のフィールドはネットワークアクティビティのタイムスタンプです。
- IP: これにはプロトコル情報が含まれています。
- 次に、送信元と宛先のアドレスが表示されます：`icebox.lan > nuq04s29-in-f4.1e100.net`。
- `seq`: これは TCP パケットの開始および終了シーケンス番号です。
- `length`: バイト単位の長さです。

tcpdump の出力からわかるように、`www.google.com`に ICMP エコーリクエストパケットを送信し、ICMP エコーリプライパケットが返ってきています！また、異なるパケットは異なる情報を出力することに注意してください。それらが何であるかについては、man ページを参照してください。

### tcpdump の出力をファイルに書き込む

```bash
sudo tcpdump -w /some/file
```

最後に、パケット解析の主題の表面をなぞっただけです。見ることができるものは非常に多く、Hex および ASCII 出力でさらに深く掘り下げることさえ触れていません。パケットアナライザーについてさらに学ぶのに役立つオンラインリソースはたくさんありますので、ぜひ見つけてください！

## Exercise

練習は完璧を導きます！パケット解析の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux で tcpdump を使ってイーサネットフレームを解析する](https://labex.io/ja/labs/linux-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - `tcpdump`を使用して、イーサネットフレームのキャプチャと検査、トラフィックの生成、フレームヘッダーと MAC アドレスの解析を練習します。

このラボは、実際のシナリオでパケット解析の概念を適用し、ネットワークトラブルシューティングに自信をつけるのに役立ちます。

## Quiz Question

tcpdump で特定のインターフェースをキャプチャするためのフラグは何ですか？

## Quiz Answer

-i
