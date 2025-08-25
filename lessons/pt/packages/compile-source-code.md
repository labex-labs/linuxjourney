---
index: 7
lang: "pt"
title: "Compilar Código-Fonte"
meta_title: "Compilar Código-Fonte - Pacotes"
meta_description: "Aprenda a compilar código-fonte no Linux usando make, configure e checkinstall. Entenda o processo de construção para usuários iniciantes e intermediários."
meta_keywords: "compilar código-fonte, make install, checkinstall, compilar Linux, build-essential, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Frequentemente, você encontrará um pacote obscuro que vem apenas na forma de código-fonte puro. Você precisará usar alguns comandos para compilar e instalar esse pacote de código-fonte em seu sistema.

Primeiro, você precisará ter software para instalar as ferramentas que permitirão compilar o código-fonte.

```bash
sudo apt install build-essential
```

Depois de fazer isso, extraia o conteúdo do arquivo do pacote, provavelmente um arquivo `.tar.gz`.

```bash
tar -xzvf package.tar.gz
```

Antes de fazer qualquer coisa, dê uma olhada no arquivo `README` ou `INSTALL` dentro do pacote. Às vezes, haverá instruções de instalação específicas.

Dependendo do método de compilação que o desenvolvedor usou, você terá que usar comandos diferentes, como `cmake` ou algo mais.

No entanto, o mais comum é a compilação básica com `make`, então vamos discutir isso:

Dentro do conteúdo do pacote haverá um script `configure`. Este script verifica as dependências em seu sistema e, se estiver faltando algo, você verá um erro e precisará corrigir essas dependências.

```bash
./configure
```

O `./` permite executar um script no diretório atual.

```bash
make
```

Dentro do conteúdo do pacote, há um arquivo chamado `Makefile` que contém regras para construir o software. Quando você executa o comando `make`, ele procura este arquivo para construir o software.

```bash
sudo make install
```

Este comando realmente instala o pacote; ele copiará os arquivos corretos para os locais corretos em seu computador.

Se você quiser desinstalar o pacote, use:

```bash
sudo make uninstall
```

Tenha cuidado ao usar `make install`; você pode não perceber o quanto está realmente acontecendo em segundo plano. Se você decidir remover este pacote, pode não remover tudo porque não percebeu o que foi adicionado ao seu sistema. Em vez disso, esqueça tudo sobre `make install` que acabei de explicar e use o comando **checkinstall**. Este comando criará um arquivo `.deb` para você que pode ser facilmente instalado e desinstalado.

```bash
sudo checkinstall
```

Este comando essencialmente fará um "make install" e construirá um pacote `.deb` e o instalará. Isso facilita a remoção do pacote posteriormente.

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão sobre a construção de software a partir do código-fonte:

1. **[Construir Software a Partir do Código-Fonte no Linux](https://labex.io/pt/labs/comptia-build-software-from-source-code-in-linux-590853)** - Pratique o processo fundamental de construção e instalação de software a partir de seu código-fonte, incluindo o uso de `configure`, `make` e `make install`.

Este laboratório o ajudará a aplicar os conceitos em um cenário real e a construir confiança na compilação de software.

## Quiz Question

O que você deve usar em vez de `make install` SEMPRE?

## Quiz Answer

checkinstall
