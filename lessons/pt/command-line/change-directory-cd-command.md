---
title: "cd (Mudar Diretório)"
description: "Aprenda a usar o comando 'cd' no Linux para navegar por diretórios. Entenda caminhos absolutos, relativos e atalhos úteis. Comece sua jornada no Linux!"
keywords: "comando cd, mudar diretório, caminhos Linux, caminho absoluto, caminho relativo, tutorial Linux, Linux para iniciantes, navegação Linux"
---

## Lesson Content

Agora que você sabe onde está, vamos ver se conseguimos nos mover um pouco pelo sistema de arquivos. Lembre-se, precisaremos navegar usando caminhos. Existem duas maneiras diferentes de especificar um caminho: com caminhos absolutos e relativos.

- Caminho absoluto: Este é o caminho a partir do diretório raiz. A raiz é o chefão. O diretório raiz é comumente mostrado como uma barra (`/`). Toda vez que seu caminho começa com `/`, significa que você está começando do diretório raiz. Por exemplo, `/home/pete/Desktop`.

- Caminho relativo: Este é o caminho a partir de onde você está atualmente no sistema de arquivos. Se eu estivesse no local `/home/pete/Documents` e quisesse ir para um diretório dentro de `Documents` chamado `taxes`, não preciso especificar o caminho completo a partir da raiz como `/home/pete/Documents/taxes`; posso simplesmente ir para `taxes/` em vez disso.

Agora que você sabe como os caminhos funcionam, só precisamos de algo para nos ajudar a mudar para o diretório que queremos. Felizmente, temos `cd` ou “change directory” para fazer isso.

```bash
cd /home/pete/Pictures
```

Então agora eu mudei meu local de diretório para `/home/pete/Pictures`.

Agora, a partir deste diretório, tenho uma pasta dentro chamada `Hawaii`. Posso navegar para essa pasta com:

```bash
cd Hawaii
```

Percebeu como eu usei apenas o nome da pasta? É porque eu já estava em `/home/pete/Pictures`.

Pode ser bastante cansativo navegar com caminhos absolutos e relativos o tempo todo. Felizmente, existem alguns atalhos para ajudar você.

- `.` (current directory): Este é o diretório em que você está atualmente.
- `..` (previous directory): Leva você para o diretório acima do seu atual.
- `~` (home directory): Este diretório padrão é o seu “home directory”, como `/home/pete`.
- `-` (previous directory): Isso o levará para o diretório anterior onde você estava.

```bash
cd .
cd ..
cd ~
cd -
```

Experimente!

## Exercise

1. Run the `cd` command without any flags. Where does it take you?

## Quiz Question

Se você está em `/home/pete/Pictures` e quer ir para `/home/pete`, qual é um bom atalho para usar?

## Quiz Answer

cd ..
