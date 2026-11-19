---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "ja"
order_index: 4
title: "ビルドとテスト"
description: "小さなページを手元で確認しながら、準備、ビルド、テストの違いを学びます。"
meta_title: "ビルドとテスト - 継続的インテグレーション"
meta_description: "小さなページを手元で確認しながら、準備、ビルド、テストの違いを学びます。"
meta_keywords: "ビルド, テスト, 終了コード, 継続的インテグレーション, DevOps, Linux Journey"
---

各工程の役割がはっきりしていると、失敗したときに結果を読み取りやすくなります。**準備**では入力となるファイルやツールをそろえます。**ビルド**では出力を作ります。**テスト**では、ソースや出力が期待する条件を満たすかを確認します。

## 入力ファイルを用意する

空の練習用フォルダーにサンプルページを書きます。リダイレクトは既存の `index.html` を上書きするため、新しい練習用ディレクトリを使ってください。

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

CI のジョブなら、チェックアウトでページを取得します。ビルドやテストに必要なライブラリやツールを依存関係と呼び、プロジェクトによってはこれらもインストールします。

:::single-choice{#ci-builds-and-tests-prepare-input} コピーするコマンドの実行前にページが見つかりません。どの工程を最初に調べますか？

::option[後のジョブで成果物をダウンロードする工程です。]{#ci-builds-and-tests-prepare-input-a explanation="出力を作るには、その前に入力ファイルが必要です。"}
::option[準備です。]{#ci-builds-and-tests-prepare-input-b .correct explanation="このジョブで入力ファイルが使えるようにしておく必要がありました。"}
::option[本番の応答時間です。]{#ci-builds-and-tests-prepare-input-c explanation="この問題はランナー上のファイルに関係します。"}
:::

## ビルドで出力を作る

完成したサイトのファイルを置くディレクトリに、ページをコピーします。

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

`-p` オプションを付けると、ディレクトリがすでにあっても `mkdir` は正常に終了します。コピーすると出力ディレクトリに別のファイルができます。後のテストはこの出力を確認できます。

:::single-choice{#ci-builds-and-tests-build-product} コピーが成功した後、どのファイルをパッケージにできますか？

::option[dist/index.html です。]{#ci-builds-and-tests-build-product-a .correct explanation="ビルドによって、出力ディレクトリにコピーが作られました。"}
::option[公開サイトにデプロイされたページです。]{#ci-builds-and-tests-build-product-b explanation="ローカルファイルをコピーしても、サービスが起動するわけではありません。"}
::option[ワークフローのステータス記録です。]{#ci-builds-and-tests-build-product-c explanation="ここでのビルドが生成するのはページです。ランナーはステータスを別に記録します。"}
:::

## ページをテストする

ビルド直後に次のチェックを実行します。`-F` は文字列をそのまま検索する指定です。`-q` を付けると一致する行が表示されません。シェルでは最後に実行したコマンドの終了コードを `$?` で参照できます。0 は文字列が見つかったことを、1 は一致する行がなかったことを表します。

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

`0` が表示されるはずです。テストはビルドしたファイルにその文字列が含まれるかを調べました。色、ブラウザーでの表示、応答時間は確認していません。

:::single-choice{#ci-builds-and-tests-test-scope} テストが成功しました。何が分かりますか？

::option[インターネットからページにアクセスできます。]{#ci-builds-and-tests-test-scope-a explanation="このチェックが読み取ったのは、ローカルの出力ファイルです。"}
::option[対応するすべてのブラウザーでページが表示されます。]{#ci-builds-and-tests-test-scope-b explanation="このテストではブラウザーを使っていません。"}
::option[ビルドしたファイルに、期待する見出しの文字列が含まれています。]{#ci-builds-and-tests-test-scope-c .correct explanation="grep コマンドが確認したのはその条件です。"}
:::

![LabEx でローカルの見出しチェックが成功し、終了コードが 0 と表示された例](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## まとめ

小さな CI チェックの各工程で、何が確認できるかを区別できるようになりました。

1. ビルドの前に入力を用意します。
2. ビルドが作るファイルを特定します。
3. 終了コードを読み、テストがどの条件を確認したかを確かめます。
