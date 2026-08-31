---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "ja"
order_index: 13
title: "rm（削除）"
description: "対象を確認して安全な `rm` オプションを選び、ファイルやディレクトリを削除する方法を学びます。"
meta_title: "rm（削除） - コマンドライン"
meta_description: "Linuxのrmコマンドを学び、安全なファイル削除、ディレクトリ削除、rm -r、rm -iの使い方、rm -rfの誤操作回避方法を解説します。"
meta_keywords: "linux rm コマンド, rm コマンド, rm -r, rm -i, rm -f, rm -rf, linux ファイル削除, linux ディレクトリ削除, rmdir"
---

`rm` コマンドはファイルシステムのエントリを削除します。コマンドラインでの削除は通常、項目をデスクトップのゴミ箱へ送りません。また `rm` に組み込みの undo はないため、実行前にすべての対象を確認してください。

基本構文は次のとおりです。

```bash
rm [OPTIONS] FILE...
```

## ファイルを削除する

1 つ以上のファイルパスを `rm` に渡します。

```bash
$ rm file1
```

```bash
$ rm notes.txt old-report.txt draft.md
```

Enter を押す前に綴りと場所を確認してください。削除後にファイルシステム復旧ツールへ頼るより、バックアップやバージョン管理のコピーの方が確実な復旧手段です。

:::single-choice{#remove-one-file}
対象を確認した後、`old-report.txt` を削除するコマンドはどれですか？

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm` は指定したファイルエントリを削除し、通常はゴミ箱へ移動しません。"}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir` は通常ファイルではなく空のディレクトリを対象にするため、この対象には使いません。"}
::option[`mv old-report.txt`]{#mv-report explanation="`mv` はコピー先を必要とし、パス名を変更するもので削除しません。この不完全なコマンドでは目的の削除を行えません。"}
:::

## ワイルドカードの対象を事前確認する

シェルはワイルドカードを複数のオペランドへ展開できます。たとえば `*.tmp` は現在のディレクトリにある、一致する隠しファイル以外の名前を選びます。

```bash
$ rm *.tmp
```

削除前に、同じ引用符なしのパターンを `ls` で確認します。

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

シェルは `rm` が始まる前にパターンを展開します。確認結果に予期しないファイルが含まれていたら、そのまま進めずパターンを修正してください。

:::single-choice{#preview-removal-pattern}
`*.tmp` の削除を予定しています。削除せず、パターンが選ぶ隠しファイル以外のパス名を先に表示するコマンドはどれですか？

::option[`rm -v *.tmp`]{#verbose-remove explanation="詳細モードは削除の実行中に報告し、一致したファイルを削除するため、読み取り専用の確認ではありません。"}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="引用符がワイルドカード展開を防ぐため、目的の対象ではなく `*` を含むリテラル名を探します。"}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="シェルが `ls` の `*.tmp` を展開するため、削除前に同じ隠しファイル以外の一致集合を確認できます。"}
:::

## 確認を求める

`-i` オプションは各削除の前に尋ねます。

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

GNU `rm` の `-I` は、より簡潔な安全策です。3 ファイルより多く削除する場合や、再帰操作の場合に一度だけ尋ねます。

:::single-choice{#confirm-each-removal}
指定した各ファイルを削除する前に確認を求めるコマンドはどれですか？

::option[`rm -i important.txt`]{#interactive-important .correct explanation="`-i` は各削除前に尋ね、操作を拒否する機会を与えます。"}
::option[`rm -f important.txt`]{#force-important explanation="`-f` はプロンプトを抑止し、存在しないオペランドを無視します。確認を加えず、取り除きます。"}
::option[`rm -v important.txt`]{#verbose-important explanation="`-v` は削除した内容を報告しますが、事前の承認は求めません。"}
:::

## `-f` で存在しないファイルを無視する

`-f` オプションは存在しないオペランドを無視し、プロンプトを抑止します。

```bash
$ rm -f old-cache.txt
```

生成ファイルがすでにない可能性のあるスクリプトでは、クリーンアップを何度実行しても同じ結果にできます。確認がなくなるため、理解していないエラーを消すためだけに `-f` を追加しないでください。

## ディレクトリを削除する

通常の `rm` はディレクトリを削除しません。

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

ディレクトリツリーとその全内容を削除する意図がある場合にだけ、`-r` または `-R` を使います。

```bash
$ rm -r old-project
```

空のディレクトリには、対象を限定できる `rmdir` があります。

```bash
$ rmdir empty-directory
```

`rmdir` はディレクトリが空でなければ失敗するため、再帰的な削除から内容を守れます。

:::single-choice{#remove-empty-directory-only}
`old-cache/` が空の場合だけ、そのディレクトリを削除するコマンドはどれですか？

::option[`rm -r old-cache/`]{#recursive-cache explanation="再帰的な `rm` はディレクトリと内容を削除し、空であるという条件を強制しません。"}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir` は空のディレクトリにだけ成功するため、中のファイルを再帰的に削除しません。"}
::option[`rm -f old-cache/`]{#force-cache explanation="`-f` を付けても通常の `rm` はディレクトリを削除せず、空かどうかの確認ではなく安全策を抑止します。"}
:::

## 再帰削除を確認する

再帰削除はツリー全体を消去できます。`-r` と `-f` を組み合わせるとプロンプトもなくなるため、`rm -rf` では対象を特に慎重に検証してください。再帰削除の前に次を確認します。

- 想定したディレクトリにいるか。`pwd` を使う
- `ls -ld -- TARGET` が意図した最上位パスを示すか
- ワイルドカードがある場合、読み取り専用の確認が期待どおりに一致したか
- パスが絶対か相対か。`/tmp/cache` と `tmp/cache` は大きく異なる
- 誤った空白がないか。`rm -rf old-project` と `rm -rf old project` は異なるパスを対象にする

ハイフンで始まる可能性のある対象の前には、オプションと解釈されないよう `--` を使います。

```bash
$ rm -- -old-name
```

`rm` がパーミッションエラーを報告したという理由だけで `sudo` を使わないでください。まず対象を確認し、自分のアカウントが親ディレクトリを変更できない理由を調べます。権限を高めた再帰削除は、オペレーティングシステムやほかのユーザーのデータを損傷させる可能性があります。

成功した各削除を `rm` に報告させるには `-v` を使います。

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree}
完全な対象を確認した後、通常のプロンプトを残しながら `old-project/` とその下のすべてを削除するコマンドはどれですか？

::option[`rm old-project/`]{#plain-rm-project explanation="通常の `rm` はディレクトリの中へ入らず、空でないツリーを削除できません。"}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="`-r` はディレクトリツリーを再帰的に削除します。`-rf` と異なり、プロンプトを抑止する `-f` は追加しません。"}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir` は空のディレクトリを必要とし、プロジェクト内に項目が残っていれば失敗します。"}
:::

管理された環境で削除を練習するには、次のハンズオンラボを利用してください。

1. **[Linux rm コマンド：ファイルの削除](https://labex.io/ja/labs/linux-linux-rm-command-file-removing-209741)**：`-r` や `-i` を含む `rm` のオプションを使い、ファイルとディレクトリを安全に削除します。
2. **[ファイルとディレクトリの整理](https://labex.io/ja/labs/linux-organizing-files-and-directories-387877)**：実践的な課題で、`rm` を使って不要なディレクトリを片付けます。

## まとめ

これで、すべての対象を元に戻せないものとして扱いながら、ファイルシステムのエントリを削除できるようになりました。

1. 削除前にファイルのパス名を確認する。
2. 読み取り専用コマンドでワイルドカード展開を事前確認する。
3. `-i` または `-I` で確認を求める。
4. ディレクトリが空でなければならない場合は `rmdir` を優先する。
5. 再帰削除の前に対象全体を検証する。
