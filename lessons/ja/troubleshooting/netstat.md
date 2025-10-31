---
index: 4
lang: "ja"
title: "netstat"
meta_title: "netstat - トラブルシューティング"
meta_description: "Linux の netstat コマンドを習得し、ネットワーク接続、ポート、ソケットを分析します。このガイドでは、SYN_SENT や netstat close_wait などの一般的な状態をカバーし、効果的なトラブルシューティングを支援します。"
meta_keywords: "linux netstat, netstat, netstat コマンド，syn_sent netstat, netstat close_wait, ネットワーク接続，linux ネットワーキング，ネットワーク分析，linux チュートリアル"
---

## Lesson Content

### 一般公開ポート

データがどのようにして私たちのマシンのポートを経由して送信されるかについて説明しました。ここでは、一般的で広く知られているポートを見てみましょう。これらのポートのリストは **/etc/services** ファイルで見つけることができます。

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

最初の列はサービス名、それに続くのが割り当てられたポート番号と使用されるトランスポート層プロトコルを示しています。

### linux netstat の紹介

詳細なネットワーク情報を収集するために非常に便利なツールが **netstat** です。`linux netstat` コマンドは、アクティブなネットワーク接続、ルーティングテーブル、インターフェイス統計など、幅広いネットワーク関連データを表示します。これはしばしばネットワークツールのスイスアーミーナイフと呼ばれます。

このレッスンでは、`netstat` を使用してネットワーク接続の状態を確認することに焦点を当てます。例に入る前に、ソケットとポートの違いを明確にしましょう。**ポート** は特定のアプリケーションにデータを送るために使用される数値識別子です。**ソケット** は通信のエンドポイントであり、プログラムがデータを送受信できるようにします。ソケットアドレスは、IP アドレスとポート番号のユニークな組み合わせです。ホストと宛先間の接続ごとに、一意のソケットが必要です。例えば、HTTP サービスはポート 80 で動作しますが、複数の HTTP 接続が同時に存在でき、それぞれに一意のソケットが作成されます。

`netstat -at` の出力を確認してみましょう。

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

`netstat -a` コマンドはリッスン中およびリッスン中でないすべてのソケットを表示し、`-t` フラグは出力を TCP 接続のみにフィルタリングします。

各列は次のとおりです。

- **Proto**: 使用されているプロトコル（例：TCP または UDP）。
- **Recv-Q**: 受信待ちのデータキュー。
- **Send-Q**: 送信待ちのデータキュー。
- **Local Address**: ローカルホストのアドレス。
- **Foreign Address**: リモートホストのアドレス。
- **State**: ソケットの現在の状態。

### 接続状態の理解

**State** 列は、接続のステータスに関する重要な情報を提供します。遭遇する可能性のある一般的な状態をいくつか示します。

- **LISTENING**: ソケットが着信接続を待機しています。TCP 接続を確立するには、宛先がリッスン状態である必要があります。
- **SYN_SENT**: `netstat` を使用する場合、`SYN_SENT` 状態はソケットが接続確立を積極的に試みていることを示します。
- **ESTABLISHED**: ソケットは完全に確立された接続を持っています。
- **CLOSE_WAIT**: `netstat close_wait` 状態は、リモートホストがシャットダウンし、ローカルシステムがアプリケーションによるソケットのクローズを待っていることを意味します。
- **TIME_WAIT**: ソケットは、ネットワーク上にまだ存在する可能性のあるパケットを処理するために、クローズ後に待機しています。

ソケット状態の完全なリストは `netstat` のマニュアルページで確認できます。

## Exercise

練習あるのみです！ネットワークインターフェイス設定の理解を深めるための実践的なラボを以下に示します。

1. **[Linux で ethtool を使用してネットワークインターフェイス設定を調べる](https://labex.io/ja/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - `ethtool` コマンドを使用して、インターフェイス速度とデュプレックスの表示と設定、リンクモードの分析など、ネットワークインターフェイス設定を調べ、管理する方法を学び、物理層のネットワーク問題をトラブルシューティングします。

このラボは、実際のシナリオで概念を適用し、ネットワークインターフェイスの管理に対する自信を構築するのに役立ちます。

## Quiz Question

HTTPS にはどのポートが使用されますか？

## Quiz Answer

443
