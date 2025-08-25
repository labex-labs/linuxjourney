---
index: 5
lang: "pt"
title: "rpm e dpkg"
meta_title: "rpm e dpkg - Pacotes"
meta_description: "Aprenda a instalar, remover e listar pacotes usando os comandos rpm e dpkg. Entenda o gerenciamento direto de pacotes para arquivos .deb e .rpm. Comece sua jornada no Linux!"
meta_keywords: "rpm, dpkg, gerenciamento de pacotes Linux, .deb, .rpm, tutorial Linux, guia para iniciantes, instalar pacotes"
---

## Lesson Content

Embora a maior parte deste curso seja sobre sistemas de gerenciamento de pacotes (os Batmans do gerenciamento de pacotes), não devemos esquecer os Robins. Embora muito úteis e confiáveis, eles não vêm com aquele Batmóvel e cinto de utilidades.

Assim como `.exe` é um único arquivo executável, o mesmo acontece com `.deb` e `.rpm`. Normalmente, você não os veria se usasse repositórios de pacotes, mas se você baixar pacotes diretamente, provavelmente os obterá nesses formatos populares. Obviamente, eles são exclusivos de suas distribuições: `.deb` para distribuições baseadas em Debian e `.rpm` para distribuições baseadas em Red Hat.

Para instalar esses pacotes diretos, você pode usar os comandos de gerenciamento de pacotes: `rpm` e `dpkg`. Essas ferramentas são usadas para instalar arquivos de pacote; no entanto, elas não instalarão as dependências do pacote. Então, se o seu pacote tivesse 10 dependências, você teria que instalar esses pacotes separadamente e depois suas dependências, e assim por diante. Como você pode ver, essa foi uma das razões que trouxeram os sistemas de gerenciamento completos que discutiremos mais tarde.

Tenha em mente que haverá inúmeras vezes em que você precisará instalar, consultar ou verificar um pacote com uma dessas ferramentas, então lembre-se desses comandos.

### Instalar um pacote

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

O `i` significa instalar. Você também pode usar o formato mais longo de `--install`.

### Remover um pacote

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` para remover
RPM: `e` para apagar

### Listar pacotes instalados

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` para listar
RPM: `q` para consulta e `a` para todos

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão do gerenciamento direto de pacotes:

1. **[Gerenciando Pacotes com RPM no Linux](https://labex.io/pt/labs/rhel-managing-packages-with-rpm-in-linux-590868)** - Ganhe experiência prática consultando informações de pacotes, verificando a integridade, listando dependências, simulando a remoção e inspecionando o conteúdo do pacote RPM com `rpm` e ferramentas relacionadas.

Este laboratório o ajudará a aplicar os conceitos de gerenciamento de arquivos de pacotes individuais em um cenário real e a construir confiança com essas ferramentas essenciais do Linux.

## Quiz Question

Qual é a ferramenta de gerenciamento de pacotes para arquivos `.deb`?

## Quiz Answer

dpkg
