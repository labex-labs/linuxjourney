---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "ja"
order_index: 8
title: "粘着ビット"
description: "sticky bit が `/tmp` のような共有書き込み可能ディレクトリのエントリーを保護する仕組みを学びます。"
meta_title: "粘着ビット - パーミッション"
meta_description: "Linux および Unix ファイルパーミッションにおける粘着ビットの目的を探ります。/tmp のような共有ディレクトリ内のファイルを粘着ビットがどのように保護するか、そして chmod を使用して設定する方法を学びます。"
meta_keywords: "粘着ビット，粘着ビット linux, unix ファイルパーミッション 粘着ビット，chmod +t, /tmp ディレクトリ，ファイルパーミッション，linux セキュリティ"
---

書き込み可能なディレクトリでは通常、権限を持つユーザーが、自身では所有していないファイルであっても内部のエントリーを削除・改名できます。sticky bit は所有権による制限を追加し、共有書き込み可能ディレクトリをより安全にします。

## Sticky Bit が削除を制限する仕組み

ディレクトリに sticky bit が設定されている場合、Linux は通常、適切な特権を持つプロセス、ディレクトリ所有者、またはエントリー所有者だけに、そのエントリーの削除・改名を許可します。通常のディレクトリ書き込み権限と検索権限も引き続き必要です。

この制限が関係するのはディレクトリエントリーです。ファイルの権限が許可している場合に、ファイル所有者が内容を編集することまでは防がず、ディレクトリを非公開にするものでもありません。

:::single-choice{#sticky-bit-removal-rule}
Sticky bit のある共有ディレクトリで、通常、特定のエントリーを削除できる一般ユーザーは誰ですか？

::option[ディレクトリを一覧表示できるすべてのユーザー。]{#sticky-bit-any-reader explanation="ディレクトリの読み取り権限で名前が見えても、sticky bit の所有権制限は回避できません。"}
::option[必要なディレクトリアクセスを持つ、そのエントリーの所有者。]{#sticky-bit-entry-owner .correct explanation="エントリー所有者は、sticky ディレクトリの規則で通常許可される識別情報の一つです。"}
::option[エントリーのグループに所属するユーザーだけ。]{#sticky-bit-entry-group explanation="グループ所属だけでは、sticky bit が定義する所有権の例外になりません。"}
:::

## `/tmp` でビットを見分ける

システムの一時ディレクトリが一般的な例です。

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

末尾の小文字 `t` は、その他クラスの実行位置にあります。Sticky bit とその他の実行権限の両方があることを示します。大文字 `T` は sticky bit が設定され、その他の実行権限がないことを示します。

`/tmp` は一般に全ユーザーが書き込み・検索できるため、複数ユーザーがエントリーを作成できます。Sticky bit により、ディレクトリが全ユーザー書き込み可能であるという理由だけで、通常ユーザーが別ユーザーのエントリーを削除することを防ぎます。それでもアプリケーションは一時オブジェクトを安全に作成しなければなりません。予測可能な名前、安全でないリンク、弱いファイルモードには別の危険があるためです。

:::single-choice{#sticky-bit-lowercase-t}
ディレクトリモードの末尾にある小文字 `t` は何を示しますか？

::option[Sticky bit とその他の実行権限が設定されている。]{#sticky-bit-t-with-execute .correct explanation="小文字 `t` は sticky 特殊ビットと通常のその他実行ビットを組み合わせて表します。"}
::option[Sticky bit は設定されているが、その他の実行権限はない。]{#sticky-bit-t-without-execute explanation="その組み合わせは大文字 `T` で表示されます。"}
::option[Setgid とグループ実行が設定されている。]{#sticky-bit-setgid-position explanation="Setgid は末尾のその他位置ではなく、グループの実行位置に現れます。"}
:::

## Sticky Bit を設定・削除する

シンボリック形式でビットを設定します。

```bash
$ chmod +t shared-directory
```

先頭の特殊ビット8進桁では、sticky bit は `1` を加えます。

```bash
$ chmod 1777 shared-directory
```

先頭の `1` が sticky bit を設定し、`777` が通常モードを指定します。このモードが適切なのは、そのディレクトリを意図的にすべてのローカルユーザーで共有する場合だけです。チーム用ディレクトリでは、より狭いグループ権限の方が適切な場合があります。Sticky bit だけを削除するには `chmod -t shared-directory` を使います。

:::single-choice{#sticky-bit-octal-value}
Sticky bit を表す先頭の8進値はどれですか？

::option[`2`]{#sticky-bit-value-two explanation="先頭の `2` は setgid を表します。"}
::option[`1`]{#sticky-bit-value-one .correct explanation="Sticky bit は先頭の特殊ビット桁へ `1` を加えます。"}
::option[`4`]{#sticky-bit-value-four explanation="先頭の `4` は setuid を表します。"}
:::

## ディレクトリポリシー全体を検証する

Sticky bit は書き込み権限や検索権限を与えません。通常権限がディレクトリの変更を許可した後で、特定の削除・改名操作を制限するだけです。ディレクトリの所有者、グループ、通常モード、ACL、マウントのコンテキストをまとめて確認してください。稼働中システムの `/tmp` を変更せず、隔離環境で非特権アカウントを使ってテストします。

:::single-choice{#sticky-bit-access-scope}
Sticky bit を追加すると、書き込み不可のディレクトリが他のユーザーから書き込み可能になりますか？

::option[はい。sticky bit はすべてのクラスへ自動的に書き込み権限を追加する。]{#sticky-bit-adds-write explanation="特殊ビットが所有者、グループ、その他の書き込みビットを書き換えることはありません。"}
::option[はい。sticky bit はディレクトリのその他権限トリプレットを無効にする。]{#sticky-bit-disables-other explanation="その他のトリプレットは通常のアクセス確認へ引き続き参加します。"}
::option[いいえ。通常の書き込み権限と検索権限が引き続きアクセスを制御する。]{#sticky-bit-no-write-grant .correct explanation="Sticky bit は特定の削除・改名操作を狭めますが、不足している通常権限を追加しません。"}
:::

練習では、破棄可能な共有ディレクトリを作り、適切な通常モードと sticky bit を設定してから、二つの非特権ユーザーとしてエントリー削除をテストしてください。[ファイルを削除・移動する](https://labex.io/labs/linux-delete-and-move-files-7777)ラボで、基礎となる改名と削除操作を復習できます。

## まとめ

共有ディレクトリの sticky bit を説明・検証できるようになりました。

1. Sticky bit を、削除と改名に対する所有権制限へ関連付ける。
2. 長形式一覧の小文字 `t` と大文字 `T` を認識する。
3. シンボリック形式または先頭の8進値 `1` でビットを設定する。
4. Sticky bit を通常のディレクトリ権限と合わせて評価する。
