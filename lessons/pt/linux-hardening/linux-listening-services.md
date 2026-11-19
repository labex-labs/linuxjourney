---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "pt"
order_index: 4
title: "Serviços em escuta"
description: "Aprenda a ler um endereço de escuta no Linux e a decidir de onde testar o acesso."
meta_title: "Serviços em escuta - Hardening do Linux"
meta_description: "Aprenda a ler um endereço de escuta no Linux e a decidir de onde testar o acesso."
meta_keywords: "serviços em escuta, sockets TCP, hardening do Linux, cibersegurança, Linux Journey"
---

Um serviço pode aguardar conexões em um endereço e uma porta específicos. Um **socket em escuta** está pronto para receber conexões de entrada. Seu endereço dá uma pista de quem pode acessá-lo.

## Listando sockets TCP em escuta

Execute este comando de consulta em um host Linux de prática. As opções fazem o `ss` mostrar sockets TCP em escuta com endereços e portas em formato numérico.

```bash
$ ss -lnt
```

Leia a coluna do endereço local. O exemplo abaixo usa `127.0.0.1:8091` para uma pré-visualização web. A porta é 8091. O endereço é de **loopback**, ou seja, aponta para o próprio host.

:::single-choice{#linux-listening-services-local-listener} Um navegador no mesmo host precisa abrir a pré-visualização. Qual endereço deve usar neste exemplo?

::option[0.0.0.0:8091.]{#linux-listening-services-local-listener-a explanation="Essa notação descreve uma configuração de escuta. O exemplo mostra outro endereço como destino local."}
::option[127.0.0.1:8091.]{#linux-listening-services-local-listener-b .correct explanation="O serviço está escutando nesse endereço de loopback e nessa porta."}
::option[Porta 80 em um servidor sem relação com o exemplo.]{#linux-listening-services-local-listener-c explanation="O socket do exemplo escuta na porta 8091 do próprio host."}
:::

![Saída do ss na LabEx mostrando o socket de prática em loopback na porta 8091](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## Interpretando a escuta em todas as interfaces

O endereço IPv4 local `0.0.0.0:8091` significa que o serviço escuta em todas as interfaces IPv4 do host. Isso pode incluir uma interface acessível por outro computador. A listagem mostra o que o processo aceita localmente. Regras de firewall e rotas podem limitar o acesso de outros computadores.

:::single-choice{#linux-listening-services-all-interfaces} Um serviço muda de 127.0.0.1 para 0.0.0.0 na mesma porta. O que mudou?

::option[Ele pode escutar em mais interfaces IPv4.]{#linux-listening-services-all-interfaces-a .correct explanation="A configuração aumenta o conjunto de endereços locais que podem receber conexões."}
::option[Ele passou a escutar em outra porta.]{#linux-listening-services-all-interfaces-b explanation="O número da porta continua igual."}
::option[O acesso imediato a partir de qualquer rede ficou garantido.]{#linux-listening-services-all-interfaces-c explanation="As regras e rotas de rede ainda determinam quais caminhos podem chegar ao serviço."}
:::

## Verificando o caminho previsto

Um serviço interno da equipe pode ser destinado a uma única rede. Verifique o acesso a partir dessa rede e teste também de um local autorizado fora dela se precisar confirmar a restrição. Confira o socket em escuta e o caminho até ele. A lista local, sozinha, não mostra o que um cliente remoto observou.

:::single-choice{#linux-listening-services-verify-from-client} Você vê um socket em escuta em todas as interfaces locais. Qual verificação mostra se uma estação de trabalho da equipe consegue acessá-lo?

::option[Ler o nome do host mais uma vez.]{#linux-listening-services-verify-from-client-a explanation="O nome do host não testa o caminho pela rede."}
::option[Contar quantos sockets estão em escuta.]{#linux-listening-services-verify-from-client-b explanation="A contagem não mostra se a estação consegue se conectar."}
::option[Fazer uma requisição autorizada a partir da rede da equipe.]{#linux-listening-services-verify-from-client-c .correct explanation="Isso testa o caminho previsto."}
:::

Para verificar quais serviços estão em escuta em um host Linux, comece pela lição Audit Listening Services em [Segurança Linux para DevSecOps](https://labex.io/courses/linux-security-for-devsecops).

## Resumo

Agora você consegue interpretar um endereço de escuta antes de decidir de onde testar o acesso.

1. Liste os sockets TCP locais em escuta com segurança.
2. Distinga loopback de todas as interfaces IPv4.
3. Verifique a conexão a partir do local relevante para o cliente.
