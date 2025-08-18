---
lang: "pt"
title: "rpm e dpkg"
meta_description: "Aprenda a instalar, remover e listar pacotes usando os comandos rpm e dpkg. Entenda o gerenciamento direto de pacotes para arquivos .deb e .rpm. Comece sua jornada no Linux!"
meta_keywords: "rpm, dpkg, gerenciamento de pacotes Linux, .deb, .rpm, tutorial Linux, guia para iniciantes, instalar pacotes"
---

## Lesson Content

Embora a maior parte deste curso seja sobre sistemas de gerenciamento de pacotes (os Batmans do gerenciamento de pacotes), não devemos esquecer os Robins. Embora muito úteis e confiáveis, eles não vêm com aquele doce Batmóvel e cinto de utilidades.

Assim como `.exe` é um único arquivo executável, também são `.deb` e `.rpm`. Normalmente, você não os veria se usasse repositórios de pacotes, mas se você baixar pacotes diretamente, provavelmente os obterá nesses formatos populares. Obviamente, eles são exclusivos de suas distribuições: `.deb` para distribuições baseadas em Debian e `.rpm` para distribuições baseadas em Red Hat.

Para instalar esses pacotes diretos, você pode usar os comandos de gerenciamento de pacotes: `rpm` e `dpkg`. Essas ferramentas são usadas para instalar arquivos de pacote; no entanto, elas não instalarão as dependências do pacote. Então, se o seu pacote tivesse 10 dependências, você teria que instalar esses pacotes separadamente e depois suas dependências, e assim por diante. Como você pode ver, essa foi uma das razões que trouxeram os sistemas de gerenciamento completos que discutiremos mais tarde.

Lembre-se de que haverá inúmeras vezes em que você precisará instalar, consultar ou verificar um pacote com uma dessas ferramentas, então lembre-se desses comandos.

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

O `i` significa install. Você também pode usar o formato mais longo de `--install`.

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` para remove
RPM: `e` para erase

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` para list
RPM: `q` para query e `a` para all

## Exercise

Encontre um programa que você queira instalar em seu sistema, como o Google Chrome, e instale-o usando um desses comandos.

## Quiz Question

Qual é a ferramenta de gerenciamento de pacotes para arquivos `.deb`?

## Quiz Answer

dpkg
