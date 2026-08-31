---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "pt"
order_index: 10
title: "expand e unexpand"
description: "Aprenda como as paradas de tabulação controlam a conversão entre tabulações e espaços com expand e unexpand."
meta_title: "expand e unexpand - Text-Fu"
meta_description: "Domine a formatação de texto no Linux com expand e unexpand. Aprenda a converter tabulações em espaços e espaços em tabulações preservando o alinhamento."
meta_keywords: "comando expand, comando unexpand, tabulações Linux, espaços Linux, formatação texto, tutorial Linux, Linux para iniciantes"
---

As tabulações armazenam um movimento até uma parada de tabulação, não uma quantidade fixa de espaços visíveis. Sua largura exibida depende da coluna atual e da configuração das paradas. Os comandos `expand` e `unexpand` convertem entre caracteres de tabulação e espaços levando essas posições em conta.

## Conversão de Tabulações em Espaços

`expand` lê a entrada, substitui as tabulações pelos espaços necessários para alcançar as paradas adequadas e grava o resultado em stdout:

```bash
$ expand sample.txt
```

Por padrão, as paradas ocorrem a cada 8 colunas. Assim, uma tabulação na coluna 1 se expande de forma diferente de uma na coluna 6; ela nem sempre é substituída por oito espaços.

:::single-choice{#expand-default-tab-stops}
Com as configurações padrão, como `expand` substitui um caractere de tabulação?

::option[Ele insere espaços suficientes para alcançar a próxima parada padrão.]{#expand-next-stop .correct explanation="`expand` preserva o alinhamento das paradas calculando os espaços necessários a partir da coluna atual."}
::option[Ele sempre insere exatamente oito espaços.]{#expand-eight-spaces explanation="As paradas padrão ficam separadas por oito colunas, mas a quantidade de espaços depende da coluna atual."}
::option[Ele remove a tabulação sem acrescentar caracteres.]{#expand-remove-tab explanation="O comando substitui a tabulação por espaços para manter o texto seguinte alinhado na parada escolhida."}
:::

## Escolha das Paradas de Tabulação

Use `-t NUMBER` para colocar paradas a cada quantidade especificada de colunas. Para paradas a cada quatro colunas:

```bash
$ expand -t 4 sample.txt
```

O GNU `expand` também aceita uma lista de posições explícitas separadas por vírgulas. Use `-i` quando apenas as tabulações anteriores ao primeiro caractere não vazio de cada linha devam ser convertidas.

:::single-choice{#expand-four-column-stops}
Qual comando converte tabulações usando paradas a cada quatro colunas?

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="A opção `-i` limita a conversão às tabulações iniciais e não recebe `4` como intervalo."}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand` converte espaços adequados em tabulações, a direção oposta à operação solicitada."}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="A opção `-t` define o intervalo das paradas, e `4` solicita uma parada a cada quatro colunas."}
:::

## Salvamento Seguro da Saída Convertida

`expand` não edita seu arquivo de entrada. Redirecione stdout para outro caminho quando quiser salvar o texto convertido:

```bash
$ expand sample.txt > result.txt
```

Não use `expand sample.txt > sample.txt`. O shell trunca o destino antes que `expand` possa lê-lo; assim, os dados de origem podem ser perdidos. Depois de verificar um resultado gravado separadamente, você pode substituir o original conscientemente com uma etapa apropriada de gerenciamento de arquivos.

:::single-choice{#expand-safe-output-file}
Qual comando salva o texto expandido sem truncar `sample.txt` antes de sua leitura?

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="O shell abre e trunca `sample.txt` para saída antes de iniciar `expand`, o que pode apagar a entrada."}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="Os caminhos de entrada e saída são diferentes; portanto, o shell pode criar `result.txt` sem destruir a origem."}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="Essa forma ainda trunca `sample.txt` e não representa uma conversão segura do arquivo original."}
:::

## Conversão de Espaços em Tabulações

`unexpand` substitui espaços elegíveis por tabulações, preservando o alinhamento nas paradas escolhidas. Por padrão, o GNU `unexpand` converte apenas os espaços iniciais anteriores ao primeiro caractere não vazio de uma linha:

```bash
$ unexpand result.txt
```

Use `-a` para considerar os espaços adequados em toda a linha:

```bash
$ unexpand -a result.txt
```

Isso não substitui simplesmente todo grupo de oito espaços. A conversão depende das posições das colunas e das paradas, assim como em `expand`. Use `-t 4` ou outra especificação quando o arquivo seguir uma convenção diferente.

:::single-choice{#unexpand-default-scope}
Sem `-a`, quais espaços o GNU `unexpand` normalmente considera para conversão?

::option[Todos os grupos de espaços em qualquer parte do arquivo.]{#unexpand-every-group explanation="Considerar espaços em toda a linha exige `-a`, e a conversão ainda depende das posições das paradas."}
::option[Apenas os espaços que aparecem depois da última palavra.]{#unexpand-trailing-blanks explanation="O escopo padrão diz respeito aos espaços iniciais, não especificamente aos espaços finais."}
::option[Apenas os espaços iniciais anteriores ao primeiro caractere não vazio.]{#unexpand-initial-blanks .correct explanation="O comportamento padrão do GNU `unexpand` se limita aos espaços em branco iniciais de cada linha."}
:::

:::single-choice{#unexpand-all-blanks}
Qual opção instrui o GNU `unexpand` a considerar também os espaços depois do primeiro caractere não vazio?

::option[`-i`]{#unexpand-initial-option explanation="Em `expand`, `-i` limita o trabalho às tabulações iniciais. Ela não é a opção para todos os espaços de `unexpand`."}
::option[`-a`]{#unexpand-all-option .correct explanation="A opção `-a` permite converter espaços adequados ao longo de toda a linha de entrada."}
::option[`-t`]{#unexpand-tab-list-option explanation="A opção `-t` define as paradas. Embora seu comportamento no GNU possa implicar uma conversão mais ampla, `-a` solicita explicitamente todos os espaços."}
:::

Os dois comandos leem stdin quando nenhum arquivo é indicado e, portanto, podem ser usados em pipelines. Lembre-se de que converter para espaços e de volta pode não reconstruir a escolha original entre tabulações e espaços, mesmo que o alinhamento exibido permaneça igual.

## Resumo

Agora você sabe converter tabulações e espaços preservando o alinhamento das paradas.

1. Expanda tabulações até a próxima parada configurada.
2. Defina paradas personalizadas com `-t`.
3. Salve a saída em outro arquivo antes de substituir a entrada.
4. Converta os espaços iniciais com `unexpand` por padrão.
5. Use `-a` quando os espaços de toda a linha devam ser considerados.
