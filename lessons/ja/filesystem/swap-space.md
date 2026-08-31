---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "ja"
order_index: 8
title: "スワップ"
description: "Linux がスワップ領域を利用、初期化、有効化、容量設計、安全に無効化する仕組みを学びます。"
meta_title: "スワップ - ファイルシステム"
meta_description: "Linux スワップ領域について、その仕組み、スワップパーティションの作成と管理方法を学びましょう。このガイドでシステムのメモリ使用量を最適化しましょう！"
meta_keywords: "Linux スワップ，mkswap, swapon, swapoff, /etc/fstab, 仮想メモリ，Linux 初心者，Linux チュートリアル"
---

Linux は、選択した匿名メモリページを RAM とスワップ用ストレージの間で移動できます。これにより、使用頻度の低いメモリを保持しつつ、アクティブなワークロードやファイルシステムキャッシュのために RAM を解放できます。ただし、ストレージは RAM よりはるかに低速です。スワップは容量とメモリ管理のための手段であり、十分なメモリやアプリケーションのメモリ制限の代わりにはなりません。

## スワップがメモリ管理に関与する仕組み

カーネルは、ワークロード、メモリ圧力、cgroup、swappiness などの調整値に応じて、RAM が完全に尽きる前からスワップを使うことがあります。ファイルを裏付けとする変更されていないページは破棄して元のファイルから読み直せることが多い一方、匿名ページはスワップへ移すか RAM に残す必要があります。

大量のスワップが継続すると、深刻な遅延やスラッシングが起こることがあります。スワップ領域を増やせば必ず性能が改善するとは考えず、メモリ需要、ワーキングセット、圧力、アプリケーションの制限を診断してください。

:::single-choice{#swap-space-anonymous-pages}
スワップへ格納する主な候補となるメモリはどれですか？

::option[`/usr` 配下にインストールされたすべての実行ファイル。]{#swap-space-installed-files explanation="インストール済みファイルはファイルシステムに残り、変更されていないマップ済みページはそこから読み直せます。"}
::option[使用頻度の低い匿名メモリページ。]{#swap-space-anonymous-memory .correct explanation="匿名ページには、単純に読み直せる通常の裏付けファイルがありません。"}
::option[ディスクのパーティションテーブルエントリ。]{#swap-space-partition-table explanation="パーティションメタデータはブロックデバイス上にあり、RAM から退避されるプロセスメモリではありません。"}
:::

## 有効なスワップを調べる

まず読み取り専用のコマンドを使います。

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

これらは、有効なスワップの構成とメモリ全体の数値を表示します。「used」が 0 でなくても、それだけで問題とは限りません。スワップインとスワップアウトの速度、メモリ圧力、遅延、ワークロードの動作と関連付けて判断してください。

:::single-choice{#swap-space-show-active}
有効なスワップ領域を構造化して一覧表示するコマンドはどれですか？

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="show モードは、有効なスワップファイルやデバイスについて、利用可能な場合はサイズ、使用量、優先度を報告します。"}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="mkswap はスワップシグネチャを初期化するもので、読み取り専用の有効領域一覧コマンドではありません。"}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="標準の初期化ツールは `mkswap` であり、フォーマットは状態を問い合わせる操作ではありません。"}
:::

## スワップデバイスを初期化して有効化する

`mkswap` はスワップシグネチャを書き込み、対象にあった以前の有効なメタデータを破壊します。練習には、確認済みの使い捨て対象だけを使ってください。

```bash
$ sudo mkswap /dev/VERIFIED-SWAP-TARGET
$ sudo swapon /dev/VERIFIED-SWAP-TARGET
```

`mkswap` の前には、`mkfs` の前と同様に、モデル、シリアル番号、サイズ、永続的な識別情報、既存のシグネチャ、マウント、RAID、LVM、暗号化、バックアップを確認します。有効化した後、`swapon --show` で正確なソースを確認してください。

永続化する場合は、ローカルの方針に適した種類とオプションを指定し、`/etc/fstab` でスワップ UUID を使います。

```text
UUID=VERIFIED-SWAP-UUID none swap sw 0 0
```

:::single-choice{#swap-space-enable-command}
初期化済みのスワップ領域を有効にするコマンドはどれですか？

::option[`swapon`]{#swap-space-command-swapon .correct explanation="swapon は、有効なスワップデバイスやファイルを、カーネルのアクティブなスワップ集合へ追加します。"}
::option[`mkswap`]{#swap-space-command-mkswap explanation="mkswap はシグネチャを初期化しますが、その領域自体を有効にはしません。"}
::option[`mount`]{#swap-space-command-mount explanation="スワップはディレクトリ用ファイルシステムとしてマウントせず、スワップサブシステムで有効化します。"}
:::

## スワップファイルとそのほかのバックエンド

スワップファイルなら、パーティションを変更せず柔軟に容量を用意できます。ただし、作成要件はファイルシステムごとに異なります。ファイルには、制限の厳しいパーミッション、未対応のホールやコピーオンライト動作を避けた適切な割り当て、スワップシグネチャ、有効化が必要です。どこでも同じ汎用的な `fallocate` 手順をコピーせず、ファイルシステムとディストリビューションの文書に従ってください。

zram のような圧縮 RAM デバイスは、CPU と容量のトレードオフが異なる別のスワップ階層になります。暗号化スワップは保存中のページを保護でき、休止状態には再開設定と十分な適合ストレージが必要です。これらの目的は容量設計に影響します。

スワップを RAM の必ず 2 倍にすべきという普遍的な規則はありません。ワークロードのピーク、望ましい障害時の動作、休止状態の要件、ストレージの遅延と耐久性、クラッシュダンプ設計、運用監視を基に容量を決めてください。

:::single-choice{#swap-space-sizing-rule}
スワップ容量を決める最適な基準はどれですか？

::option[常に搭載 RAM のちょうど 2 倍。]{#swap-space-twice-ram explanation="歴史的なこの経験則は、すべてのワークロードや現代のメモリ容量には適しません。"}
::option[測定したワークロード要件、休止状態の目的、障害時の方針。]{#swap-space-sizing-requirements .correct explanation="固定の RAM 倍率より、システムの用途と観測されたメモリ動作が重要です。"}
::option[SSD を搭載したシステムでは常にゼロ。]{#swap-space-zero-ssd explanation="ストレージの種類だけでは、メモリ圧力や休止状態の要件は決まりません。"}
:::

## スワップを安全に無効化する

確認済みの領域を指定して無効化します。

```bash
$ sudo swapoff /dev/VERIFIED-SWAP-TARGET
```

カーネルは、その領域にある使用中のスワップページを別の場所へ移動する必要があります。RAM と残りのスワップに収まらなければ、操作が失敗したり危険なメモリ圧力が生じたりします。先にワークロードを停止または制限してメモリを監視し、正しい対象だと確認してから永続的な fstab エントリを削除します。ストレージを別用途に使う前に、`swapon --show` で無効化を確認してください。

:::single-choice{#swap-space-swapoff-capacity}
高負荷のシステムで `swapoff` が失敗したり危険になったりするのはなぜですか？

::option[swapoff は必ずすべての RAM モジュールを再フォーマットするから。]{#swap-space-formats-ram explanation="変更するのは有効なスワップ構成であり、物理メモリハードウェアをフォーマットすることはありません。"}
::option[その領域にあるページを収める容量が、RAM またはほかのスワップに必要だから。]{#swap-space-pages-need-capacity .correct explanation="無効化では、システムの稼働中に使用中のスワップページを移動する必要があります。"}
::option[無効なスワップ領域は `/swap` にマウントしたままにする必要があるから。]{#swap-space-mounted-path explanation="スワップ領域は、ディレクトリへマウントするファイルシステムではありません。"}
:::

管理された環境でファイルのパーミッション、有効化、永続化を練習するには、[Linux でスワップファイルを作成して有効にする](https://labex.io/ja/labs/comptia-create-and-activate-a-swap-file-in-linux-590858) を利用してください。

## まとめ

これで、スワップを明示的なメモリ管理リソースとして扱えるようになりました。

1. スワップを、主にメモリ圧力下の匿名メモリと関連付ける。
2. 容量を変更する前に、有効なスワップとワークロードの動作を調べる。
3. 確認済みの使い捨て対象だけを初期化し、`swapon` で有効化する。
4. ワークロードと休止状態の要件に応じて、スワップの容量と保護を設計する。
5. `swapoff` の前に、ページを移動できる容量を確保する。
