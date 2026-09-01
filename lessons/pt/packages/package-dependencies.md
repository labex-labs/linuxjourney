---
lesson_id: "package-dependencies"
course_id: "packages"
lang: "pt"
order_index: 4
title: "Dependências de Pacotes"
description: "Aprenda como os metadados dos pacotes expressam recursos, versões, conflitos e relações com bibliotecas compartilhadas."
meta_title: "Dependências de Pacotes - Pacotes"
meta_description: "Aprenda sobre dependências de pacotes no Linux e sua importância para a instalação de software. Entenda bibliotecas compartilhadas e como o gerenciamento de pacotes evita programas quebrados."
meta_keywords: "dependências de pacotes Linux, bibliotecas compartilhadas, pacotes Linux, gerenciamento de pacotes, instalação de software Linux, tutorial Linux, Linux para iniciantes"
---

Uma dependência de pacote declara que um pacote precisa de outro pacote, recurso ou versão compatível para ser instalado ou funcionar. Gerenciadores de pacotes que conhecem os repositórios usam esses metadados para calcular um conjunto coerente de alterações, em vez de tratar cada arquivo de pacote isoladamente.

## Relações de Dependência

Os metadados de um pacote podem expressar mais do que um simples nome obrigatório. Dependendo do formato da distribuição, as relações podem incluir:

- dependências obrigatórias
- restrições de versão mínima, máxima ou exata
- alternativas, nas quais qualquer um entre vários provedores satisfaz um requisito
- recomendações ou sugestões com semântica menos rigorosa
- conflitos, incompatibilidades ou substituições
- recursos virtuais fornecidos por mais de um pacote

Essas regras permitem que um resolvedor escolha um conjunto de versões de pacotes compatível com os repositórios configurados, a arquitetura e o estado instalado. Uma solução pode exigir atualizações, remoções ou a escolha entre provedores; por isso, examine a transação proposta antes de aprová-la.

:::single-choice{#package-dependencies-solver-role} O que um resolvedor de dependências que conhece os repositórios procura produzir?

::option[Um conjunto coerente de versões de pacotes e alterações necessárias.]{#package-dependencies-consistent-set .correct explanation="O resolvedor avalia as relações declaradas entre os pacotes instalados e disponíveis."}
::option[Uma nova conta de usuário para cada aplicativo instalado.]{#package-dependencies-user-account explanation="A criação de contas pode ser uma ação do ciclo de vida de um pacote, mas não é a finalidade da resolução de dependências."}
::option[Uma cópia compactada de todos os arquivos do repositório.]{#package-dependencies-compressed-repository explanation="O resolvedor seleciona metadados e pacotes; ele não arquiva o repositório inteiro."}
:::

## Bibliotecas Compartilhadas como Dependências

Uma biblioteca compartilhada contém código compilado que vários programas podem mapear durante a execução. O compartilhamento reduz implementações duplicadas e permite que as distribuições atualizem uma biblioteca comum de forma independente, mas os programas dependem de uma interface binária de aplicação, ou ABI, compatível.

Em sistemas Linux baseados em ELF, um executável pode registrar o nome de uma biblioteca necessária, como um SONAME. O vinculador dinâmico localiza uma biblioteca instalada correspondente quando o programa é iniciado. Em geral, os metadados do pacote representam esse requisito como uma dependência do pacote ou recurso que fornece a biblioteca compatível.

:::single-choice{#package-dependencies-shared-library} O que é uma biblioteca compartilhada?

::option[Código compilado que vários programas podem carregar e usar.]{#package-dependencies-library-code .correct explanation="Uma biblioteca compartilhada fornece interfaces binárias reutilizáveis, em vez de incorporar uma implementação separada em cada programa."}
::option[Uma lista de repositórios compartilhada entre distribuições não relacionadas.]{#package-dependencies-shared-repository explanation="A configuração de repositórios e o código de bibliotecas executáveis são conceitos diferentes."}
::option[Um arquivo de texto que contém o histórico do shell de todos os usuários.]{#package-dependencies-shared-history explanation="O histórico do shell é um dado do usuário, não uma dependência de biblioteca de um programa."}
:::

## Compatibilidade de Versão e ABI

A existência de um arquivo com nome semelhante ao da biblioteca não é suficiente. A ABI exigida, a arquitetura, os símbolos e, em alguns casos, a versão mínima precisam corresponder. Substituir manualmente uma biblioteca da distribuição pode quebrar todos os programas que dependem dela, mesmo que o nome do arquivo pareça correto.

Os mantenedores de pacotes codificam as relações entre bibliotecas e coordenam as transições quando uma ABI muda. Mantenha as bibliotecas nativas sob o controle do gerenciador de pacotes; para software que precise de uma versão incompatível, use mecanismos compatíveis de instalação paralela, contêiner, ambiente ou compilação.

:::single-choice{#package-dependencies-filename-insufficient} Por que um programa ainda pode falhar quando existe um arquivo de biblioteca com nome semelhante?

::option[Porque o Linux permite que apenas um executável use cada biblioteca.]{#package-dependencies-one-consumer explanation="Uma das finalidades essenciais das bibliotecas compartilhadas é atender a vários processos e programas."}
::option[Porque as dependências de pacotes só se aplicam antes da primeira inicialização do sistema.]{#package-dependencies-boot-only explanation="As dependências continuam relevantes durante instalações, atualizações e execução."}
::option[Porque a ABI ou a arquitetura da biblioteca pode não atender ao programa.]{#package-dependencies-abi-mismatch .correct explanation="A vinculação em tempo de execução depende de interfaces binárias e arquitetura de máquina compatíveis, não apenas de um nome de arquivo."}
:::

## Estados de Dependência Quebrada

Um problema de dependência pode surgir de repositórios misturados, operações interrompidas, arquivos de pacote instalados manualmente, versões retidas, arquivos removidos ou software de terceiros incompatível. Não tente resolvê-lo excluindo arquivos do banco de dados de pacotes nem forçando cegamente uma instalação.

Primeiro, leia os diagnósticos do gerenciador de pacotes, atualize apenas os metadados de repositórios confiáveis, inspecione versões retidas ou fixadas e examine o reparo proposto. Um instalador de baixo nível pode desempacotar um arquivo sem obter todas as dependências; uma ferramenta de repositório de nível mais alto costuma ser mais segura para instalações comuns, pois resolve a transação completa.

:::single-choice{#package-dependencies-low-level-limit} Qual é uma limitação comum de instalar um pacote local com uma ferramenta de baixo nível para arquivos de pacote?

::option[Ela pode não obter nem resolver todas as dependências ausentes nos repositórios.]{#package-dependencies-no-repository-resolution .correct explanation="As ferramentas de baixo nível gerenciam arquivos e bancos de dados de pacotes, mas podem deixar a obtenção de dependências para um gerenciador de nível mais alto."}
::option[Ela sempre recompila o kernel do Linux a partir do código-fonte.]{#package-dependencies-recompile-kernel explanation="Instalar um arquivo de pacote não implica recompilar o kernel."}
::option[Ela impede que o pacote contenha bibliotecas compartilhadas.]{#package-dependencies-no-libraries explanation="Um arquivo de pacote pode conter bibliotecas independentemente da ferramenta usada para instalá-lo."}
:::

Use [Gerenciar Bibliotecas Compartilhadas no Linux](https://labex.io/labs/comptia-manage-shared-libraries-in-linux-590867) para inspecionar relações em tempo de execução e depois compare-as com os metadados de pacotes em [Gerenciamento de Pacotes com RPM](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868).

## Resumo

Agora você sabe explicar como funciona a resolução de dependências de pacotes.

1. Reconheça relações obrigatórias, alternativas, versionadas e conflitantes.
2. Relacione pacotes de bibliotecas compartilhadas aos requisitos de ABI em tempo de execução.
3. Considere nomes de arquivos uma evidência mais fraca do que a compatibilidade de arquitetura e interface.
4. Examine a transação completa do gerenciador de pacotes antes de aplicar reparos.
