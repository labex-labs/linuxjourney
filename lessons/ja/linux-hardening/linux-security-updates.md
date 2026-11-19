---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "ja"
order_index: 7
title: "セキュリティ更新"
description: "利用可能なパッケージ更新を調べ、承認済みの保守後にサービスを確認する方法を学びます。"
meta_title: "セキュリティ更新 - Linux の堅牢化"
meta_description: "利用可能なパッケージ更新を調べ、承認済みの保守後にサービスを確認する方法を学びます。"
meta_keywords: "セキュリティ更新, パッケージ更新, Linux の堅牢化, サイバーセキュリティ, Linux Journey"
---

セキュリティ更新は、インストール済みソフトウェアの欠陥を修正します。まず、インストールされているバージョンと、使用中の OS 向けに提供されている修正を確認します。利用者が使うサービスへの影響を考えて、変更を計画します。

## 利用可能な更新を調べる

練習用の Ubuntu ホストで次の読み取り専用コマンドを使うと、APT が更新可能と認識しているパッケージが表示されます。使用するのはホストにすでにあるパッケージ情報です。

```bash
$ apt list --upgradable
```

表示されたパッケージには、現在のパッケージ情報に新しい候補バージョンがあります。その更新に必要な修正が入っているか、ディストリビューションのセキュリティ情報で確認します。一覧が空でも、手元の情報が古い場合があります。

:::single-choice{#linux-security-updates-candidate-is-listed} あるパッケージが一覧に表示されました。そこから何が分かりますか？

::option[更新はすでに適用されています。]{#linux-security-updates-candidate-is-listed-a explanation="一覧は、利用可能な更新候補を示しています。"}
::option[APT はインストール済みパッケージについて、より新しい候補を把握しています。]{#linux-security-updates-candidate-is-listed-b .correct explanation="これが、ローカルのパッケージ情報が現在示す内容です。"}
::option[より新しい候補はすべてセキュリティ更新です。]{#linux-security-updates-candidate-is-listed-c explanation="その更新の理由は、ディストリビューションの告知で確認します。"}
:::

## 変更を計画する

承認済みの変更では、対象サービス、更新先のバージョン、保守時間帯を明確にします。更新を反映するために、サービスの再起動やホストの再起動が必要な場合もあります。ホストを変更する前に、確認用のリクエストと復旧手段を用意します。

:::single-choice{#linux-security-updates-reboot-check} 長時間稼働するサービスが使うコードの修正がパッケージ更新に含まれます。インストール後に何を確認しますか？

::option[更新したコードを使うためにサービスの再起動が必要かどうかです。]{#linux-security-updates-reboot-check-a .correct explanation="稼働中のプロセスは、古いコードを読み込んだままかもしれません。"}
::option[インストール前にパッケージ一覧に更新が出ていたかどうかです。]{#linux-security-updates-reboot-check-b explanation="更新の有無は保守の計画に役立ちますが、プロセスが読み込んだバージョンまでは分かりません。"}
::option[パッケージ一覧に更新が残っていないかどうかです。]{#linux-security-updates-reboot-check-c explanation="パッケージが最新でも、プロセスが更新済みのコードを読み込んでいないことがあります。"}
:::

## 結果を確認する

インストール済みのバージョンが承認された更新先と一致するか確認します。通常の利用者が使う経路からサービスを確認し、結果を記録します。修正対象が稼働中のコンポーネントなら、更新したバージョンが実際に使われていることも確かめます。

:::single-choice{#linux-security-updates-security-verification} サービス更新後、完了の根拠として最適な組み合わせはどれですか？

::option[一覧を表示するコマンドが 2 回実行できます。]{#linux-security-updates-security-verification-a explanation="一覧を何度表示しても、サービスが動作するかは分かりません。"}
::option[保守チケットのタイトルが新しくなっています。]{#linux-security-updates-security-verification-b explanation="タイトルからは稼働中の状態が分かりません。"}
::option[承認済みのバージョンが動作し、通常の利用を代表するリクエストが成功します。]{#linux-security-updates-security-verification-c .correct explanation="ソフトウェアの状態と、利用者が使うサービスの動作をともに確認できます。"}
:::

## 二つのバージョン情報を読み分ける

インストール済みパッケージと、リクエストを処理中のプログラムのバージョンは一時的に食い違うことがあります。例えば、パッケージ一覧では修正済みのバージョンでも、更新前に起動したプロセスはそのまま動いている場合があります。稼働中のプロセスについても証拠を得てから、確認を終えます。

:::single-choice{#linux-security-updates-final-application} インストール済みのバージョンは修正済みですが、古いプロセスが残っています。何がまだ確認できていませんか？

::option[マシン上のほかのすべてのプロセスも置き換える必要があるかどうかです。]{#linux-security-updates-final-application-c explanation="確認の対象は更新したサービスと、承認済みの保守要件です。"}
::option[リクエストを処理しているのが更新済みのプログラムかどうかです。]{#linux-security-updates-final-application-a .correct explanation="パッケージ一覧でファイルのバージョンを確認し、プロセスを調べて実際に稼働しているサービスを確認します。"}
::option[更新パッケージがそもそも提供されていたかどうかです。]{#linux-security-updates-final-application-b explanation="インストール済みパッケージには、すでに修正済みのバージョンが表示されています。"}
:::

## まとめ

更新候補を見つけてから結果を検証するまでの流れを学びました。

1. 利用可能な更新と、適用済みの変更を区別します。
2. 再起動と復旧の手順を保守計画に含めます。
3. 稼働中のバージョンと、期待するサービスの動作を確認します。
