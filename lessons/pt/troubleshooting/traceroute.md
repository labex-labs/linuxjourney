---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "pt"
order_index: 3
title: "traceroute"
description: "Aprenda como traceroute descobre saltos que respondem e como interpretar lacunas, tempos e variações de caminho."
meta_title: "traceroute - Solução de Problemas"
meta_description: "Domine o comando traceroute do Linux para rastrear rotas de rede e solucionar problemas de conectividade. Este tutorial explica como o traceroute usa o TTL para mapear o caminho que os pacotes percorrem até o destino."
meta_keywords: "traceroute, traceroute linux, rede Linux, solução de problemas de rede, TTL, roteamento de pacotes, comandos Linux, iniciante, tutorial"
---

`traceroute` envia sondagens com valores crescentes de TTL IPv4 ou Hop Limit IPv6. Roteadores onde o valor expira podem devolver Time Exceeded, revelando alguns pontos que respondem no caminho de ida.

## Como a descoberta de saltos funciona

As sondagens começam com limite um e aumentam. O primeiro roteador reduz para zero e pode retornar erro. Limite dois chega ao segundo antes de expirar, e o processo continua até resposta do destino ou limite máximo.

:::single-choice{#traceroute-expiring-field} Qual campo faz sondagens sucessivas expirarem em roteadores posteriores?

::option[O TTL do cache DNS do nome de destino.]{#traceroute-dns-ttl explanation="A validade do registro DNS não controla saltos de encaminhamento."}
::option[O endereço MAC Ethernet de origem.]{#traceroute-source-mac explanation="Endereços de enlace não carregam contador de saltos de ponta a ponta."}
::option[TTL IPv4 ou Hop Limit IPv6.]{#traceroute-hop-field .correct explanation="Aumentar esse limite de encaminhamento expõe saltos roteados que respondem."}
:::

## Métodos de sondagem

O traceroute Linux tradicional costuma enviar UDP a portas altas. O destino pode encerrar com ICMP Port Unreachable. Opções usam ICMP Echo ou TCP SYN, que atravessam filtros de modo diferente:

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

Os privilégios e as opções disponíveis variam. Use métodos autorizados para o destino e registre o método ao comparar os resultados.

:::single-choice{#traceroute-default-destination-response} O que normalmente encerra um traceroute UDP tradicional no Linux?

::option[Uma resposta ICMP Port Unreachable do destino.]{#traceroute-port-unreachable .correct explanation="Portas UDP altas costumam estar sem uso, permitindo que o destino se identifique pelo erro."}
::option[Uma resposta HTTP 200 obrigatória de todo roteador.]{#traceroute-http-every-router explanation="Roteadores retornam erros de controle, não HTTP."}
::option[Um broadcast Ethernet do destino pela Internet.]{#traceroute-ethernet-broadcast explanation="Broadcasts de enlace não cruzam caminhos roteados."}
:::

## Interpretação dos asteriscos

Um asterisco significa que não se observou resposta antes do timeout. O roteador pode encaminhar tráfego enquanto filtra ou limita respostas diagnósticas. Se saltos posteriores respondem, o silencioso encaminhou ao menos algumas sondagens.

:::single-choice{#traceroute-asterisk-meaning} O que um `*` em um salto prova?

::option[Que o roteador descartou permanentemente todo tráfego.]{#traceroute-star-all-drop explanation="Respostas posteriores podem demonstrar encaminhamento."}
::option[Apenas que nenhuma resposta correspondente chegou antes do timeout.]{#traceroute-star-no-response .correct explanation="Filtro, rate limiting, perda e problemas no retorno podem causar silêncio."}
::option[Que o destino não tem endereço IP.]{#traceroute-star-no-address explanation="A sondagem já aponta para um endereço, e um salto silencioso não o apaga."}
:::

## Tempo e variação do caminho

Os tempos por salto medem ida e volta das respostas de controle, não latência acrescentada entre duas linhas. Roteadores podem despriorizar respostas. Balanceamento pode enviar sondagens por caminhos diferentes, e resolução de nomes acrescentar atraso; `-n` evita consultas reversas.

O retorno de cada resposta pode diferir do caminho de ida. Repita testes e correlacione com o tempo do aplicativo antes de apontar um gargalo.

:::single-choice{#traceroute-hop-rtt-limit} Por que não subtrair RTTs de saltos adjacentes como latência exata do enlace?

::option[Traceroute informa tempos em bytes, não milissegundos.]{#traceroute-times-bytes explanation="Os tempos normalmente são em milissegundos."}
::option[Respostas podem usar retornos e processamento de controle diferentes.]{#traceroute-rtt-asymmetry .correct explanation="São viagens de ida e volta separadas, não amostras sincronizadas do enlace."}
::option[Todo roteador tem o mesmo relógio da origem.]{#traceroute-router-clock explanation="A medição não depende de relógios remotos sincronizados."}
:::

## Comparação com o aplicativo

Traceroute pode chegar ao destino enquanto o serviço está bloqueado, e o serviço pode funcionar enquanto roteadores ocultam respostas. Teste a mesma família, destino, protocolo e porta do aplicativo e use traceroute como evidência auxiliar.

:::single-choice{#traceroute-service-proof} Um traceroute completo prova que HTTPS está saudável?

::option[Sim, pois todo salto valida o certificado.]{#traceroute-validates-cert explanation="Roteadores não realizam validação TLS do cliente."}
::option[Não; transporte, TLS e HTTP exigem testes próprios.]{#traceroute-not-app-proof .correct explanation="Descoberta do caminho e saúde do aplicativo são camadas diferentes."}
::option[Sim, mas apenas com nomes DNS reversos.]{#traceroute-rdns-proof explanation="Nomes não demonstram funcionamento do aplicativo."}
:::

## Resumo

Agora você consegue interpretar traceroute como sondagens de saltos limitados, não um oráculo completo.

1. Explicar descoberta pela expiração de TTL ou Hop Limit.
2. Registrar o uso de UDP, ICMP ou TCP.
3. Tratar asteriscos como respostas ausentes, não falhas provadas.
4. Não derivar latência exata entre saltos por RTTs adjacentes.
5. Correlacionar o caminho com o aplicativo real.
