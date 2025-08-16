---
title: "Compilar Código-Fonte"
description: "Aprenda a compilar código-fonte no Linux usando make, configure e checkinstall. Entenda o processo de construção para usuários iniciantes e intermediários."
keywords: "compilar código-fonte, make install, checkinstall, compilar Linux, build-essential, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Frequentemente, você encontrará um pacote obscuro que vem apenas na forma de código-fonte puro. Você precisará usar alguns comandos para compilar e instalar esse pacote de código-fonte em seu sistema.

Primeiro, você precisará ter o software para instalar as ferramentas que permitirão compilar o código-fonte.

```bash
sudo apt install build-essential
```

Depois de fazer isso, extraia o conteúdo do arquivo do pacote, provavelmente um arquivo `.tar.gz`.

```bash
tar -xzvf package.tar.gz
```

Antes de fazer qualquer coisa, dê uma olhada no arquivo `README` ou `INSTALL` dentro do pacote. Às vezes, haverá instruções de instalação específicas.

Dependendo do método de compilação que o desenvolvedor usou, você terá que usar comandos diferentes, como `cmake` ou algo mais.

No entanto, na maioria das vezes você verá a compilação básica `make`, então discutiremos isso:

Dentro do conteúdo do pacote haverá um script `configure`. Este script verifica as dependências em seu sistema e, se você estiver perdendo algo, verá um erro e precisará corrigir essas dependências.

```bash
./configure
```

O `./` permite executar um script no diretório atual.

```bash
make
```

Dentro do conteúdo do pacote, há um arquivo chamado `Makefile` que contém regras para construir o software. Quando você executa o comando `make`, ele olha para este arquivo para construir o software.

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

Encontre um programa de código-fonte (de um site confiável) e instale a partir do código-fonte.

## Quiz Question

O que você deve usar SEMPRE em vez de `make install`?

## Quiz Answer

checkinstall
