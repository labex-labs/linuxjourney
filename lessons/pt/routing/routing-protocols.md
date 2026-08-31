---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "pt"
order_index: 4
title: "Protocolos de roteamento"
description: "Aprenda como protocolos de roteamento dinâmico trocam informações de acessibilidade e convergem para caminhos de encaminhamento utilizáveis."
meta_title: "Protocolos de roteamento - Roteamento"
meta_description: "Explore os fundamentos dos protocolos de roteamento em redes Linux. Este guia aborda protocolos de vetor de distância e estado de enlace, convergência de rede e como roteadores constroem e mantêm tabelas de roteamento. Um tutorial ideal para iniciantes."
meta_keywords: "protocolos de roteamento, convergência de rede, vetor de distância, estado de enlace, redes linux, tabela de roteamento, tutorial de redes, guia para iniciantes, comunicação entre roteadores"
---

Rotas estáticas são configuradas diretamente, enquanto protocolos de roteamento dinâmico trocam informações de acessibilidade e topologia para que os roteadores possam se adaptar. O aprendizado dinâmico reduz o trabalho manual, mas introduz estados de protocolo, limites de confiança, temporizadores e modos de falha que precisam ser monitorados.

## Plano de controle e plano de encaminhamento

Um protocolo de roteamento aprende candidatos em seu próprio banco de dados. O roteador seleciona rotas para uma base de informações de roteamento e instala próximos saltos utilizáveis em uma tabela de encaminhamento. O hardware ou o kernel então encaminha os pacotes a partir dessa tabela.

Uma adjacência de protocolo estabelecida não comprova que o prefixo desejado foi aprendido, selecionado, instalado ou permitido pela política de encaminhamento.

:::single-choice{#routing-protocols-adjacency-limit}
O que uma adjacência de roteamento estabelecida não consegue comprovar?

::option[Que todas as rotas desejadas estão instaladas e encaminhando com sucesso.]{#routing-protocols-not-full-proof .correct explanation="Anúncio, seleção, instalação e filtragem de rotas e operação do plano de dados são etapas separadas."}
::option[Que dois participantes do protocolo trocaram alguma mensagem de controle.]{#routing-protocols-no-messages explanation="O estabelecimento de uma adjacência normalmente exige comunicação pelo protocolo."}
::option[Que existe um plano de controle.]{#routing-protocols-no-control explanation="A própria adjacência é um estado do plano de controle."}
:::

## Roteamento interior e exterior

Protocolos de gateway interior operam dentro de um domínio administrativo de roteamento. Alguns exemplos são RIP, OSPF e IS-IS. O BGP troca informações de acessibilidade controladas por política dentro e entre sistemas autônomos e é o protocolo de roteamento exterior da Internet.

As métricas possuem significados específicos de cada protocolo. Um custo OSPF, uma contagem de saltos RIP e um conjunto de atributos BGP não podem ser comparados como se compartilhassem uma escala numérica universal. As implementações usam preferência de rota ou distância administrativa para escolher entre origens antes ou em conjunto com a seleção específica do protocolo.

:::single-choice{#routing-protocols-metric-comparison}
Uma contagem de saltos RIP pode ser comparada diretamente com um custo OSPF?

::option[Sim, porque todas as métricas de roteamento usam as mesmas unidades.]{#routing-protocols-universal-metric explanation="Cada protocolo define sua própria métrica e seu processo de seleção."}
::option[Sim, mas apenas quando ambos os valores são zero.]{#routing-protocols-zero-metric explanation="Suas semânticas continuam diferentes independentemente do número exibido."}
::option[Não; elas possuem significados específicos dos protocolos.]{#routing-protocols-specific-metric .correct explanation="A seleção entre origens usa a política da implementação, em vez de tratar métricas diferentes como uma única escala."}
:::

## Vetor de distância e estado de enlace

Protocolos de vetor de distância anunciam acessibilidade e distância por meio de vizinhos, derivando caminhos dos relatórios deles. Protocolos de estado de enlace formam adjacências, inundam informações sobre o estado dos enlaces dentro de um escopo, constroem um banco de dados da topologia e calculam árvores de caminhos mais curtos. Protocolos modernos incluem refinamentos que tornam incompletos os resumos simples por categoria.

:::single-choice{#routing-protocols-link-state-input}
O que um roteador de estado de enlace usa para calcular seus caminhos?

::option[Apenas o nome de host de seu gateway padrão.]{#routing-protocols-hostname-only explanation="Um cálculo de topologia exige informações de enlaces e prefixos."}
::option[Um banco de dados sincronizado que descreve os enlaces no escopo de roteamento.]{#routing-protocols-link-database .correct explanation="O roteador executa um algoritmo de caminho mais curto sobre a topologia aprendida."}
::option[Senhas da camada de aplicação de todos os hosts.]{#routing-protocols-passwords explanation="A troca da topologia de roteamento não exige credenciais de usuários finais."}
:::

## Convergência

Depois de uma mudança de topologia ou política, os roteadores a detectam, propagam informações de controle, calculam caminhos e atualizam o estado de encaminhamento. Convergência é o período e o resultado em que a rede alcança um roteamento estável e mutuamente utilizável para os destinos afetados. Ela não exige que todos os roteadores tenham uma tabela completa idêntica; funções e políticas podem diferir intencionalmente.

Durante a convergência, podem ocorrer perdas transitórias, loops ou buracos negros. Meça separadamente detecção, propagação, cálculo e instalação e verifique com sondagens do plano de dados.

:::single-choice{#routing-protocols-convergence}
O que é convergência de roteamento?

::option[O processo de alcançar um roteamento estável e utilizável depois de uma mudança.]{#routing-protocols-stable-routing .correct explanation="Ela inclui a propagação do controle e as atualizações de encaminhamento resultantes."}
::option[Uma exigência de que todo roteador armazene uma tabela global idêntica.]{#routing-protocols-identical-table explanation="Política, área e função podem criar diferenças intencionais."}
::option[A prevenção permanente de toda falha de roteamento possível.]{#routing-protocols-no-failure explanation="Uma rede convergida ainda pode ter problemas de política ou capacidade."}
:::

## Resumo

Agora você pode posicionar as informações de roteamento dinâmico no caminho entre a troca de protocolos e o encaminhamento.

1. Separe candidatos aprendidos, rotas selecionadas e entradas de encaminhamento.
2. Diferencie o roteamento interior da troca de políticas do BGP.
3. Compare métricas apenas dentro da semântica de seus protocolos.
4. Verifique a convergência tanto no plano de controle quanto no plano de dados.
