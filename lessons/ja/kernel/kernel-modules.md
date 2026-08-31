---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "ja"
order_index: 6
title: "カーネルモジュール"
description: "release 固有の Linux kernel module を調査、load、設定し、安全に削除する方法を学びます。"
meta_title: "カーネルモジュール - カーネル"
meta_description: "Linux におけるカーネルモジュールとは何か、そしてそれがカーネル機能をどのように拡張するかを発見してください。このレッスンでは、lsmod と modprobe を使用して、モジュールをオンデマンドで一覧表示、ロード、アンロードする方法を解説します。"
meta_keywords: "カーネルモジュールとは，Linux カーネルモジュール，modprobe, lsmod, カーネル管理，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

loadable kernel module は、driver、filesystem、network feature などの subsystem を追加して、動作中カーネルを拡張できる特権 code です。module によって全 optional feature を一つの kernel image に build せずに済みますが、load すると信頼される kernel attack surface が広がります。

## Module を一覧・調査する

現在 load 済みの module を一覧表示します。

```bash
$ lsmod
```

出力は `/proc/modules` などの kernel state から得られ、module name、size、use count または dependency を含みます。count が 0 に見えても、安全に削除できる完全な証拠ではありません。driver が active device を所有したり、subsystem state に参加したりしている場合があります。

動作中カーネルで利用可能な module を調べます。

```bash
$ modinfo MODULE_NAME
```

`modinfo` は filename、alias、parameter、license、description、signature information を表示できます。metadata は説明情報として扱い、module が信頼できる、または workload と互換だという証明にはしないでください。

:::single-choice{#kernel-modules-lsmod-purpose}
`lsmod` は何を表示しますか？

::option[remote repository で利用可能な全 module package。]{#kernel-modules-repository-list explanation="repository inventory には package-manager query が必要です。"}
::option[kernel image へ直接 compile された driver だけ。]{#kernel-modules-builtins explanation="built-in feature は loadable module ではなく、通常 lsmod に現れません。"}
::option[動作中カーネルに現在 load されている module。]{#kernel-modules-loaded-list .correct explanation="一覧は live module state と dependency/use information を反映します。"}
:::

## `modprobe` で Load する

名前で module を load します。

```bash
$ sudo modprobe MODULE_NAME
```

`modprobe` は `/lib/modules/$(uname -r)/` 以下にある動作中カーネルの dependency index、alias、configuration を参照します。必要な dependency を load し、設定済み parameter を渡します。一方 `insmod` は指定した一つの module file を直接 insert し、同じ dependency-resolution workflow を提供しません。

load 前に module provenance、signature policy、kernel release compatibility、parameter、想定する hardware binding、rollback を確認します。Secure Boot や kernel lockdown は unsigned module を拒否できます。非互換 code の強制は crash や compromise の危険があります。

:::single-choice{#kernel-modules-modprobe-dependencies}
通常、直接の `insmod` より `modprobe` が推奨されるのはなぜですか？

::option[module 全体を非特権ユーザー空間で実行するから。]{#kernel-modules-modprobe-userspace explanation="insert された module は privileged kernel code として動きます。"}
::option[すべての third-party module が署名済みで安全だと保証するから。]{#kernel-modules-modprobe-guarantee explanation="強制は policy に依存し、有効な signature も defect がないことは証明しません。"}
::option[module の alias、dependency、configuration を解決するから。]{#kernel-modules-modprobe-resolves .correct explanation="modprobe は正確な動作中 release の indexed module tree を使います。"}
:::

## Module Parameter と Boot-Time Loading

永続的な parameter・alias policy は、`/etc/modprobe.d/` 以下の `.conf` file に置きます。

```text
options example_module mode=careful
```

この行は modprobe が module を load する方法へ影響しますが、それ自体では boot 時の load を要求しません。単純な boot-time load list は通常 `/etc/modules-load.d/` 以下に置きます。

```text
example_module
```

hardware alias によって明示的な list なしでも自動 load される場合があります。early boot 内で必要な module は、設定変更後にディストリビューション指定手順で initramfs を更新します。

:::single-choice{#kernel-modules-options-versus-load}
`/etc/modprobe.d/` の `options` 行は何をしますか？

::option[その行だけで module が毎 boot 必ず load されるようにする。]{#kernel-modules-options-autoload explanation="boot-time load request には modules-load 設定や device alias など別の仕組みを使います。"}
::option[指定 module が load されるときに使う parameter を設定する。]{#kernel-modules-options-parameters .correct explanation="modprobe が insert 時に設定済み key-value argument を適用します。"}
::option[インストール済み全 kernel release 向けに module を compile する。]{#kernel-modules-options-compiles explanation="configuration は binary module を build しません。"}
:::

## Blacklist とその限界

modprobe 設定には次の行を書けます。

```text
blacklist example_module
```

blacklist は通常、module alias を通じた自動 load を抑止します。すでに load 済み module を unload せず、initramfs からも取り除かず、正確な名前による明示 load や dependency としての load を必ず防ぐわけでもありません。security hardening には、threat 固有の module availability、signature enforcement、initramfs content、boot parameter、policy の組み合わせが必要です。

:::single-choice{#kernel-modules-blacklist-effect}
基本的な modprobe の `blacklist` 行が主に抑止するものは何ですか？

::option[module alias を通じた自動 load。]{#kernel-modules-blacklist-aliases .correct explanation="この directive は、code がすでに load 済み、または load される全経路を普遍的に禁止するものではありません。"}
::option[似た名前を持つ全 user-space program の実行。]{#kernel-modules-blacklist-user-programs explanation="modprobe configuration が適用されるのは kernel module resolution です。"}
::option[image に compile 済みのすべての kernel code。]{#kernel-modules-blacklist-builtins explanation="built-in functionality は module として unload・block できません。"}
:::

## Module を安全に削除する

削除を要求します。

```bash
$ sudo modprobe -r MODULE_NAME
```

modprobe は適切な場合、使われなくなった dependency も削除できます。通常の reference tracking で module が busy ならカーネルは拒否しますが、それだけを安全確認にしないでください。active hardware を支える code を削除する前に、service を停止し、filesystem を unmount し、device を detach し、networking を quiesce して、別 driver または recovery path を確認します。

維持すべき system で module を強制 unload してはいけません。削除 bug や outstanding activity が kernel crash または data corruption を起こす可能性があります。

:::single-choice{#kernel-modules-remove-command}
名前を指定し、dependency を考慮して module の削除を要求するコマンドはどれですか？

::option[`lsmod -r MODULE_NAME`]{#kernel-modules-lsmod-remove explanation="lsmod は読み取り専用の一覧ツールで、削除の役割はありません。"}
::option[`uname -r MODULE_NAME`]{#kernel-modules-uname-remove explanation="uname は kernel information を報告し、module は管理しません。"}
::option[`modprobe -r MODULE_NAME`]{#kernel-modules-modprobe-remove .correct explanation="remove mode は要求 module 周辺の indexed dependency relationship を考慮します。"}
:::

ラボで安全と指定された module を使って練習するには、[Linux でカーネルモジュールを管理する](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865)を利用できます。

## まとめ

これで、kernel-level risk を考慮しながら module を管理できます。

1. live state には `lsmod`、利用可能な metadata には `modinfo` を使う。
2. alias と dependency を考慮した load に `modprobe` を使う。
3. modprobe parameter と boot-time load request を分離する。
4. blacklisting を絶対的な block ではなく、限界のある policy として扱う。
5. `modprobe -r` 前にすべての consumer を quiesce する。
