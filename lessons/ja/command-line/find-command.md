---
lesson_id: "find-command"
course_id: "command-line"
lang: "ja"
order_index: 14
title: "find"
description: "名前、種類、サイズ、時刻でディレクトリツリーを検索し、確認済みの一致項目へ操作する方法を学びます。"
meta_title: "find - コマンドライン"
meta_description: "名前、タイプ、サイズ、変更時間で検索し、一致するファイルに対して操作を実行するLinuxのfindコマンドを例とともに学びます。"
meta_keywords: "linux find コマンド, find コマンド, linux ファイル検索, 名前で検索, タイプで検索, サイズで検索, mtimeで検索, find exec"
---

`find` コマンドはディレクトリツリーをたどり、各項目を名前、種類、サイズ、変更時刻などの条件に照らしてテストします。

## 検索場所を選ぶ

基本構文は次のとおりです。

```bash
find [PATH] [EXPRESSION]
```

パスが出発点を選び、式がその下の項目を選択または操作します。

次のコマンドは、`/home` とその子孫から `puppies.jpg` という名前の項目を検索します。

```bash
$ find /home -name puppies.jpg
```

既定で再帰的に検索します。現在のディレクトリツリーを検索する場合は、出発点に `.` を使います。

:::single-choice{#search-current-tree}
現在のディレクトリとその子孫から、`notes.txt` という名前の項目を検索するコマンドはどれですか？

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="ドットが現在のディレクトリを出発点として選び、`-name` が各項目のベース名をテストします。"}
::option[`find / -name notes.txt`]{#find-root-notes explanation="出発点の `/` はファイルシステムのルートから検索するため、現在のディレクトリツリーよりはるかに広い範囲になります。"}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find` は式より前に出発点のパスを受け取ります。この順序では要求された検索を表せません。"}
:::

## 名前と種類を一致させる

`-name` テストは正確なベース名またはシェル形式のパターンを受け取ります。現在のシェルが展開せず `find` へそのまま渡すよう、ワイルドカードパターンを引用します。

```bash
$ find . -name "*.txt"
```

引用符がなければ、`find` の開始前に現在のディレクトリを対象としてシェルが `*.txt` を展開することがあります。大文字と小文字を区別しない名前の一致には、`-name` の代わりに `-iname` を使います。

`-type d` でディレクトリ、`-type f` で通常ファイルを選びます。

```bash
$ find /home -type d -name MyFolder
```

ここでは両方のテストを満たす必要があります。項目がディレクトリであり、ベース名が `MyFolder` でなければなりません。

:::single-choice{#find-text-regular-files}
現在のディレクトリ以下で、名前が `.txt` で終わる通常ファイルを検索するコマンドはどれですか？

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f` が通常ファイルを選び、引用済みの `-name` パターンを `find` が各項目に対して評価します。"}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="パターンは正しく引用されていますが、`-type d` は通常ファイルではなくディレクトリを選びます。"}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="引用されていないワイルドカードは、`find` の実行前に現在のシェルが展開し、意図した式を変える可能性があります。"}
:::

## サイズと変更時刻を一致させる

`-size` では、指定単位より大きい場合に `+`、小さい場合に `-` を使います。

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

大文字の `M` は 1,048,576 バイト単位、小文字の `k` は 1,024 バイト単位です。`find` は数値比較の前に、選択した単位へサイズを切り上げるため、境界の動作はその単位に基づきます。

`-mtime` で、ファイルの変更から経過した完全な 24 時間単位の数をテストします。

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` は 7 未満、`-mtime +30` は 30 より大きい値に一致します。完全な 24 時間単位を使うため、カレンダーの日付が変わる午前 0 時を境界にはしません。

:::single-choice{#find-recent-regular-files}
`.` 以下で、変更からの経過時間が完全な 24 時間の 7 単位未満である通常ファイルを検索するコマンドはどれですか？

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f` が通常ファイルを選び、`-mtime -7` が完全な 24 時間単位で 7 未満の変更時刻を選びます。"}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="プラス記号は 7 単位より大きい経過時間を選ぶため、最近ではなく古いファイルを探します。"}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="時刻テストは最近のものですが、`-type d` は結果を通常ファイルではなくディレクトリに限定します。"}
:::

## 一致項目を表示、操作する

操作を指定しなければ、GNU `find` は一致したパスを表示します。式の操作を明確にしたい場合は、`-print` を明示できます。

一致項目を明示的に表示します。

```bash
$ find . -name "*.log" -print
```

`-exec` で一致項目に別のコマンドを実行します。

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

`\;` 形式では、コマンドを呼び出すたびに `{}` が 1 つの一致パスへ置き換えられます。セミコロンは `-exec` 操作を終え、シェルから `find` へ渡るようエスケープされています。

`-delete` や、ファイルを変更する `-exec` コマンドなどの破壊的操作を使う前に、同じテストを `-print` で実行し、すべての結果を確認してください。出発点を狭くし、`-maxdepth N` を使うことでも検索範囲を制限できます。

:::single-choice{#verify-before-delete}
後で古い `.log` ファイルを削除する可能性のある `find` コマンドを作っています。最初に何をすべきですか？

::option[すぐに `-delete` を追加し、消えたファイルを確認する。]{#delete-first explanation="削除は安全な事前確認ではなく、組み込みの undo もありません。追加前に完全な一致集合を確認します。"}
::option[同じテストを `-print` で実行し、すべての一致を確認する。]{#print-first .correct explanation="読み取り専用の一覧で出発点とテストを検証してから、破壊的操作を導入します。"}
::option[ログファイルを見逃さないよう `/` から検索する。]{#root-first explanation="`/` から始めると範囲が広がり、無関係または保護されたパスまで含む可能性があります。適切な最小範囲を使います。"}
:::

:::single-choice{#run-ls-for-each-match}
`find . -name "*.log" -exec ls -l {} \;` で、`{}` は何を表しますか？

::option[`ls -l` へ渡される現在の一致パス。]{#match-placeholder .correct explanation="この `-exec` 形式では、`ls -l` を呼び出す前に `find` が `{}` を現在の一致へ置き換えます。"}
::option[`find` コマンドを開始したディレクトリ。]{#starting-placeholder explanation="開始ディレクトリはコマンド先頭付近のドットで、`-exec` 内の波括弧は別の役割を持ちます。"}
::option[`-exec` 式を終えるセミコロン。]{#terminator-placeholder explanation="エスケープされたセミコロンが `-exec` 操作を終了し、波括弧はパス名のプレースホルダーです。"}
:::

permission denied メッセージは通常、現在のアカウントがツリーの一部を検索できないことを示します。より狭く関連する出発点を優先し、拡大されたアクセスを理解して意図するまでは権限を高めないでください。

検索式の構築を練習するには、次のハンズオンラボを利用してください。

1. **[Linux find コマンド：ファイルの検索](https://labex.io/ja/labs/linux-linux-find-command-file-searching-219191)**：さまざまな条件に基づいてファイルとディレクトリを探す `find` の使い方を練習します。
2. **[重要なシステムリソースの発見](https://labex.io/ja/labs/linux-discover-critical-system-resources-388032)**：`find` などでファイルや実行可能ファイルを効率よく見つけます。

## まとめ

これで範囲を絞った `find` 式を作り、操作前に結果を確認できるようになりました。

1. 有用な最小範囲の出発点を選ぶ。
2. 名前パターンを引用し、種類テストと組み合わせる。
3. サイズまたは完全な 24 時間単位の変更時刻で絞り込む。
4. 必要に応じて再帰の深さを制限する。
5. 破壊的操作の前に一致項目を表示して確認する。
