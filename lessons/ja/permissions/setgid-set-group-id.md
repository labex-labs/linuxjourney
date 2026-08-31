---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "ja"
order_index: 6
title: "Setgid"
description: "set-group-ID が実行時の資格情報と、共有ディレクトリのグループ継承へ与える影響を学びます。"
meta_title: "Setgid - パーミッション"
meta_description: "Linux SGID（Set Group ID）パーミッション、その仕組み、および変更方法について学びます。この重要な Linux セキュリティ概念を理解しましょう。"
meta_keywords: "Linux SGID, Set Group ID, Linux パーミッション，chmod g+s, Linux セキュリティ，初心者 Linux, Linux チュートリアル"
---

set-group-ID ビットは一般に setgid または SGID と呼ばれ、二つの重要な用途があります。実行可能な通常ファイルでは、新しいプロセスの実効グループ ID を変更できます。ディレクトリでは、新しく作られるエントリーにそのディレクトリのグループを継承させるため、共同作業用ツリーで特に便利です。

## 実行可能ファイルの Setgid

長形式一覧では、グループの実行位置に setgid が表示されます。

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

小文字 `s` は setgid とグループ実行の両方が設定されていることを示します。大文字 `S` は setgid が設定され、グループ実行がないことを示します。

実行時にカーネルがこのビットを有効にすると、プロセスは実行ファイルのグループ所有者に基づく実効グループ ID を受け取ります。`nosuid` マウントなどの制御によって動作が抑止される場合があり、あらゆるファイル種別と環境に共通する保証として扱ってはいけません。

:::single-choice{#setgid-executable-effect}
実行可能ファイルの setgid が有効なとき、実行ファイルのグループ所有者から得る資格情報はどれですか？

::option[プロセスの実効グループ ID。]{#setgid-effective-group .correct explanation="Set-group-ID 実行は、実行ファイル所有者のグループをプロセスの実効グループ識別情報として設定します。"}
::option[プロセスの実ユーザー ID。]{#setgid-real-user explanation="このビットが関係するのはグループ資格情報であり、呼び出し元の実ユーザー識別情報ではありません。"}
::option[プロセスが開くすべてのファイルの所有者。]{#setgid-opened-owner explanation="実行時資格情報によって、開いたファイルの所有権メタデータが書き換えられることはありません。"}
:::

## ディレクトリの Setgid

ディレクトリの setgid には別の目的があります。新しいファイルとサブディレクトリは通常、作成者の既定グループではなく、そのディレクトリのグループを継承します。Linux では新しいサブディレクトリが setgid ビットも継承するため、共有プロジェクトツリーで一貫したグループを維持できます。

Setgid 自体がグループ書き込み権限を与えるわけではありません。ディレクトリのモード、プロセスの umask、要求された作成モード、既定 ACL などの制御によって、引き続きアクセスが決まります。

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance}
`/srv/project` の setgid によって、新しく作成したファイルは通常何を継承しますか？

::option[ディレクトリのユーザー所有者。]{#setgid-inherit-user explanation="ディレクトリの setgid が影響するのはグループ継承であり、新規エントリーのユーザー所有者ではありません。"}
::option[ディレクトリの完全な権限モード。]{#setgid-inherit-mode explanation="作成権限は引き続き、要求モード、umask、ACL などから計算されます。"}
::option[ディレクトリのグループ所有者。]{#setgid-inherit-group .correct explanation="新しいエントリーは通常、setgid ディレクトリのグループを受け取り、一貫した共有所有権を支えます。"}
:::

## Setgid を設定・削除する

シンボリック形式でビットを設定します。

```bash
$ sudo chmod g+s myfile
```

先頭の8進数 `2` を使い、通常モードビットと同時に設定できます。

```bash
$ sudo chmod 2755 myfile
```

特殊ビットだけを削除するには `chmod g-s myfile` を使います。

:::single-choice{#setgid-octal-value}
Setgid が先頭の特殊ビット8進桁へ加える値はどれですか？

::option[`4`]{#setgid-value-four explanation="値 `4` は特殊ビット桁で setuid を表します。"}
::option[`1`]{#setgid-value-one explanation="値 `1` は sticky bit を表します。"}
::option[`2`]{#setgid-value-two .correct explanation="Setgid は `2755` のように値 `2` を加えます。"}
:::

## 共有ディレクトリを安全に使う

共同作業用ディレクトリでは、意図したグループ所有者、setgid、範囲を絞ったアクセスビットを組み合わせます。代表的なユーザーとして作成をテストし、`ls -ld` で結果を確認してください。グループ共有の問題を解決するためだけにツリーを全ユーザー書き込み可能にしてはいけません。専用グループ、適切な umask または既定 ACL、setgid ディレクトリを組み合わせれば、通常はより明確に制御できます。

:::single-choice{#setgid-directory-write-access}
Setgid だけを設定すれば、グループメンバーはディレクトリにファイルを作成できますか？

::option[はい。setgid は常にグループの読み取り、書き込み、実行を追加する。]{#setgid-adds-rwx explanation="特殊ビットが三つの通常グループ権限ビットを自動的に変更することはありません。"}
::option[はい。setgid はグループメンバーに対するすべての確認を無効にする。]{#setgid-disables-checks explanation="通常の任意アクセス制御と追加のセキュリティ確認は引き続き適用されます。"}
::option[いいえ。該当する書き込み権限と検索権限も作成を許可する必要がある。]{#setgid-no-automatic-write .correct explanation="Setgid はグループ継承を制御し、ディレクトリへの書き込みは通常権限などのアクセス制御が決めます。"}
:::

## まとめ

実行可能ファイルとディレクトリにおける setgid の意味を区別できるようになりました。

1. グループの実行位置にある setgid を認識する。
2. 実行可能ファイルの setgid を実効グループ ID へ関連付ける。
3. ディレクトリの setgid で共有ツリーのグループ所有権を維持する。
4. 通常の書き込み権限と混同せず、ビットを設定・削除する。
