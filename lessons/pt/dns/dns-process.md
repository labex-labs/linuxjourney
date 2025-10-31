---
index: 3
lang: "pt"
title: "Processo DNS"
meta_title: "Processo DNS - DNS"
meta_description: "Explore o processo de resolução DNS passo a passo, de servidores raiz ao servidor DNS autoritativo. Entenda como um servidor Linux encontra um domínio, um conceito crucial para ambientes de produção e hospedagem de domínios."
meta_keywords: "processo DNS, consulta DNS, resolução de domínio, dns linux, servidor de produção, hospedagem de domínio, servidor dns, TLD, servidores raiz, dns autoritativo"
---

## Lesson Content

Vamos explorar como um computador, como um `servidor Linux`, encontra um `domínio` como `catzontheinterwebz.com` usando DNS. O processo funciona como um funil, estreitando a busca até chegarmos ao `servidor DNS` específico que detém a resposta.

### A Consulta Inicial

Primeiro, seu host pergunta ao seu servidor DNS recursivo configurado: "Onde fica `catzontheinterwebz.com`?" Este servidor recursivo, geralmente fornecido pelo seu ISP, provavelmente não sabe a resposta diretamente. Portanto, ele inicia o processo de resolução contatando a autoridade máxima: os Servidores Raiz (Root Servers). Esta etapa inicial é a mesma, quer você esteja navegando de casa ou um `servidor de produção` esteja se comunicando com uma API.

### Servidores Raiz (Root Servers)

A hierarquia DNS da internet começa com 13 Servidores Raiz lógicos, que são espelhados em centenas de locais físicos ao redor do mundo. Esses servidores não sabem o endereço IP de todos os `domínios`, mas sabem quem gerencia os Domínios de Nível Superior (TLDs), como `.com`, `.org` e `.net`. Quando questionado sobre `catzontheinterwebz.com`, um Servidor Raiz responderá: "Eu não sei, mas você deve perguntar ao servidor TLD de `.com`", e fornecerá seu endereço IP.

### Servidores de Domínio de Nível Superior (TLD Servers)

Em seguida, o servidor recursivo envia uma nova consulta ao servidor TLD de `.com`, novamente perguntando sobre a localização de `catzontheinterwebz.com`. O trabalho do servidor TLD é apontar para os servidores de nomes autoritativos corretos para aquele `domínio` específico. Ele não possui o endereço IP final, mas sabe qual `servidor DNS` é responsável pelo `domínio`, um detalhe frequentemente configurado através do seu provedor de `hospedagem de domínio` (domain hosting). O servidor TLD responde com o endereço IP desse servidor de nomes autoritativo.

### Servidor DNS Autoritativo

Finalmente, o servidor recursivo envia um último pedido ao `servidor DNS` autoritativo. Este é o servidor que detém os registros DNS reais para o `domínio` `catzontheinterwebz.com`. Este servidor verifica seus registros, encontra o registro 'A' para o host e retorna o endereço IP final. Esta é uma etapa crítica para quem coloca um site ou aplicação no ar, pois este servidor fornece o elo definitivo entre o nome do `domínio` e o endereço IP do `servidor de produção`. Com o endereço IP em mãos, seu computador pode agora se conectar e recuperar o conteúdo.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da resolução e gerenciamento de DNS:

1. **[Consultar Registros DNS no Linux com dig e nslookup](https://labex.io/pt/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Aprenda a consultar registros DNS como A, PTR e MX, e a identificar seu servidor DNS padrão, essencial para a solução de problemas de rede.
2. **[Configurar um Servidor DNS Autoritativo Local no Linux](https://labex.io/pt/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Ganhe experiência prática instalando e configurando um servidor DNS autoritativo local, definindo zonas e testando a resolução DNS.
3. **[Gerenciar a Resolução de Hostnames Locais no Linux](https://labex.io/pt/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Pratique o gerenciamento da resolução de nomes de host locais editando o arquivo `/etc/hosts`, uma habilidade fundamental para desenvolvimento web e testes de rede.

Estes laboratórios ajudarão você a aplicar os conceitos em cenários reais e a construir confiança com o DNS.

## Quiz Question

Qual é a abreviação para os nameservers onde os endereços .com, .net, .org, etc., são encontrados? Responda usando apenas letras maiúsculas em inglês.

## Quiz Answer

TLD
