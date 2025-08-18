---
index: 5
lang: "ja"
title: "パケット解析"
meta_title: "パケット解析 - トラブルシューティング"
meta_description: "tcpdump を使用したパケット解析の基本を学びます。この初心者向けの Linux ガイドで、ネットワークトラフィックを理解し、データをキャプチャし、出力を解釈します。"
meta_keywords: "tcpdump, パケット解析，ネットワーク解析，Linux ネットワーキング，初心者チュートリアル，Wireshark, Linux コマンド，ネットワークトラフィック"
---

## Lesson Content

パケット解析というテーマは、それだけで一つのコースを埋め尽くすことができ、パケット解析に関する書籍も多数出版されています。しかし、今回はその基本を学ぶだけに留めます。非常に人気のあるパケットアナライザーは Wireshark と tcpdump の 2 つです。これらのツールは、ネットワークインターフェースをスキャンし、パケットアクティビティをキャプチャし、パケットを解析し、その情報を私たちが見られるように出力します。これらを使用することで、ネットワーク解析の核心に迫り、低レベルの事柄を深く掘り下げることができます。今回はよりシンプルなインターフェースを持つ tcpdump を使用しますが、もしパケット解析をあなたのツールベルトに加えるのであれば、Wireshark を調べることをお勧めします。

### Install tcpdump

```bash
sudo apt install tcpdump
```

### Capture packet data on an interface

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

パケットキャプチャを実行すると、多くのことが起こっていることに気づくでしょう。それは当然のことです。バックグラウンドでは多くのネットワークアクティビティが発生しています。上記の例では、私が`www.google.com`に ping を打つことにした時のスニペットのみを抜粋しています。

### Understanding the output

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- 最初のフィールドは、ネットワークアクティビティのタイムスタンプです。
- IP: これにはプロトコル情報が含まれています。
- 次に、送信元と宛先のアドレスが表示されます：`icebox.lan > nuq04s29-in-f4.1e100.net`。
- `seq`: これは TCP パケットの開始および終了シーケンス番号です。
- `length`: バイト単位の長さです。

tcpdump の出力からわかるように、私たちは`www.google.com`に ICMP echo request パケットを送信し、ICMP echo reply パケットを返してもらっています！また、異なるパケットは異なる情報を出力することにも注意してください。それらが何であるかについては、manpage を参照してください。

### Writing tcpdump output to a file

```bash
sudo tcpdump -w /some/file
```

最後に、パケット解析というテーマの表面をなぞったに過ぎません。見ることができるものは非常に多く、Hex および ASCII 出力でさらに深く掘り下げることさえ触れていません。パケットアナライザーについてさらに学ぶのに役立つオンラインリソースはたくさんありますので、ぜひ見つけてみてください！

## Exercise

Wireshark ツールをダウンロードしてインストールし、インターフェースを操作してみてください。

## Quiz Question

tcpdump で特定のインターフェースをキャプチャするためのフラグは何ですか？

## Quiz Answer

-i
