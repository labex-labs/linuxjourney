---
index: 3
lang: "ja"
title: "traceroute"
meta_title: "traceroute - トラブルシューティング"
meta_description: "traceroute Linux コマンドを習得し、ネットワーク経路の追跡と接続問題のトラブルシューティングを行いましょう。このチュートリアルでは、traceroute が TTL を使用してパケットが宛先に到達するまでの経路をマッピングする方法を解説します。"
meta_keywords: "traceroute, traceroute linux, Linux ネットワーキング，ネットワークトラブルシューティング，TTL, パケットルーティング，Linux コマンド，初心者，チュートリアル"
---

## Lesson Content

traceroute コマンドは、パケットがコンピューターから宛先ホストへ到達するまでの経路をトレースするために使用される基本的なネットワーク診断ツールです。途中の各「ホップ」またはルーターを明らかにし、ネットワークのボトルネックを特定し、接続の問題をトラブルシューティングするのに役立ちます。traceroute linux ユーティリティは、すべてのシステム管理者やネットワークエンジニアにとって不可欠です。

### traceroute の仕組み

traceroute の背後にあるメカニズムは、IP パケットヘッダーの Time To Live (TTL) フィールドを巧みに操作することにあります。プロセスは次のとおりです。

1. traceroute は、TTL 値が 1 のプローブパケットを送信します。
2. 経路上の最初のルーターがパケットを受信し、TTL を 0 に減らして破棄します。その後、ルーターは ICMP「Time Exceeded」メッセージをコンピューターに返送します。
3. traceroute はそのルーターの IP アドレスと往復時間（RTT）を記録します。
4. 次に、今度は TTL が 2 の別のパケットを送信します。このパケットは最初のルーターを正常に通過しますが、2 番目のルーターによって破棄され、やはり「Time Exceeded」メッセージが返送されます。
5. このプロセスは、後続のパケットセットごとに TTL が 1 ずつ増加しながら繰り返されます。 「Time Exceeded」メッセージを返すルーターのリストを作成することにより、traceroute は完全な経路をマッピングします。
6. パケットが最終的に宛先に到達すると（宛先は ICMP「Echo Reply」メッセージで応答します）、プロセスは終了します。

## Exercise

ネットワーク診断を習得するには実践が鍵となります。次のハンズオンラボは、traceroute のようなツールを使用したネットワーク経路の検出とトラブルシューティングの理解を深めるのに役立ちます。

1. **[Linux での IP アドレス指定の管理](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - ip コマンドを使用してネットワーク設定を行い、その後 traceroute で接続性とルーティングパスを確認する練習をします。
2. **[Linux での ping と arp を使用したネットワーク層の相互作用の探求](https://labex.io/ja/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - ping と arp がどのように連携してネットワーク層の相互作用を理解するかを学びます。これは traceroute の動作の基礎となる概念です。

これらのラボは、現実世界のシナリオでネットワーク診断の概念を適用し、不可欠な Linux ネットワーキングツールに対する自信を構築するのに役立ちます。

## Quiz Question

ネットワークをホップする際に、1 つずつ減らされるものは何ですか？ (英語で、大文字と小文字に注意して回答してください。)

## Quiz Answer

TTL
