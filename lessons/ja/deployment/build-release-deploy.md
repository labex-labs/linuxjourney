---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "ja"
order_index: 1
title: "ビルド、リリース、デプロイ"
description: "ビルド、リリース、デプロイの記録から、元のリビジョンを追跡する方法を学びます。"
meta_title: "ビルド、リリース、デプロイ - デプロイ"
meta_description: "ビルド、リリース、デプロイの記録から、元のリビジョンを追跡する方法を学びます。"
meta_keywords: "ビルド, リリース, デプロイ, DevOps, Linux Journey"
---

チームメイトが「バージョン 2 の準備ができた」と言いました。ファイルのビルドが終わったのか、バージョンが承認されたのか、利用者がすでにアクセスできるのかは、この言葉だけでは分かりません。記録をたどって、どこまで進んだかを確認します。

## ビルドを特定する

ビルドは、特定のソースリビジョンから出力を作ります。この例では、小さな Web サイトをコンテナイメージにまとめ、イメージレジストリに保存します。生成したイメージの参照と一緒に、元のコミットを記録します。

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

この記録から、何が作られたかが分かります。サイトではまだ以前のバージョンを提供しているかもしれません。

:::single-choice{#build-release-deploy-build-record} パッケージ化したイメージを元のリビジョンと結び付ける記録はどれですか？

::option[ブラウザーのブックマークです。]{#build-release-deploy-build-record-b explanation="ブックマークにはアドレスがありますが、ファイルをどのようにビルドしたかは記録されません。"}
::option[ビルド 81 です。]{#build-release-deploy-build-record-a .correct explanation="元のコミットと、そこから作ったイメージの両方が記載されています。"}
::option[最新のローカルブランチの名前です。]{#build-release-deploy-build-record-c explanation="ブランチが指すコミットは変わるため、名前ではこのビルドを特定できません。"}
:::

## リリースの記録を読む

**リリース**は、配布が承認されたバージョンを特定します。例えばリリースの記録で、ビルド 81 のイメージをそのままステージングに使うと承認できます。これにより、承認後に作り直すことなく、同じ成果物を参照できます。

:::single-choice{#build-release-deploy-release-record} リリース 2 がステージング用に承認されました。何が分かりますか？

::option[記録された成果物は、その用途に使うことが承認されています。]{#build-release-deploy-release-record-b .correct explanation="リリースの記録には、どの成果物をステージングで使ってよいかが示されています。"}
::option[すべての環境がすでにバージョン 2 を提供しています。]{#build-release-deploy-release-record-a explanation="承認は次の工程に進む許可です。現在実行中のバージョンは、別の方法で確認します。"}
::option[バージョン 2 はリクエスト数が増えています。]{#build-release-deploy-release-record-c explanation="リリースの記録はトラフィックを測定しません。"}
:::

## デプロイされたバージョンを見つける

**デプロイ**は、特定のバージョンを環境に配置し、その環境でアプリケーションを起動または更新する作業です。ステージングや本番などの環境には、それぞれ固有の設定やリソースがあります。バージョンを返すエンドポイントにリクエストを送れば、どのバージョンが応答するかを確認できます。

```text
Staging version response: 2
Production version response: 1
```

この例では、ステージングは新しいバージョンを返し、本番は引き続きバージョン 1 を返します。

:::single-choice{#build-release-deploy-running-version} レビューする人が、本番でバージョン 2 が提供されているかを確認したいと考えています。直接役立つ情報はどれですか？

::option[ステージングからバージョン 2 が返った二回目の応答です。]{#build-release-deploy-running-version-a explanation="これで確認できるのはステージングの状態です。"}
::option[リリースの承認メッセージです。]{#build-release-deploy-running-version-b explanation="承認は、実行中のサービスが応答するかを確認したものではありません。"}
::option[本番のアドレスから返されたバージョン情報です。]{#build-release-deploy-running-version-c .correct explanation="確認したい環境に直接リクエストを送っています。"}
:::

## まとめ

リリースまでの流れで、どの段階でどの記録が作られるかを区別できるようになりました。

1. ビルドの出力を元のソースに結び付けます。
2. リリースで承認された成果物を特定します。
3. 目的の環境で、どのバージョンが応答するかを確認します。
