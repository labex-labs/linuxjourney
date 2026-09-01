---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "ja"
order_index: 5
title: "Setuid"
description: "set-user-ID モードビットが実行可能プログラムへ与える影響と、慎重なセキュリティレビューが必要な理由を学びます。"
meta_title: "Setuid - パーミッション"
meta_description: "Linux Setuid (SUID) パーミッション、その仕組み、および変更方法について学びます。Linux での安全なファイルアクセスにおける SUID を理解します。"
meta_keywords: "Linux Setuid, SUID, Linux パーミッション，chmod, passwd コマンド，Linux セキュリティ，初心者 Linux, Linux チュートリアル"
---

一部のプログラムには、呼び出し元が通常持たないアクセスを狭く制御して与える必要があります。実行可能な通常ファイルで set-user-ID ビットを使うと、新しいプロセスがファイル所有者のユーザー ID を実効ユーザー ID として受け取る場合があります。そのプログラムは呼び出し元の情報を保持しつつ、その識別情報で認可された操作を行えます。

Setuid は一般的な「root として実行」という命令ではありません。効果は実行ファイルの所有者、オペレーティングシステム、ファイルシステムとマウントオプション、プログラムによる資格情報管理に左右されます。

## Setuid を見分ける

setuid の `passwd` 実行ファイルを使うシステムでは、長形式一覧が次のようになる場合があります。

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

所有者の実行位置にある小文字 `s` は、setuid と所有者実行の両方が設定されていることを示します。setuid があって所有者実行がない場合、`ls -l` はその位置に大文字 `S` を表示します。

すべてのディストリビューションが同じモードや認証設計を使うとは限りません。例に依存せず、実際のシステムを確認してください。

:::single-choice{#setuid-lowercase-s} 所有者の実行位置にある小文字 `s` は何を示しますか？

::option[Setuid は設定されているが、所有者実行はない。]{#setuid-s-without-execute explanation="その組み合わせは小文字 `s` ではなく大文字 `S` で表示されます。"}
::option[ファイルに sticky bit とグループ実行が設定されている。]{#setuid-sticky-group explanation="Sticky bit はその他の実行位置に現れ、setuid は所有者の位置に現れます。"}
::option[Setuid と所有者実行の両方が設定されている。]{#setuid-s-with-execute .correct explanation="小文字 `s` は setuid ビットと通常の所有者実行ビットを同時に表します。"}
:::

## 資格情報の変更を理解する

実行時にカーネルが setuid を有効にすると、新しいプロセスは通常、実行ファイルの所有者に基づく実効ユーザー ID を得ます。root 所有のプログラムなら root として認可されるアクセスを提供できますが、それはプログラムの実行中に、そのコードが行う操作を通じてだけです。

この機構により、慎重に作られたプログラムが要求を検証し、保護された状態へ限定的な変更を加えられます。たとえば、ローカルのパスワード変更ツールには、通常ユーザーが直接編集できない認証データへの制御されたアクセスが必要な場合があります。現代の実装は PAM、ファイルロック、ポリシーなどの保護策にも依存し、setuid だけで完全なワークフローを説明することはできません。

:::single-choice{#setuid-effective-identity} Setuid 実行ファイルの効果が有効なとき、主にファイル所有者から得る識別情報はどれですか？

::option[`/etc/passwd` に保存されたログイン名。]{#setuid-login-name explanation="ファイルの実行は呼び出し元のアカウントレコードやログイン名を書き換えません。"}
::option[プロセスの実効ユーザー ID。]{#setuid-effective-user .correct explanation="Set-user-ID 実行機構は、多くの認可判断で使われる実効ユーザー識別情報を変更します。"}
::option[開いたすべてのファイルのグループ所有者。]{#setuid-opened-file-group explanation="Setuid はプロセス資格情報へ影響し、無関係なファイルの所有権メタデータは変更しません。"}
:::

## ビットを設定・削除する

Setuid はシンボリック形式で設定できます。

```bash
$ sudo chmod u+s myfile
```

8進表記では、setuid は先頭の特殊ビット桁に `4` を加えます。

```bash
$ sudo chmod 4755 myfile
```

ここでは先頭の `4` が setuid を、`755` が通常の所有者、グループ、その他のビットを設定します。ほかのモードを変えず setuid だけを削除するには `chmod u-s myfile` を使います。

:::single-choice{#setuid-octal-value} Setuid 特殊ビットを表す先頭の8進値はどれですか？

::option[`4`]{#setuid-octal-four .correct explanation="Setuid は先頭の特殊ビット桁へ値 `4` を加えます。"}
::option[`1`]{#setuid-octal-one explanation="先頭の `1` は sticky bit を表します。"}
::option[`2`]{#setuid-octal-two explanation="先頭の `2` は setgid ビットを表します。"}
:::

## Setuid をセキュリティ上重要なものとして扱う

特権 setuid プログラムの欠陥は、権限昇格の経路になる可能性があります。このようなプログラムは入力を検証し、信頼する環境とファイルパスを制御し、安全でないサブプロセス動作を避け、特権コードを最小化し、できるだけ早く昇格済み資格情報を破棄しなければなりません。

Linux は通常、解釈されるスクリプトの setuid を有効にしません。安全に実現するには競合状態やインタープリターに関する問題があるためです。`nosuid` でマウントされたファイルシステムも、setuid と setgid の効果を抑止します。要件に合うなら、サービスが仲介する操作、慎重に範囲を絞った `sudo` ポリシー、ケーパビリティなど、より狭い仕組みを優先してください。

共有システム上での実験として、任意のシェル、インタープリター、コピーしたプログラムへ setuid を追加してはいけません。既存の setuid ファイルを監査し、隔離された破棄可能な環境だけで練習してください。

:::single-choice{#setuid-nosuid-mount} ファイルシステムを `nosuid` でマウントする目的は何ですか？

::option[そのファイルシステム内の全ファイルに保存された実行ビットを削除する。]{#setuid-nosuid-remove-execute explanation="このオプションはファイルメタデータの通常実行ビットを書き換えません。"}
::option[そのファイルシステム上で setuid と setgid の実行効果を抑止する。]{#setuid-nosuid-suppress .correct explanation="`nosuid` マウントオプションは、これらの特殊モードビットが通常の資格情報変更動作を与えるのを防ぎます。"}
::option[ファイルシステム上の全ファイルを root 所有にする。]{#setuid-nosuid-root-owner explanation="`nosuid` でマウントしても、ユーザーやグループの所有権フィールドは変わりません。"}
:::

## まとめ

Setuid を見分け、その資格情報とセキュリティ上の影響を説明できるようになりました。

1. 所有者の実行位置にある `s` または `S` を見つける。
2. Setuid 実行を、実行ファイル所有者の実効ユーザー識別情報へ関連付ける。
3. シンボリック形式または8進形式の `chmod` でビットを設定・削除する。
4. すべての特権実行ファイルをセキュリティ上重要なコードとして扱う。
