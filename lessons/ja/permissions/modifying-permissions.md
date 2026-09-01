---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "ja"
order_index: 2
title: "権限の変更"
description: "シンボリック形式と8進形式の `chmod` を使って、Linux の権限ビットを変更する方法を学びます。"
meta_title: "権限の変更 - パーミッション管理"
meta_description: "chmod コマンドを使用して Linux で権限を変更する方法を学びます。このガイドでは、シンボリック方式と数値方式の両方をカバーし、ファイルとディレクトリへのアクセスを安全に管理できるようにします。システム管理向上のために Linux の権限変更プロセスを習得しましょう。"
meta_keywords: "Linux 権限変更，Linux 権限変更方法，Linux 権限変更方法，Linux ファイル権限変更方法，chmod, ファイル権限，Linux セキュリティ，シンボリック権限，数値権限"
---

`chmod` コマンドは、ファイルとディレクトリのモードビットを変更します。通常、この変更を行えるのはファイル所有者か、必要な特権を持つプロセスだけです。`chmod` の実行前後に `ls -l` で現在のモードを確認してください。

## シンボリック形式を使う

シンボリック形式では、変更する権限クラス、変更方法、対象の権限を指定します。

- `u` は所有者クラスを選びます。
- `g` はグループクラスを選びます。
- `o` はその他クラスを選びます。
- `a` は三つのクラスすべてを選びます。
- `+` は権限を追加し、`-` は削除し、`=` は選択したクラスを厳密に設定します。

たとえば、所有者へ実行権限を追加します。

```bash
$ chmod u+x myfile
```

グループから書き込み権限を削除します。

```bash
$ chmod g-w myfile
```

所有者とグループの両方へ書き込み権限を追加します。

```bash
$ chmod ug+w myfile
```

複数の指定はコンマで区切れます。次のコマンドは所有者を読み書き、グループを読み取りのみ、その他を権限なしへ設定します。

```bash
$ chmod u=rw,g=r,o= myfile
```

`chmod +x myfile` のようにクラスを省略すると、どのクラスが変更されるかにプロセスの umask が影響します。クラスを明記すれば、意図した結果を確認しやすくなります。

:::single-choice{#modifying-permissions-remove-group-write} ほかのグループ権限ビットを変えず、グループの書き込み権限を削除するシンボリック形式はどれですか？

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="これはグループではなく所有者クラスから書き込み権限を削除します。"}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="`g` がグループクラスを選び、`-` がビットを削除し、`w` が書き込み権限を指定します。"}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="`=` は書き込みを削除するのではなく、選択クラスを書き込み権限だけに置き換えます。"}
:::

## 8進形式を使う

8進形式では、各基本権限トリプレットを1桁で設定します。各クラス内で次の値を足します。

- `4`: 読み取り
- `2`: 書き込み
- `1`: 実行
- `0`: 権限なし

右端の3桁は、所有者、グループ、その他をこの順で表します。例を示します。

```bash
$ chmod 755 myfile
```

モード `755` は次のように展開できます。

- 所有者の `7` は `4 + 2 + 1`、つまり `rwx`。
- グループの `5` は `4 + 1`、つまり `r-x`。
- その他の `5` は `4 + 1`、つまり `r-x`。

`+` や `-` によるシンボリック操作と異なり、8進形式は通常権限の完全な組を指定します。特殊モードビットに使う任意の先頭桁は、後のレッスンで扱います。

:::single-choice{#modifying-permissions-octal-read-value} 読み取り権限を表す8進値はどれですか？

::option[`1`]{#modifying-permissions-value-one explanation="値 `1` は実行権限を表します。"}
::option[`2`]{#modifying-permissions-value-two explanation="値 `2` は書き込み権限を表します。"}
::option[`4`]{#modifying-permissions-value-four .correct explanation="読み取り権限はクラスの桁へ8進値 `4` を加えます。"}
:::

:::single-choice{#modifying-permissions-mode-640} `chmod 640 report` はどの通常権限を設定しますか？

::option[所有者は読み取り、グループは書き込み、その他は実行。]{#modifying-permissions-640-separated explanation="8進数の各桁はクラスごとの合計であり、読み取り、書き込み、実行を別々の列で表したものではありません。"}
::option[所有者は読み取り／実行、グループは書き込み、その他はなし。]{#modifying-permissions-640-wrong-sums explanation="所有者の `6` は読み取りと書き込み、グループの `4` は読み取りです。"}
::option[所有者は読み取り／書き込み、グループは読み取り、その他はなし。]{#modifying-permissions-640-correct .correct explanation="各桁は所有者 `6`（`rw-`）、グループ `4`（`r--`）、その他 `0`（`---`）へ展開されます。"}
:::

## 安全に変更を適用する

ユーザーとサービスに必要なアクセスだけを与えます。`chmod 777` は各クラスへ読み取り、書き込み、実行を与え、所有権、ディレクトリ探索、ACL、サービスのポリシーといった原因を解決せずに危険だけを増やすことが多いため、トラブルシューティングの近道として使ってはいけません。

再帰的な変更には特に注意が必要です。対象ツリーを事前に確認し、シンボリックリンクとマウント済みファイルシステムを考慮し、小さな範囲でテストしてから `chmod -R` を使います。変更後は、意図したオブジェクトへ影響したと仮定せず、結果のモードを検証してください。

:::single-choice{#modifying-permissions-least-privilege} `chmod 777` がアクセス問題への一般的な解決策として不適切なのはなぜですか？

::option[所有者からすべての権限を削除するから。]{#modifying-permissions-777-removes explanation="各 `7` は読み取り、書き込み、実行を与え、所有者の権限を削除しません。"}
::option[所有者、グループ、その他へすべての基本権限を与えるから。]{#modifying-permissions-777-grants-all .correct explanation="三つのクラスすべてが `rwx` を受け取り、実際に必要なアクセスを超えることがよくあります。"}
::option[ファイルのグループ所有権だけを変更するから。]{#modifying-permissions-777-group explanation="`chmod` はモードビットを変更します。グループ所有権は `chgrp` や `chown` などで変更します。"}
:::

隔離された環境で実践するには、[Linux のユーザー、グループ、ファイルパーミッション](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002)ラボを使い、変更前後の各モードを確認してください。

## まとめ

意図を明確にした `chmod` 式で、Linux の通常モードビットを変更できるようになりました。

1. 対象を絞った追加、削除、代入にはシンボリック形式を使う。
2. 読み取り `4`、書き込み `2`、実行 `1` から8進数の各桁を組み立てる。
3. 8進数のクラスを所有者、グループ、その他の順に読む。
4. 変更を検証し、必要な最小権限を適用する。
