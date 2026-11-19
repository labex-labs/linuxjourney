---
lesson_id: "dockerfile"
course_id: "docker"
lang: "ja"
order_index: 7
title: "Dockerfile"
description: "Dockerfile でページとベースイメージを組み合わせ、再利用できる Web サーバーのイメージを作ります。"
meta_title: "Dockerfile - Docker"
meta_description: "小さな Dockerfile の FROM、COPY、CMD を読み、イメージのビルドとコンテナの起動を区別します。"
meta_keywords: "Dockerfile, Docker ビルド, FROM, COPY, CMD, ビルドコンテキスト"
---

これまで既存の Web サーバーのイメージを使ってコンテナを起動しました。自分のページを配信したいなら、そのページを含むイメージを作れます。**Dockerfile** は、イメージの作り方を記すテキストファイルです。

## ベースイメージから始める

**ベースイメージ**には、作業の土台となるファイルとプログラムが入っています。次の Dockerfile は Nginx のイメージをもとにページを追加し、コンテナが既定で使用するコマンドを記録します。同じ練習用ディレクトリに Dockerfile と `index.html` を置いてください。ページの中身は、たとえば `<h1>Hello from Docker</h1>` の 1 行で十分です。

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine` は、Nginx がすでに入っているイメージを土台に選びます。Docker は新しいイメージを作るときにこのイメージを使います。

:::single-choice{#dockerfile-base-image-purpose} ページを追加する前に Nginx を用意する行はどれですか？

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY はページを追加します。サーバー自体はベースイメージにあります。"}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM は出発点となるイメージを選びます。そのイメージにはサーバーが入っています。"}
::option[`CMD` で始まる行。]{#dockerfile-base-image-cmd explanation="CMD は既定の起動コマンドを指定します。サーバープログラムはベースイメージから提供されます。"}
:::

## ファイルを追加する

`COPY` は、ビルドに渡したファイルの中から `index.html` を読み取ります。右に書いた場所にページをコピーします。この版の Nginx イメージは、その場所から既定のページを配信します。後で手元のページを編集したら、変更を入れるためにイメージを作り直します。

:::single-choice{#dockerfile-copy-after-edit} ビルドした後に手元の index.html の見出しを変更しました。新しいイメージに反映するにはどうしますか？

::option[既存のイメージから別のコンテナを起動する。]{#dockerfile-copy-edit-run explanation="そのコンテナで使うのは、既存のイメージに入っているページです。"}
::option[既存のコンテナの名前だけを変える。]{#dockerfile-copy-edit-rename explanation="コンテナの名前は、イメージ内のファイルには影響しません。"}
::option[更新したページを使ってイメージをビルドし直す。]{#dockerfile-copy-edit-rebuild .correct explanation="ビルド時に COPY が手元の更新済みファイルを読み、新しいイメージに含めます。"}
:::

## 起動コマンドを指定する

`CMD` は新しいコンテナの既定のコマンドを指定します。この例ではコンテナ内の Nginx がフォアグラウンドで動き続けるようにしています。`docker run -d` を使えば、コンテナ自体は手元のターミナルから切り離して実行できます。

:::single-choice{#dockerfile-cmd-start-time} この例の CMD で指定した既定のコマンドはいつ実行されますか？

::option[コンテナが既定のコマンドで起動するとき。]{#dockerfile-cmd-when-start .correct explanation="Docker はコンテナの起動時にイメージの既定のコマンドを使います。"}
::option[Docker がページをイメージにコピーするとき。]{#dockerfile-cmd-when-copy explanation="COPY はビルド中にページを追加します。この時点でサーバーは動きません。"}
::option[Docker がイメージの書き込みを終えたとき。]{#dockerfile-cmd-when-build explanation="ビルドでは、後で使う起動コマンドを記録します。"}
:::

## イメージをビルドしてコンテナを起動する

二つのファイルがあるディレクトリでビルドします。`-t` はイメージに `journey-web:1` という参照名を付けます。末尾のドットは、現在のディレクトリをビルドに渡すファイルの場所として使うという意味です。

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

二つ目のコマンドでコンテナが起動します。ポート 8082 が空いていれば、Docker ホスト上のブラウザーで `http://127.0.0.1:8082` を開き、自分のページを表示できます。

:::single-choice{#dockerfile-build-versus-run} ビルドが成功し、二つ目のコマンドはまだ実行していません。何が用意できていますか？

::option[イメージがあり、コンテナの作成に使える。]{#dockerfile-build-ready-image .correct explanation="ビルドでイメージが作成されました。次のコマンドでそのイメージからコンテナを起動します。"}
::option[名前を付けたコンテナがすでに自分のページを配信している。]{#dockerfile-build-ready-container explanation="サーバーは、イメージからコンテナを実行したときに起動します。"}
::option[イメージに対してブラウザー用のポートがすでに公開されている。]{#dockerfile-build-ready-port explanation="ポートマッピングは docker run のオプションです。ビルド時に接続は設定されません。"}
:::

![イメージのビルド、コンテナの起動、自分で追加したページの HTML 応答を示す LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

最後のリクエストでは、ビルド時に取り込んだページが返ります。環境によって、ビルドの進行表示やイメージ ID は異なることがあります。

## まとめ

小さな Dockerfile を読み、手元のページをサーバーで配信するまでの流れが分かりました。

1. `FROM` の行からベースイメージを見分ける。
2. `COPY` がファイルをどこから読み、どこに書くかを説明する。
3. `CMD` がコンテナの既定の起動コマンドを指定することを理解する。
4. イメージをビルドし、そこからコンテナを起動する。
