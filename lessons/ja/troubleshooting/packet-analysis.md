---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "ja"
order_index: 5
title: "パケット解析"
description: "範囲とフィルターを限定したパケットトレースを取得し、tcpdump で安全に解析する方法を学びます。"
meta_title: "パケット解析 - トラブルシューティング"
meta_description: "Linux におけるネットワークパケット解析の基礎を学びます。このガイドでは、強力なパケットアナライザである tcpdump を紹介し、ネットワークトラフィックのキャプチャと解釈方法を解説します。"
meta_keywords: "tcpdump, パケット解析，ネットワークパケット解析，ネットワークパケットアナライザ，ネットワーク分析，ネットワークパケット解析ツール，Linux ネットワーキング，Wireshark, Linux コマンド，ネットワークトラフィック"
---

パケットキャプチャは、選択した観測点から見えるトラフィックを記録します。プロトコルのやり取りや時間を明らかにできますが、認証情報、個人データ、無関係な利用者の通信まで収集する可能性があります。許可を得て、範囲を最小限にし、ファイルを保護し、保存方針に従ってください。

## 観測点を選ぶ

問題の通信フローが実際に通るインターフェースとネットワーク名前空間でキャプチャします。ブリッジ、コンテナ、VPN、ボンド、VLAN、オフロードによって、一つのインターフェースから見える内容は変わります。キャプチャ前に `ip route get` と `ip link` で候補を特定してください。

:::single-choice{#packet-analysis-interface-choice}
キャプチャするインターフェースの選択が重要なのはなぜですか？

::option[すべてのインターフェースがインターネット全体を自動的にミラーするから。]{#packet-analysis-mirrors-internet explanation="通常、ホストに見えるのは、そのインターフェースを通るか、そこへミラーされた通信だけです。"}
::option[その観測点から見えるトラフィックだけを記録できるから。]{#packet-analysis-visible-point .correct explanation="名前空間、トンネル、ブリッジ、ルーティングによって、目的の通信フローが別の場所を通る場合があります。"}
::option[インターフェース名によって TLS ペイロードを復号できるから。]{#packet-analysis-name-decrypts explanation="名前には復号機能がありません。"}
:::

## 範囲を限定して通信フローを取得する

名前解決をせず、対象ホストと TCP ポートを限定して、最大 100 パケットを取得します。

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i` はインターフェース、`-n` は数値表示、`-c` はパケット数の上限、`-w` は pcap データの保存先を指定し、最後の式がキャプチャフィルターです。通信が発生しない可能性がある場合は、外部から時間制限も設定してください。

:::single-choice{#packet-analysis-count-bound}
`-c 100` は何をしますか？

::option[TCP ポート 100 だけを取得する。]{#packet-analysis-port-hundred explanation="ポートの選択はフィルター式で行います。"}
::option[ファイルを 100 バイトに圧縮する。]{#packet-analysis-compress-hundred explanation="このオプションはパケット数であり、ファイルサイズの上限ではありません。"}
::option[100 パケットを取得したら停止する。]{#packet-analysis-hundred .correct explanation="パケット数を制限すると、無人のキャプチャが際限なく増えることを防げます。"}
:::

## 取得したパケットを読む

保存済みファイルを変更せずに解析します。

```bash
$ tcpdump -n -tttt -r incident.pcap
```

プロトコルに従い、タイムスタンプ、プロトコル、送信元、宛先、フラグ、シーケンスまたは確認応答のデータ、長さを読み取ります。キャプチャのタイムスタンプが示すのはこのホストでの観測時刻であり、別の場所で実際に送信された正確な時刻とは限りません。複数システムのキャプチャを照合するには時計の同期が重要です。

:::single-choice{#packet-analysis-read-file}
保存済み pcap ファイルからパケットを読むオプションはどれですか？

::option[`-r`]{#packet-analysis-option-read .correct explanation="read オプションは既存のキャプチャファイルを処理します。"}
::option[`-i`]{#packet-analysis-option-interface explanation="これはライブキャプチャのインターフェースを選びます。"}
::option[`-w`]{#packet-analysis-option-write explanation="これは生のパケットをファイルへ書き込みます。"}
:::

## パケットの不在と暗号化を解釈する

パケットを取得できない原因には、誤ったインターフェースや名前空間、キャプチャ時の損失、狭すぎるフィルター、オフロードの影響、別経路へのルーティング、実際に通信がないことなどがあります。tcpdump が報告する受信数と破棄数を確認し、既知のイベントを再現してください。

TLS などの暗号化は通常、アプリケーションペイロードを隠しますが、エンドポイント、時刻、サイズ、TCP の動作、ハンドシェイクの一部といった有用なメタデータは残ります。許可のない復号を試みたり、秘密鍵を安易に収集したりしてはいけません。

:::single-choice{#packet-analysis-no-packets}
フィルター結果が空のキャプチャから、何が証明できますか？

::option[リモートアプリケーションが恒久的に削除されたこと。]{#packet-analysis-empty-deleted explanation="観測点やフィルターが誤っていても同じ結果になります。"}
::option[ネットワーク全体のトラフィックがゼロであること。]{#packet-analysis-empty-network explanation="狭いフィルターは、無関係なトラフィックを除外します。"}
::option[その観測点で一致するパケットが記録されなかったことだけ。]{#packet-analysis-empty-limited .correct explanation="結論を出す前に、インターフェース、名前空間、フィルター、キャプチャ時の破棄、テスト通信の生成を検証します。"}
:::

## 証拠を保護して共有する

pcap は厳しい権限で保存し、コマンド、ホスト、インターフェース、タイムゾーン、フィルター、障害の時間帯を記録します。完全性が重要なら証拠のハッシュも取得します。共有前に、必要なフィールドを保持できるツールと手順でデータを最小化または匿名化してください。パケットのペイロードだけでなく、メタデータからも利用者やシステムが特定される場合があります。

:::single-choice{#packet-analysis-pcap-safety}
障害調査の pcap は、どのように扱うべきですか？

::option[アクセスを制限し、来歴を記録した機密性の高い証拠として扱う。]{#packet-analysis-sensitive-evidence .correct explanation="キャプチャには機密情報が含まれ得るため、機密性だけでなく完全性も管理する必要があります。"}
::option[確認せず公開してよい無害なテキストとして扱う。]{#packet-analysis-public explanation="バイナリキャプチャから、ペイロード、個人識別情報、インフラ情報が露出する場合があります。"}
::option[元ファイルを保存せず、バイト列を直接上書き編集する。]{#packet-analysis-edit-original explanation="来歴が損なわれ、後の解析が無効になる可能性があります。"}
:::

## まとめ

これで、不必要に広範囲または危険にせず、有用なパケットキャプチャを作成できます。

1. 正しいインターフェースとネットワーク名前空間を選ぶ。
2. フィルター、パケット数、時間でキャプチャ範囲を制限する。
3. 生パケットを保存し、ファイルを読み取り専用で解析する。
4. 不在と暗号化ペイロードを、その限界を踏まえて解釈する。
5. キャプチャの機密性、完全性、来歴を保護する。
