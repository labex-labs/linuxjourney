---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "ja"
order_index: 5
title: "環境変数"
description: "Compose ファイルに展開する値と、コンテナに渡す値の違いを学びます。"
meta_title: "環境変数 - Docker Compose"
meta_description: "Compose ファイルに展開する値と、コンテナに渡す値の違いを学びます。"
meta_keywords: "環境変数, 変数展開, Docker Compose, DevOps, Linux Journey"
---

環境変数は、プログラムから読み取れる名前付きの値です。Compose では、ファイルを読み込むときに値を設定へ埋め込むことも、コンテナ内のプログラムに値を渡すこともできます。

## ファイル内の式を値に置き換える

練習用フォルダーに `compose.env.yaml` として保存します。このファイルの `${PAGE_MODE:-demo}` は、`PAGE_MODE` が設定されていて値が空でなければその値を使い、それ以外の場合は `demo` を使うという指定です。

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose はコンテナを作成する前に式を解決します。これを**変数展開**と呼びます。別の設定ファイルでは、同じ仕組みを使ってホスト側のポートやイメージのタグを選ぶこともあります。

:::single-choice{#compose-environment-variables-interpolate-default} PAGE_MODE が未設定の場合、展開後の設定にはどの値が表示されますか？

::option[ファイルに書かれた式がそのまま表示されます。]{#compose-environment-variables-interpolate-default-a explanation="Compose はファイルを読み込むときに式を解決します。"}
::option[自動生成されたコンテナ名が表示されます。]{#compose-environment-variables-interpolate-default-c explanation="コンテナ名と環境変数の値は別々の設定です。"}
::option[デフォルト値を指定する演算子の後ろにある demo です。]{#compose-environment-variables-interpolate-default-b .correct explanation="この式では、ほかに値がなければ demo を使います。"}
:::

## 展開された値を確認する

コマンドの前に変数への代入を書くと、その一回の実行にだけ値を設定できます。別の値を使うと設定がどう変わるかを試してみます。`config` は展開後の設定を表示するコマンドで、コンテナを作成することはありません。

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

サービスの環境設定で `PAGE_MODE: review` を探します。`review` は動作確認用の値です。設定のサンプルや画面に表示される出力には、秘密情報を含めないようにします。

:::single-choice{#compose-environment-variables-config-scope} 展開後の設定に review が表示されました。この時点で何が行われましたか？

::option[その値でサービスがすでに起動しました。]{#compose-environment-variables-config-scope-b explanation="設定を表示する操作と、コンテナを起動する操作は別です。"}
::option[Compose が設定を読むときに値を展開しました。]{#compose-environment-variables-config-scope-a .correct explanation="config はコンテナを起動する前に展開済みの設定を表示します。"}
::option[既存のコンテナがすべてその値を使っています。]{#compose-environment-variables-config-scope-c explanation="このコマンドは実行中のコンテナを変更しません。"}
:::

## コンテナへ値を渡す

`environment` セクションは、展開後の値を新しいコンテナに渡します。`printenv` を使って、この実行のために作ったコンテナ内から値を出力します。

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

`review` と表示されるはずです。変数展開で値が決まり、環境設定によってコンテナへ渡されました。ホスト側のポートを選ぶためだけに使った変数は、プログラムの環境に自動で追加されるわけではありません。

:::single-choice{#compose-environment-variables-actual-value} ツール用コンテナ内のプログラムが受け取る値は、どう確認しますか？

::option[コンテナ内から PAGE_MODE の値を表示します。]{#compose-environment-variables-actual-value-c .correct explanation="プログラム自身の環境を見れば、実際に受け取った値が分かります。"}
::option[元のファイルのデフォルト値だけを確認します。]{#compose-environment-variables-actual-value-a explanation="別の値がファイルのデフォルト値に優先することがあります。"}
::option[ツール用コンテナの IP アドレスを調べます。]{#compose-environment-variables-actual-value-b explanation="IP アドレスからはプログラムの設定は分かりません。"}
:::

## まとめ

環境変数の二つの使い方を区別できるようになりました。

1. Compose ファイルでデフォルト値を指定する式を読みます。
2. コンテナを起動する前に展開後の設定を確認します。
3. 起動したプログラムの環境で値を確認します。
