---
lesson_id: "power-states"
course_id: "init"
lang: "ja"
order_index: 7
title: "電源状態"
description: "Linux のシャットダウンと再起動を予約、取り消し、安全に検証する方法を学びます。"
meta_title: "電源状態 - Init"
meta_description: "Linux システムの電源状態の管理方法を学びます。このガイドでは、Linux システムを安全にシャットダウンまたは再起動するための必須の shutdown、reboot、halt コマンドを網羅しています。システム管理のためのこれらの基本的な Linux コマンドを習得しましょう。"
meta_keywords: "linux 電源状態，shutdown コマンド，reboot コマンド，halt コマンド，poweroff linux, 再起動 linux, linux システム管理，初心者向け linux, linux コマンド，systemd, init"
---

シャットダウンや再起動は、システム全体の可用性を変えます。操作前に対象ホストを確認して許可を得て、接続中のユーザーへ通知し、重要な書き込み、バックアップ、保守作業を完了できるようにしてください。リモートシステムでは、マシンが復帰しない場合に備え、独立したコンソールまたは復旧経路を確保します。

## 安全に電源を切る

systemd ベースのディストリビューションでは、次のコマンドで秩序立った電源オフを要求します。

```bash
$ sudo systemctl poweroff
```

従来の `shutdown` インターフェースも広く利用できます。

```bash
$ sudo shutdown -h now
```

秩序立ったシャットダウンでは、サービスに停止を要求し、ファイルシステムをアンマウントした後、マシンの電源状態を変えます。強制再起動や物理的な電源スイッチを通常の近道として使わないでください。書き込みが中断され、データやサービスが不整合になるおそれがあります。

:::single-choice{#power-states-orderly-poweroff}
リモートの本番ホストの電源を切る前に、何をすべきですか？

::option[コマンドを実行する前に管理コンソールを切断する。]{#power-states-remove-console explanation="管理コンソールは復旧に役立つアクセス手段なので、利用できる状態に保つべきです。"}
::option[サービスに操作を遅らせないよう、強制的に電源を切る。]{#power-states-force-first explanation="強制操作は書き込みを中断する可能性があり、通常の方法にすべきではありません。"}
::option[ホストを確認し、復旧用のアクセス経路を確保する。]{#power-states-confirm-and-recover .correct explanation="対象確認は別のホストを操作する事故を防ぎ、復旧アクセスはマシンが戻らない場合に役立ちます。"}
:::

## シャットダウンを予約、取り消す

操作を予約し、ユーザーとワークロードに準備時間を与えます。`+m` 形式は現在からの分数を表します。

```bash
$ sudo shutdown -h +4
```

この例は4分後の停止または電源オフを予約し、ログイン中のユーザーへ警告を送ります。保守を延期する場合は、期限前に予約済みシャットダウンを取り消します。

```bash
$ sudo shutdown -c
```

警告を送れば安全だと思い込まないでください。アクティブなセッションとシステム固有のワークロードを確認し、サービスやクラスタに文書化されたドレイン手順があれば従います。

:::single-choice{#power-states-four-minute-schedule}
現在から4分後のシャットダウンを予約するコマンドはどれですか？

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="-h 操作と +4 の組み合わせで、現在から4分後のシャットダウンを要求します。"}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="プラス記号がなければ、時刻引数は文書化された相対分数の形式ではありません。"}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="-c オプションは新しい予約を作らず、保留中のシャットダウンを取り消します。"}
:::

## システムを再起動する

マシンを停止して再び起動する必要があるときは、秩序立った再起動を使います。

```bash
$ sudo systemctl reboot
```

一般的な互換コマンドには、次のものがあります。

```bash
$ sudo shutdown -r now
$ sudo reboot
```

再起動前に、暗号化ディスク、起動設定、ネットワーク、必須サービスが現在の対話型セッションなしで復旧できることを確認してください。ほかのシステムがこのホストに依存する場合は、先にフェイルオーバーまたはワークロード移行を調整します。

:::single-choice{#power-states-reboot-action}
`shutdown` を通じて即時の秩序立った再起動を要求するコマンドはどれですか？

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="-c オプションは保留中のシャットダウンを取り消します。"}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="-r オプションは再起動を選び、now は即時実行を予約します。"}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="-h 操作は再起動ではなく、停止または電源オフを行います。"}
:::

## 停止と電源オフを区別する

`halt`、`poweroff`、`reboot` は init システムへの互換フロントエンドの場合がありますが、要求する最終状態は異なります。halt は通常のシステム動作を停止しますが、プラットフォームと実装によっては電力が供給されたままになります。power-off はさらに、対応ハードウェアへ電力供給の停止を要求します。意図する結果を名前で表すコマンドを優先し、互換動作は環境によって異なるためローカルのマニュアルを確認してください。

:::single-choice{#power-states-halt-versus-poweroff}
`halt` と `poweroff` を区別すべきなのはなぜですか？

::option[power-off は電力供給の停止を要求するが、halt では供給が続く場合があるから。]{#power-states-power-distinction .correct explanation="どちらも通常動作を停止しますが、要求する最終的なハードウェア状態は異なる場合があります。"}
::option[halt は停止後、必ずサービスを再起動するから。]{#power-states-halt-restarts explanation="halt は停止状態であり、サービスの再起動要求ではありません。"}
::option[power-off は現在の端末ユーザーをログアウトするだけだから。]{#power-states-power-logout explanation="power-off はシェルのログアウトではなく、システム全体の状態移行です。"}
:::

## 結果を検証する

予約した操作では、ユーザーが通知を受け取り、重要な作業がドレインされたことを確認します。再起動後は、想定したカーネルと起動状態、失敗したユニット、アプリケーションの正常性、ストレージのマウント、ネットワーク到達性、直近の起動ログを確認します。ログインに成功しただけでは、サービス全体の復旧は証明できません。

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

これらは出発点です。実際のワークロードには、アプリケーション固有のヘルスチェックを使ってください。

:::single-choice{#power-states-post-reboot-check}
再起動したアプリケーションの準備が整ったことを示す最も強い証拠はどれですか？

::option[サービスの状態、ログ、ヘルスチェックがすべて成功すること。]{#power-states-health-evidence .correct explanation="システムとアプリケーションの複数の検査により、ホストへのアクセスだけでなくワークロードも検証できます。"}
::option[筐体の電源ランプが点灯していること。]{#power-states-light-on explanation="ハードウェアへの通電は、アプリケーションの正常性を証明しません。"}
::option[管理者がシェルへログインできること。]{#power-states-shell-open explanation="シェルアクセスが証明するのは、システム可用性の一部だけです。"}
:::

## まとめ

準備、明確な意図、検証を伴って Linux の電源状態を変更できるようになりました。

1. 対象、影響、許可、復旧経路を確認する。
2. 通常の運用では、秩序立った電源オフまたは再起動コマンドを使う。
3. ユーザーとワークロードに警告が必要なら、シャットダウンを予約する。
4. 保守計画が変わったら、保留中のシャットダウンを取り消す。
5. マシンの復帰後、システムとアプリケーションの正常性を検証する。
