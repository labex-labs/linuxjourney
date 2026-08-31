---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "pt"
order_index: 5
title: "Análise de Pacotes"
description: "Aprenda a capturar um trace de pacotes limitado e filtrado e analisá-lo com segurança usando tcpdump."
meta_title: "Análise de Pacotes - Solução de Problemas"
meta_description: "Aprenda os fundamentos da análise de pacotes de rede no Linux. Este guia apresenta o tcpdump, um poderoso analisador de pacotes, para capturar e interpretar tráfego de rede."
meta_keywords: "tcpdump, análise de pacotes, análise de pacotes de rede, analisador de pacotes de rede, análise de rede, ferramentas de análise de pacotes de rede, rede Linux, Wireshark, comandos Linux, tráfego de rede"
---

A captura registra tráfego visível em um ponto de observação. Ela revela trocas e tempos, mas também pode coletar credenciais, dados pessoais e tráfego de terceiros. Obtenha autorização, reduza o escopo, proteja arquivos e siga a política de retenção.

## Escolha do ponto de observação

Capture na interface e no namespace pelos quais o fluxo afetado realmente passa. Bridges, containers, VPNs, bonds, VLANs e offload mudam o que uma interface mostra. Use `ip route get` e `ip link` para identificar candidatas.

:::single-choice{#packet-analysis-interface-choice}
Por que a escolha da interface de captura importa?

::option[Toda interface espelha automaticamente a Internet inteira.]{#packet-analysis-mirrors-internet explanation="Um host normalmente vê apenas tráfego entregue ou espelhado às suas interfaces."}
::option[Apenas o tráfego visível nesse ponto pode ser registrado.]{#packet-analysis-visible-point .correct explanation="Namespaces, túneis, bridges e rotas podem colocar o fluxo em outro lugar."}
::option[O nome da interface descriptografa TLS.]{#packet-analysis-name-decrypts explanation="O nome não oferece capacidade de descriptografia."}
:::

## Captura de um fluxo limitado

Capture até 100 pacotes sem resolver nomes, restritos a host e porta TCP:

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i` seleciona interface, `-n` mantém números, `-c` limita pacotes, `-w` grava pcap e a expressão final filtra. Defina também um limite externo de tempo quando puder não haver tráfego.

:::single-choice{#packet-analysis-count-bound}
O que `-c 100` faz?

::option[Captura apenas a porta TCP 100.]{#packet-analysis-port-hundred explanation="A porta pertence à expressão de filtro."}
::option[Comprime o arquivo para 100 bytes.]{#packet-analysis-compress-hundred explanation="A opção limita quantidade de pacotes, não tamanho."}
::option[Para depois de capturar 100 pacotes.]{#packet-analysis-hundred .correct explanation="A contagem evita crescimento indefinido por número de pacotes."}
:::

## Leitura dos pacotes capturados

Analise o arquivo salvo sem modificá-lo:

```bash
$ tcpdump -n -tttt -r incident.pcap
```

Leia horários, protocolo, origem, destino, flags, sequência, acknowledgements e tamanho conforme o protocolo. O horário marca a observação neste host, não necessariamente o envio exato em outro. Sincronização importa ao correlacionar vários sistemas.

:::single-choice{#packet-analysis-read-file}
Qual opção lê pacotes de um pcap salvo?

::option[`-r`]{#packet-analysis-option-read .correct explanation="A opção read processa um arquivo de captura existente."}
::option[`-i`]{#packet-analysis-option-interface explanation="Essa opção seleciona uma interface ativa."}
::option[`-w`]{#packet-analysis-option-write explanation="Essa opção grava pacotes brutos."}
:::

## Interpretação de ausência e criptografia

Nenhum pacote pode significar interface ou namespace errado, perda de captura, filtro estreito, offload, outra rota ou nenhum tráfego. Confira os contadores recebidos e descartados e reproduza um evento conhecido.

TLS e outras criptografias ocultam payloads, mas deixam metadados como endpoints, tempos, tamanhos, comportamento TCP e partes do handshake. Não tente descriptografia não autorizada nem colete chaves privadas casualmente.

:::single-choice{#packet-analysis-no-packets}
O que uma captura filtrada vazia prova?

::option[Que o aplicativo remoto foi apagado permanentemente.]{#packet-analysis-empty-deleted explanation="Erros no ponto ou filtro produzem o mesmo resultado."}
::option[Que toda a rede tem tráfego zero.]{#packet-analysis-empty-network explanation="Um filtro estreito exclui tráfego alheio."}
::option[Apenas que nenhum pacote correspondente foi registrado nesse ponto.]{#packet-analysis-empty-limited .correct explanation="Valide interface, namespace, filtro, descartes e geração do teste."}
:::

## Proteção e compartilhamento da evidência

Guarde pcaps com permissões restritas, registre comando, host, interface, fuso, filtro e janela e calcule hash quando a integridade importar. Antes de compartilhar, minimize ou sanitize preservando campos necessários; payload e metadados podem identificar pessoas e sistemas.

:::single-choice{#packet-analysis-pcap-safety}
Como tratar um pcap de incidente?

::option[Como evidência sensível, com acesso restrito e procedência documentada.]{#packet-analysis-sensitive-evidence .correct explanation="Capturas podem conter conteúdo confidencial e exigem integridade e confidencialidade."}
::option[Como texto inofensivo para publicação sem revisão.]{#packet-analysis-public explanation="Capturas binárias expõem payloads, identidades e infraestrutura."}
::option[Editando bytes no original sem preservá-lo.]{#packet-analysis-edit-original explanation="Isso danifica a procedência e pode invalidar análises."}
:::

## Resumo

Agora você consegue criar uma captura útil sem torná-la ampla ou insegura.

1. Escolher interface e namespace corretos.
2. Limitar por filtro, contagem e tempo.
3. Salvar pacotes brutos e analisar somente leitura.
4. Tratar ausência e criptografia com limites adequados.
5. Proteger confidencialidade, integridade e procedência.
