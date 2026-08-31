---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "pt"
order_index: 6
title: "Protocolos de estado de enlace"
description: "Aprenda como protocolos de estado de enlace formam adjacências, inundam informações de topologia e calculam caminhos."
meta_title: "Protocolos de estado de enlace - Roteamento"
meta_description: "Aprenda sobre protocolos de estado de enlace como OSPF para redes grandes. Entenda sua rápida convergência e como eles atualizam tabelas de roteamento. Comece sua jornada pelas redes Linux!"
meta_keywords: "protocolos de estado de enlace, OSPF, redes Linux, protocolos de roteamento, topologia de rede, iniciante"
---

Protocolos de estado de enlace descrevem enlaces e prefixos locais, distribuem essas descrições por um escopo de roteamento e permitem que cada roteador calcule caminhos a partir de um banco de dados da topologia. OSPF e IS-IS são exemplos comuns.

## Formando adjacências

Os roteadores descobrem vizinhos compatíveis e formam adjacências de protocolo de acordo com o tipo de interface, a área, os temporizadores, a autenticação e outros parâmetros. Ver pacotes hello não garante uma adjacência completa; configurações incompatíveis podem interromper a máquina de estados antes.

:::single-choice{#link-state-hello-limit}
O que o recebimento de um hello OSPF não consegue comprovar?

::option[Que os roteadores formaram uma adjacência completa e sincronizada.]{#link-state-not-full .correct explanation="Área, temporizadores, autenticação, MTU e outros estados podem impedir a troca completa do banco de dados."}
::option[Que o vizinho enviou pelo menos uma mensagem do protocolo.]{#link-state-hello-sent explanation="O recebimento do hello comprova diretamente esse fato limitado."}
::option[Que uma interface consegue receber um quadro.]{#link-state-frame-received explanation="O pacote recebido comprova que parte do caminho de recepção local funcionou."}
:::

## Inundando informações de estado de enlace

Cada roteador origina anúncios sobre seu estado relevante. Os vizinhos inundam de forma confiável as informações mais recentes por toda a área ou domínio definido, em vez de manter as atualizações apenas entre o par de vizinhos original. Mecanismos de sequência e envelhecimento diferenciam informações atuais e removem estados obsoletos.

:::single-choice{#link-state-flooding-scope}
Por que as informações de estado de enlace são inundadas além de um vizinho?

::option[Toda aplicação precisa de uma cópia de todas as senhas dos roteadores.]{#link-state-password-copy explanation="Credenciais de aplicações não são anúncios de topologia."}
::option[O Ethernet não consegue enviar quadros unicast.]{#link-state-no-unicast explanation="O Ethernet oferece suporte a unicast; a inundação aqui é um mecanismo de distribuição do protocolo de roteamento."}
::option[Os roteadores no escopo de roteamento precisam de um banco de dados de topologia consistente.]{#link-state-consistent-database .correct explanation="Cada roteador calcula caminhos a partir do conjunto compartilhado de anúncios atuais de estado de enlace."}
:::

## Calculando os caminhos mais curtos

Depois de construir um banco de dados de estado de enlace, um roteador executa um algoritmo de caminho mais curto primeiro, normalmente o algoritmo de Dijkstra, tendo a si próprio como raiz. O OSPF soma os custos das interfaces; a política e as regras de custos iguais influenciam quais resultados são instalados.

“Mais curto” significa o menor custo do protocolo, não necessariamente menos roteadores nem a menor latência medida pela aplicação. O projeto dos custos deve refletir a intenção operacional.

:::single-choice{#link-state-shortest-meaning}
O que “mais curto” significa em um cálculo de caminho por estado de enlace?

::option[A rota cujo prefixo possui menos caracteres escritos.]{#link-state-shortest-text explanation="O comprimento do texto não tem relação com o custo da topologia."}
::option[O caminho com a menor soma de custos do protocolo.]{#link-state-lowest-cost .correct explanation="O modelo de custos pode ou não corresponder diretamente à contagem de saltos ou à latência atual."}
::option[O caminho que sempre possui perda zero de pacotes.]{#link-state-zero-loss explanation="Uma rota calculada não garante o desempenho da aplicação."}
:::

## Áreas e convergência

As áreas OSPF limitam o escopo da inundação de topologia e dos cálculos, e a Área 0 atua como backbone no projeto normal entre áreas. A sumarização e os tipos de área podem fazer intencionalmente com que roteadores diferentes tenham detalhes distintos no banco de dados.

Depois de uma mudança de enlace, a detecção, a inundação de anúncios, o cálculo SPF, a instalação das rotas e a recuperação do encaminhamento levam tempo individualmente. Uma convergência mais rápida do que em um projeto simples de vetor de distância é possível, mas não automática em toda falha ou configuração.

:::single-choice{#link-state-convergence-stages}
O que deve ser medido durante uma investigação da convergência do OSPF?

::option[Apenas o momento em que um administrador abriu um terminal.]{#link-state-terminal-time explanation="Isso não isola as etapas do protocolo nem do encaminhamento."}
::option[Apenas a ordem alfabética dos nomes dos roteadores.]{#link-state-router-names explanation="Os nomes não determinam o tempo de convergência."}
::option[Detecção, inundação, cálculo, instalação e recuperação do encaminhamento.]{#link-state-all-stages .correct explanation="Separar as etapas revela onde ocorre o atraso ou a falha de convergência."}
:::

## Resumo

Agora você pode acompanhar o roteamento por estado de enlace desde a descoberta de vizinhos até os caminhos instalados.

1. Diferencie o recebimento de hello de uma adjacência completa.
2. Explique a inundação confiável por um escopo de roteamento.
3. Interprete o caminho mais curto como o menor custo configurado do protocolo.
4. Meça todas as etapas de convergência dos planos de controle e dados.
