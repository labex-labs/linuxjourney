---
lesson_id: "package-repositories"
course_id: "packages"
lang: "ja"
order_index: 2
title: "パッケージリポジトリ"
description: "リポジトリが署名済みパッケージ索引を公開する仕組みと、APT が設定済みの Debian 系ソースを検出する方法を学びます。"
meta_title: "パッケージリポジトリ - パッケージ"
meta_description: "Linux パッケージリポジトリとそのパッケージ管理における役割を探ります。システムが/etc/apt/sources.list ファイルなどのソースを使用して Linux パッケージを見つけてインストールする方法を学びます。"
meta_keywords: "Linux パッケージリポジトリ，apt ソースリスト，/etc/apt/sources.list, Linux パッケージ，初心者 Linux, Linux チュートリアル，パッケージ管理"
---

パッケージリポジトリは、パッケージを索引やリリースメタデータとともに公開します。パッケージマネージャーは索引をダウンロードし、設定されたディストリビューションとアーキテクチャに適合するバージョンを選び、リポジトリの認証を検証して、必要なパッケージファイルを取得します。

## リポジトリメタデータとローカルカタログ

リポジトリは単なるアーカイブのディレクトリではありません。メタデータには、利用可能なパッケージ名、バージョン、アーキテクチャ、チェックサム、依存関係、リポジトリセクションが記述されます。クライアントはローカルカタログをキャッシュするため、すべてのアーカイブを先にダウンロードせず、パッケージの検索と解決ができます。

Debian 系システムでは、設定済みメタデータを次のように更新します。

```bash
$ sudo apt update
```

これはローカルのパッケージ索引を更新するもので、利用可能なアップグレードをすべてインストールする操作ではありません。失敗した項目を無視せず、報告された情報源と認証エラーを確認してください。

:::single-choice{#package-repositories-apt-update}
`apt update` が主に更新するものは何ですか？

::option[確認なしに、インストール済みのすべてのパッケージバイナリ。]{#package-repositories-all-binaries explanation="アップグレードのインストールは、メタデータの更新とは別の操作です。"}
::option[パッケージのインストールを許可されたユーザーのパスワード。]{#package-repositories-user-passwords explanation="リポジトリ索引の更新はローカル認証情報を変更しません。"}
::option[設定済みソースから利用できるパッケージを記述するローカル索引。]{#package-repositories-local-indexes .correct explanation="APT は最新のリポジトリメタデータをダウンロードし、後の検索と依存関係解決で更新済みカタログを使えるようにします。"}
:::

## APT のソース設定

APT は次の両方から設定済みソースを読み取ります。

- `/etc/apt/sources.list`
- `/etc/apt/sources.list.d/` 以下にある、`.list` または `.sources` で終わるファイル

`.list` 拡張子は従来の1行形式を使います。`.sources` 拡張子は deb822 形式のスタンザを使い、現在の APT 文書では新規設定に推奨されています。ディストリビューションは既定ソースをどちらにも配置できるため、`/etc/apt/sources.list` に完全な設定や主要な設定が必ず含まれるとは限りません。

deb822 形式のソースは次のようになります。

```text
Types: deb
URIs: https://deb.example.invalid/repository
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/example.gpg
```

これは構文例にすぎず、予約された `.invalid` ドメインは利用可能なリポジトリではありません。

:::single-choice{#package-repositories-apt-locations}
APT はどこから有効なリポジトリ定義を読み取れますか？

::option[`/etc/apt/sources.list` だけ。]{#package-repositories-only-main-list explanation="APT は `/etc/apt/sources.list.d/` 以下の対応するソースファイルも読み取ります。"}
::option[各ユーザーのホームディレクトリ内のファイルだけ。]{#package-repositories-only-home explanation="システムの APT ソース設定は通常 `/etc/apt` 以下にあります。"}
::option[`/etc/apt/sources.list` と、`/etc/apt/sources.list.d/` 内の対応ファイル。]{#package-repositories-both-locations .correct explanation="APT は主要ファイルと、ソース一覧ディレクトリの `.list` および `.sources` 定義を組み合わせます。"}
:::

## リポジトリの認証

APT は署名されたリポジトリのリリースメタデータを検証し、ダウンロードしたパッケージファイルを、その認証済みメタデータにあるチェックサムと照合します。`Signed-By` を使えば、そのリポジトリでグローバルに設定された全鍵を信頼するのではなく、特定のキーリングへソースを限定できます。

有効な署名から分かるのは、受け入れた署名鍵の所有者からメタデータが届き、検出されない変更を受けていないことです。公開者のソフトウェアに欠陥や悪意がなく、そのシステムに適していることまでは証明しません。鍵のフィンガープリントとソースの手順は、独立した信頼できる経路で確認してください。

:::single-choice{#package-repositories-signed-by}
APT ソース定義における `Signed-By` のセキュリティ上の目的は何ですか？

::option[インストール済みの全パッケージを暗号化し、root からも読めなくする。]{#package-repositories-package-encryption explanation="リポジトリ署名は出所と整合性の確認を提供し、ローカル管理者からの秘匿性は提供しません。"}
::option[そのソースで使える署名鍵を選択したものに限定する。]{#package-repositories-key-scope .correct explanation="このフィールドは、制限のないグローバル鍵集合ではなく、選択したキーリング資料へリポジトリ検証を結び付けます。"}
::option[リポジトリに脆弱なソフトウェアが一切ないことを保証する。]{#package-repositories-no-vulnerabilities explanation="暗号学的な真正性は、ソフトウェアの品質やセキュリティ上の欠陥を評価しません。"}
:::

## 第三者ソースを意図的に追加する

リポジトリはシステム権限でパッケージとライフサイクルスクリプトをインストールできるため、追加するとシステムのソフトウェア信頼境界が広がります。追加前に次を行います。

1. 要件を満たすならディストリビューションのリポジトリを優先する。
2. 公開者、対応リリース、アーキテクチャ、署名鍵のフィンガープリントを確認する。
3. 専用のソースファイルと、範囲を限定したキーリングを使う。
4. インストール前に、パッケージ名と依存関係の変更を確認する。
5. ソースを無効化し、そのパッケージを移行または削除する方法を文書化する。

署名確認を無効化したり、監査していないリモートスクリプトを特権シェルへパイプしたりする古い手順をコピーしてはいけません。

:::single-choice{#package-repositories-third-party-risk}
第三者リポジトリの追加がシステムの信頼境界を広げるのはなぜですか？

::option[認証済みのパッケージとスクリプトがシステム権限でインストールされ得るから。]{#package-repositories-privileged-install .correct explanation="署名ソースを信頼すると、オペレーティングシステムへ影響するコードとライフサイクル操作を認可できます。"}
::option[Linux カーネルがファイル権限を強制しなくなるから。]{#package-repositories-disable-permissions explanation="リポジトリ設定はカーネルの通常のアクセス制御機構を無効にしません。"}
::option[すべてのネイティブパッケージをソースアーカイブへ変換するから。]{#package-repositories-convert-source explanation="リポジトリの追加は利用可能なパッケージソースを変えますが、既存パッケージの基本形式は変えません。"}
:::

[Linux でのソフトウェアインストール](https://labex.io/labs/linux-software-installation-on-linux-18005)でリポジトリを使うインストールを練習するか、[YUM でパッケージを照会・更新する](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)で Red Hat 系のワークフローと比較してください。APT の正確な構文は、ローカルの `sources.list(5)` マニュアルを参照します。

## まとめ

設定済みリポジトリが信頼されたパッケージメタデータになる仕組みを説明できるようになりました。

1. リポジトリ索引とパッケージアーカイブを区別する。
2. `apt update` でローカルカタログを更新する。
3. 1行形式と deb822 形式の両方の APT ソース定義を見つける。
4. 署名鍵の範囲を限定し、第三者への信頼を意図的に確認する。
