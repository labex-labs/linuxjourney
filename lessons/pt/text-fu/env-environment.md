---
index: 5
lang: "pt"
title: "env (Ambiente)"
meta_title: "env (Ambiente) - Text-Fu"
meta_description: "Explore o que o comando env faz no Linux. Este guia explica como visualizar e usar variáveis de ambiente do Linux como PATH, HOME e USER com o comando env."
meta_keywords: "env, env linux, comando env linux, o que o env faz no linux, variáveis de ambiente, variável PATH, variáveis de shell"
---

## Lesson Content

Seu sistema Linux usa variáveis de ambiente para armazenar informações que o shell e outros processos podem acessar. Essas variáveis contêm dados úteis sobre sua sessão de usuário e configuração do sistema.

### Explorando Variáveis de Ambiente Básicas

Você pode visualizar o valor de uma variável específica prefixando seu nome com um símbolo de `$`. Por exemplo, execute o seguinte comando:

```bash
echo $HOME
```

Este comando exibirá o caminho para o seu diretório inicial, que pode ser algo como `/home/pete`.

Agora, tente outro:

```bash
echo $USER
```

Isso exibirá seu nome de usuário atual. Mas de onde vêm essas informações? Elas são armazenadas no ambiente do seu shell.

### O que o env faz no Linux

Para ver todas as variáveis de ambiente atualmente definidas para sua sessão, você pode usar o comando `env`. O `comando linux env` é uma ferramenta fundamental para inspecionar a configuração do seu shell.

```bash
env
```

Executar o comando `env` produzirá uma lista de pares chave-valor. Aqui está um pequeno exemplo do que você pode ver:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Entender o `linux env` é crucial para gerenciar seu sistema de forma eficaz.

### A Importância da Variável PATH

Uma das variáveis mais importantes na sua saída do `env linux` é `PATH`. Você pode visualizar seu conteúdo especificamente com:

```bash
echo $PATH
```

Este comando retorna uma lista de diretórios separados por dois pontos. Quando você digita um comando, seu sistema procura nesses diretórios para encontrar o arquivo executável correspondente.

Imagine que você instala manualmente um programa em um diretório não padrão como `/opt/coolapp/bin`. Se você tentar executá-lo digitando `coolcommand`, poderá receber um erro de "comando não encontrado". Isso acontece porque o diretório que contém seu programa não está listado na variável `PATH`, então o shell não sabe onde procurá-lo.

Para corrigir isso, você pode modificar a variável `PATH` para incluir o novo diretório. Ao adicionar seu diretório personalizado ao `PATH`, você permite que o shell encontre e execute seus programas de qualquer lugar no terminal.

### Definindo uma Variável de Ambiente para a Sessão Atual

Executar o seguinte comando no seu terminal define a variável de ambiente `TEST` apenas para a sessão atual:

```bash
export TEST=test
```

Depois disso, se você executar:

```bash
echo $TEST
```

A saída será:

```
test
```

Esta variável estará disponível enquanto a sessão do terminal permanecer aberta. Assim que você fechar e reabrir o terminal, a variável não existirá mais.

### Tornando a Variável de Ambiente Persistente Entre Sessões

Se você deseja que a variável de ambiente esteja disponível em todas as sessões de terminal (mesmo após fechar e reabrir o terminal), você precisa adicioná-la ao arquivo de inicialização do seu shell. No caso do Bash (o shell padrão para muitas distribuições Linux e macOS), este arquivo geralmente é o `.bashrc` no seu diretório inicial.

Veja como fazer isso:

1.  Abra o `.bashrc` no seu editor de texto preferido. Por exemplo:

        ```bash

    nano ~/.bashrc
    ```

2.  Adicione a linha `export` ao final do arquivo:

        ```bash

    export TEST=test
    ```

3.  Salve e saia do editor (no Nano, isso seria `Ctrl+X`, depois `S` para confirmar, e `Enter`).

4.  Para aplicar as alterações imediatamente sem reabrir o terminal, execute:

        ```bash

    source ~/.bashrc
    ```

Depois disso, a variável `TEST` estará disponível em todas as sessões de terminal futuras, e executar `echo $TEST` imprimirá `test` mesmo depois de fechar e reabrir o terminal.

### Uma Nota sobre Arquivos de Configuração do Shell

- Para **Bash** (o padrão na maioria dos sistemas), o arquivo relevante é `~/.bashrc` para shells interativos não de login.
- Para **Zsh**, o arquivo equivalente geralmente é `~/.zshrc`.
- Para **Fish**, você normalmente usaria `~/.config/fish/config.fish`.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão das variáveis de ambiente do Linux:

1. **[Gerenciar Ambiente de Shell e Configuração no Linux](https://labex.io/pt/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Pratique a criação e o gerenciamento de variáveis locais e de ambiente, entendendo a herança e tornando as configurações persistentes modificando o arquivo `.bashrc`.
2. **[Variáveis de Ambiente no Linux](https://labex.io/pt/labs/linux-environment-variables-in-linux-385274)** - Aprenda o conceito e o uso de variáveis de ambiente, como criá-las, modificá-las e gerenciá-las, e seu papel na configuração do sistema.
3. **[Configurar Variáveis de Ambiente do Linux](https://labex.io/pt/labs/linux-configure-linux-environment-variables-437861)** - Obtenha experiência prática criando, definindo e gerenciando variáveis de ambiente em um sistema Linux.

Esses laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança no gerenciamento do ambiente do seu shell Linux.

## Quiz Question

Qual comando exibe todas as suas variáveis de ambiente atuais? (Por favor, responda em inglês, usando apenas o nome do comando em minúsculas).

## Quiz Answer

env
