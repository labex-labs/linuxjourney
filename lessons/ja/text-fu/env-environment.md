---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "ja"
order_index: 5
title: "env (環境)"
description: "Bash が環境変数を展開、エクスポート、確認し、一時的に上書きする方法を学びます。"
meta_title: "env (環境) - Text-Fu"
meta_description: "Linux の env コマンドの機能を探ります。このガイドでは、env Linux コマンドを使用して、PATH、HOME、USER などの Linux 環境変数を表示および使用する方法を説明します。"
meta_keywords: "env, linux env, env linux, env コマンド linux, linux env コマンド，linux で env は何をするか，環境変数，PATH 変数，シェル変数"
---

すべてのプロセスには、親プロセスから継承した名前と値の文字列集合である「環境」があります。シェルは環境変数を使い、言語設定や実行ファイルの検索パスなどを起動するプログラムへ渡します。

## Bash で変数の値を展開する

Bash はコマンドを実行する前に `$NAME` または `${NAME}` を変数の値へ展開します。値を 1 つの引数として保つには展開を引用符で囲みます。

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

よく使われる環境変数には次があります。

- `HOME`：現在のユーザーのホームディレクトリ。
- `USER`：多くのシステムでログイン環境が設定するユーザー名。
- `PWD`：シェルの現在の作業ディレクトリ。
- `PATH`：コマンド名を検索するディレクトリ。

値は現在のプロセス環境によって異なり、普遍的な定数ではありません。未設定の変数は、より厳格なシェル動作を有効にしていなければ空文字列へ展開されます。

:::single-choice{#env-print-home-value} `HOME` の値を 1 つの引数として保ちながら表示する Bash コマンドはどれですか？

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="単一引用符はパラメーター展開を防ぐため、文字列 `$HOME` がそのまま表示されます。"}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="Bash は二重引用符内の `$HOME` を展開し、`printf` は完全な値を 1 つの引数として受け取ります。"}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="ドル記号やパラメーター構文がなければ、`HOME` は変数展開ではなく通常の文字列です。"}
:::

## 現在の環境を確認する

`env` を引数なしで実行すると、その `env` プロセスが継承した環境が表示されます。

```bash
$ env
```

出力には次のような `NAME=value` 形式のレコードが含まれます。

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

環境変数には認証情報、トークン、内部パスなどの機密データが含まれることがあります。`env` の完全な出力を公開の課題やログへ貼る前に、必ず確認して機密部分を伏せてください。

:::single-choice{#env-list-exported-values} 新しく起動したプロセスから見える環境を表示するコマンドはどれですか？

::option[`env`]{#env-print-all .correct explanation="コマンドや代入を指定しない `env` は、受け取った環境の名前と値を表示します。"}
::option[`alias`]{#env-alias-list explanation="`alias` はエクスポートされた環境ではなく、シェル状態であるエイリアス定義を一覧表示します。"}
::option[`history`]{#env-history-list explanation="`history` はシェルが記憶したコマンドラインを表示し、エクスポート済み変数は列挙しません。"}
:::

## PATH からコマンドを探す

`PATH` は、スラッシュを含まないコマンド名を Bash が検索するディレクトリをコロンで区切った一覧です。

```bash
$ printf '%s\n' "$PATH"
```

順序は重要で、Bash は名前解決規則に従って最初に見つけた適切なコマンドを使います。現在のシェルが名前をどう解決するかは `type -a NAME` で確認できます。

既存の検索パスを残し、現在のシェルと今後の子プロセス用に `/opt/coolapp/bin` を追加するには次のようにします。

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

誤って `PATH` を新しいディレクトリだけで置き換えたり、信頼できない書き込み可能なディレクトリを追加したりしないでください。通常のコマンドが見つからなくなったり、意図しない実行ファイルが動いたりする恐れがあります。

:::single-choice{#env-prepend-path-directory} 現在の Bash と今後の子プロセスで、既存の `PATH` の前に `/opt/coolapp/bin` を追加するコマンドはどれですか？

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="既存の検索ディレクトリをすべて捨てるため、通常のコマンドが見つけにくくなります。"}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="新しいディレクトリを先頭へ加え、以前の値を残し、結果を子プロセスへエクスポートします。"}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="単一引用符は文字列 `$PATH` をそのまま残し、この代入は今後の子プロセスへエクスポートされません。"}
:::

## 変数を子プロセスへエクスポートする

Bash 変数は自動的には子プロセスの環境へ入りません。`export` で名前をエクスポート対象にします。

```bash
$ export TEST=test
```

```bash
$ printenv TEST
test
```

現在の Bash に `TEST` が作られ、起動するコマンドは `TEST=test` を継承します。子プロセスから親の環境を変更することはできません。通常、この代入は解除するかシェルを終了するまで続き、システム全体の環境は変更しません。

:::single-choice{#env-export-inheritance} Bash で `export TEST=test` を実行する主な効果は何ですか？

::option[すべてのユーザーのシステム設定へ `TEST` を書き込む。]{#env-system-wide explanation="現在のシェルとその子による継承に作用し、全ユーザーや OS 全体には作用しません。"}
::option[今後の子プロセスが `TEST=test` を継承できるようにする。]{#env-child-inheritance .correct explanation="`export` は、Bash が起動するコマンドへ渡す環境にシェル変数を追加します。"}
::option[すでに動作中のプロセスの環境を変更する。]{#env-existing-processes explanation="既存のプロセスはそれぞれの環境を保ち、エクスポートはその後に起動するプロセスへ作用します。"}
:::

## 1 つのコマンドだけに値を設定する

コマンドの前に代入を書くと、そのコマンドの環境だけへ値を渡せます。

```bash
$ LANG=C sort names.txt
```

```bash
$ env LANG=C sort names.txt
```

現在のシェルの `LANG` は恒久的には変わりません。`env -i COMMAND` は最初は空の環境でコマンドを起動しますが、多くのプログラムが環境値に依存するため意図的に使ってください。

:::single-choice{#env-one-command-value} 現在のシェルの `LANG` を恒久的に変えず、`sort names.txt` を `LANG=C` で実行するコマンドはどれですか？

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env` は起動するコマンドの環境へ代入を追加し、親シェルは以前の値を保ちます。"}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="これは現在のシェルで `LANG=C` をエクスポートし、`sort` 終了後も変更を残します。"}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="空の環境で起動しますが、要求された `LANG=C` は設定しません。"}
:::

## 今後のセッションで個人用の値を読み込む

今後の対話型 Bash セッションで変数を再作成するには、そのセッションが実際に読む起動ファイル（対話型の非ログイン Bash では一般に `~/.bashrc`）へ適切な `export` 行を書きます。

```bash
export TEST=test
```

Zsh は一般に `~/.zshrc` を使い、Fish は異なる構文と設定を使います。ログインシェルや非対話型シェルは別のファイルを読むことがあるため、1 つのファイルですべてを設定できると思い込まず、シェルとセッションの種類を確認してください。

環境の継承とシェル設定を練習するには、次のラボを試してください。

1. **[Linux でのシェル環境と設定の管理](https://labex.io/ja/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - ローカル変数と環境変数、継承、`.bashrc` による永続化を練習します。
2. **[Linux の環境変数](https://labex.io/ja/labs/linux-environment-variables-in-linux-385274)** - 環境変数の概念、作成、変更、管理とシステム設定での役割を学びます。

## まとめ

Bash から子プロセスへ渡す環境を確認し、制御できるようになりました。

1. 適切に引用符を使って変数の値を展開する。
2. 機密情報を公開せず、エクスポート済みの値を確認する。
3. `PATH` のコマンドディレクトリを保持し、順序を管理する。
4. 今後の子プロセス用にシェル変数をエクスポートする。
5. 親シェルを変えず、1 つのコマンドだけ値を上書きする。
