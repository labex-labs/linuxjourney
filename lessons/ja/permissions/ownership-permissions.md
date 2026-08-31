---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "ja"
order_index: 3
title: "所有権の権限"
description: "Linux のファイルシステムオブジェクトについて、ユーザー所有者とグループ所有者を確認・変更する方法を学びます。"
meta_title: "所有権の権限 - 権限"
meta_description: "chown および chgrp Linux コマンドの使用方法を学習し、Linux ファイルの所有権を習得します。この Linux チュートリアルでは、ファイルのユーザーおよびグループの所有権を変更する方法を説明します。これは Linux 権限を管理するための重要なスキルです。"
meta_keywords: "chown, chgrp, Linux ファイル所有権，ファイル所有者の変更，ファイルグループの変更，Linux 権限，Linux コマンド，Linux チュートリアル，Linux ガイド，ユーザー所有権，グループ所有権"
---

Linux の各ファイルシステムオブジェクトには、ユーザー所有者とグループ所有者が記録されています。これらの識別情報は、所有者とグループのどちらの権限トリプレットを適用するかを決めますが、それ自体が特定の権限を与えるわけではありません。所有権とモードの両方を `ls -l` で確認してください。

## ユーザー所有者を変更する

change owner の略である `chown` を使い、別のユーザー所有者を割り当てます。

```bash
$ sudo chown patty myfile
```

これは `myfile` のユーザー所有者を `patty` へ変更し、グループは変えません。現在の所有者が自分であっても、ファイルのユーザー所有者を変更するには通常、適切な特権が必要です。この制限により、クォータなど所有権に基づく制御を回避するためのファイル移管を防ぎます。

:::single-choice{#ownership-permissions-change-user}
グループを変えず、`myfile` のユーザー所有者を `patty` へ変更するコマンドはどれですか？

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="`chown` の所有権オペランドにユーザー名だけを指定すると、ユーザー所有者を変更し、グループを維持します。"}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp` はユーザー所有者ではなくグループ所有者を変更します。"}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod` はモードビットを変更し、新しい所有者としてユーザー名を受け取りません。"}
:::

## グループ所有者を変更する

`chgrp` を使って別のグループ所有者を割り当てます。

```bash
$ chgrp whales myfile
```

一般的なシステムでは、非特権の所有者がファイルのグループを変更できるのは、自身が所属するグループに限られます。特権プロセスはより広い変更を行えます。同等の `chown` 形式では先頭にコロンを付けます。

```bash
$ chown :whales myfile
```

変更後、カーネルがグループクラスを選んだ場合は、そのグループのモードビットが適用されます。グループを変えても、読み取り、書き込み、実行ビットが自動的に追加されることはありません。

:::single-choice{#ownership-permissions-change-group}
`chgrp whales myfile` は何を変更しますか？

::option[`myfile` に記録されたユーザー所有者。]{#ownership-permissions-group-not-user explanation="ユーザー所有者は `chgrp` ではなく `chown` で変更します。"}
::option[`whales` グループに列挙されたメンバー。]{#ownership-permissions-group-members explanation="このコマンドはファイルのメタデータを変更し、システムのグループ所属データベースは編集しません。"}
::option[`myfile` に記録されたグループ所有者。]{#ownership-permissions-group-owner .correct explanation="`chgrp` は指定したグループをファイルシステムオブジェクトのグループ所有者として割り当てます。"}
:::

## ユーザーとグループを同時に変更する

`chown` に `USER:GROUP` を指定すると、両方のフィールドを一度に更新できます。

```bash
$ sudo chown patty:whales myfile
```

このコマンドは `patty` をユーザー所有者、`whales` をグループ所有者へ割り当てます。成功したと仮定せず、結果を確認してください。

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both}
一つの `chown` コマンドでユーザー `patty` とグループ `whales` を割り当てる所有権指定はどれですか？

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="ユーザー名とグループ名は、組み合わせた所有権指定内でコロンにより区切ります。"}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="スラッシュは、ここで紹介した `chown` のユーザーとグループを区切る記号ではありません。"}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="`chown` の二つの所有権フィールドを組み合わせるためにプラス記号は使いません。"}
:::

## 再帰変更を慎重に扱う

`-R` オプションは所有権を再帰的に変更しますが、広範な再帰コマンドは予期しないディレクトリツリーを越えたり、サービスデータへ影響したりする場合があります。正確な対象を確認し、使用する実装のシンボリックリンク動作を理解し、ツリーを事前に確認し、大きな階層を変更する前に小さなサンプルで検証してください。例にある特権付き所有権コマンドを、範囲を確認せず実システムへコピーしてはいけません。

:::single-choice{#ownership-permissions-mode-separate}
ファイルのグループ所有者を変更すると、通常のグループ権限ビットはどうなりますか？

::option[必ず自動的に読み取りと書き込みになる。]{#ownership-permissions-mode-read-write explanation="`chgrp` が固定のグループモードを自動選択することはありません。"}
::option[所有者の権限トリプレットからコピーされる。]{#ownership-permissions-mode-copied explanation="所有権を変更しても、所有者とグループのトリプレットは独立したままです。"}
::option[別の操作で変更しない限り、設定されたまま残る。]{#ownership-permissions-mode-unchanged .correct explanation="所有権フィールドとモードビットは別のメタデータであり、グループ変更だけで新しいグループビットは付与されません。"}
:::

隔離された環境で練習するには、[Linux のユーザー、グループ、ファイルパーミッション](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)ラボで、ファイルモードとともに所有権の確認・変更を行ってください。

## まとめ

所有権メタデータと権限ビットを区別し、意図的に変更できるようになりました。

1. `chown USER FILE` でユーザー所有者を変更する。
2. `chgrp GROUP FILE` または `chown :GROUP FILE` でグループ所有者を変更する。
3. `chown USER:GROUP FILE` で両方のフィールドを設定する。
4. 結果を検証し、再帰変更の範囲を慎重に扱う。
