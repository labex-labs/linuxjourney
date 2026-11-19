---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "ja"
order_index: 6
title: "ビルド成果物"
description: "CI が作ったファイルを、その実行と元のリビジョンに結び付ける方法を学びます。"
meta_title: "ビルド成果物 - 継続的インテグレーション"
meta_description: "CI が作ったファイルを、その実行と元のリビジョンに結び付ける方法を学びます。"
meta_keywords: "ビルド成果物, アーティファクト, 継続的インテグレーション, DevOps, Linux Journey"
---

**ビルド成果物**（アーティファクト）は、後から使うために実行結果として保存するファイルやファイル一式です。テストレポートやサイトのアーカイブが例です。成果物と一緒に実行とリビジョンを記録すると、レビューする人はどのソースから作ったかを確認できます。

## 出力ディレクトリをまとめる

ビルドしたページが `dist` に入っている練習用フォルダーを使います。この例では、ディレクトリの中身を一つにまとめた圧縮アーカイブを作ります。現在のフォルダーに同じ名前のアーカイブがあれば、上書きします。

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

最初のコマンドでは、`-c` でアーカイブを作り、`-z` で圧縮し、`-f` で出力ファイル名を指定します。`-C dist .` は、tar に `dist` を起点として処理するよう指定します。二つ目のコマンドは `-t` でアーカイブの中身を一覧表示します。共有する前に `./index.html` があることを確認します。

:::single-choice{#ci-build-artifacts-inspect-archive} ページがアーカイブに含まれることは、どのコマンドで確認できますか？

::option[tar -tzf site.tar.gz で中身を一覧表示します。]{#ci-build-artifacts-inspect-archive-b .correct explanation="一覧を見れば index.html が含まれるかを確認できます。"}
::option[アーカイブをもう一度作ります。]{#ci-build-artifacts-inspect-archive-a explanation="作り直しても、何が含まれるかは表示されません。"}
::option[アーカイブの名前だけを確認します。]{#ci-build-artifacts-inspect-archive-c explanation="アーカイブ名から中身は分かりません。"}
:::

![site.tar.gz の中に index.html があることを示す tar の一覧](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## 成果物を実行結果と対応付ける

ワークフローで、完成したアーカイブをアップロードできます。実行ページには、どのリビジョンをビルドしたかが表示されます。同じ `site.tar.gz` という名前でも、別のリビジョンから作られた成果物は中身が異なる場合があります。実行とリビジョンの両方を見て、ダウンロードするファイルを選びます。

:::single-choice{#ci-build-artifacts-choose-run} 実行 41 と 42 はどちらも site.tar.gz を含んでいます。レビューしたリビジョンのパッケージはどう特定しますか？

::option[最初に見つけた site.tar.gz を選びます。]{#ci-build-artifacts-choose-run-b explanation="名前だけでは、どのソースから作られたかは分かりません。"}
::option[リビジョンに関係なく、直近の成功した実行を選びます。]{#ci-build-artifacts-choose-run-c explanation="新しい実行が成功していても、ソースが異なることがあります。使いたいリビジョンと照合してください。"}
::option[記録されたリビジョンがレビュー対象と同じ実行を選びます。]{#ci-build-artifacts-choose-run-a .correct explanation="同じファイル名は、複数の実行で使われることがあります。"}
:::

## アーカイブとコンテナイメージを区別する

サイトのアーカイブには、展開できるファイルが入っています。コンテナイメージには、Docker がコンテナを起動するときに使うファイルシステムと設定が含まれます。ワークフローは、イメージをイメージレジストリに公開できます。そのイメージを使う予定なら、イメージの参照と元のリビジョンを記録します。

:::single-choice{#ci-build-artifacts-deployable-type} 次の工程はレジストリにあるイメージからコンテナを起動します。どの出力を参照すればよいですか？

::option[実行結果からダウンロードしたテストレポートです。]{#ci-build-artifacts-deployable-type-a explanation="レポートはテスト結果を示しますが、コンテナのファイルシステムは提供しません。"}
::option[公開されたコンテナイメージの参照です。]{#ci-build-artifacts-deployable-type-c .correct explanation="Docker はその参照を使って、用意されたイメージを取得できます。"}
::option[サイトのアーカイブのファイル名です。]{#ci-build-artifacts-deployable-type-b explanation="アーカイブにはページのファイルが入っていますが、レジストリのイメージは特定できません。"}
:::

## まとめ

ビルド成果物を見分け、どの実行やソースから作られたかをたどれるようになりました。

1. ビルドしたファイルをまとめ、中身を確認します。
2. 成果物を作った実行と、元のリビジョンを確認します。
3. 次の工程に合わせて、ファイルの成果物かコンテナイメージかを選びます。
