---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "ja"
order_index: 6
title: "yum と apt"
description: "リポジトリを認識する APT と DNF で、パッケージを調査、インストール、削除、アップグレードするワークフローを学びます。"
meta_title: "yum と apt - パッケージ管理"
meta_description: "yum と apt の主な違いを探ります。このガイドでは、RPM ベースおよび Debian ベースの Linux システムでのパッケージのインストール、削除、更新における yum と apt の使用方法を解説します。"
meta_keywords: "yum vs apt, yum apt, Linux パッケージ管理，apt, yum, Debian, Red Hat, パッケージインストール，パッケージ更新，Linux コマンド"
---

リポジトリを認識するパッケージマネージャーは、メタデータを取得し、依存関係を解決し、認証済みの内容を検証し、トランザクションを調整します。Debian 系システムは一般に APT を使います。現在の Fedora と Red Hat Enterprise Linux は DNF を使い、現在の RHEL では `yum` コマンドが DNF の互換エイリアスとして残っています。古いシステムでは元の YUM 実装が使われていました。

一つのコマンド体系がどこでも通用すると考えず、インストールされているディストリビューションとリリースの文書に従ってください。

## メタデータを更新・調査する

APT はメタデータの更新とパッケージのアップグレードを分けます。

```bash
Debian family: $ sudo apt update
```

インストール前に検索し、内容を調べます。

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

これらのコマンドが検出できるものは、リポジトリ設定によって決まります。ソース名、アーキテクチャ、バージョン、署名エラーを注意深く読んでください。

:::single-choice{#package-management-systems-apt-show}
`package-name` の APT パッケージ詳細を表示するコマンドはどれですか？

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="`remove` サブコマンドはパッケージのアンインストールを提案します。"}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="これは RPM 系リポジトリを検索するもので、APT の詳細表示コマンドではありません。"}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="`show` サブコマンドは指定したバイナリパッケージのメタデータを表示します。"}
:::

## パッケージをインストールする

リポジトリのパッケージ名を指定してインストールします。

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

マネージャーは依存関係と、競合または置換を提案します。パッケージの出所、バージョン、アーキテクチャ、ダウンロードサイズ、ディスク上の変更、削除、新しくインストールされる依存関係を確認するまで、自動的に承認してはいけません。

:::single-choice{#package-management-systems-dnf-install}
設定済みの RPM 系リポジトリから `package-name` をインストールする現在のコマンドはどれですか？

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="これは RPM のインストール済みデータベースへの問い合わせであり、リポジトリからのインストール要求ではありません。"}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF は Fedora と最近の RHEL リリースで使われる、現在のリポジトリ対応マネージャーです。"}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update は索引を更新し、指定した RPM 系パッケージをインストールしません。"}
:::

## パッケージを削除する

削除は次のように要求します。

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

削除によって依存するパッケージへ影響したり、不要になった依存関係や設定が残ったりする場合があります。提案されたトランザクションを確認し、Debian 系では remove と purge の意味を区別し、アプリケーションデータはそのバックアップと保持手順に従って保全してください。パッケージ削除は、ユーザーが作成したデータの削除を保証しません。

:::single-choice{#package-management-systems-remove-review}
削除トランザクションを承認前に確認すべきなのはなぜですか？

::option[削除すると、パッケージを含むファイルシステムが必ず再フォーマットされるから。]{#package-management-systems-removal-format explanation="パッケージマネージャーは管理対象ファイルと状態を削除しますが、通常はファイルシステムをフォーマットしません。"}
::option[パッケージマネージャーは提案された変更内容を表示できないから。]{#package-management-systems-no-proposal explanation="対話的マネージャーは通常、確認できるよう計画したトランザクションを表示します。"}
::option[選択したパッケージへ他のパッケージが依存し、それらも影響を受ける場合があるから。]{#package-management-systems-dependent-removal .correct explanation="依存関係の制約により、要求が最初に入力した一つのパッケージ名を超えて広がる場合があります。"}
:::

## 更新を適用する

APT システムでは、メタデータを更新し、その後にアップグレードを確認する処理を、別々に成功させます。

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

DNF システムでは、ローカル文書に従ったワークフローで利用可能な更新を確認・適用します。

```bash
$ dnf check-update
$ sudo dnf upgrade
```

更新コマンドは主要ライブラリ、サービス、カーネル、依存関係を変更する場合があります。システムに応じたバックアップ、保守ポリシー、リリースノート、再起動計画を使ってください。コマンドの終了ステータスの意味も確認します。たとえば、一部の「更新確認」操作は、実行失敗ではなく更新が利用可能であることを非ゼロのステータスで報告します。

:::single-choice{#package-management-systems-apt-update-upgrade}
`apt update` と `apt upgrade` の関係はどれですか？

::option[`update` がパッケージを削除し、`upgrade` がその設定ファイルを復元する。]{#package-management-systems-apt-remove-restore explanation="二つのコマンドに、そのような削除と復元の関係はありません。"}
::option[`update` がメタデータを更新し、`upgrade` が承認されたパッケージアップグレード計画を適用する。]{#package-management-systems-apt-two-steps .correct explanation="APT はカタログの更新と、新しいパッケージバージョンのインストールを分離します。"}
::option[二つは同じ操作を表す別名である。]{#package-management-systems-apt-identical explanation="これらは別の段階を実行し、それぞれ個別に確認すべきです。"}
:::

## `dnf` と `yum` を選ぶ

現在の Fedora と RHEL の文書では `dnf` を使います。最近の RHEL システムで `yum` を実行すると DNF の互換動作を呼び出す場合がありますが、スクリプトでは実行ファイル名だけから実装を推測してはいけません。古いホストでは、手順を置き換える前にインストール済みバージョンと対応構文を確認します。

:::single-choice{#package-management-systems-yum-current-rhel}
現在の RHEL システムで `yum` が一般に表すものは何ですか？

::option[DNF が支える互換コマンド。]{#package-management-systems-yum-dnf-alias .correct explanation="最近の RHEL リリースは DNF を使いつつ、互換性のため yum コマンド名を維持します。"}
::option[Debian の低レベル `.deb` アーカイブツール。]{#package-management-systems-yum-dpkg explanation="Debian システムはネイティブパッケージ管理に YUM ではなく、APT や dpkg などを使います。"}
::option[リポジトリメタデータ専用の圧縮器。]{#package-management-systems-yum-compressor explanation="YUM と DNF はパッケージ管理インターフェースであり、単独の圧縮形式ではありません。"}
:::

[パッケージをインストール・削除する](https://labex.io/labs/linux-installing-and-removing-packages-385380)で APT を練習し、[YUM でパッケージを照会・更新する](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)で DNF／YUM 系の概念を学んでください。

## まとめ

一般的なリポジトリパッケージ操作を選び、内容を確認できるようになりました。

1. Debian 系では APT、現在の RPM 系では DNF を使う。
2. インストール前にメタデータと提案された依存関係の変更を調べる。
3. 削除を単一ファイルの削除ではなく、依存関係を考慮するトランザクションとして扱う。
4. ツールが分離している場合は、メタデータ更新とアップグレード適用を分ける。
5. `yum` が旧 YUM か DNF 互換コマンドかを確認する。
