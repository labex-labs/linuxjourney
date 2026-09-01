---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "pt"
order_index: 6
title: "yum e apt"
description: "Aprenda os fluxos de trabalho do APT e do DNF para inspecionar, instalar, remover e atualizar pacotes por meio de repositórios."
meta_title: "yum e apt - Pacotes"
meta_description: "Explore as principais diferenças entre yum e apt. Aprenda a instalar, remover e atualizar pacotes em sistemas Linux das famílias RPM e Debian."
meta_keywords: "yum vs apt, yum apt, gerenciamento de pacotes Linux, apt, yum, dnf, Debian, Red Hat, instalar pacotes, atualizar pacotes"
---

Gerenciadores de pacotes que conhecem repositórios obtêm metadados, resolvem dependências, verificam conteúdo autenticado e coordenam transações. Os sistemas da família Debian normalmente usam APT. As versões atuais do Fedora e do Red Hat Enterprise Linux usam DNF; no RHEL atual, o comando `yum` continua disponível como um alias de compatibilidade para o DNF, enquanto sistemas mais antigos usavam a implementação YUM original.

Sempre siga a documentação da distribuição e da versão instaladas, em vez de presumir que um conjunto de comandos se aplica a todos os sistemas.

## Atualização e Inspeção de Metadados

O APT separa a atualização dos metadados da atualização dos pacotes:

```bash
Debian family: $ sudo apt update
```

Pesquise e inspecione antes de instalar:

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

A configuração dos repositórios determina o que esses comandos conseguem encontrar. Leia atentamente os nomes das fontes, as arquiteturas, as versões e os erros de assinatura.

:::single-choice{#package-management-systems-apt-show} Qual comando exibe os detalhes do pacote `package-name` no APT?

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="O subcomando `remove` propõe a desinstalação do pacote."}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="Esse comando pesquisa nos repositórios da família RPM e não é o comando de detalhes do APT."}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="O subcomando `show` apresenta os metadados do pacote binário indicado."}
:::

## Instalação de Pacotes

Instale pelo nome do pacote no repositório com:

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

O gerenciador propõe as dependências e quaisquer conflitos ou substituições. Não confirme automaticamente antes de examinar a origem, a versão e a arquitetura do pacote, o tamanho do download, a alteração no espaço em disco, as remoções e as novas dependências que serão instaladas.

:::single-choice{#package-management-systems-dnf-install} Qual comando atual instala `package-name` usando os repositórios configurados da família RPM?

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="Essa é uma consulta ao banco de dados de pacotes RPM instalados, não uma solicitação de instalação por repositório."}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="O DNF é o gerenciador atual que conhece repositórios no Fedora e nas versões recentes do RHEL."}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update atualiza os índices e não instala um pacote nomeado da família RPM."}
:::

## Remoção de Pacotes

Solicite a remoção com:

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

A remoção pode afetar pacotes dependentes ou deixar dependências e configurações que deixaram de ser usadas. Examine a transação proposta, diferencie a semântica de remoção da de expurgo nos sistemas da família Debian e preserve os dados do aplicativo de acordo com seu próprio procedimento de backup e retenção. A remoção de um pacote não garante a exclusão dos dados criados pelo usuário.

:::single-choice{#package-management-systems-remove-review} Por que você deve examinar uma transação de remoção antes de confirmá-la?

::option[Porque a remoção sempre reformata o sistema de arquivos que contém o pacote.]{#package-management-systems-removal-format explanation="Os gerenciadores removem arquivos e estados gerenciados; normalmente, eles não formatam sistemas de arquivos."}
::option[Porque os gerenciadores de pacotes não conseguem exibir o conjunto de alterações proposto.]{#package-management-systems-no-proposal explanation="Gerenciadores interativos normalmente exibem a transação planejada justamente para permitir sua análise."}
::option[Porque outros pacotes podem depender do pacote selecionado e também ser afetados.]{#package-management-systems-dependent-removal .correct explanation="As restrições de dependência podem ampliar uma solicitação para além do único nome de pacote informado inicialmente."}
:::

## Aplicação de Atualizações

Em um sistema com APT, atualize os metadados e depois examine as atualizações como etapas separadas, ambas bem-sucedidas:

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

Em um sistema com DNF, inspecione e aplique as atualizações disponíveis usando o fluxo de trabalho documentado localmente:

```bash
$ dnf check-update
$ sudo dnf upgrade
```

Um comando de atualização pode alterar bibliotecas essenciais, serviços, kernels e dependências. Use backups, políticas de manutenção, notas de versão e planejamento de reinicializações de serviços ou do sistema adequados ao ambiente. Verifique a semântica do status de saída: por exemplo, algumas operações de “verificação de atualizações” usam um status diferente de zero para informar que há atualizações disponíveis, e não que ocorreu uma falha de execução.

:::single-choice{#package-management-systems-apt-update-upgrade} Qual é a relação entre `apt update` e `apt upgrade`?

::option[`update` remove pacotes; `upgrade` restaura seus arquivos de configuração.]{#package-management-systems-apt-remove-restore explanation="Nenhum desses comandos possui essa relação de remoção e restauração."}
::option[`update` atualiza os metadados; `upgrade` aplica um plano aprovado de atualização de pacotes.]{#package-management-systems-apt-two-steps .correct explanation="O APT separa a atualização do catálogo da instalação de versões mais recentes dos pacotes."}
::option[Os dois são nomes idênticos para uma única operação.]{#package-management-systems-apt-identical explanation="Eles realizam etapas distintas e devem ser verificados separadamente."}
:::

## Escolha entre `dnf` e `yum`

Use `dnf` na documentação atual do Fedora e do RHEL. Em um sistema RHEL recente, o comando `yum` pode invocar o comportamento de compatibilidade do DNF, mas scripts não devem deduzir a implementação apenas pelo nome do executável. Em máquinas legadas, verifique a versão instalada e a sintaxe compatível antes de adaptar instruções.

:::single-choice{#package-management-systems-yum-current-rhel} O que `yum` normalmente representa em um sistema RHEL atual?

::option[Um comando de compatibilidade fornecido pelo DNF.]{#package-management-systems-yum-dnf-alias .correct explanation="As versões recentes do RHEL usam DNF, mas preservam o nome do comando yum para compatibilidade."}
::option[A ferramenta Debian de baixo nível para arquivos `.deb`.]{#package-management-systems-yum-dpkg explanation="Os sistemas Debian usam ferramentas como APT e dpkg, não YUM, para o gerenciamento de pacotes nativos."}
::option[Um compactador exclusivo para metadados de repositórios.]{#package-management-systems-yum-compressor explanation="YUM e DNF são interfaces de gerenciamento de pacotes, não formatos independentes de compactação."}
:::

Pratique o APT em [Instalação e Remoção de Pacotes](https://labex.io/labs/linux-installing-and-removing-packages-385380) e os conceitos da família DNF/YUM em [Consulta e Atualização de Pacotes com YUM](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869).

## Resumo

Agora você sabe escolher e examinar operações comuns com pacotes de repositórios.

1. Use APT em sistemas da família Debian e DNF em sistemas atuais da família RPM.
2. Inspecione os metadados e as alterações de dependências propostas antes da instalação.
3. Trate a remoção como uma transação que considera dependências, não como a exclusão de um único arquivo.
4. Separe a atualização dos metadados da aplicação de atualizações quando a ferramenta fizer essa distinção.
5. Verifique se `yum` é o YUM legado ou um comando de compatibilidade do DNF.
