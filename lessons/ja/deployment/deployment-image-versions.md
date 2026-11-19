---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "ja"
order_index: 2
title: "イメージのバージョン"
description: "イメージタグとダイジェストを区別し、二つの環境で使われたイメージを正確に比較する方法を学びます。"
meta_title: "イメージのバージョン - デプロイ"
meta_description: "イメージタグとダイジェストを区別し、二つの環境で使われたイメージを正確に比較する方法を学びます。"
meta_keywords: "イメージのバージョン, イメージタグ, ダイジェスト, デプロイ, DevOps, Linux Journey"
---

`site:2` のようなタグがあると、イメージの参照が読みやすくなります。新しいイメージをプッシュするとき、公開する人は同じタグの参照先を変更できます。イメージの内容を正確に特定するには、参照先の内容から計算された値である**ダイジェスト**を記録します。

## タグを読む

二つの異なる日に、レジストリに次のような記録が表示されたとします。省略したダイジェストは説明用の値です。実際にイメージをプルするには、完全な値が必要です。

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

同じタグが別の内容を指すようになりました。月曜日にプルしたマシンは、引き続き古いイメージを使っているかもしれません。

:::single-choice{#deployment-image-versions-moving-tag} 両方の環境で site:2 というタグが表示されています。実際にどのイメージをプルしたかは、何を見れば分かりますか？

::option[共通のタグだけを見ます。]{#deployment-image-versions-moving-tag-b explanation="この例では二つの異なるイメージに同じタグが付いています。"}
::option[各マシンのコンテナ数を見ます。]{#deployment-image-versions-moving-tag-c explanation="コンテナ数では、イメージを特定できません。"}
::option[それぞれに記録されたダイジェストを見ます。]{#deployment-image-versions-moving-tag-a .correct explanation="タグは参照先が変わります。ダイジェストはプル時に選ばれた内容を特定します。"}
:::

## ダイジェストで指定した参照を読む

イメージの参照には、`@` と、それに続く完全なダイジェストを指定できます。この形式で、レジストリからそのオブジェクトを直接指定して取得できます。レジストリやビルドの記録にある完全なダイジェストを使います。短縮表示は例には便利ですが、イメージの取得には完全な値が必要です。

:::single-choice{#deployment-image-versions-fixed-reference} レジストリ内の特定のオブジェクトを選べるのは、どの指定方法ですか？

::option[タグを省略したイメージ名です。]{#deployment-image-versions-fixed-reference-a explanation="Docker はデフォルトのタグを使います。そのタグは別の内容を指すことがあります。"}
::option[イメージ名に完全なダイジェストを付けた参照です。]{#deployment-image-versions-fixed-reference-c .correct explanation="ダイジェストは特定の内容を指します。"}
::option[ビルド日を書いたコメントです。]{#deployment-image-versions-fixed-reference-b explanation="レジストリは、コメントからオブジェクトを取得できません。"}
:::

## 同じプラットフォームのイメージを比較する

イメージ名の参照先は、複数のマシンの種類に対応したビルドの一覧の場合も、一つのプラットフォーム向けのイメージの場合もあります。二つのホストで実行中のイメージを比べるときは、それぞれのプラットフォームを記録し、対応するイメージの参照を比較します。完全な元の参照は、リリースの記録に残します。

:::single-choice{#deployment-image-versions-compare-platform} リリースは arm64 と amd64 に対応しています。二台の amd64 ホストを調べるときは、何を比較すると役立ちますか？

::option[それぞれが選んだ amd64 イメージの参照です。]{#deployment-image-versions-compare-platform-b .correct explanation="同じプラットフォーム向けの内容を比較できます。"}
::option[異なるアーキテクチャー向けのイメージです。]{#deployment-image-versions-compare-platform-a explanation="その二つは異なるプラットフォームに対応するものです。"}
::option[各ホストの名前です。]{#deployment-image-versions-compare-platform-c explanation="名前はホストを識別しますが、デプロイした内容は特定できません。"}
:::

## まとめ

読みやすいタグに加えて、実際に使われたイメージを正確に追跡できるようになりました。

1. 同じタグが別の内容を指せる理由を説明します。
2. 完全なダイジェストを指定した参照を見分けます。
3. 対応するプラットフォームのイメージを比較します。
