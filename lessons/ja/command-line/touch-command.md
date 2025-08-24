---
index: 5
lang: "ja"
title: "touch"
meta_title: "touch - コマンドライン"
meta_description: "Linux の touch コマンドを使って新しいファイルを作成したり、タイムスタンプを更新したりする方法を学びましょう。この初心者向けのガイドは、ファイル管理を理解するのに役立ちます。"
meta_keywords: "touch コマンド，ファイル作成，Linux チュートリアル，ファイルタイムスタンプ，初心者向け Linux, Linux ガイド，基本コマンド"
---

## Lesson Content

ファイルを作成する方法を学びましょう。非常に簡単な方法は、`touch`コマンドを使用することです。`touch`を使用すると、新しい空のファイルを作成できます。

```bash
touch mysuperduperfile
```

そして、新しいファイルができました！

`touch`は、既存のファイルやディレクトリのタイムスタンプを変更するためにも使用されます。試してみてください。ファイルに対して`ls -l`を実行してタイムスタンプをメモし、そのファイルを`touch`すると、タイムスタンプが更新されます。

リダイレクトやテキストエディタなど、ファイルを作成する他の多くの方法がありますが、それについては「テキスト操作」コースで説明します。

## Exercise

1. 新しいファイルを作成します。
2. タイムスタンプをメモします。
3. ファイルを touch し、もう一度タイムスタンプを確認します。

ファイル管理の実践的な演習については、以下のインタラクティブなラボをご覧ください。

- [Linux Directory Navigation](https://labex.io/ja/labs/linux-directory-navigation-387844)
- [Setting Up a New Project Structure](https://labex.io/ja/labs/linux-setting-up-a-new-project-structure-387859)

## Quiz Question

`myfile`というファイルを作成するにはどうすればよいですか？

## Quiz Answer

touch myfile
