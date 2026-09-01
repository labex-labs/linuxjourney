---
lesson_id: "application-layer"
course_id: "network-basics"
lang: "pt"
order_index: 5
title: "Camada de aplicação"
description: "Aprenda como os protocolos de aplicação definem mensagens de serviço, estado, nomenclatura e comportamento de segurança."
meta_title: "Camada de aplicação - Fundamentos de rede"
meta_description: "Explore a camada de aplicação, a camada superior do modelo TCP/IP. Aprenda o que é um protocolo da camada de aplicação, veja um exemplo com SMTP e entenda como os dados da aplicação são preparados para a comunicação de rede."
meta_keywords: "camada de aplicação, a camada de aplicação, protocolo da camada de aplicação, exemplo de protocolo da camada de aplicação, cabeçalho da camada de aplicação, modelo TCP/IP, SMTP, protocolos de rede"
---

A camada de aplicação do TCP/IP contém os protocolos que as aplicações usam para solicitar e fornecer serviços de rede. Ela abrange muitas funções que a terminologia OSI separa nas camadas de aplicação, apresentação e sessão.

## Mensagens e semântica dos protocolos

Um protocolo de aplicação define como os pares interpretam mensagens e estados. O HTTP define solicitações, respostas, métodos, códigos de estado e campos. O DNS define consultas e registros de recursos. O SMTP define comandos e respostas para a transferência de mensagens.

Nem todo protocolo de aplicação acrescenta um “cabeçalho de aplicação” fixo. Alguns usam campos textuais, outros registros binários, outros vários formatos aninhados, e alguns transportam uma sequência contínua de mensagens por uma única conexão de transporte.

:::single-choice{#application-layer-protocol-role} O que um protocolo de aplicação define principalmente?

::option[O significado e as regras de troca das mensagens do serviço.]{#application-layer-message-semantics .correct explanation="Os pares precisam compartilhar sintaxe, semântica e comportamento de estado para interoperar."}
::option[A tensão em cada cabo Ethernet.]{#application-layer-voltage explanation="A sinalização física pertence à tecnologia das camadas inferiores."}
::option[A rota escolhida independentemente por cada roteador da Internet.]{#application-layer-router-choice explanation="As decisões de roteamento são um comportamento da camada de rede."}
:::

## Clientes, servidores e pares

Um cliente inicia uma solicitação ou conexão com um serviço; um servidor escuta ou aceita essa interação de outra forma. Esses são papéis em uma interação, não categorias permanentes de dispositivos. Um host pode ser cliente de DNS e servidor de SSH ao mesmo tempo, e alguns protocolos usam papéis ponto a ponto.

:::single-choice{#application-layer-client-role} O que torna um programa o cliente em uma troca típica de solicitação e resposta?

::option[Ele inicia uma solicitação ao serviço.]{#application-layer-client-initiates .correct explanation="Cliente e servidor descrevem papéis de interação que um host pode desempenhar simultaneamente para serviços diferentes."}
::option[Ele precisa ser executado em um laptop, e não em um servidor.]{#application-layer-client-laptop explanation="A categoria do hardware não determina o papel no protocolo."}
::option[Ele é proprietário do prefixo IP de destino.]{#application-layer-client-prefix explanation="A propriedade da rede não tem relação com o início de uma solicitação da aplicação."}
:::

## Nomes, portas e seleção de serviços

Uma aplicação pode resolver um nome de serviço para um ou mais endereços IP e escolher um ponto de extremidade de transporte. Portas conhecidas fornecem valores padrão, não uma prova imutável de um protocolo. O HTTP geralmente usa a porta TCP 80 e o HTTPS, a porta TCP 443, mas ambos podem operar em outros lugares. O SMTP usa portas e políticas diferentes para retransmissão e envio de mensagens.

:::single-choice{#application-layer-port-limit} O que uma porta TCP 443 aberta comprova por si só?

::option[Que um processo aceitou um ponto de extremidade TCP ali, mas o comportamento de sua aplicação ainda precisa ser testado.]{#application-layer-port-endpoint .correct explanation="A troca de protocolo e a validação TLS fornecem evidências mais fortes na camada de aplicação."}
::option[Que o serviço é definitivamente uma aplicação HTTPS configurada corretamente.]{#application-layer-port-proves-https explanation="Um número de porta não valida o comportamento do protocolo, a identidade nem a integridade."}
::option[Que o DNS não pode retornar um endereço IPv6.]{#application-layer-port-dns explanation="As portas de transporte não restringem as famílias de registros DNS."}
:::

## Segurança e testes de ponta a ponta

O TLS pode acrescentar confidencialidade, integridade e identidade autenticada do par quando a validação do certificado e o nome do ponto de extremidade estão corretos. Ele não autoriza automaticamente todas as ações da aplicação. Teste o mesmo nome, família de endereços, porta, protocolo, credenciais e solicitação usados pelo cliente real.

Por exemplo, um diagnóstico de HTTPS pode verificar separadamente a resolução, a conexão TCP, o certificado e o nome TLS, a resposta HTTP e o conteúdo da aplicação. O sucesso em uma etapa delimita o problema, mas não comprova todas as etapas posteriores.

:::single-choice{#application-layer-tls-limit} O que a validação bem-sucedida de um certificado TLS estabelece?

::option[Que todos os usuários estão autorizados a acessar todos os recursos.]{#application-layer-tls-all-users explanation="A autenticação do transporte não substitui a política de acesso da aplicação."}
::option[A identidade do par para o nome validado e um canal seguro autenticado.]{#application-layer-tls-identity .correct explanation="A autorização da aplicação e a correção do conteúdo ainda exigem verificações próprias."}
::option[Que nenhum roteador poderá descartar um pacote posterior.]{#application-layer-tls-routing explanation="O TLS não pode garantir a entrega futura pela rede."}
:::

## Resumo

Agora você pode descrever o comportamento da camada de aplicação além de um número de porta ou nome de programa.

1. Identifique sintaxe, semântica e estado do protocolo como questões da aplicação.
2. Trate cliente e servidor como papéis em uma troca.
3. Use portas como convenções de ponto de extremidade, não como prova do protocolo.
4. Teste nomenclatura, segurança e respostas da aplicação de ponta a ponta.
