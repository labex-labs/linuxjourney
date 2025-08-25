---
index: 5
lang: "ja"
title: "I/O 監視"
meta_title: "I/O 監視 - プロセス利用率"
meta_description: "Linux I/O 監視のために iostat を使用する方法を学びます。この必須コマンドで CPU とディスク使用量のメトリックを理解します。システムパフォーマンスを向上させましょう！"
meta_keywords: "iostat, Linux I/O 監視，CPU 使用率，ディスク使用量，Linux コマンド，初心者，チュートリアル，ガイド"
---

## Lesson Content

**iostat**という便利なツールを使って、CPU 使用率とディスク使用率を監視できます。

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

最初の部分は CPU 情報です。

- **%user** - ユーザーレベル（アプリケーション）で実行中に発生した CPU 使用率の割合を示します。
- **%nice** - nice 優先度でユーザーレベルで実行中に発生した CPU 使用率の割合を示します。
- **%system** - システムレベル（カーネル）で実行中に発生した CPU 使用率の割合を示します。
- **%iowait** - システムが未処理のディスク I/O 要求を持っていた間に、CPU がアイドル状態であった時間の割合を示します。
- **%steal** - ハイパーバイザーが別の仮想プロセッサを処理している間に、仮想 CPU が不随意の待機に費やした時間の割合を示します。
- **%idle** - CPU がアイドル状態であり、システムが未処理のディスク I/O 要求を持っていなかった時間の割合を示します。

2 番目の部分はディスク使用率です。

- **tps** - デバイスに対して発行された 1 秒あたりの転送数を示します。転送はデバイスへの I/O 要求です。複数の論理要求を 1 つの I/O 要求にまとめることができます。転送のサイズは不定です。
- **kB_read/s** - デバイスから読み取られたデータ量で、1 秒あたりのキロバイトで表されます。
- **kB_wrtn/s** - デバイスに書き込まれたデータ量で、1 秒あたりのキロバイトで表されます。
- **kB_read** - 読み取られたキロバイトの総数。
- **kB_wrtn** - 書き込まれたキロバイトの総数。

## Exercise

練習は完璧をもたらします！システム監視とディスク使用量の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux df コマンド：ディスク容量のレポート](https://labex.io/ja/labs/linux-linux-df-command-disk-space-reporting-219188)** - マウントされたファイルシステムのディスク容量使用状況をレポートする練習をします。これは監視の重要な側面です。
2. **[Linux du コマンド：ファイル容量の見積もり](https://labex.io/ja/labs/linux-linux-du-command-file-space-estimating-219190)** - ディレクトリとサブディレクトリのディスク容量使用状況を見積もる方法を学びます。これは`iostat`からのディスク I/O 情報を補完します。
3. **[Linux top コマンド：リアルタイムシステム監視](https://labex.io/ja/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - CPU とメモリ使用量を含むリアルタイムシステム監視を探求します。これは`iostat`で表示される CPU メトリックのより広いコンテキストを提供します。

これらのラボは、実際のシナリオで概念を適用し、Linux システムリソースの監視に自信を持つために役立ちます。

## Quiz Question

I/O と CPU の使用状況を表示するために使用できるコマンドは何ですか？

## Quiz Answer

iostat
