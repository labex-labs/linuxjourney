---
lesson_id: "osi-model"
course_id: "network-basics"
lang: "pt"
order_index: 2
title: "Modelo OSI"
description: "Aprenda como o modelo de referência OSI de sete camadas organiza as funções de rede e a linguagem de solução de problemas."
meta_title: "Modelo OSI - Fundamentos de rede"
meta_description: "Explore o modelo OSI, uma estrutura fundamental de sete camadas para redes. Aprenda como esse conceito teórico influencia o modelo TCP/IP e sua importância no universo das redes Linux."
meta_keywords: "osi linux, modelo OSI, conceitos de rede, TCP/IP, redes Linux, camadas de rede, modelo teórico, modelo de 7 camadas"
---

O modelo de Interconexão de Sistemas Abertos é uma estrutura de referência de sete camadas. Ele oferece aos engenheiros um vocabulário comum para localizar responsabilidades, interfaces e falhas; não é uma descrição literal de toda implementação.

## As sete camadas

Da mais baixa para a mais alta, as camadas OSI são:

1. Física: sinais, meios, conectores e transmissão de bits.
2. Enlace de Dados: quadros locais, endereçamento de enlace e acesso ao meio.
3. Rede: endereçamento lógico e encaminhamento entre redes.
4. Transporte: comunicação entre pontos de extremidade ou processos.
5. Sessão: gerenciamento de sessões de comunicação.
6. Apresentação: representação, transformação e codificação de dados.
7. Aplicação: serviços de rede usados pelas aplicações.

:::single-choice{#osi-network-layer-number} Qual camada OSI cuida do endereçamento lógico e do encaminhamento entre redes?

::option[Camada 3, Rede.]{#osi-layer-three .correct explanation="A camada de rede descreve o endereçamento lógico e o encaminhamento entre redes."}
::option[Camada 1, Física.]{#osi-layer-one explanation="A camada física trata dos sinais e dos meios."}
::option[Camada 7, Aplicação.]{#osi-layer-seven explanation="A camada de aplicação descreve os serviços expostos às aplicações de rede."}
:::

## Usando o modelo como vocabulário

Afirmações como “um loop de Camada 2” ou “uma porta de Camada 4” identificam uma área funcional sem explicar todos os detalhes da implementação. Um protocolo real pode atravessar limites, e criptografia, túneis, proxies ou sobreposições podem criar várias camadas aninhadas.

:::single-choice{#osi-model-purpose} Para que o modelo OSI é mais útil na solução cotidiana de problemas?

::option[Garantir que todo protocolo tenha exatamente sete cabeçalhos.]{#osi-seven-headers explanation="As implementações não correspondem individualmente a sete cabeçalhos no meio de transmissão."}
::option[Substituir todas as capturas de pacotes por um diagrama.]{#osi-replace-captures explanation="O modelo orienta a investigação, mas não substitui as evidências."}
::option[Fornecer uma maneira comum de classificar as funções de rede.]{#osi-shared-vocabulary .correct explanation="A estrutura ajuda as equipes a delimitar a área funcional em discussão."}
:::

## Comparando OSI e TCP/IP

A suíte de protocolos da Internet e o modelo de referência OSI se desenvolveram por meio de histórias de padronização diferentes. O modelo TCP/IP prático geralmente agrupa as responsabilidades de sessão e apresentação do OSI em sua camada de aplicação e combina as questões físicas e de enlace de dados em uma camada de enlace ou de acesso à rede. Os mapeamentos são aproximados, não uma prova de que uma pilha foi implementada diretamente a partir da outra.

:::single-choice{#osi-tcpip-mapping} Como um mapeamento das camadas OSI para TCP/IP deve ser interpretado?

::option[Como uma regra exata que todo protocolo deve seguir.]{#osi-exact-rule explanation="As responsabilidades dos protocolos frequentemente atravessam limites conceituais."}
::option[Como evidência de que o TCP/IP usa sete camadas obrigatórias no meio de transmissão.]{#osi-tcp-seven explanation="O TCP/IP costuma ser apresentado com quatro ou cinco camadas."}
::option[Como uma comparação aproximada entre modelos funcionais.]{#osi-approximate-map .correct explanation="Os modelos agrupam algumas responsabilidades de maneiras diferentes."}
:::

## Solucionando problemas entre camadas

Comece pelo sintoma e teste as suposições, em vez de verificar mecanicamente as camadas em ordem numérica. Uma falha na Web pode envolver o estado do enlace local, o roteamento IP, a acessibilidade do transporte, TLS, resolução de nomes, autenticação ou comportamento da aplicação. Evidências em uma camada podem orientar o próximo teste sem comprovar que as camadas superiores funcionam.

:::single-choice{#osi-link-success-limit} O que um enlace Ethernet local funcionando comprova?

::option[Que todos os serviços HTTP remotos estão íntegros.]{#osi-link-proves-http explanation="O estado do enlace local não pode comprovar a integridade de uma aplicação remota."}
::option[Que o DNS não contém registros incorretos.]{#osi-link-proves-dns explanation="Os dados de nomes são independentes da conectividade básica do enlace."}
::option[Apenas que as condições relevantes do enlace local funcionam.]{#osi-link-limited-proof .correct explanation="Falhas de roteamento, transporte, nomenclatura, segurança e aplicação ainda podem existir."}
:::

## Resumo

Agora você pode usar o modelo OSI como um vocabulário de diagnóstico em camadas.

1. Nomeie as sete camadas em ordem.
2. Associe cada camada à sua responsabilidade geral.
3. Trate os mapeamentos para TCP/IP como aproximados.
4. Use as evidências das camadas para orientar, não substituir, testes de ponta a ponta.
