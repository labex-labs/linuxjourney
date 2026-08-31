---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "ja"
order_index: 12
title: "mkdir（ディレクトリ作成）"
description: "`mkdir` のオプションを使い、1 つ、複数、入れ子のディレクトリを作成する方法を学びます。"
meta_title: "mkdir（ディレクトリ作成） - コマンドライン"
meta_description: "Linuxのmkdirコマンドを学び、単一ディレクトリの作成、複数ディレクトリの作成、親ディレクトリのネスト作成、権限設定の例を紹介します。"
meta_keywords: "mkdirコマンド, linux mkdir, ディレクトリ作成 linux, ディレクトリ作成コマンド, mkdir -p, mkdir -m, フォルダ作成 linux"
---

make directory の略である `mkdir` コマンドは、ファイルやほかのディレクトリを整理するためのディレクトリを作成します。

基本構文は次のとおりです。

```bash
mkdir [OPTIONS] DIRECTORY...
```

## 1 つのディレクトリを作成する

パス名を渡して 1 つのディレクトリを作ります。この例では、現在の作業ディレクトリに `documents` を作成します。

```bash
$ mkdir documents
```

`documents` という項目がすでに存在する場合、`mkdir` は置換せずエラーを報告します。`ls -ld documents` で既存の項目を調べてください。

:::single-choice{#create-one-directory}
現在の作業ディレクトリに `documents` というディレクトリを作成するコマンドはどれですか？

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` は相対パス `documents` に、要求されたディレクトリを作成します。"}
::option[`touch documents`]{#touch-documents explanation="`touch` はパスが存在しない場合に空の通常ファイルを作成し、ディレクトリは作りません。"}
::option[`cd documents`]{#cd-documents explanation="`cd` は既存のディレクトリへ入ろうとするもので、存在しないディレクトリは作成しません。"}
:::

## 複数のディレクトリを作成する

複数のパス名を並べると、1 つのコマンドで複数のディレクトリを作成できます。

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories}
`books` と `paintings` という 2 つの同階層のディレクトリを作成するコマンドはどれですか？

::option[`mkdir books/paintings`]{#nested-paintings explanation="このパス名は同階層の 2 ディレクトリではなく、`books` の中の `paintings` を表します。`books` がなければ失敗もします。"}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="引用符が単語を 1 つのパス名へまとめるため、空白を含む名前のディレクトリを 1 つ要求します。"}
::option[`mkdir books paintings`]{#two-directories .correct explanation="別々のオペランドにより、`mkdir` は `books` と `paintings` を 2 ディレクトリとして作成します。"}
:::

## 存在しない親ディレクトリを作成する

オプションなしの `mkdir books/hemingway/favorites` は、中間ディレクトリが存在しないと失敗します。`-p` を追加すると、パス上の存在しない親ディレクトリを作成します。

```bash
$ mkdir -p books/hemingway/favorites
```

パスの存在しない部分を作成します。最後のディレクトリがすでに存在するという理由だけではエラーを報告しませんが、権限不足などのほかのエラーは発生し得ます。

:::single-choice{#create-nested-path}
`projects/app/src` のどの部分もまだ存在しません。完全なディレクトリパスを作るコマンドはどれですか？

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="`-p` は最後のディレクトリを作る前に、存在しない各親ディレクトリを作成します。"}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="`-p` がなければ、中間ディレクトリが存在しない状態で `src` を作成できません。"}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="`-m` はモード引数を必要とし、存在しない親の作成を要求しません。"}
:::

## 初期モードを設定する

`-m MODE` で、新しく作るディレクトリのパーミッションを指定します。

```bash
$ mkdir -m 755 public
```

パーミッションモードは後で学びます。この例のモード `755` は、所有者に読み取り、書き込み、検索権限を与え、グループとその他には読み取りと検索権限を与えます。

`-v` を追加すると、各ディレクトリの作成時にメッセージを表示します。

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode}
パーミッションモード `755` で `public` を作成するコマンドはどれですか？

::option[`mkdir -p 755 public`]{#parents-755 explanation="`-p` は残りの単語をディレクトリのパス名として扱い、`755` をパーミッションモードには設定しません。"}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="`-v` は作成メッセージを表示し、`755` をパーミッションモードとしては解釈しません。"}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="`-m` が要求するモードを受け取り、`public` が作成するディレクトリのパス名になります。"}
:::

ディレクトリの作成と整理を練習するには、次のハンズオンラボを利用してください。

1. **[Linux mkdir コマンド：ディレクトリの作成](https://labex.io/ja/labs/linux-linux-mkdir-command-directory-creating-209739)**：`mkdir` でディレクトリを作り、パーミッションを設定し、入れ子のディレクトリを含むファイルシステムを整理します。
2. **[新しいプロジェクト構造のセットアップ](https://labex.io/ja/labs/linux-setting-up-a-new-project-structure-387859)**：`mkdir` や `cd` を使い、特定のプロジェクト構造を作成して移動します。

## まとめ

これで、名前、親、モードを意図してディレクトリ構造を作成できるようになりました。

1. 1 つのコマンドで 1 つ以上のディレクトリを作成する。
2. 既存のパス名によるエラーを認識する。
3. `-p` で存在しない親ディレクトリを構築する。
4. `-m` で新しいディレクトリのモードを設定する。
