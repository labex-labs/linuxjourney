---
index: 10
lang: "ja"
title: "expand と unexpand"
meta_title: "expand と unexpand - テキスト操作"
meta_description: "`expand`コマンドでタブをスペースに、`unexpand`コマンドでスペースをタブに変換する方法を学びます。この Linux チュートリアルでテキストファイルのフォーマットを改善しましょう。"
meta_keywords: "expand command, unexpand command, Linux tabs, Linux spaces, text formatting, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

`cut`コマンドに関するレッスンでは、タブを含む`sample.txt`ファイルを使用しました。通常、タブは目に見える違いを示しますが、一部のテキストファイルではそれが十分に表示されません。テキストファイルにタブがあると、目的のスペースが得られない場合があります。タブをスペースに変換するには、`expand`コマンドを使用します。

```bash
expand sample.txt
```

上記のコマンドは、各タブがスペースのグループに変換された出力を表示します。この出力をファイルに保存するには、以下に示すように出力リダイレクトを使用します。

```bash
expand sample.txt > result.txt
```

`expand`とは反対に、`unexpand`コマンドを使用して、各スペースのグループをタブに変換し直すことができます。

```bash
unexpand -a result.txt
```

## Exercise

ファイル入力なしで`expand`とだけ入力するとどうなりますか？

## Quiz Question

タブをスペースに変換するために使用されるコマンドは何ですか？

## Quiz Answer

expand
