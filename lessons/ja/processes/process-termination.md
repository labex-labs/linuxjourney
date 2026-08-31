---
lesson_id: "process-termination"
course_id: "processes"
lang: "ja"
order_index: 5
title: "プロセス終了"
description: "終了状態、待機、ゾンビ、親の付け替えが Linux プロセスのライフサイクルを完了する仕組みを学びます。"
meta_title: "プロセス終了 - プロセス管理"
meta_description: "Linux のプロセス終了、wait システムコール、そしてゾンビプロセスと孤児プロセスの違いについて解説します。安定したシステムのために、子プロセスの状態管理と Linux での kill 方法を学びましょう。"
meta_keywords: "Linux プロセス終了，ゾンビプロセス，孤児プロセス，ゾンビ vs 孤児プロセス，Linux 子プロセス kill, wait システムコール，_exit, プロセス管理"
---

プロセスは main 関数から戻る、終了インターフェースを呼ぶ、シグナルで終了させられる、という方法で終わります。カーネルは大半のリソースを解放しますが、親が終了情報を回収するまで親子間の記録は続きます。

## 終了状態

正常終了するプログラムは整数の状態を返します。慣例上 `0` は成功、0以外は何らかの失敗または別の結果です。0以外の正確な意味は各プログラムのインターフェースが定義します。

シェルでは直前のフォアグラウンドパイプラインの状態を確認できます。

```bash
$ command
$ printf '%s\n' "$?"
```

シェルの状態は限られた符号化範囲で、シグナル終了も表すため、完全な診断記録ではありません。各プログラムの終了コードは文書で確認します。

:::single-choice{#process-termination-success-status}
Unix の慣例で正常終了の成功を示す状態はどれですか？

::option[`1`]{#process-termination-status-one explanation="多くのプログラムが一般的な失敗に1を使いますが、意味はコマンド固有です。"}
::option[`0`]{#process-termination-status-zero .correct explanation="正常な状態0が慣例上、処理の成功を示します。"}
::option[`255`]{#process-termination-status-255 explanation="0以外で、慣例上の成功を表しません。"}
:::

## 待機と回収

カーネルは子がどう終了したかを記録し、親へ通知します。親は `wait()` システムコール群で情報を取得し、この記録の回収を reaping と呼びます。

待機は実行の調整にも使います。シェルはフォアグラウンドコマンドを待ってから次のプロンプトを出し、バックグラウンドジョブの待機は延期できます。長く動く親は、無関係な作業を止めず子を回収する設計が必要です。

:::single-choice{#process-termination-wait-purpose}
成功した wait 操作で親が取得できるものは何ですか？

::option[子の終了情報。]{#process-termination-wait-status .correct explanation="wait 群は子が停止・終了した方法を報告し、完了した子を回収します。"}
::option[子の以前のアドレス空間のコピー。]{#process-termination-wait-memory explanation="大半のメモリはすでに解放され、wait() が親へ返すものではありません。"}
::option[子が開いた全ファイルの所有権。]{#process-termination-wait-files explanation="待機でファイルシステムの所有権メタデータは移転しません。"}
:::

## ゾンビプロセス

子が終了してから終了記録を回収されるまで、`ps` で状態 `Z` のゾンビとして現れます。すでに実行せず通常のアドレス空間もありませんが、最小限のプロセス表エントリーと使用記録が残ります。

ゾンビへシグナルを送っても再び終了させられません。蓄積する場合は待機していない親を診断し、適切な運用手順で親を修正・再起動するか、回収するプロセスへ親を付け替えます。大量になると PID またはプロセス表の容量を使い切ることがあります。

:::single-choice{#process-termination-zombie-definition}
ゾンビプロセスに当てはまる説明はどれですか？

::option[親がすでに終了した、実行中の子。]{#process-termination-zombie-orphan explanation="これは孤児となった子で、ゾンビ状態ではありません。"}
::option[実行を終えたが、終了記録をまだ回収されていない子。]{#process-termination-zombie-unreaped .correct explanation="実行は停止済みですが、親のためにカーネルが最小限の状態を保持します。"}
::option[割り込み不可能なループで CPU を消費するプロセス。]{#process-termination-zombie-cpu explanation="ゾンビは命令を実行せず、CPU 時間を消費しません。"}
:::

## 孤児と親の付け替え

子が残ったまま親が終了すると、カーネルは該当 PID 名前空間の適切な subreaper または init プロセスへ子を付け替えます。その子は実行中、スリープ中、停止中のいずれでもよく、後にゾンビになる場合もあります。「孤児」は1つの実行状態ではなく、元の親関係を失ったことを表します。

引き取ったプロセスが終了状態の回収責任を負います。サービスマネージャーやコンテナ環境では、新しい親が必ずホストの PID 1 だと思い込めません。

:::single-choice{#process-termination-orphan-definition}
プロセスが元の親より長く生きるとどうなりますか？

::option[適切な subreaper または名前空間の init プロセスへ付け替えられる。]{#process-termination-orphan-reparented .correct explanation="カーネルは引き取り先を割り当て、有効な親関係を保ちます。"}
::option[終了していなくても即座にゾンビになる。]{#process-termination-orphan-zombie explanation="ゾンビ状態は実行終了後、状態回収待ちになって初めて始まります。"}
::option[PID を永久に失い、匿名で実行を続ける。]{#process-termination-orphan-no-pid explanation="実行中の孤児は、親関係が変わってもプロセス ID を保ちます。"}
:::

[Linux プロセスの管理と監視](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) では、本番ワークロードを妨げず終了コードとプロセス状態を観測できます。

## まとめ

実行の終了と、親側での後始末を区別できるようになりました。

1. 0を慣例上の成功として解釈し、0以外はプログラムの文書で確認する。
2. 待機で子の終了情報を回収する。
3. ゾンビを、終了済みだが未回収の子として理解する。
4. 孤児を、元の親の終了後に親を付け替えられた子として理解する。
