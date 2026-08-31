---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "pt"
order_index: 4
title: "netstat"
description: "Aprenda a inspecionar sockets, listeners, filas e estados TCP do Linux usando ss."
meta_title: "netstat - Solução de Problemas"
meta_description: "Domine o comando netstat do linux para analisar conexões de rede, portas e sockets. Este guia aborda estados comuns como SYN_SENT e netstat close_wait para solução de problemas eficaz."
meta_keywords: "netstat linux, netstat, comando netstat, syn_sent netstat, netstat close_wait, conexões de rede, rede linux, análise de rede, tutorial linux"
---

O legado `netstat` exibe sockets, rotas e estatísticas. No Linux moderno, `ss` é preferível para inspecionar sockets, pois expõe eficientemente o estado do kernel e é mantido com iproute2.

## Listagem de sockets em escuta

Mostre listeners TCP e UDP numericamente, com processos quando permitido:

```bash
$ sudo ss -lntup
```

`-l` seleciona listeners, `-n` evita resolução de nomes, `-t` e `-u` escolhem TCP e UDP, e `-p` solicita processos. UDP não tem conexão, portanto sockets vinculados não realizam handshake `LISTEN` como TCP.

:::single-choice{#netstat-ss-numeric}
Por que usar `-n` ao diagnosticar sockets?

::option[Ele cria um namespace de rede.]{#netstat-new-namespace explanation="A opção controla a resolução de nomes na saída."}
::option[Ele impede consultas de nomes de endereços e portas.]{#netstat-numeric-output .correct explanation="A saída numérica evita confundir mapeamento de serviço com identidade observada."}
::option[Ele fecha todo socket que não está ouvindo.]{#netstat-close-sockets explanation="A inspeção não encerra sockets."}
:::

## Portas, endpoints e serviços

Um endpoint local combina endereço, protocolo de transporte e porta. Uma conexão TCP é distinguida por protocolo e endereços e portas de origem e destino. `/etc/services` mapeia nomes convencionais, mas não prova qual processo possui uma porta nem qual protocolo de aplicação fala.

:::single-choice{#netstat-services-file-limit}
O que uma entrada `https 443/tcp` em `/etc/services` estabelece?

::option[Que há um servidor HTTPS saudável ouvindo.]{#netstat-healthy-listener explanation="Um banco estático não prova estado de runtime."}
::option[O mapeamento convencional de nome para essa porta.]{#netstat-conventional-name .correct explanation="Proprietário e protocolo real exigem inspeção e teste."}
::option[Que todo tráfego na porta 443 está criptografado corretamente.]{#netstat-all-encrypted explanation="O número da porta não valida TLS."}
:::

## Leitura dos estados TCP

Estados comuns:

- `SYN-SENT`: o endpoint local enviou pedido e aguarda progresso.
- `ESTAB`: a conexão está estabelecida.
- `CLOSE-WAIT`: o peer fechou seu envio, mas o aplicativo local ainda não fechou o socket.
- `TIME-WAIT`: o ponto de extremidade que fechou ativamente espera os segmentos atrasados expirarem e a troca final ser tratada com segurança.

Populações grandes ou crescentes de `CLOSE-WAIT` costumam apontar para o comportamento de limpeza da aplicação local. `TIME-WAIT` é um estado normal do protocolo; a quantidade e o impacto sobre os recursos determinam se há uma preocupação operacional.

:::single-choice{#netstat-close-wait-owner}
Qual lado ainda precisa fechar um socket em `CLOSE-WAIT`?

::option[Todos os roteadores da Internet.]{#netstat-all-routers-close explanation="Roteadores não possuem o socket do endpoint."}
::option[O servidor DNS autoritativo.]{#netstat-dns-close explanation="DNS não participa do fechamento TCP local."}
::option[O aplicativo local.]{#netstat-local-close .correct explanation="TCP recebeu o FIN do peer e aguarda o processo local fechar seu lado."}
:::

## Interpretação das filas

O significado de `Recv-Q` e `Send-Q` depende do estado e do protocolo. Em sockets TCP estabelecidos, eles podem indicar dados na fila para recebimento pela aplicação ou para confirmação da transmissão. Em sockets em escuta, os campos de fila descrevem o estado do backlog de conexões, e não bytes da carga útil da aplicação da mesma forma.

Um snapshot não demonstra vazamento ou gargalo. Observe ao longo do tempo e correlacione processo, latência, retransmissões e limites.

:::single-choice{#netstat-queue-snapshot}
Por que um único snapshot de fila grande é insuficiente?

::option[O Linux nunca armazena dados em filas.]{#netstat-no-queues explanation="A rede do kernel depende de filas de envio e recebimento."}
::option[Todo valor de fila é uma permissão de arquivo.]{#netstat-queue-permission explanation="Os campos descrevem estado de rede."}
::option[O impacto exige estado, tendência e contexto da carga.]{#netstat-queue-context .correct explanation="Um pico transitório difere de gargalo persistente."}
:::

## Filtragem da investigação

Limite a saída ao protocolo, estado ou endpoint:

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

Um listener prova prontidão local do transporte, não alcance remoto nem saúde do aplicativo. Continue com testes de rota, firewall, pacotes, TLS e aplicação.

:::single-choice{#netstat-listener-limit}
O que um listener TCP na porta 443 não prova?

::option[Que um socket local aceitou bind e listen.]{#netstat-listen-local explanation="Esse é exatamente o estado mostrado."}
::option[Que clientes remotos concluem uma solicitação HTTPS válida.]{#netstat-not-remote-proof .correct explanation="Caminho, TLS e aplicação continuam sem teste."}
::option[Que TCP possui um campo numérico de porta.]{#netstat-port-field explanation="A saída mostra diretamente a porta."}
:::

## Resumo

Agora você consegue usar `ss` sem confundir portas com aplicativos.

1. Listar listeners numericamente com processos.
2. Distinguir nomes convencionais de proprietários ativos.
3. Interpretar fechamentos pela perspectiva local.
4. Observar filas no tempo e no contexto.
5. Verificar o aplicativo remoto além do listener local.
