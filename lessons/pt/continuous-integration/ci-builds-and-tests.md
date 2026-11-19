---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "pt"
order_index: 4
title: "Builds e testes"
description: "Aprenda a distinguir preparação, build e testes com uma pequena verificação local de uma página."
meta_title: "Builds e testes - Integração contínua"
meta_description: "Aprenda a distinguir preparação, build e testes com uma pequena verificação local de uma página."
meta_keywords: "builds, testes, código de saída, integração contínua, DevOps, Linux Journey"
---

Fica mais fácil interpretar uma falha quando cada etapa tem uma função. A **preparação** disponibiliza arquivos de entrada e ferramentas. O **build** gera uma saída. Um **teste** confere se o código-fonte ou a saída atende a uma condição.

## Como preparar a entrada

Crie uma página de exemplo em uma pasta de prática vazia. O redirecionamento sobrescreve `index.html` se o arquivo já existir. Por isso, use um diretório de prática novo.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

Em um job de CI, o checkout forneceria a página. Alguns projetos também instalam dependências, que são as bibliotecas ou ferramentas necessárias para executar o build ou os testes.

:::single-choice{#ci-builds-and-tests-prepare-input} A página já está ausente antes do comando que deveria copiá-la. Que etapa você deve investigar primeiro?

::option[O download do artefato em um job posterior.]{#ci-builds-and-tests-prepare-input-a explanation="O arquivo de entrada é necessário antes de gerar a saída."}
::option[A preparação.]{#ci-builds-and-tests-prepare-input-b .correct explanation="O arquivo de entrada deveria estar disponível neste job."}
::option[O tempo de resposta em produção.]{#ci-builds-and-tests-prepare-input-c explanation="A situação envolve arquivos no runner."}
:::

## Como gerar a saída do build

Copie a página para o diretório que vai conter o site pronto.

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

Com a opção `-p`, `mkdir` funciona mesmo se o diretório já existir. A cópia cria um arquivo separado no diretório de saída. Os testes seguintes podem conferir esse resultado.

:::single-choice{#ci-builds-and-tests-build-product} Qual arquivo está pronto para entrar no pacote depois que a cópia dá certo?

::option[dist/index.html.]{#ci-builds-and-tests-build-product-a .correct explanation="O build colocou uma cópia no diretório de saída."}
::option[Uma página implantada no site público.]{#ci-builds-and-tests-build-product-b explanation="Copiar o arquivo localmente não inicia um serviço."}
::option[Um registro da situação do fluxo.]{#ci-builds-and-tests-build-product-c explanation="Neste exemplo, o build produz uma página. O runner acompanha o estado da verificação separadamente."}
:::

## Como testar a página

Execute a verificação logo após o build. A opção `-F` procura o texto literal, e `-q` evita que as linhas correspondentes apareçam. O shell guarda o código de saída do último comando em `$?`. Zero indica que o texto foi encontrado. Um indica que não houve nenhuma linha correspondente.

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

A saída esperada é `0`. O teste procurou o texto exato no arquivo produzido. Ele não avaliou as cores, a aparência no navegador ou o tempo de resposta.

:::single-choice{#ci-builds-and-tests-test-scope} O teste passou. O que você pode concluir?

::option[A página pode ser acessada pela internet.]{#ci-builds-and-tests-test-scope-a explanation="A verificação leu um arquivo de saída local."}
::option[A página aparece em todos os navegadores compatíveis.]{#ci-builds-and-tests-test-scope-b explanation="Nenhum navegador foi usado no teste."}
::option[O arquivo produzido contém o texto esperado do título.]{#ci-builds-and-tests-test-scope-c .correct explanation="Essa foi a condição verificada pelo comando grep."}
:::

![Verificação local do título bem-sucedida no LabEx com código de saída igual a zero](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## Resumo

Agora você consegue interpretar o que cada etapa de uma pequena verificação de CI comprova.

1. Prepare a entrada antes do build.
2. Identifique o arquivo gerado pelo build.
3. Interprete o código de saída e a condição exata que o teste verificou.
