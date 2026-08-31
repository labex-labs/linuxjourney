---
lesson_id: "package-repositories"
course_id: "packages"
lang: "pt"
order_index: 2
title: "Repositórios de Pacotes"
description: "Aprenda como os repositórios publicam índices de pacotes assinados e como o APT encontra as fontes configuradas em sistemas da família Debian."
meta_title: "Repositórios de Pacotes - Pacotes"
meta_description: "Explore os repositórios de pacotes Linux e seu papel no gerenciamento de pacotes. Aprenda como o sistema usa fontes como /etc/apt/sources.list para localizar e instalar pacotes."
meta_keywords: "repositórios de pacotes Linux, fontes do apt, /etc/apt/sources.list, pacotes Linux, Linux para iniciantes, tutorial Linux, gerenciamento de pacotes"
---

Um repositório de pacotes publica pacotes junto com índices e metadados de versão. Um gerenciador de pacotes baixa esses índices, seleciona versões compatíveis com a distribuição e a arquitetura configuradas, verifica a autenticação do repositório e obtém os arquivos de pacote necessários.

## Metadados do Repositório e Catálogos Locais

Um repositório é mais do que um diretório de arquivos compactados. Seus metadados descrevem os nomes, as versões e as arquiteturas dos pacotes disponíveis, além de somas de verificação, dependências e seções do repositório. O cliente mantém um catálogo local em cache para pesquisar e resolver pacotes sem precisar baixar todos os arquivos primeiro.

Em um sistema da família Debian, atualize os metadados das fontes configuradas com:

```bash
$ sudo apt update
```

Esse comando atualiza os índices de pacotes locais; por si só, ele não instala todas as atualizações disponíveis. Examine as fontes e os erros de autenticação informados, em vez de ignorar entradas que falharam.

:::single-choice{#package-repositories-apt-update}
O que o comando `apt update` atualiza principalmente?

::option[Todos os binários de pacotes instalados sem solicitar confirmação.]{#package-repositories-all-binaries explanation="A instalação de atualizações é uma operação separada da atualização dos metadados."}
::option[As senhas dos usuários autorizados a instalar pacotes.]{#package-repositories-user-passwords explanation="A atualização dos índices do repositório não altera as credenciais de autenticação locais."}
::option[Os índices locais que descrevem os pacotes disponíveis nas fontes configuradas.]{#package-repositories-local-indexes .correct explanation="O APT baixa os metadados atuais dos repositórios para que pesquisas e resoluções de dependências posteriores usem um catálogo atualizado."}
:::

## Configuração de Fontes do APT

O APT lê as fontes configuradas em:

- `/etc/apt/sources.list`
- arquivos terminados em `.list` ou `.sources` dentro de `/etc/apt/sources.list.d/`

A extensão `.list` usa o formato tradicional de uma linha. A extensão `.sources` usa blocos no estilo deb822, recomendados pela documentação atual do APT para novas configurações. Uma distribuição pode colocar suas fontes padrão em qualquer um desses locais; portanto, `/etc/apt/sources.list` não necessariamente contém a configuração completa ou principal.

Uma fonte no estilo deb822 pode se parecer com:

```text
Types: deb
URIs: https://deb.example.invalid/repository
Suites: stable
Components: main
Signed-By: /etc/apt/keyrings/example.gpg
```

Esse exemplo serve apenas para ilustrar a sintaxe; o domínio reservado `.invalid` não corresponde a um repositório utilizável.

:::single-choice{#package-repositories-apt-locations}
Onde o APT pode ler definições de repositórios ativos?

::option[Apenas em `/etc/apt/sources.list`.]{#package-repositories-only-main-list explanation="O APT também lê arquivos de fontes compatíveis em `/etc/apt/sources.list.d/`."}
::option[Apenas em arquivos dentro do diretório pessoal de cada usuário.]{#package-repositories-only-home explanation="A configuração das fontes do APT no sistema normalmente fica sob `/etc/apt`."}
::option[Em `/etc/apt/sources.list` e nos arquivos compatíveis em `/etc/apt/sources.list.d/`.]{#package-repositories-both-locations .correct explanation="O APT combina o arquivo principal com as definições `.list` e `.sources` do diretório de listas de fontes."}
:::

## Autenticação de Repositórios

O APT verifica os metadados de versão assinados do repositório e, em seguida, confere os arquivos de pacote baixados usando as somas de verificação autenticadas nesses metadados. O campo `Signed-By` pode restringir uma fonte a um chaveiro específico, em vez de confiar em todas as chaves configuradas globalmente para esse repositório.

Uma assinatura válida comprova que os metadados vieram do detentor de uma chave de assinatura aceita e não foram modificados sem que isso fosse detectado. Ela não comprova que o software do publicador esteja livre de defeitos, não seja malicioso ou seja adequado ao sistema. Confirme a impressão digital da chave e as instruções da fonte por meio de um canal confiável independente.

:::single-choice{#package-repositories-signed-by}
Qual é a finalidade de segurança de `Signed-By` em uma definição de fonte do APT?

::option[Criptografar todos os pacotes instalados para que nem o root possa lê-los.]{#package-repositories-package-encryption explanation="A assinatura do repositório verifica origem e integridade; ela não oculta os dados do administrador local."}
::option[Restringir essa fonte a determinadas chaves de assinatura.]{#package-repositories-key-scope .correct explanation="O campo vincula a verificação do repositório ao material dos chaveiros selecionados, em vez de usar um conjunto global irrestrito de chaves."}
::option[Garantir que o repositório não contenha software vulnerável.]{#package-repositories-no-vulnerabilities explanation="A autenticidade criptográfica não avalia a qualidade do software nem seus defeitos de segurança."}
:::

## Adição Cuidadosa de Fontes de Terceiros

Um repositório pode instalar pacotes e scripts de ciclo de vida com privilégios do sistema; portanto, adicioná-lo amplia o limite de confiança de software do sistema. Antes de fazer isso:

1. Prefira o repositório da distribuição quando ele atender à necessidade.
2. Confirme o publicador, a versão compatível, a arquitetura e a impressão digital da chave de assinatura.
3. Use um arquivo de fonte dedicado e um chaveiro com escopo restrito.
4. Examine os nomes dos pacotes e as alterações de dependências antes da instalação.
5. Documente como desativar a fonte e migrar ou remover seus pacotes.

Não copie instruções obsoletas que desativem a verificação de assinaturas nem envie um script remoto não auditado diretamente para um shell privilegiado.

:::single-choice{#package-repositories-third-party-risk}
Por que adicionar um repositório de terceiros amplia o limite de confiança do sistema?

::option[Porque seus pacotes e scripts autenticados podem ser instalados com privilégios do sistema.]{#package-repositories-privileged-install .correct explanation="Confiar na fonte de assinatura pode autorizar código e ações de ciclo de vida que afetam o sistema operacional."}
::option[Porque ele faz o kernel do Linux deixar de aplicar permissões de arquivos.]{#package-repositories-disable-permissions explanation="A configuração de repositórios não desativa os mecanismos normais de controle de acesso do kernel."}
::option[Porque ele converte todos os pacotes nativos em arquivos de código-fonte.]{#package-repositories-convert-source explanation="Adicionar um repositório altera as fontes de pacotes disponíveis, não o formato fundamental dos pacotes existentes."}
:::

Pratique a instalação por repositórios em [Instalação de Software no Linux](https://labex.io/labs/linux-software-installation-on-linux-18005) ou compare o fluxo de trabalho da família Red Hat em [Consultar e Atualizar Pacotes com o YUM](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869). Para consultar a sintaxe exata do APT, use o manual local `sources.list(5)`.

## Resumo

Agora você sabe explicar como um repositório configurado se transforma em metadados de pacotes confiáveis.

1. Diferencie os índices do repositório dos arquivos de pacote.
2. Use `apt update` para atualizar o catálogo local.
3. Localize as definições de fontes do APT nos formatos de uma linha e deb822.
4. Restrinja o escopo das chaves de assinatura e avalie conscientemente a confiança em terceiros.
