---
lesson_id: "compile-source-code"
course_id: "packages"
lang: "ja"
order_index: 7
title: "ソースコードのコンパイル"
description: "ソースからコンパイルするソフトウェアを検証、設定、ビルド、テスト、ステージング、追跡する方法を学びます。"
meta_title: "ソースコードのコンパイル - パッケージ"
meta_description: "Linux でソースコードからコンパイルする方法を学びます。このガイドでは、configure、make、およびクリーンなパッケージ管理のために推奨される checkinstall コマンドを使用してソースコードをビルドする必須の手順を説明します。"
meta_keywords: "ソースコードからコンパイルする方法，ソースコードのビルド方法，ソースコードのコンパイル，make install, checkinstall, Linux コンパイル，build-essential, configure スクリプト，makefile, Linux チュートリアル"
---

ソースからビルドすれば、設定済みリポジトリにないバージョンや機能を利用できますが、統合、更新、信頼性の確認をディストリビューションではなく自分で担うことになります。要件を満たす対応済みディストリビューションパッケージがあるなら、それを優先してください。

## ビルド前に検証して文書を読む

認証された upstream のリリース経路からソースを取得します。信頼できる経路で署名またはチェックサムを検証し、アーカイブを調べてから、非特権のステージングディレクトリへ展開します。`README`、`INSTALL`、`SECURITY`、プロジェクトのビルド文書を読んでください。

ビルド手順は実行可能なコードです。`configure` スクリプト、ビルド定義、テスト、コンパイラープラグインは、ユーザー権限で任意のコマンドを実行できます。信頼できないソースをビルドせず、ビルド自体を `sudo` で実行してはいけません。

:::single-choice{#compile-source-code-build-privilege} 通常、コンパイル処理を `sudo` なしで実行すべきなのはなぜですか？

::option[コンパイラーは root ユーザー向けの機械語生成を拒否するから。]{#compile-source-code-root-compiler explanation="コンパイラーは root でも動作しますが、そうすると不必要に危険が増します。"}
::option[`sudo` が生成したすべてのオブジェクトファイルを自動削除するから。]{#compile-source-code-sudo-delete explanation="権限昇格がビルド出力を本質的に削除することはありません。"}
::option[ビルドロジックは任意のコマンドを実行でき、通常はシステム権限を必要としないから。]{#compile-source-code-unprivileged-build .correct explanation="非特権でビルドすれば、誤りや悪意あるビルド手順による被害を限定できます。"}
:::

## ビルド要件をインストールする

Debian 系の開発システムでは、一般的な出発点は次のとおりです。

```bash
$ sudo apt install build-essential
```

これは基本的なコンパイラーとビルドツールをインストールしますが、すべてのプロジェクトに必要な全依存関係ではありません。言語ランタイム、生成器、ビルドシステム用ツール、開発用ヘッダー、厳密なライブラリバージョンが追加で必要になる場合があります。信頼できるリポジトリから要件をインストールし、ビルド時依存関係と実行時依存関係を区別してください。

:::single-choice{#compile-source-code-build-essential-scope} Debian 系システムの `build-essential` は何を提供しますか？

::option[一般的なコンパイルとビルドツールの基本セット。]{#compile-source-code-baseline-tools .correct explanation="基礎ツールを提供しますが、プロジェクト固有のライブラリや生成器をすべて予測することはできません。"}
::option[あらゆるソースプロジェクトの全依存関係。]{#compile-source-code-all-dependencies explanation="各プロジェクトは追加要件や、特定バージョンの要件を宣言します。"}
::option[ダウンロードしたソースが信頼できるという保証。]{#compile-source-code-trust-guarantee explanation="ツールのインストールは、別途入手したソースリリースを認証しません。"}
:::

## 設定してビルドする

従来の Autoconf 形式のプロジェクトでは、次のように実行します。

```bash
$ ./configure --prefix=/usr/local
$ make
```

`configure` は環境を確認し、選択したオプションに従ってビルドファイルを生成します。`make` は通常 `Makefile` にある依存関係とコマンドの規則を読み、要求されたターゲットを作成します。

この手順は普遍的ではありません。CMake、Meson、Ninja、言語固有ツール、独自スクリプトを使うプロジェクトもあります。慣れているというだけで `./configure` を実行せず、そのリリースの文書に従ってください。ビルドシステムが対応する場合は、ソースツリー外のビルドディレクトリで生成ファイルを分離できます。

:::single-choice{#compile-source-code-make-role} 従来のワークフローで `make` は何をしますか？

::option[すべての出力をディストリビューションのパッケージデータベースへ登録する。]{#compile-source-code-make-package-db explanation="コンパイルだけでは、ネイティブパッケージの所有権レコードは作られません。"}
::option[認証済みソースリリースを自動的にダウンロードする。]{#compile-source-code-make-download explanation="プロジェクトが特別に定義していない限り、ソースの取得と検証はローカルビルド前に行います。"}
::option[ビルド記述にある該当規則を実行する。]{#compile-source-code-make-rules .correct explanation="Make は依存関係を評価し、選択したターゲットを最新状態にするために必要なコマンドを実行します。"}
:::

## インストール前にテストする

たとえば、プロジェクトが文書化したテストターゲットを実行します。

```bash
$ make check
```

実際のターゲットは `test`、`check`、または別コマンドの場合があります。テストされていない出力をインストールせず、失敗原因を調査してください。テストにはネットワークアクセス、サービス、特殊なハードウェア、隔離環境が必要な場合があります。他のビルドコードと同様、実行前に内容を確認します。

:::single-choice{#compile-source-code-test-failure} 文書化されたテストスイートが失敗した場合はどうすべきですか？

::option[同じインストールを直ちに root として実行する。]{#compile-source-code-install-after-failure explanation="権限では未知の正当性エラーを解決できず、結果の影響だけを大きくします。"}
::option[競合を避けるためパッケージマネージャーのデータベースを削除する。]{#compile-source-code-delete-database explanation="ネイティブデータベースはソースのテスト失敗の解決とは無関係であり、破棄してはいけません。"}
::option[ビルドをインストールする前に失敗原因を調査する。]{#compile-source-code-investigate-tests .correct explanation="テスト失敗は、互換性のない依存関係、ビルド上の欠陥、環境上の前提を示す場合があります。"}
:::

## インストールをステージングして追跡する

`sudo make install` は、ネイティブパッケージデータベースへ記録せず、システムプレフィックスへファイルを直接コピーする場合があります。アンインストールターゲットは任意で不完全なことがあり、後のアップグレードでファイルが上書きされたり孤立したりする可能性があります。

次の制御された方法のいずれかを優先してください。

- ディストリビューションのパッケージツールで正式なネイティブパッケージをビルドする
- ポリシーが許すなら `/usr/local` など明確に分離したプレフィックスへインストールする
- `DESTDIR` など対応する仕組みで一時パッケージングルートへファイルをステージングする
- 適切な場合は非特権ユーザープレフィックス、隔離環境、コンテナを使う

`checkinstall` は一部の `make install` ワークフローから単純なパッケージを作れますが、普遍的ではなく、確認済みのディストリビューション品質のパッケージレシピを置き換えません。「常に使う」規則として扱ってはいけません。特権コピーの前に、ステージングされたファイル一覧、所有権、権限、パス、アンインストールまたはアップグレード計画を確認します。

:::single-choice{#compile-source-code-destdir-purpose} 対応する `DESTDIR` ステージングインストールの目的は何ですか？

::option[予定されたインストールファイルを、検査またはパッケージ化のため一時ルート以下へ配置する。]{#compile-source-code-stage-root .correct explanation="ステージングにより、ファイル収集を稼働中のシステムプレフィックスへの即時書き込みから分離できます。"}
::option[コンパイラーをリモートパッケージリポジトリへ変更する。]{#compile-source-code-destdir-repository explanation="この変数はインストールパスを変更するもので、リポジトリメタデータを公開しません。"}
::option[コンパイルを省略し、出所不明のバイナリを代わりにダウンロードする。]{#compile-source-code-destdir-download explanation="ステージングはビルド後に適用され、外部バイナリのダウンロードへ置き換わるものではありません。"}
:::

本番システムへ実験的なファイルを混在させずに手順を練習するには、破棄可能な環境で[Linux でソースコードからソフトウェアをビルドする](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853)を利用してください。

## まとめ

ソースビルドを、制御されたソフトウェアサプライワークフローとして扱えるようになりました。

1. ソースを認証し、その手順を実行可能コードとして確認する。
2. 明示されたビルド要件を信頼できるリポジトリからインストールする。
3. 不要な権限なしで設定、ビルド、テストを行う。
4. システムへインストールする前に出力をステージングして調べる。
5. ネイティブパッケージまたは意図的に隔離したプレフィックスでインストール済みファイルを追跡する。
