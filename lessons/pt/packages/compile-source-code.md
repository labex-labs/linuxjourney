---
index: 7
lang: "pt"
title: "Compilar Código Fonte"
meta_title: "Compilar Código Fonte - Pacotes"
meta_description: "Aprenda a compilar a partir do código fonte no Linux. Este guia cobre os passos essenciais sobre como construir código fonte usando configure, make e o comando recomendado checkinstall para um gerenciamento de pacotes limpo."
meta_keywords: "como compilar a partir do código fonte, como construir código fonte, compilar código fonte, make install, checkinstall, compilar Linux, build-essential, script configure, makefile, tutorial Linux"
---

## Lesson Content

Ocasionalmente, você pode encontrar um pacote que está disponível apenas como código-fonte. Para usá-lo, você precisará compilá-lo e instalá-lo no seu sistema. Esta lição o guiará pelo processo comum de como compilar a partir do código-fonte.

### Preparando Seu Sistema

Antes de poder compilar qualquer coisa, você precisa das ferramentas necessárias. Em sistemas baseados em Debian, como o Ubuntu, você pode instalá-las com um único comando.

```bash
sudo apt install build-essential
```

O pacote `build-essential` instala um conjunto de ferramentas de desenvolvimento de software, incluindo o compilador GCC e o utilitário `make`, que são essenciais para a compilação.

Após instalar as ferramentas, extraia o conteúdo do pacote de código-fonte, que geralmente é um arquivo `.tar.gz`.

```bash
tar -xzvf package.tar.gz
```

Antes de prosseguir, sempre verifique se há um arquivo `README` ou `INSTALL` dentro do diretório extraído. Esses arquivos geralmente contêm instruções específicas ou dependências necessárias para aquele pacote em particular.

### O Processo de Compilação Padrão

Embora desenvolvedores diferentes possam usar vários sistemas de compilação como `cmake`, o método mais tradicional envolve um processo de três etapas. Entender isso é fundamental para aprender a construir código-fonte.

Primeiro, execute o script `configure`. Este script verifica seu sistema em busca de todas as dependências e bibliotecas necessárias que o software precisa para ser compilado e executado corretamente.

```bash
./configure
```

O prefixo `./` diz ao shell para executar o script a partir do diretório atual. Se o script relatar dependências ausentes, você deve instalá-las antes de continuar.

Em seguida, execute o comando `make`. Este comando lê um arquivo chamado `Makefile` no diretório, que contém um conjunto de regras sobre como compilar o código-fonte em programas executáveis.

```bash
make
```

Finalmente, para instalar o software no seu sistema, você normalmente executaria:

```bash
sudo make install
```

Este comando copia os arquivos compilados para os diretórios apropriados do sistema, tornando o software disponível para uso.

### Uma Maneira Melhor de Instalar

Embora `sudo make install` funcione, ele tem uma desvantagem significativa: ele não registra o software no gerenciador de pacotes do seu sistema. Isso torna difícil rastrear, atualizar ou desinstalar o pacote de forma limpa mais tarde.

A abordagem muito melhor é usar `checkinstall`. Esta ferramenta executa o processo de instalação, mas, em vez de copiar arquivos diretamente, ela cria um pacote de sistema nativo (como um arquivo `.deb` no Debian/Ubuntu) e o instala.

```bash
sudo checkinstall
```

Usar `checkinstall` integra o software compilado ao seu sistema de gerenciamento de pacotes. Isso significa que você pode removê-lo facilmente mais tarde usando `apt` ou `dpkg`, assim como qualquer outro pacote que você instalou dos repositórios oficiais. Por esse motivo, você deve sempre preferir `checkinstall` a `make install`.

Para desinstalar um pacote instalado com `make install`, você teria que voltar ao diretório de origem e executar `sudo make uninstall`, mas isso nem sempre é confiável.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão da compilação de software a partir da fonte:

1. **[Compilar Software a Partir do Código-Fonte no Linux](https://labex.io/pt/labs/comptia-build-software-from-source-code-in-linux-590853)** - Pratique o processo fundamental de compilação e instalação de software a partir do seu código-fonte, incluindo o uso de `configure`, `make` e `make install`.

Este laboratório o ajudará a aplicar os conceitos em um cenário real e a ganhar confiança na compilação de software.

## Quiz Question

O que você deve usar em vez de `make install` SEMPRE? (Por favor, responda em inglês, prestando atenção à sensibilidade a maiúsculas e minúsculas).

## Quiz Answer

checkinstall
