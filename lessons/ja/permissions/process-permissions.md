---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "ja"
order_index: 7
title: "プロセスパーミッション"
description: "実ユーザー ID、実効ユーザー ID、保存ユーザー ID が、呼び出し元の追跡と権限管理に役立つ仕組みを学びます。"
meta_title: "プロセスパーミッション - パーミッション"
meta_description: "Linux のプロセスパーミッションについて学びましょう。実ユーザーID、実効ユーザーID、保存ユーザーID を含みます。UID がセキュリティとコマンド実行にどのように影響するかを理解しましょう。今日から学習を始めましょう！"
meta_keywords: "Linux プロセスパーミッション，実ユーザーID, 実効ユーザーID, 保存ユーザーID, Linux セキュリティ，passwd コマンド，Linux チュートリアル，初心者 Linux"
---

Linux の認可確認は、入力されたユーザー名へ直接作用するのではなく、プロセスの資格情報へ作用します。プロセスには役割の異なる複数のユーザー ID とグループ ID があります。多くの通常プログラムは一致する識別情報で開始しますが、特権プログラムは意図的に異なる値を使う場合があります。

## 実ユーザー ID

実ユーザー ID は、プロセスを開始したアカウント、またはその祖先となるログインセッションを識別します。プログラムはこれを参照し、呼び出し元と昇格済みの実効識別情報を区別できます。

ユーザー Bob が開始した通常コマンドでは、実ユーザー ID は通常 Bob の UID と等しくなります。別のプロセスを作成するだけで、新しいアカウントが作られたり、この識別情報が変わったりはしません。

:::single-choice{#process-permissions-real-uid}
プロセスの実ユーザー ID は通常何を識別しますか？

::option[最後に開いたファイルの所有者。]{#process-permissions-real-opened-file explanation="ファイルを開いても、プロセスの実 UID がそのファイルの所有者へ置き換わることはありません。"}
::option[プロセスの元の呼び出し元に関連するアカウント。]{#process-permissions-real-caller .correct explanation="実 UID は、プロセス起動時に継承された呼び出し元ユーザーの識別情報を記録します。"}
::option[すべてのアクセス確認で選ばれるグループ。]{#process-permissions-real-group explanation="UID はユーザー識別情報であり、グループ確認には別のグループ資格情報を使います。"}
:::

## 実効ユーザー ID

実効ユーザー ID は、多くのファイルシステムと特権の確認に使われるユーザー資格情報です。通常は実 UID と一致します。有効な setuid プログラムを実行すると、代わりに実行ファイルの所有者から初期化される場合があります。

たとえば、慎重に設計されたパスワードツールは、保護された認証データを更新できるよう、昇格済みの実効 UID で動くことがあります。それでもプログラムは、呼び出し元、要求対象のアカウント、PAM の結果などのコンテキストに基づいてポリシーを強制しなければなりません。ある実効 UID を持つだけで、要求されたすべての操作が正当になるわけではありません。

:::single-choice{#process-permissions-effective-uid}
プロセスのために行われる多くのアクセス制御判断で使われるユーザー ID はどれですか？

::option[実効ユーザー ID。]{#process-permissions-effective-active .correct explanation="実効 UID は、多くの認可確認で参照される有効なユーザー資格情報です。"}
::option[保存ユーザー ID だけ。]{#process-permissions-effective-saved-only explanation="保存 ID は資格情報の移行を支えますが、通常、アクセス確認で有効な識別情報ではありません。"}
::option[現在のディレクトリに保存された UID。]{#process-permissions-effective-directory explanation="ファイルシステムの所有権はオブジェクトのメタデータであり、プロセスの有効なユーザー資格情報ではありません。"}
:::

## 保存 Set-User-ID

保存 set-user-ID によって、プログラムはシステムコールの規則に従い、後で復元できる識別情報を保持できます。特権プログラムは、実効 UID を一時的に低い権限の値へ切り替え、通常作業を縮小された権限で行い、範囲を絞った操作に限って保存済み識別情報を復元できます。

正しく実装されている場合、プログラム全体で昇格権限を維持するより安全です。不要になった権限は恒久的に破棄し、資格情報を変更するすべての呼び出しが成功したか確認しなければなりません。

:::single-choice{#process-permissions-saved-uid}
特権プログラムが保存 set-user-ID を保持する理由は何ですか？

::option[制御された特権段階と非特権段階で、実効識別情報を切り替えるため。]{#process-permissions-saved-switch .correct explanation="保存済み識別情報により、権限を一時的に下げ、許可された後の時点で復元できます。"}
::option[読み取るすべてのファイルへその UID を自動割り当てするため。]{#process-permissions-saved-file-owner explanation="ファイルを読み取っても、その所有権がプロセスの保存 UID へ変わることはありません。"}
::option[プロセス用のシステムアカウントデータベースを置き換えるため。]{#process-permissions-saved-database explanation="プロセス資格情報はアカウントレコードや名前サービスデータの代わりにはなりません。"}
:::

## ユーザー ID は資格情報の一部にすぎない

プロセスは実、実効、保存、補助のグループ資格情報も持ちます。ファイルシステム ID、ケーパビリティ、名前空間、セキュリティモジュール、ACL、マウントオプション、サービスのポリシーも認可へ影響します。したがって、「その UID だから許可される」という説明だけでは不完全な場合がよくあります。

Linux では `ps` や `/proc/PROCESS/status` などで資格情報を調べられます。利用可能なフィールドと表示形式は異なるため、ローカル文書を参照し、共有システムでの実験のためだけに資格情報を変更してはいけません。

:::single-choice{#process-permissions-ordinary-identities}
権限移行のない通常コマンドでは、実 UID と実効 UID はどのような関係になりますか？

::option[実効 UID は常に0である。]{#process-permissions-effective-root explanation="通常コマンドが自動的に root の UID を受け取ることはありません。"}
::option[実 UID は常に実行ファイルの所有者と等しい。]{#process-permissions-real-file-owner explanation="実行ファイルの所有者が影響するのは setuid の動作であり、通常の実 UID ではありません。"}
::option[通常、呼び出したユーザーの UID と両方とも一致する。]{#process-permissions-uids-match .correct explanation="Setuid や明示的な資格情報変更がなければ、通常プロセスは一致する実・実効識別情報で動きます。"}
:::

## まとめ

Linux プロセスが複数のユーザー識別情報を持つ理由を説明できるようになりました。

1. 実 UID で元の呼び出し元を識別する。
2. 実効 UID を有効な認可確認へ関連付ける。
3. 制御された権限移行を理解するために保存済み識別情報を使う。
4. 完全な判断の一部として、グループ ID と追加のセキュリティ機構を考慮する。
