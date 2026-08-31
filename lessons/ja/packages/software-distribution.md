---
lesson_id: "software-distribution"
course_id: "packages"
lang: "ja"
order_index: 1
title: "ソフトウェア配布"
description: "upstream プロジェクト、ディストリビューション保守者、パッケージ、パッケージ形式が Linux のソフトウェアサプライチェーンを形成する仕組みを学びます。"
meta_title: "ソフトウェア配布 - パッケージ"
meta_description: "Linux のソフトウェア配布、パッケージマネージャ、.deb や.rpm などのパッケージ形式を理解することで、Linux を学ぶ最良の方法を探求しましょう。無料の Linux 認定コースの重要な一部です。"
meta_keywords: "Linux ソフトウェア配布，パッケージマネージャ，.deb, .rpm, Linux を学ぶ最良の方法，無料 Linux 認定コース，Linux を学ぶための最良のリソース，Linux コマンドラインを学ぶ最良の方法，ソフトウェアインストール"
---

Linux ソフトウェアは一般に、ディストリビューション固有のツールが管理するパッケージとして配布されます。パッケージはインストール可能なファイルをメタデータとまとめ、システムがバージョン、依存関係、所有権、チェックサム、ライフサイクル操作を追跡できるようにします。

## パッケージに含まれるもの

バイナリパッケージには、実行ファイル、ライブラリ、文書、既定の設定、サービス定義などの資源を含められます。また、次のようなメタデータも持ちます。

- パッケージ名とバージョン
- 対象アーキテクチャとディストリビューションのコンテキスト
- 宣言された依存関係と競合関係
- ファイル一覧と整合性情報
- ライフサイクル操作で使う任意のスクリプトやトリガー

すべてのパッケージが対話的アプリケーションとは限りません。ライブラリ、カーネルコンポーネント、言語データ、フォント、デバッグシンボル、ほかのパッケージ群へ依存するメタデータを提供する場合もあります。

:::single-choice{#software-distribution-package-metadata}
アプリケーションの実行ファイルではなく、通常パッケージメタデータに当たる情報はどれですか？

::option[アプリケーションを実装する CPU 命令。]{#software-distribution-executable-code explanation="コンパイル済み命令は依存関係メタデータではなく、パッケージのペイロード内容です。"}
::option[宣言された依存関係。]{#software-distribution-dependencies .correct explanation="管理ツールがインストールを判断できるよう、パッケージは必要または競合するパッケージを記述します。"}
::option[ユーザーがメモリ上で現在開いている未保存の文書。]{#software-distribution-user-document explanation="実行時のユーザーデータは、配布されるパッケージメタデータの一部ではありません。"}
:::

## Upstream とディストリビューションの役割

upstream プロジェクトは元のソースコードを開発し、リリースします。Linux ディストリビューションの保守者は、選択したリリースをそのディストリビューションへ適合させます。ライセンスの確認、統合またはセキュリティパッチの適用、ビルド手順の定義、出力のパッケージ分割、依存関係の宣言、テストの実行、更新の保守などが作業に含まれます。

ディストリビューションのビルド基盤は、対応リリースとアーキテクチャ向けのパッケージを生成します。リポジトリーツールは、クライアントが検証できるメタデータと署名を公開します。正確な役割分担は異なり、upstream プロジェクト自身がパッケージを公開する場合も、ディストリビューションがソースから独自にビルドする場合もあります。

:::single-choice{#software-distribution-maintainer-role}
ディストリビューションのパッケージ保守者が一般に担当する作業はどれですか？

::option[upstream のソースをディストリビューションのビルド規則と依存関係規則へ適合させる。]{#software-distribution-maintainer-integrates .correct explanation="保守者はソフトウェアをディストリビューションのポリシー、ビルド、依存関係、対応環境へ適合させます。"}
::option[全ユーザーのローカルアカウントパスワードを選ぶ。]{#software-distribution-maintainer-passwords explanation="ローカルの認証データはパッケージ保守とは無関係です。"}
::option[インストール済みの各プロセスを CPU へ割り当てる。]{#software-distribution-maintainer-scheduler explanation="インストール後の CPU 実行は、稼働中のカーネルスケジューラーが処理します。"}
:::

## 一般的なネイティブパッケージ形式

広く使われるネイティブ形式には次の二つがあります。

- `.deb`: Debian と、Ubuntu や Linux Mint を含む派生ディストリビューションで使用
- `.rpm`: Fedora、Red Hat Enterprise Linux、多くの関連ディストリビューションで使用

ほかのネイティブ形式やディストリビューション横断形式もあります。ファイル名の拡張子が一致するだけでは互換性を保証できません。パッケージのアーキテクチャ、ディストリビューションのリリース、ライブラリのバージョン、ポリシー、署名、依存関係も適合する必要があります。

:::single-choice{#software-distribution-debian-format}
Debian と Ubuntu が使うネイティブパッケージ形式はどれですか？

::option[`.deb`]{#software-distribution-format-deb .correct explanation="Debian 系のパッケージツールは `.deb` アーカイブ形式を使います。"}
::option[`.rpm`]{#software-distribution-format-rpm explanation="RPM は Fedora、RHEL、関連するディストリビューション系列のネイティブ形式です。"}
::option[`.tar`]{#software-distribution-format-tar explanation="tar アーカイブは汎用コンテナーであり、それだけでは Debian パッケージのメタデータとライフサイクル動作を提供しません。"}
:::

## 管理された配布が重要な理由

パッケージマネージャーはインストール済み状態を記録し、パッケージ間の変更を調整します。信頼されたディストリビューションリポジトリからインストールすれば、通常、一貫した依存関係の解決、署名検証、セキュリティ更新、きれいな削除を利用できます。手動でコピーしたバイナリやソースからのインストールが適切な場合もありますが、自動的にこの管理ライフサイクルへ入るわけではありません。

信頼性は、それでもリポジトリ設定と署名鍵に依存します。暗号学的に有効なパッケージから分かるのは、信頼された鍵との関連であり、任意のサードパーティーソフトウェアが安全または適切であることではありません。可能ならディストリビューションのリポジトリを優先し、外部情報源へインストール権限を与える前に評価してください。

:::single-choice{#software-distribution-package-manager-benefit}
信頼されたパッケージリポジトリを通じてインストールする利点の一つは何ですか？

::option[マネージャーがバージョンを追跡し、宣言された依存関係を解決できる。]{#software-distribution-managed-lifecycle .correct explanation="リポジトリメタデータとインストール済み状態の記録により、インストール、更新、削除を調整できます。"}
::option[インストールしたすべてのプログラムにセキュリティ上の欠陥がなくなる。]{#software-distribution-no-vulnerabilities explanation="パッケージ管理は更新を支えますが、ソフトウェアに欠陥がないことは保証できません。"}
::option[あらゆるディストリビューションの全パッケージを相互交換できる。]{#software-distribution-universal-compatibility explanation="ネイティブパッケージは引き続き、形式、リリース、アーキテクチャ、依存関係環境に結び付いています。"}
:::

[RPM でパッケージを管理する](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868)ラボでパッケージのメタデータと整合性を調べるか、[ソースコードからソフトウェアをビルドする](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853)ラボでソースワークフローと管理されたパッケージを比較してください。

## まとめ

Linux ソフトウェア配布の主要な構成要素を識別できるようになりました。

1. パッケージのペイロードファイルとメタデータを分ける。
2. upstream の開発とディストリビューションの統合作業を区別する。
3. `.deb` と `.rpm` をそれぞれのディストリビューション系列に関連付ける。
4. ファイル名の拡張子だけでなく、互換性と信頼性を評価する。
