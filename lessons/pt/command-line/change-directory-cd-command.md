---
index: 3
lang: "pt"
title: "cd (Mudar Diretório)"
meta_title: "cd (Mudar Diretório) - Linha de Comando"
meta_description: "Aprenda a usar o comando 'cd' no Linux para navegar por diretórios. Entenda caminhos absolutos, relativos e atalhos úteis. Comece sua jornada no Linux!"
meta_keywords: "comando cd, mudar diretório, caminhos Linux, caminho absoluto, caminho relativo, tutorial Linux, Linux para iniciantes, navegação Linux"
---

## Lesson Content

Agora que você sabe onde está, vamos ver se conseguimos nos mover um pouco pelo sistema de arquivos. Lembre-se, precisaremos navegar usando caminhos. Existem duas maneiras diferentes de especificar um caminho: com caminhos absolutos e relativos.

- Caminho absoluto: Este é o caminho a partir do diretório raiz. A raiz é o chefão. O diretório raiz é comumente mostrado como uma barra (`/`). Toda vez que seu caminho começa com `/`, significa que você está começando do diretório raiz. Por exemplo, `/home/pete/Desktop`.

- Caminho relativo: Este é o caminho a partir de onde você está atualmente no sistema de arquivos. Se eu estivesse no local `/home/pete/Documents` e quisesse ir para um diretório dentro de `Documents` chamado `taxes`, não preciso especificar o caminho completo a partir da raiz como `/home/pete/Documents/taxes`; posso simplesmente ir para `taxes/`.

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

Pode ser bastante cansativo navegar com caminhos absolutos e relativos o tempo todo. Felizmente, existem alguns atalhos para ajudá-lo.

- `.` (diretório atual): Este é o diretório em que você está atualmente.
- `..` (diretório anterior): Leva você para o diretório acima do seu atual.
- `~` (diretório home): Este diretório padrão é o seu “diretório home”, como `/home/pete`.
- `-` (diretório anterior): Isso o levará para o diretório anterior onde você estava.

```bash
cd .
cd ..
cd ~
cd -
```

Experimente-os!

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da navegação de diretórios Linux:

1. **[Comando Linux cd: Mudança de Diretório](https://labex.io/pt/labs/linux-linux-cd-command-directory-changing-209733)** - Aprenda o comando Linux `cd` para navegar eficientemente em seu sistema de arquivos, incluindo várias técnicas para mudar diretórios, entender caminhos e explorar a estrutura de arquivos.
2. **[Navegação de Diretório Linux](https://labex.io/pt/labs/linux-directory-navigation-387844)** - Teste suas habilidades básicas de linha de comando Linux navegando por diretórios usando comandos essenciais.
3. **[Configurando uma Nova Estrutura de Projeto](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)** - Pratique suas habilidades de gerenciamento de diretórios Linux criando uma estrutura de projeto específica e navegando por ela usando comandos essenciais como `mkdir` e `cd`.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança na navegação do sistema de arquivos Linux.

## Quiz Question

Se você está em `/home/pete/Pictures` e quer ir para `/home/pete`, qual é um bom atalho para usar?

## Quiz Answer

cd ..
