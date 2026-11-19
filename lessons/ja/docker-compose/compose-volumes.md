---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "ja"
order_index: 4
title: "ボリューム"
description: "コンテナを入れ替えても、名前付きボリュームのファイルが残る理由を学びます。"
meta_title: "ボリューム - Docker Compose"
meta_description: "コンテナを入れ替えても、名前付きボリュームのファイルが残る理由を学びます。"
meta_keywords: "名前付きボリューム, データの永続化, Docker Compose, DevOps, Linux Journey"
---

コンテナは、自分の書き込み可能なレイヤーにファイルを書き込めます。コンテナを削除すると、Docker はそのレイヤーも削除します。**名前付きボリューム**は、Docker がコンテナとは別に管理する保存領域です。コンテナを入れ替えても、同じボリュームを新しいコンテナに接続できます。

## 練習用のボリュームを定義する

次の例は別のファイルとして、練習用ディレクトリに `compose.volume.yaml` という名前で保存します。`notes` という保存領域を、ツール用コンテナ内の `/data` にマウントします。末尾の `volumes` セクションで、この名前付きボリュームを宣言しています。

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

サービスの定義では、コンテナのどこにボリュームをマウントするかを指定します。トップレベルの宣言で、Compose がこのプロジェクトと一緒にボリュームを管理するよう指定します。

:::single-choice{#compose-volumes-attached-path} ツール用コンテナのどのパスで名前付きボリュームを使いますか？

::option[/notes です。]{#compose-volumes-attached-path-b explanation="notes はボリュームの名前です。コンテナ内のマウント先はコロンの右側にあります。"}
::option[/data です。]{#compose-volumes-attached-path-a .correct explanation="notes:/data の右側がコンテナ内のパスです。"}
::option[コンテナ内のすべてのパスです。]{#compose-volumes-attached-path-c explanation="ボリュームがマウントされるのは設定したディレクトリです。"}
:::

## 別々のコンテナで書き込みと読み取りを行う

`-f` オプションで別の設定ファイルを選び、`-p` で別のプロジェクト名を指定します。`run --rm` は一度だけ使うコンテナを作り、実行が終わると削除します。他の作業から分けた練習用フォルダーで実行します。最初のコマンドはテスト用ファイル `/data/note.txt` を上書きします。

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

二番目のコンテナでは `ready` と表示されるはずです。最初のコンテナと同じボリュームをマウントしています。

:::single-choice{#compose-volumes-persistence} 最初のコンテナを削除した後も、二番目のコンテナでファイルを読めるのはなぜですか？

::option[両方のコンテナが同じ名前付きボリュームをマウントしたためです。]{#compose-volumes-persistence-b .correct explanation="ファイルは、/data にマウントした独立した保存領域に書き込まれました。"}
::option[両方のコンテナが一番目のコンテナの書き込みレイヤーを保持したためです。]{#compose-volumes-persistence-a explanation="最初のコンテナの書き込みレイヤーは、コンテナと一緒に削除されました。"}
::option[BusyBox がファイルを自動でイメージに追加したためです。]{#compose-volumes-persistence-c explanation="コンテナを実行しても元のイメージは変わりません。"}
:::

![二つの独立したツール用コンテナが、名前付きボリュームにある同じファイルに書き込み、読み取る例](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## 残すデータを確認する

マウント先の外にある `/tmp/note.txt` のようなファイルは、その場所で別の保存領域を使っていない限り、コンテナに残ります。ファイルが保持されるかどうかは、まずパスを見て確かめます。ボリューム自体を削除すると、そこにあるデータが失われる場合があります。バックアップは別に保管するコピーで、ボリュームを失ったときにデータを復元できます。

:::single-choice{#compose-volumes-inside-mount} 次のツール用コンテナは、このボリュームを通してどのファイルを参照できますか？

::option[最初のコンテナの書き込みレイヤーにある /tmp/note.txt です。]{#compose-volumes-inside-mount-a explanation="このパスは設定したマウント先の外にあります。"}
::option[別の名前のボリュームに保存したファイルです。]{#compose-volumes-inside-mount-b explanation="そのファイルを見るには、新しいコンテナにその別のボリュームをマウントする必要があります。"}
::option[最初のコンテナが書き込んだ /data/note.txt です。]{#compose-volumes-inside-mount-c .correct explanation="それぞれのコンテナが /data をマウントすると、同じ保存先のファイルにアクセスできます。"}
:::

## まとめ

ファイルを書き込んだコンテナがなくなっても、そのファイルが残る理由を説明できるようになりました。

1. ボリュームの名前とマウント先を読み取ります。
2. 別のコンテナからファイルを読み、保存されていることを確認します。
3. ボリュームの削除とコンテナの入れ替えを区別します。
