---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "ja"
order_index: 3
title: "ファイルの整合性"
description: "ハッシュとメタデータを使って、ファイルの内容と権限を比較する方法を学びます。"
meta_title: "ファイルの整合性 - システム監査"
meta_description: "ハッシュとメタデータを使って、ファイルの内容と権限を比較する方法を学びます。"
meta_keywords: "ファイル整合性, ハッシュ, メタデータ, システム監査, サイバーセキュリティ, Linux Journey"
---

整合性チェックでは、現在のファイルが比較の基準と一致するかを調べます。内容とメタデータは別々に確認します。内容はファイル内のバイト列です。**メタデータ**には、アクセス権限などの情報が含まれます。

## 内容のハッシュを記録する

空の練習用ディレクトリに、小さな設定ファイルを作ります。リダイレクトは同名のファイルがあると上書きするため、新しいディレクトリを使います。

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

最初のフィールドは**ハッシュ**です。ファイルのバイト列から計算した固定長の値です。後で同じファイルに同じ方法を使います。ハッシュが変わっていれば、入力のバイト列が異なります。

:::single-choice{#host-file-integrity-changed-hash} ファイルを編集した後に SHA-256 の値が変わりました。比較から何が分かりますか？

::option[ファイルの内容が、前に測定したバイト列と異なります。]{#host-file-integrity-changed-hash-a .correct explanation="計算に使う内容が変わるとハッシュも変わります。"}
::option[編集は必ず無許可で行われました。]{#host-file-integrity-changed-hash-b explanation="編集が承認されたかどうかは別途確認します。"}
::option[アカウントの権限が確実に変わりました。]{#host-file-integrity-changed-hash-c explanation="内容のハッシュにはアクセス権限が記録されません。"}
:::

## ファイルの権限を記録する

Linux では、`stat -c` で指定したメタデータを表示できます。`%a` は権限を数値のモードで表示し、`%n` は名前を表示します。

```bash
$ stat -c '%a %n' site.conf
```

最初のモードは、ファイルの作り方によって異なる場合があります。後で両方を比較できるよう、内容のハッシュと一緒に記録します。

:::single-choice{#host-file-integrity-mode-vs-content} ハッシュは基準と一致し、stat は異なるモードを表示しました。確認結果によると、何が変わりましたか？

::option[ファイルのバイト列が変わり、モードは同じでした。]{#host-file-integrity-mode-vs-content-a explanation="ハッシュは一致し、モードが異なります。"}
::option[ファイルは確実に削除されました。]{#host-file-integrity-mode-vs-content-c explanation="どちらの確認からも、そのファイルの情報が得られました。"}
::option[観測した内容のハッシュは同じで、権限が変わりました。]{#host-file-integrity-mode-vs-content-b .correct explanation="二つのツールは、それぞれ異なる属性を測定します。"}
:::

## モードを変えて確認する

次のコマンドで、練習用ファイルの権限を `640` に変更します。所有者には読み取りと書き込み、グループには読み取りを許可します。二つの確認を再び実行し、結果を比べます。

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

モードは 640 になり、内容のハッシュは最初の測定値と一致するはずです。

:::single-choice{#host-file-integrity-repeat-check} 後からファイル内の mode=preview が編集された場合、それを検出できるのはどの確認ですか？

::option[stat が表示するファイル名だけを確認します。]{#host-file-integrity-repeat-check-a explanation="内容を編集してもファイル名は変わらないことがあります。"}
::option[SHA-256 を再度計算し、最初の値と比較します。]{#host-file-integrity-repeat-check-c .correct explanation="内容が変わるとハッシュも変わります。"}
::option[所有者の権限を表す数値だけを確認します。]{#host-file-integrity-repeat-check-b explanation="ほとんどの場合、内容を編集しても権限は変わりません。"}
:::

![権限モードが 640 に変わっても、内容のハッシュは変わらないことを示す LabEx の出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## まとめ

ファイルの内容とアクセス権限を個別に比較できるようになりました。

1. 内容の SHA-256 ハッシュを記録します。
2. stat でモードを読み取ります。
3. 権限を変更した結果を確認します。
