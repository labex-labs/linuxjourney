---
lesson_id: "fedora"
course_id: "getting-started"
lang: "ja"
order_index: 6
title: "Fedora"
description: "Fedora が Red Hat とつながるコミュニティプロジェクトとして、最新の Linux 技術を届ける仕組みを学びます。"
meta_title: "Fedora Linux ディストリビューション"
meta_description: "Fedora Linux ディストリビューションの概要、Red Hat との関係、DNF パッケージ管理の仕組み、開発者やデスクトップユーザーに人気がある理由を解説します。"
meta_keywords: "fedora linux, fedora linux ディストリビューション，fedora とは，fedora red hat, fedora リリース，dnf パッケージ管理，linux ディストリビューション"
---

## Fedora とは

Fedora は Red Hat が支援する、コミュニティ主導の Linux ディストリビューションです。現代的な技術、洗練されたデスクトップ体験、開発者や技術利用者への充実した対応で知られます。

より保守的なディストロより速く進化しながら、品質と使いやすさも目指します。このバランスにより、すべてを最初から構築せず、現代的な Linux システムを使いたい人に適します。

:::single-choice{#identify-fedora-project-model}
Fedora プロジェクトを正しく説明しているものはどれですか？

::option[廃止された Red Hat Enterprise Linux のバージョン]{#discontinued-rhel explanation="Fedora は独自のリリースを持つ活動中のディストリビューションで、古い RHEL ではなく RHEL の上流に位置します。"}
::option[1つのハードウェアメーカーが保守するディストリビューション]{#hardware-maintained explanation="ハードウェアメーカーとも協力しますが、開発はコミュニティ主導で Red Hat が支援しています。"}
::option[Red Hat が支援するコミュニティプロジェクト]{#community-sponsored .correct explanation="Fedora は Red Hat の支援を受けてコミュニティが構築する、独立したコミュニティディストリビューションです。"}
:::

## Fedora の特徴

Fedora は企業向けディストリビューションより早く新しい Linux 機能を採用することが多く、最新のシステムと強い上流とのつながりを求める開発者、オープンソース貢献者、デスクトップ利用者に魅力的です。

整理された既定の体験でも知られます。Fedora Workstation は、現代的なデスクトップ、最新のツール、コンテナ、仮想化などの開発作業への対応を望む開発者に特に人気です。

:::single-choice{#match-fedora-user}
Fedora Workstation に最もよく合う利用者の目的はどれですか？

::option[1つの企業向けリリースを何年も変えずに保つ]{#long-enterprise-lifecycle explanation="長く保守的な企業ライフサイクルは RHEL の役割に近く、Fedora はより速いリリースと更新周期で進みます。"}
::option[洗練されたデスクトップで最新の開発ツールを使う]{#current-developer-desktop .correct explanation="Fedora Workstation は厳選されたデスクトップと、開発、コンテナ、仮想化向けの最新ツールを組み合わせます。"}
::option[すべてのシステムコンポーネントをソースから手動構築する]{#fedora-manual-source explanation="Fedora は完全にパッケージ化されたシステムを提供し、すべての構築を要求しません。"}
:::

## Fedora と Red Hat

Fedora は Red Hat エコシステムで重要な役割を持ちます。新技術や変更は Fedora に先に入り、その一部が後に Red Hat Enterprise Linux へ影響します。この関係により、Fedora はより新しく、RHEL はより保守的で企業向けになります。

企業向けの選択肢との比較は [Red Hat Enterprise Linux](https://labex.io/lesson/red-hat-enterprise-linux)、ディストロ系統の概要は [Linux ディストリビューションの選び方](https://labex.io/lesson/choosing-a-linux-distribution) を参照してください。

:::single-choice{#explain-fedora-upstream-role}
Fedora が RHEL の上流であるとは、どういう意味ですか？

::option[RHEL のリリースが後から変更なしで Fedora へコピーされる]{#rhel-copied-to-fedora explanation="関係が逆です。Fedora は速く進む上流であり、後発の RHEL コピーではありません。"}
::option[Fedora と RHEL は常に同じソフトウェアバージョンを提供する]{#identical-software-versions explanation="リリースの目的と日程が異なり、RHEL は Fedora の全バージョンに合わせず技術を選択して安定化します。"}
::option[Fedora で開発された成果が後に RHEL へ影響することがある]{#fedora-influences-rhel .correct explanation="Fedora は新技術を早期に統合する場で、その一部が後に Red Hat の企業プラットフォームへ貢献します。"}
:::

## Fedora のリリース

Fedora は定期リリース方式で、多くの年に2つのメジャーリリースを公開し、各リリースを約13か月サポートします。保守的なディストリビューションより、新しいカーネル、デスクトップ環境、開発ツールを速い周期で届けます。

最新ソフトウェアを求めながら、手動作業の多いローリングリリースではなく、整理された主流のディストリビューションを使いたい人に適します。

:::single-choice{#plan-fedora-upgrades}
Fedora のリリースモデルでは、どのような保守を想定すべきですか？

::option[コンピューターの寿命中、バージョン更新は一切不要]{#no-version-upgrades explanation="各バージョンのサポート期間は限られ、支援対象を保つには新しいリリースへ移る必要があります。"}
::option[支援対象リリースを保つための定期的なアップグレード]{#regular-release-upgrades .correct explanation="比較的速い周期で進み、各リリースの更新は約13か月なので、定期的なバージョン更新を計画します。"}
::option[明確なシステムリリースを持たない継続的なパッケージ変更]{#no-distinct-releases explanation="Fedora は通常のローリングリリースではなく、明確なメジャーリリースを公開します。"}
:::

## パッケージ管理

Fedora は RPM パッケージ形式と DNF パッケージマネージャーを使い、ソフトウェアを導入、更新、削除します。DNF はシステムを最新に保つ中心的なツールで、Red Hat 系のシステムにも自然につながります。

:::single-choice{#identify-fedora-package-tool}
Fedora が上位のパッケージ管理に使うツールはどれですか？

::option[APT]{#fedora-apt-tool explanation="APT は Debian ベースのディストリビューションに関連します。Fedora は RPM 系で DNF を使います。"}
::option[DNF]{#fedora-dnf-tool .correct explanation="DNF は Fedora リポジトリからパッケージを導入、更新、削除し、その下では RPM 形式を使います。"}
::option[Pacman]{#fedora-pacman-tool explanation="Pacman は Arch Linux のパッケージマネージャーで、Fedora の上位ツールは DNF です。"}
:::

## 一般的な用途

Fedora は開発者のワークステーション、技術者向けデスクトップ、ノート PC でよく使われます。コーディング、コンテナ、仮想マシン、一般的なデスクトップ作業のための現代的な環境を求める人に適します。サーバーにも利用できますが、最新で開発者に優しいディストリビューションという性格が特に強くあります。

## Fedora は初心者向けか

初心者にも使えますが、少し速く変化するシステムに抵抗がない人に向きます。高度に手動なディストロより取り組みやすい一方、Debian より保守性が低く、Ubuntu や Linux Mint ほど初心者中心ではないと感じる場合があります。学びながら現代的な Linux を使いたい人には有力な選択です。

## 関連資料

- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Fedora Docs](https://docs.fedoraproject.org/)
- [Fedora のリリースライフサイクル](https://docs.fedoraproject.org/en-US/releases/lifecycle/)
- [Fedora Workstation Working Group](https://docs.fedoraproject.org/en-US/workstation-working-group/)

1. **[Linux クイックスタート](https://labex.io/courses/quick-start-with-linux)** - 多くのディストリビューションへ応用できる Linux の基礎を学びます。
2. **[Linux コマンドのオンライン練習](https://labex.io/courses/linux-basic-commands-practice-online)** - 日常の Linux 作業に必要なコマンドライン習慣を伸ばします。
3. **[RPM と DNF のパッケージ管理](https://labex.io/courses/rpm-and-dnf-package-management)** - RPM と DNF の概念を練習します。

## まとめ

Fedora が Red Hat エコシステムで最新の技術を扱う、コミュニティ主導のディストリビューションであることを説明できるようになりました。

1. Fedora のコミュニティと支援モデルを説明する。
2. Fedora Workstation が支える利用者と作業を見分ける。
3. RHEL との上流関係を説明する。
4. 定期的なリリースアップグレードを計画する。
5. パッケージ管理ツールが DNF だと特定する。
