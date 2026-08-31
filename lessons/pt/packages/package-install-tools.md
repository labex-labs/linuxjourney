---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "pt"
order_index: 5
title: "rpm e dpkg"
description: "Aprenda como `dpkg` e `rpm` inspecionam e modificam seus bancos de dados de pacotes nativos e arquivos locais."
meta_title: "rpm e dpkg - Pacotes"
meta_description: "Aprenda a instalar, remover e listar pacotes com os comandos rpm e dpkg. Entenda o gerenciamento direto de arquivos .deb e .rpm no Linux."
meta_keywords: "rpm, dpkg, gerenciamento de pacotes Linux, .deb, .rpm, tutorial Linux, guia para iniciantes, instalar pacotes"
---

`dpkg` é a ferramenta de pacotes de baixo nível dos sistemas da família Debian, enquanto `rpm` desempenha função semelhante nos sistemas da família RPM. Elas desempacotam arquivos nativos, executam ações do ciclo de vida dos pacotes e atualizam os bancos de dados de pacotes instalados. Ferramentas que conhecem repositórios, como APT e DNF, utilizam esses mecanismos de baixo nível.

## Inspeção de um Arquivo Antes da Instalação

Um arquivo de pacote não equivale a um único executável. Ele pode conter muitos arquivos de carga útil, metadados, tratamento de configurações e scripts privilegiados do ciclo de vida. Antes da instalação, inspecione sua origem, a assinatura ou o caminho de download autenticado, os metadados e o conteúdo.

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

O `p` nas formas de consulta do RPM exibidas significa “consultar um arquivo de pacote”, e não o banco de dados instalado. A saída da consulta ajuda a examinar um pacote, mas não comprova que seus scripts ou programas sejam seguros.

:::single-choice{#package-install-tools-native-format}
Qual ferramenta de baixo nível gerencia os pacotes `.deb` do Debian e seu banco de dados instalado?

::option[`rpm`]{#package-install-tools-rpm-debian explanation="O RPM gerencia seu próprio formato nativo e banco de dados nos sistemas da família RPM."}
::option[`tar`]{#package-install-tools-tar-debian explanation="O tar pode ler arquivos de arquivamento, mas não implementa o ciclo de vida dos pacotes Debian instalados."}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="Os sistemas da família Debian usam `dpkg` para operações de baixo nível com arquivos `.deb` e o banco de dados de pacotes."}
:::

## Instalação de um Arquivo Local

A instalação direta de baixo nível usa:

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i` pode desempacotar e configurar o arquivo solicitado, mas não obtém dependências ausentes nos repositórios. De modo semelhante, o uso direto de `rpm` não oferece o fluxo de trabalho normal do resolvedor de repositórios. Em geral, um comando de nível mais alto é preferível para um arquivo local, pois pode resolver dependências usando as fontes configuradas:

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

Examine a transação antes de confirmá-la. No APT, o prefixo `./` diferencia o caminho de um arquivo Debian local do nome de um pacote do repositório.

:::single-choice{#package-install-tools-local-dependencies}
Qual comando exibido pode instalar um arquivo `.deb` local e resolver as dependências disponíveis nos repositórios?

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l` lista as seleções de pacotes instalados e não é o fluxo de instalação local que resolve dependências."}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="A sintaxe de consulta do RPM não instala um arquivo Debian."}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="O APT reconhece o caminho local explícito e pode usar os repositórios configurados para satisfazer as dependências declaradas."}
:::

## Remoção de um Pacote Instalado

A remoção recebe o nome de um pacote instalado, não o nome do arquivo usado anteriormente:

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

No Debian, `--remove` normalmente preserva os arquivos de configuração classificados como conffiles; `--purge` também solicita a remoção deles, sujeita aos scripts do pacote e aos dados não gerenciados. Nenhum dos comandos garante a exclusão de dados criados pelo usuário. Em geral, `apt remove` ou `dnf remove` é uma opção melhor, pois pode avaliar os pacotes relacionados e apresentar a transação completa.

:::single-choice{#package-install-tools-remove-operand}
Que operando `dpkg --remove` espera para um pacote instalado?

::option[A URL do índice do repositório.]{#package-install-tools-remove-url explanation="O local do repositório não é a identidade do pacote fornecida para uma remoção de baixo nível."}
::option[O nome do pacote instalado.]{#package-install-tools-remove-name .correct explanation="A remoção usa o registro do pacote, como `example`, e não exige o caminho do antigo arquivo `.deb`."}
::option[O PID de um processo iniciado pelo pacote.]{#package-install-tools-remove-pid explanation="IDs de processos não têm relação com a chave do banco de dados de pacotes instalados."}
:::

## Consulta do Estado Instalado

Liste os registros de pacotes instalados ou conhecidos com:

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

Para uma inspeção direcionada, prefira um nome de pacote específico e um formato legível por máquina quando a confiabilidade de um script for importante. Os bancos de dados de pacotes descrevem o estado gerenciado, mas administradores locais ou aplicativos ainda podem modificar arquivos posteriormente; use os recursos de verificação quando precisar comparar os arquivos instalados com os metadados registrados.

:::single-choice{#package-install-tools-rpm-list-installed}
Qual comando consulta todos os pacotes registrados como instalados no banco de dados RPM?

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q` seleciona o modo de consulta e `-a` o amplia para todos os registros de pacotes instalados."}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e` solicita a remoção de um pacote, não uma listagem somente para leitura."}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="Esse comando inspeciona a carga útil de um arquivo Debian, não o banco de dados RPM instalado."}
:::

Use [Gerenciamento de Pacotes com RPM](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868) para praticar consultas de arquivos e verificações de integridade em um sistema isolado.

## Resumo

Agora você sabe diferenciar operações de baixo nível com pacotes de transações com repositórios.

1. Inspecione os metadados e o conteúdo de arquivos locais antes da instalação.
2. Use `dpkg` para operações de baixo nível com `.deb` e `rpm` para `.rpm`.
3. Prefira APT ou DNF quando for necessário resolver dependências.
4. Remova pelo nome do pacote instalado e verifique separadamente o estado gerenciado.
