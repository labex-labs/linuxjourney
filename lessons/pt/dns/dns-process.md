---
lang: "pt"
title: "Processo DNS"
meta_description: "Aprenda como o DNS funciona passo a passo, desde os servidores raiz até o DNS autoritativo. Entenda o processo de pesquisa de DNS para usuários iniciantes e intermediários."
meta_keywords: "processo DNS, pesquisa DNS, como o DNS funciona, tutorial DNS, DNS para iniciantes, DNS Linux, TLD, servidores raiz"
---

## Lesson Content

Vamos ver um exemplo de como seu host encontra um domínio (catzontheinterwebz.com) com DNS. Essencialmente, nós afunilamos nosso caminho até chegarmos ao servidor DNS que conhece esse domínio.

### Local DNS Server

Primeiro, nosso host pergunta: "Onde está catzontheinterwebz.com?" Nosso servidor DNS local não sabe, então ele vai e começa do topo do funil para perguntar aos Root Servers. Tenha em mente que nosso host não está fazendo essas requisições para encontrar catzontheinterwebz.com diretamente; a maioria dos usuários fala com um servidor DNS recursivo fornecido por seus ISPs, e esse servidor é então encarregado de encontrar a localização de catzontheinterwebz.com.

### Root Servers

Existem 13 Root Servers para a Internet. Eles são espelhados e distribuídos ao redor do mundo para lidar com requisições DNS para a Internet, então existem realmente centenas de servidores que estão trabalhando. Eles são controlados por diferentes organizações e contêm informações sobre Top-Level Domains. Top-level domains são o que você conhece como endereços .org, .com, .net, etc. Então o Root Server não sabe onde catzontheinterwebz.com está, mas ele nos diz para perguntar ao DNS Server de Top-Level Domain .com em um endereço IP que ele nos fornece.

### Top-Level Domain

Então agora enviamos outra requisição para o servidor de nomes que conhece endereços ".com" e perguntamos se ele sabe onde catzontheinterwebz.com está. O TLD não tem catzontheinterwebz.com em seus arquivos de zona, mas ele vê um registro para o servidor de nomes para catzontheinterwebz.com. Então ele nos dá o endereço IP desse servidor de nomes e nos diz para procurar lá.

### Authoritative DNS Server

Agora enviamos uma requisição final para o servidor DNS que realmente tem o registro que queremos. O servidor de nomes vê que ele tem um arquivo de zona para catzontheinterwebz.com, e há um registro de recurso para 'www' para este host. Ele então nos dá o endereço IP deste host, e finalmente podemos ver alguns gatos na Internet.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é a abreviação para os servidores de nomes onde os endereços .com, .net, .org, etc., são encontrados?

## Quiz Answer

TLD
