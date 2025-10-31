---
index: 3
lang: "pt"
title: "cd (Mudar Diretório)"
meta_title: "cd (Mudar Diretório) - Linha de Comando"
meta_description: "Aprenda o comando essencial cd linux para mudar de diretório. Este guia cobre o uso do comando cd no prompt de comando, navegando para qualquer pasta cd com caminhos absolutos e relativos, e usando atalhos úteis."
meta_keywords: "comando cd, comando cd linux, pasta cd, prompt de comando cd, comando cd cmd, mudar diretório, navegação linux, caminho absoluto, caminho relativo"
---

## Lesson Content

Para se mover pelo sistema de arquivos Linux, você usará caminhos (paths) para especificar seu destino. A ferramenta principal para isso é o comando `cd` (change directory - mudar diretório). Entender como usar este `comando cd linux` é uma habilidade fundamental para trabalhar no terminal ou no `prompt de comando cd`.

### Entendendo Caminhos

Existem duas maneiras de especificar um caminho: absoluto e relativo.

- **Caminho Absoluto**: É o caminho completo começando pelo diretório raiz (`/`). A raiz é o diretório de nível superior no sistema de arquivos. Qualquer caminho que comece com `/` é um caminho absoluto. Exemplo: `/home/pete/Desktop`.

- **Caminho Relativo**: Este caminho é relativo à sua localização atual no sistema de arquivos. Se você estiver em `/home/pete/Documents` e quiser acessar um subdiretório chamado `taxes`, você não precisa do caminho completo. Você pode simplesmente usar o caminho relativo: `taxes/`.

### Usando o Comando cd

Depois de entender os caminhos, você pode usar o `comando cd` para mudar seu diretório atual. Se você está em um terminal Linux ou em um prompt `cd command cmd` do Windows, o conceito de mudar de diretório é universal, embora a sintaxe possa diferir ligeiramente.

Para mudar para um diretório específico usando um caminho absoluto, você digitaria:

```bash
cd /home/pete/Pictures
```

Este comando move você diretamente para o diretório `Pictures`.

### Navegando para uma pasta cd

Se você já está em um diretório e deseja mover-se para um subdiretório, pode usar um caminho relativo. Por exemplo, se sua localização atual for `/home/pete/Pictures` e ela contiver uma `pasta cd` chamada `Hawaii`, você pode navegar até ela com:

```bash
cd Hawaii
```

Note que usamos apenas o nome da pasta. Isso ocorre porque já estávamos em seu diretório pai, `/home/pete/Pictures`.

### Atalhos Essenciais de Navegação

Navegar com caminhos completos pode ser tedioso. Felizmente, o shell fornece vários atalhos para tornar a movimentação muito mais rápida.

- `.` (diretório atual): Representa o diretório em que você está atualmente.
- `..` (diretório pai): Move você um nível acima para o diretório que contém o seu diretório atual.
- `~` (diretório home): Um atalho para o seu diretório pessoal, como `/home/pete`.
- `-` (diretório anterior): Leva você de volta ao último diretório em que você esteve.

You can use these shortcuts with the `cd command`:

```bash
cd .
cd ..
cd ~
cd -
```

Experimente estes atalhos para se tornar mais eficiente na linha de comando.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da navegação de diretórios no Linux:

1. **[Comando cd Linux: Mudança de Diretório](https://labex.io/pt/labs/linux-linux-cd-command-directory-changing-209733)** - Aprenda o comando `cd` do Linux para navegar eficientemente pelo seu sistema de arquivos, incluindo várias técnicas para mudar de diretório, entender caminhos e explorar a estrutura de arquivos.
2. **[Navegação de Diretórios Linux](https://labex.io/pt/labs/linux-directory-navigation-387844)** - Coloque suas habilidades básicas de linha de comando Linux à prova, navegando por diretórios usando comandos essenciais.
3. **[Configurando uma Nova Estrutura de Projeto](https://labex.io/pt/labs/linux-setting-up-a-new-project-structure-387859)** - Pratique suas habilidades de gerenciamento de diretórios no Linux criando uma estrutura de projeto específica e navegando por ela usando comandos essenciais como `mkdir` e `cd`.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a ganhar confiança na navegação pelo sistema de arquivos Linux.

## Quiz Question

Se você estiver em `/home/pete/Pictures` e quiser navegar para o diretório pai (`/home/pete`), qual é o comando completo que você deve usar? Por favor, responda em inglês, prestando atenção a maiúsculas/minúsculas e espaços.

## Quiz Answer

cd ..
