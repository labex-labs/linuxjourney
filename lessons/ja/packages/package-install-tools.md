---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "ja"
order_index: 5
title: "rpm と dpkg"
description: "`dpkg` と `rpm` が、それぞれのネイティブパッケージデータベースとローカルアーカイブを調査・変更する仕組みを学びます。"
meta_title: "rpm と dpkg - パッケージ"
meta_description: "rpm と dpkg コマンドを使用してパッケージをインストール、削除、一覧表示する方法を学びます。.deb および.rpm ファイルの直接パッケージ管理を理解します。Linux の旅を始めましょう！"
meta_keywords: "rpm, dpkg, Linux パッケージ管理，.deb, .rpm, Linux チュートリアル，初心者ガイド，パッケージインストール"
---

`dpkg` は Debian 系システムの低レベルパッケージツールで、`rpm` は RPM 系システムで同様の役割を担います。ネイティブアーカイブを展開し、パッケージのライフサイクル操作を実行し、インストール済みパッケージデータベースを更新します。APT や DNF などのリポジトリ対応ツールは、これらの低レベル機構の上に構築されています。

## インストール前にアーカイブを調べる

パッケージアーカイブは、一つの実行ファイルと同じではありません。多数のペイロードファイル、メタデータ、設定処理、特権で動くライフサイクルスクリプトを含む場合があります。インストール前に、出所、署名または認証済みのダウンロード経路、メタデータ、内容を調べてください。

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

示した RPM 問い合わせ形式の `p` は、インストール済みデータベースではなくパッケージファイルを問い合わせることを意味します。問い合わせ出力は確認に役立ちますが、スクリプトやプログラムが安全であることは証明できません。

:::single-choice{#package-install-tools-native-format}
Debian の `.deb` パッケージとインストール済みデータベースを管理する低レベルツールはどれですか？

::option[`rpm`]{#package-install-tools-rpm-debian explanation="RPM は RPM 系システムで独自のネイティブ形式とデータベースを管理します。"}
::option[`tar`]{#package-install-tools-tar-debian explanation="Tar はアーカイブを読めますが、Debian のインストール済みパッケージのライフサイクルは実装しません。"}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="Debian 系システムでは、低レベルの `.deb` アーカイブとパッケージデータベース操作に `dpkg` を使います。"}
:::

## ローカルアーカイブをインストールする

低レベルの直接インストールは次のように行います。

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i` は指定アーカイブを展開して設定できますが、不足するリポジトリ依存関係を取得しません。生の `rpm` も、通常のリポジトリソルバーのワークフローを提供しません。設定済みソースから依存関係を解決できるため、ローカルアーカイブにも通常は高レベルのコマンドが望ましい選択です。

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

確認前にトランザクションを確認します。APT では先頭の `./` により、ローカルの Debian アーカイブパスとリポジトリのパッケージ名を区別します。

:::single-choice{#package-install-tools-local-dependencies}
利用可能なリポジトリ依存関係を解決しながら、ローカルの `.deb` をインストールできるコマンドはどれですか？

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l` はインストール済みパッケージの選択状態を一覧表示し、ローカル依存関係を解決するインストール手順ではありません。"}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="RPM の問い合わせ構文で Debian アーカイブをインストールすることはできません。"}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="APT は明示されたローカルパスを認識し、設定済みリポジトリから宣言済み依存関係を満たせます。"}
:::

## インストール済みパッケージを削除する

削除では、以前使ったアーカイブファイル名ではなく、インストール済みパッケージ名を指定します。

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

Debian の `--remove` は通常、conffile と分類された設定ファイルを残します。`--purge` は、パッケージスクリプトと管理外データの扱いに従いつつ、それらも削除するよう要求します。どちらのコマンドもユーザーが作成したデータの削除を保証しません。関連パッケージを評価して完全なトランザクションを提示できるため、一般には高レベルの `apt remove` または `dnf remove` の方が適しています。

:::single-choice{#package-install-tools-remove-operand}
`dpkg --remove` はインストール済みパッケージについて何を引数として受け取りますか？

::option[リポジトリ索引の URL。]{#package-install-tools-remove-url explanation="リポジトリの場所は、低レベルの削除へ渡すパッケージ識別情報ではありません。"}
::option[インストール済みパッケージ名。]{#package-install-tools-remove-name .correct explanation="削除では、以前の `.deb` パスではなく、`example` のようなパッケージレコードを指定します。"}
::option[パッケージが開始したプロセスの PID。]{#package-install-tools-remove-pid explanation="プロセス ID はインストール済みパッケージデータベースのキーとは無関係です。"}
:::

## インストール済み状態を問い合わせる

インストール済みまたは既知のパッケージレコードを一覧表示します。

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

対象を絞った調査では、特定のパッケージ名を指定し、スクリプトの信頼性が重要なら機械可読形式を優先します。パッケージデータベースが記述するのは管理された状態です。ローカル管理者やアプリケーションが後からファイルを変更することもあるため、インストール済みファイルを記録済みメタデータと比較する必要がある場合は検証機能を使ってください。

:::single-choice{#package-install-tools-rpm-list-installed}
RPM データベースにインストール済みとして記録された全パッケージを問い合わせるコマンドはどれですか？

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q` は問い合わせモードを選び、`-a` は全インストール済みパッケージレコードを対象にします。"}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e` は読み取り専用一覧ではなく、パッケージ削除を要求します。"}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="これは Debian アーカイブファイルのペイロードを調べるもので、RPM のインストール済みデータベースではありません。"}
:::

[RPM でパッケージを管理する](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868)で、隔離されたシステム上のアーカイブ問い合わせと整合性検査を練習してください。

## まとめ

低レベルのパッケージ操作とリポジトリトランザクションを区別できるようになりました。

1. インストール前にローカルアーカイブのメタデータと内容を調べる。
2. `.deb` には `dpkg`、`.rpm` には `rpm` を低レベル操作に使う。
3. 依存関係の解決が必要なら APT または DNF を優先する。
4. インストール済みパッケージ名で削除し、管理状態を別途検証する。
