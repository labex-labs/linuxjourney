---
lesson_id: "compile-source-code"
course_id: "packages"
lang: "pt"
order_index: 7
title: "Compilação de Código-fonte"
description: "Aprenda a verificar, configurar, compilar, testar, preparar e acompanhar software compilado a partir do código-fonte."
meta_title: "Compilação de Código-fonte - Pacotes"
meta_description: "Aprenda a compilar código-fonte no Linux. Este guia aborda verificação, configuração, compilação, testes e instalação controlada com ferramentas como configure e make."
meta_keywords: "como compilar código-fonte, como construir código-fonte, compilar código-fonte, make install, checkinstall, compilação Linux, build-essential, script configure, makefile, tutorial Linux"
---

Compilar a partir do código-fonte pode fornecer uma versão ou um recurso indisponível nos repositórios configurados, mas transfere da distribuição para você o trabalho de integração, atualização e confiança. Prefira um pacote compatível da distribuição quando ele atender à necessidade.

## Verificação e Leitura Antes da Compilação

Obtenha o código-fonte por um canal de versões autenticado do projeto original. Verifique sua assinatura ou soma de verificação por um caminho confiável e inspecione o arquivo antes de extraí-lo em um diretório de preparação sem privilégios. Leia arquivos como `README`, `INSTALL`, `SECURITY` e a documentação de compilação do projeto.

As instruções de compilação são código executável. Um script `configure`, uma definição de compilação, um teste ou um plugin do compilador pode executar comandos arbitrários como seu usuário. Não compile código-fonte não confiável e não execute a compilação com `sudo`.

:::single-choice{#compile-source-code-build-privilege}
Por que a etapa de compilação normalmente deve ser executada sem `sudo`?

::option[Porque os compiladores se recusam a produzir código de máquina para o usuário root.]{#compile-source-code-root-compiler explanation="Os compiladores podem ser executados como root, mas isso aumenta o risco desnecessariamente."}
::option[Porque `sudo` exclui automaticamente todos os arquivos-objeto gerados.]{#compile-source-code-sudo-delete explanation="A elevação de privilégios não remove por si só os resultados da compilação."}
::option[Porque a lógica de compilação pode executar comandos arbitrários e normalmente não precisa de privilégios do sistema.]{#compile-source-code-unprivileged-build .correct explanation="Manter a compilação sem privilégios limita os danos causados por erros ou instruções maliciosas."}
:::

## Instalação dos Requisitos de Compilação

Em um sistema de desenvolvimento da família Debian, um ponto de partida comum é:

```bash
$ sudo apt install build-essential
```

Esse comando instala um compilador básico e ferramentas de compilação, mas não todas as dependências exigidas por todos os projetos. Um projeto também pode precisar de ambientes de execução de linguagens, geradores, ferramentas do sistema de compilação, cabeçalhos de desenvolvimento ou versões exatas de bibliotecas. Instale os requisitos a partir de repositórios confiáveis e diferencie as dependências de compilação das dependências de execução.

:::single-choice{#compile-source-code-build-essential-scope}
O que `build-essential` fornece em um sistema da família Debian?

::option[Um conjunto básico de ferramentas comuns de compilação e construção.]{#compile-source-code-baseline-tools .correct explanation="Ele fornece ferramentas fundamentais, mas não pode prever todas as bibliotecas ou os geradores específicos de cada projeto."}
::option[Todas as dependências de todos os projetos de código-fonte.]{#compile-source-code-all-dependencies explanation="Cada projeto declara requisitos adicionais e, às vezes, versões específicas."}
::option[Uma garantia de que o código-fonte baixado é confiável.]{#compile-source-code-trust-guarantee explanation="A instalação das ferramentas não autentica uma versão de código-fonte obtida separadamente."}
:::

## Configuração e Compilação

Um projeto tradicional no estilo Autoconf usa:

```bash
$ ./configure --prefix=/usr/local
$ make
```

`configure` verifica o ambiente e gera arquivos de compilação de acordo com as opções selecionadas. `make` lê regras de dependências e comandos, normalmente em um `Makefile`, e cria os alvos solicitados.

Essa sequência não é universal. Os projetos podem usar CMake, Meson, Ninja, ferramentas específicas de uma linguagem ou scripts personalizados. Siga a documentação da versão exata, em vez de executar `./configure` apenas por familiaridade. Quando o sistema de compilação permitir, um diretório de compilação separado da árvore de código pode manter os arquivos gerados isolados.

:::single-choice{#compile-source-code-make-role}
No fluxo de trabalho tradicional, o que `make` faz?

::option[Registra todos os resultados no banco de dados de pacotes da distribuição.]{#compile-source-code-make-package-db explanation="A compilação por si só não cria registros de propriedade em um pacote nativo."}
::option[Baixa automaticamente uma versão autenticada do código-fonte.]{#compile-source-code-make-download explanation="A obtenção e a verificação do código ocorrem antes da compilação local, salvo se o projeto definir explicitamente o contrário."}
::option[Executa as regras aplicáveis da descrição de compilação.]{#compile-source-code-make-rules .correct explanation="O make avalia as dependências e executa os comandos necessários para atualizar os alvos selecionados."}
:::

## Testes Antes da Instalação

Execute o alvo de testes documentado pelo projeto, por exemplo:

```bash
$ make check
```

O alvo real pode ser `test`, `check` ou um comando separado. Investigue as falhas em vez de instalar um resultado não testado. Os testes podem exigir acesso à rede, serviços, hardware especial ou isolamento; examine-os antes da execução, assim como faria com qualquer outro código de compilação.

:::single-choice{#compile-source-code-test-failure}
O que você deve fazer quando a suíte de testes documentada falhar?

::option[Executar imediatamente a mesma instalação como root.]{#compile-source-code-install-after-failure explanation="Privilégios não resolvem uma falha desconhecida de correção e ainda aumentam suas consequências."}
::option[Excluir o banco de dados do gerenciador de pacotes para evitar conflitos.]{#compile-source-code-delete-database explanation="O banco de dados nativo não tem relação com a resolução da falha em um teste do código-fonte e não deve ser descartado."}
::option[Investigar a falha antes de instalar a compilação.]{#compile-source-code-investigate-tests .correct explanation="Um teste com falha pode revelar dependências incompatíveis, defeitos na compilação ou suposições sobre o ambiente."}
:::

## Preparação e Acompanhamento da Instalação

`sudo make install` pode copiar arquivos diretamente para prefixos do sistema sem registrá-los no banco de dados de pacotes nativo. Alvos de desinstalação são opcionais e podem ser incompletos, enquanto atualizações posteriores podem sobrescrever arquivos ou deixá-los órfãos.

Prefira uma destas abordagens controladas:

- crie um pacote nativo oficial usando as ferramentas de empacotamento da distribuição
- instale sob um prefixo claramente separado, como `/usr/local`, quando a política permitir
- prepare os arquivos em uma raiz temporária de empacotamento com um mecanismo compatível, como `DESTDIR`
- use um prefixo de usuário sem privilégios, um ambiente isolado ou um contêiner, quando apropriado

`checkinstall` pode criar um pacote simples para alguns fluxos com `make install`, mas não é universal e não substitui uma receita de pacote com qualidade de distribuição devidamente revisada. Nunca o trate como uma regra obrigatória. Antes de qualquer cópia com privilégios, inspecione a lista de arquivos preparados, seus proprietários, permissões e caminhos, além do plano de desinstalação ou atualização.

:::single-choice{#compile-source-code-destdir-purpose}
Qual é a finalidade de uma instalação de preparação compatível com `DESTDIR`?

::option[Colocar os arquivos destinados à instalação sob uma raiz temporária para inspeção ou empacotamento.]{#compile-source-code-stage-root .correct explanation="A preparação separa a coleta dos arquivos da gravação imediata no prefixo do sistema em uso."}
::option[Transformar o compilador em um repositório remoto de pacotes.]{#compile-source-code-destdir-repository explanation="A variável redireciona os caminhos de instalação e não publica metadados de repositório."}
::option[Pular a compilação e baixar binários desconhecidos.]{#compile-source-code-destdir-download explanation="A preparação ocorre depois da compilação e não a substitui por um download binário externo."}
:::

Use [Compilar Software a Partir do Código-fonte no Linux](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853) em um ambiente descartável para praticar o fluxo sem misturar arquivos experimentais em um sistema de produção.

## Resumo

Agora você sabe tratar a compilação de código-fonte como um fluxo controlado de fornecimento de software.

1. Autentique o código-fonte e examine suas instruções como código executável.
2. Instale os requisitos explícitos de compilação a partir de repositórios confiáveis.
3. Configure, compile e teste sem privilégios desnecessários.
4. Prepare e inspecione os resultados antes da instalação no sistema.
5. Acompanhe os arquivos instalados por meio de empacotamento nativo ou de um prefixo isolado intencional.
