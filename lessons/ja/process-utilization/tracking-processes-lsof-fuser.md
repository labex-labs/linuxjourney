---
index: 2
lang: "ja"
title: "lsof と fuser"
meta_title: "lsof と fuser - プロセス利用率"
meta_description: "Linux で lsof および fuser コマンドを使用して、ファイルを使用しているプロセスを特定する方法を学びます。「Device or Resource Busy」エラーを理解し、開いているファイルを効果的に管理します。"
meta_keywords: "lsof, fuser, Linux コマンド，開いているファイル，プロセス管理，Linux チュートリアル，初心者向けガイド，デバイスビジー"
---

## Lesson Content

USB ドライブを接続して、いくつかのファイルの作業を始めたとします。作業が終わり、USB デバイスをアンマウントしようとしたところ、「Device or Resource Busy」というエラーが表示されました。USB ドライブ上のどのファイルがまだ使用されているかをどうやって見つけますか？これには 2 つのツールを使用できます。

### lsof

ファイルは単なるテキストファイルや画像などではなく、ディスク、パイプ、ネットワークソケット、デバイスなど、システム上のすべてであることを思い出してください。プロセスによって何が使用されているかを確認するには、`lsof`コマンド（「list open files」の略）を使用できます。これにより、すべての開いているファイルとそれに関連するプロセスのリストが表示されます。

```bash
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
```

これで、どのプロセスが現在デバイス/ファイルをオープンしているかを確認できます。USB の例では、これらのプロセスを強制終了して、この厄介なドライブをアンマウントすることもできます。

### fuser

プロセスを追跡するもう 1 つの方法は、`fuser`コマンド（「file user」の略）を使用することです。これにより、ファイルまたはファイルユーザーを使用しているプロセスに関する情報が表示されます。

```bash
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
```

現在、どのプロセスが`/home/pete`ディレクトリを使用しているかを確認できます。`lsof`と`fuser`ツールは非常によく似ています。これらのツールに慣れて、次回ファイルやプロセスを追跡する必要があるときに試してみてください。

## Exercise

`lsof`と`fuser`の man ページを読んでください。これらのツールをより柔軟に利用できる、ここでは触れていない多くの情報があります。

## Quiz Question

開いているファイルとそのプロセス情報を一覧表示するために使用されるコマンドは何ですか？

## Quiz Answer

lsof
