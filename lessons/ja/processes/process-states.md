---
lang: "ja"
title: "プロセス状態"
meta_title: "プロセス状態 - プロセス"
meta_description: "`ps aux` を使用して Linux プロセス状態 (R, S, D, Z, T) を学びましょう。一般的な STAT コードを理解し、プロセスを効果的に管理します。Linux の学習を始めましょう！"
meta_keywords: "Linux プロセス状態，ps aux, プロセス管理，Linux チュートリアル，Linux 初心者，STAT コード，Linux ガイド"
---

## Lesson Content

`ps aux` コマンドをもう一度見てみましょう。

```bash
ps aux
```

STAT 列には多くの値が表示されます。Linux プロセスはさまざまな状態になることがあります。最もよく見られる一般的な状態コードを以下に示します。

- **R**: Running または runnable。CPU が処理するのを待っている状態です。
- **S**: Interruptible sleep。端末からの入力など、イベントが完了するのを待っている状態です。
- **D**: Uninterruptible sleep。シグナルで強制終了したり中断したりできないプロセスです。通常、これらを終了させるには、再起動するか問題を修正する必要があります。
- **Z**: Zombie。以前のレッスンで、ゾンビはステータスが収集されるのを待っている終了したプロセスであると説明しました。
- **T**: Stopped。一時停止/停止されたプロセスです。

## Exercise

システムで実行中のプロセスを確認し、それらのプロセス状態を調べてください。

## Quiz Question

Uninterruptible sleep を表す STAT コードは何ですか？

## Quiz Answer

D
