---
lang: "ja"
title: "syslog"
meta_description: "Linux における syslog と rsyslog、システムログの管理方法、logger コマンドの使用方法について学びます。この初心者向けのチュートリアルで始めましょう！"
meta_keywords: "syslog, rsyslog, Linux ログ，logger コマンド，/var/log/syslog, Linux チュートリアル，初心者 Linux, システムロギング"
---

## Lesson Content

syslog サービスは、ログを管理し、システムロガーに送信します。Rsyslog は syslog の高度なバージョンであり、ほとんどの Linux ディストリビューションはこの新しいバージョンを使用しているはずです。syslog サービスが収集するすべてのログの出力は、`/var/log/syslog`で見つけることができます（認証メッセージを除くすべてのメッセージ）。

システムロガーによってどのファイルが管理されているかを確認するには、`/etc/rsyslog.d`内の設定ファイルを見てください。

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

これらのログファイルのルールは、左側の列のセレクターと右側の列のアクションによって示されます。アクションは、ログ情報をどこに送信するか（ファイル、コンソールなど）を示します。すべてのアプリケーションとサービスがログの管理に rsyslog を使用するわけではないため、具体的に何がログに記録されているかを知りたい場合は、このディレクトリ内を確認する必要があります。

実際にロギングが動作するのを見てみましょう。`logger`コマンドを使用して手動でログを送信できます。

```bash
logger -s Hello
```

次に、`/var/log/syslog`の中を見てください。ログにこのエントリが表示されるはずです！

## Exercise

`/etc/rsyslog.d`設定ファイルを見て、システムロガーを介して他に何がログに記録されているかを確認してください。

## Quiz Question

メッセージを手動でログに記録するために使用できるコマンドは何ですか？

## Quiz Answer

logger
