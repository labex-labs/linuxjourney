---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "pt"
order_index: 6
title: "Camada de transporte"
description: "Aprenda como TCP e UDP usam portas e diferentes semânticas de entrega entre pontos de extremidade das aplicações."
meta_title: "Camada de transporte - Fundamentos de rede"
meta_description: "Explore a Camada de Transporte em redes Linux. Esta lição aborda protocolos importantes como TCP e UDP, a função das portas de rede, a segmentação de dados e o handshake TCP para a transferência confiável de dados."
meta_keywords: "Camada de Transporte Linux, TCP, UDP, handshake TCP, portas de rede, segmentação de dados, redes Linux, protocolos de rede, transferência confiável de dados"
---

A camada de transporte conecta pontos de extremidade das aplicações através de uma rede IP. Tanto o TCP quanto o UDP usam números de porta de 16 bits, mas expõem às aplicações modelos de comunicação e garantias diferentes.

## Portas e sockets

Uma porta de destino ajuda o sistema operacional a entregar o tráfego a um socket em escuta. Uma conexão ou fluxo é identificado por mais de uma porta: importam o protocolo, os endereços de origem e destino e as portas de origem e destino. Por isso, a mesma porta de servidor pode atender muitos clientes simultaneamente.

:::single-choice{#transport-layer-many-clients} Como uma porta de servidor TCP pode atender vários clientes ao mesmo tempo?

::option[Cada conexão possui uma combinação distinta de endereços e portas dos pontos de extremidade.]{#transport-layer-connection-tuple .correct explanation="A tupla completa do transporte diferencia conexões simultâneas que compartilham uma porta de escuta."}
::option[O servidor renomeia permanentemente sua porta depois de cada pacote.]{#transport-layer-renames-port explanation="A porta de escuta pode permanecer estável enquanto as conexões aceitas possuem tuplas de pares distintas."}
::option[O IP remove todos os endereços de origem antes da entrega.]{#transport-layer-removes-source explanation="Os endereços de origem fazem parte da identificação do par e do caminho."}
:::

## Fluxos de bytes TCP

O TCP fornece um fluxo de bytes confiável e ordenado enquanto a conexão permanece viável. Ele usa números de sequência, confirmações, retransmissão, controle de fluxo e controle de congestionamento. O TCP não preserva os limites das mensagens da aplicação: uma gravação pode chegar por meio de várias leituras, ou uma leitura pode retornar várias gravações. As aplicações definem seu próprio enquadramento.

Confiabilidade não significa entrega absoluta. Uma conexão pode atingir o tempo limite, ser redefinida ou falhar, e uma confirmação não comprova que uma aplicação gravou os dados de forma durável.

:::single-choice{#transport-layer-tcp-boundaries} O que acontece com os limites das mensagens da aplicação no TCP?

::option[O TCP expõe um fluxo de bytes ordenado sem preservar os limites das gravações.]{#transport-layer-byte-stream .correct explanation="O protocolo de aplicação deve definir como as mensagens são delimitadas ou dimensionadas."}
::option[Toda gravação se torna exatamente um pacote IP e uma leitura.]{#transport-layer-one-write-packet explanation="A segmentação, o armazenamento em buffer e as APIs de recepção não preservam esse mapeamento."}
::option[O TCP converte cada mensagem em um registro DNS.]{#transport-layer-tcp-dns explanation="O DNS é um protocolo de aplicação separado."}
:::

## O handshake TCP

Uma conexão TCP normal começa com um handshake de três vias:

1. O iniciador envia `SYN` com suas informações iniciais de sequência.
2. O ouvinte responde com `SYN-ACK`, suas próprias informações de sequência e uma confirmação.
3. O iniciador retorna `ACK`.

Isso estabelece o estado do transporte nos dois pontos de extremidade. Não autentica o servidor da aplicação nem comprova que a operação solicitada da aplicação terá sucesso.

:::single-choice{#transport-layer-handshake-order} Qual é a ordem normal do handshake TCP de três vias?

::option[SYN, SYN-ACK, ACK.]{#transport-layer-syn-order .correct explanation="A troca sincroniza e confirma o estado inicial da conexão nas duas direções."}
::option[ACK, ACK, SYN.]{#transport-layer-ack-ack-syn explanation="O iniciador primeiro solicita a sincronização."}
::option[SYN, FIN, RST.]{#transport-layer-syn-fin-rst explanation="FIN e RST encerram ou abortam o estado, em vez de formar um handshake normal."}
:::

## Datagramas UDP

O UDP preserva os limites dos datagramas e fornece detecção de erros baseada em soma de verificação, mas não oferece o estado de conexão, a ordenação, a retransmissão, o controle de fluxo nem o controle de congestionamento do TCP. Uma aplicação pode acrescentar por conta própria qualquer comportamento necessário de confiabilidade ou congestionamento. O UDP não é automaticamente mais rápido; o desempenho depende do projeto do protocolo, da carga de trabalho, do caminho e da implementação.

:::single-choice{#transport-layer-udp-boundaries} Qual propriedade o UDP fornece às aplicações?

::option[Um fluxo de bytes ordenado e retransmitido automaticamente.]{#transport-layer-udp-stream explanation="Isso descreve serviços semelhantes ao TCP, não o UDP básico."}
::option[Limites preservados entre os datagramas enviados.]{#transport-layer-udp-datagrams .correct explanation="Um datagrama UDP recebido corresponde a um datagrama enviado, a menos que ele seja perdido."}
::option[Entrega garantida antes de um prazo fixo.]{#transport-layer-udp-deadline explanation="O UDP não fornece garantia de prazo de entrega."}
:::

## Inspecionando pontos de extremidade do transporte

Use `ss` para inspecionar sockets em escuta e conectados sem alterá-los:

```bash
$ ss -lntup
$ ss -tn state established
```

Os detalhes dos processos podem exigir privilégios. Um socket em escuta comprova a prontidão local apenas no limite do transporte; firewall, roteamento, família de endereços, TLS e integridade da aplicação ainda precisam dos testes adequados.

:::single-choice{#transport-layer-listener-proof} O que um socket TCP em escuta estabelece?

::option[Todos os firewalls remotos permitem a conexão.]{#transport-layer-all-firewalls explanation="O estado do socket local não revela todas as políticas do caminho."}
::option[A aplicação passou em todas as verificações de integridade.]{#transport-layer-all-health explanation="A escuta é uma evidência mais fraca do que uma transação bem-sucedida da aplicação."}
::option[Um processo local está preparado para aceitar conexões TCP correspondentes.]{#transport-layer-local-listener .correct explanation="A acessibilidade remota e as respostas corretas da aplicação continuam sendo questões separadas."}
:::

## Resumo

Agora você pode diferenciar o comportamento de fluxo do TCP do comportamento de datagrama do UDP.

1. Identifique um fluxo usando o protocolo, os endereços e as portas.
2. Trate o TCP como um fluxo de bytes confiável e ordenado, sem limites de mensagens.
3. Reconheça o que o handshake TCP comprova e o que ele não comprova.
4. Trate a confiabilidade e o comportamento de congestionamento do UDP como escolhas de projeto da aplicação.
5. Verifique a integridade da aplicação além do estado do socket local.
