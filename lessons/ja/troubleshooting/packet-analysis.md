---
index: 5
lang: "ja"
title: "パケット解析"
meta_title: "パケット解析 - トラブルシューティング"
meta_description: "Linux におけるネットワークパケット解析の基礎を学びます。このガイドでは、強力なパケットアナライザである tcpdump を紹介し、ネットワークトラフィックのキャプチャと解釈方法を解説します。"
meta_keywords: "tcpdump, パケット解析，ネットワークパケット解析，ネットワークパケットアナライザ，ネットワーク分析，ネットワークパケット解析ツール，Linux ネットワーキング，Wireshark, Linux コマンド，ネットワークトラフィック"
---

## Lesson Content

ネットワークパケット解析の分野は広大であり、それだけで完全なコースや書籍の主題になり得ます。このレッスンでは、その基本を紹介します。パケット解析とは、ネットワーク上を流れるデータをキャプチャし、検査することを含みます。これは、ネットワークのトラブルシューティング、パフォーマンスチューニング、セキュリティ分析にとって不可欠なスキルです。個々のパケットを調べることで、ネットワークで何が起こっているのかを低レベルで深く理解することができます。

### 人気のネットワークパケット解析ツール

ネットワークパケット解析ツールとして非常に人気があるのは、Wireshark と tcpdump の 2 つです。どちらも強力なパケットアナライザアプリケーションであり、ネットワークインターフェースをスキャンし、パケットアクティビティをキャプチャし、検査のためにデータを解析します。これにより、ネットワーク解析の核心部分に踏み込むことができます。ここでは、コマンドラインのシンプルさから tcpdump を使用しますが、ネットワークパケット解析をさらに深く掘り下げる予定がある場合は、Wireshark のグラフィカルインターフェースを調べることを強くお勧めします。

### tcpdump のインストール

Ubuntu のような Debian ベースのシステムでは、次のコマンドで tcpdump をインストールできます。

```bash
sudo apt install tcpdump
```

### ライブパケットデータのキャプチャ

特定のインターフェースでデータキャプチャを開始するには、`-i`フラグの後にインターフェース名を指定します。

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

パケットキャプチャを実行すると多くの活動が見られることに気づくでしょうが、これは絶え間ないバックグラウンドネットワークトラフィックを考えると予想されます。上記の例は、`www.google.com`に ping を実行している間に取得されたキャプチャのスニペットを示しています。

### tcpdump 出力の解釈

キャプチャ行を分解してみましょう。

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
```

- **タイムスタンプ**: 最初のフィールド (`11:28:23.958840`) は、パケットがキャプチャされた時刻を示します。
- **プロトコル**: `IP` はネットワーク層プロトコルを示します。
- **送信元と宛先**: `icebox.lan > nuq04s29-in-f4.1e100.net` は、パケットの送信元と宛先を示します。
- **プロトコル固有の情報**: 行の残りの部分は、プロトコル固有の詳細を含んでいます。この ICMP パケットの場合：
  - `seq`: パケットのシーケンス番号。
  - `length`: パケット長（バイト単位）。

ご覧のとおり、私たちのマシンは ICMP エコーリクエストを送信し、ICMP エコーリプライを受信しました。プロトコルによって表示される情報は異なるため、詳細についてはマニュアルページを参照してください。

### 後で解析するためにキャプチャを保存する

ライブトラフィックを表示する代わりに、`-w`フラグを使用してキャプチャをファイルに保存できます。これは、より詳細なオフラインパケット解析に役立ちます。

```bash
sudo tcpdump -w /some/file.pcap
```

私たちはパケット解析の表面をなぞったにすぎません。高度なフィルタリングや、パケット内容を Hex や ASCII で検査することを含め、探求すべきことはまだたくさんあります。数多くのオンラインリソースがネットワークパケット解析ツールの習得に役立ちます。学習の旅を続けることをお勧めします。

## Exercise

パケット解析の理解を深めるために、このハンズオンラボを試してみてください。練習あるのみです！

1. **[Linux で tcpdump を使用してイーサネットフレームを解析する](https://labex.io/ja/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - `tcpdump`を使用してイーサネットフレームのキャプチャと検査、トラフィックの生成、フレームヘッダーと MAC アドレスの解析を練習します。

このラボは、パケット解析の概念を実世界のシナリオで適用し、ネットワークトラブルシューティングへの自信を築くのに役立ちます。

## Quiz Question

tcpdump で特定のインターフェースをキャプチャするためのフラグは何ですか？必要なフラグのみを英語で回答してください。大文字と小文字は区別されます。

## Quiz Answer

-i
