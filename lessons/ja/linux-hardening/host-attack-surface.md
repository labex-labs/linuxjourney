---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "ja"
order_index: 1
title: "攻撃対象領域"
description: "Linux ホストで公開が必要な機能と、見直すべきアクセス経路の見分け方を学びます。"
meta_title: "攻撃対象領域 - Linux の堅牢化"
meta_description: "Linux ホストで公開が必要な機能と、見直すべきアクセス経路の見分け方を学びます。"
meta_keywords: "攻撃対象領域, Linux の堅牢化, サイバーセキュリティ, Linux Journey"
---

Linux ホストでは、公開の Web ページや保守用の接続、バックグラウンドサービスが使われることがあります。まず、各サービスの役割と、誰にアクセスを許すべきかを書き出します。こうすると、用途がはっきりしないアクセスを見つけやすくなります。

## 想定するアクセスを一覧にする

簡単な台帳を作り、リソースごとに利用する人やプログラムを結び付けます。練習用ホストの例を見てみましょう。

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

**アクセス経路**とは、人やプログラムがリソースに到達するための経路です。利用者やプログラムが到達でき、システムに影響を与えられるインターフェースの集合は、**攻撃対象領域**の一部です。

:::single-choice{#host-attack-surface-intended-audience} この台帳のうち、公開ネットワークからのアクセスが必要なのはどれですか？

::option[保守用 SSH です。]{#host-attack-surface-intended-audience-b explanation="想定している利用者は運用チームです。"}
::option[公開のトップページです。]{#host-attack-surface-intended-audience-a .correct explanation="ホストの外部から訪れる人も利用者に含まれます。"}
::option[プレビュー画面です。]{#host-attack-surface-intended-audience-c explanation="想定する用途はホスト上での利用です。"}
:::

## 想定と実際のアクセスを比べる

台帳ではホスト上だけで利用するとされているのに、プレビュー画面にネットワーク経由でアクセスできるとします。変更する前に、管理担当者に確認し、実際の経路を確かめます。サービスの稼働は必要でも、リモートからのリクエストを受け付ける必要がない場合があります。

:::single-choice{#host-attack-surface-mismatch} 記載されたポリシーに照らして、見直すべき観測結果はどれですか？

::option[訪問者がプレビュー画面にアクセスできます。]{#host-attack-surface-mismatch-b .correct explanation="想定する利用者以外にも、画面へのアクセス経路があります。"}
::option[訪問者がトップページを開けます。]{#host-attack-surface-mismatch-a explanation="それはトップページの想定どおりの用途です。"}
::option[担当者がホスト上でプレビューを開けます。]{#host-attack-surface-mismatch-c explanation="ローカルからのアクセスは記載された用途に合っています。"}
:::

## 確認の優先順位を付ける

不要で、悪用された場合の影響が大きいアクセスから確認します。練習例では、サイトを変更できるプレビュー画面は、重要なデータを持たない未使用サービスより優先度が高くなります。想定する利用者、確認した公開範囲、正当な利用を妨げずに制限が機能することを確かめるテストを記録します。

:::single-choice{#host-attack-surface-priority-check} プレビューへのアクセスを変更した後、どの二つの結果がそろえば、制限が目的を満たしたと確認できますか？

::option[画面が引き続きローカルからのリクエストを受け付けます。]{#host-attack-surface-priority-check-a explanation="必要なアクセスは確認できますが、想定外のリモート経路は未確認です。"}
::option[マシンが再起動し、以前と同じホスト名を使っています。]{#host-attack-surface-priority-check-b explanation="ホストの状態からは、ポリシーが守られたかは分かりません。"}
::option[担当者はホスト上で引き続き利用でき、想定外のリモート経路は閉じています。]{#host-attack-surface-priority-check-c .correct explanation="二つの結果を合わせると、必要なアクセスと制限の両方を確認できます。"}
:::

## まとめ

どのアクセス経路を堅牢化の観点から見直すべきか判断できるようになりました。

1. リソースと想定する利用者を書き出します。
2. 想定しているアクセスと実際に観測したアクセスを比較します。
3. 変更後は、制限と正当な利用の両方を確認します。
