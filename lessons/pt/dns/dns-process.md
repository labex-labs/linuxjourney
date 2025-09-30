---
index: 3
lang: "pt"
title: "Processo DNS"
meta_title: "Processo DNS - DNS"
meta_description: "Aprenda como o DNS funciona passo a passo, desde os servidores raiz até o DNS autoritativo. Entenda o processo de pesquisa de DNS para usuários iniciantes e intermediários."
meta_keywords: "processo DNS, pesquisa DNS, como o DNS funciona, tutorial DNS, DNS para iniciantes, DNS Linux, TLD, servidores raiz"
---

## Lesson Content

Vamos ver um exemplo de como seu host encontra um domínio (catzontheinterwebz.com) com DNS. Essencialmente, nós afunilamos nosso caminho até chegarmos ao servidor DNS que conhece esse domínio.

### Servidor DNS Local

Primeiro, nosso host pergunta: "Onde está catzontheinterwebz.com?" Nosso servidor DNS local não sabe, então ele vai e começa do topo do funil para perguntar aos Servidores Raiz. Tenha em mente que nosso host não está fazendo essas requisições para encontrar catzontheinterwebz.com diretamente; a maioria dos usuários fala com um servidor DNS recursivo fornecido por seus ISPs, e esse servidor é então encarregado de encontrar a localização de catzontheinterwebz.com.

### Servidores Raiz

Existem 13 Servidores Raiz para a Internet. Eles são espelhados e distribuídos ao redor do mundo para lidar com requisições DNS para a Internet, então existem realmente centenas de servidores que estão trabalhando. Eles são controlados por diferentes organizações e contêm informações sobre Domínios de Nível Superior. Domínios de nível superior são o que você conhece como endereços .org, .com, .net, etc. Então o Servidor Raiz não sabe onde catzontheinterwebz.com está, mas ele nos diz para perguntar ao Servidor DNS de Domínio de Nível Superior .com em um endereço IP que ele nos dá.

### Domínio de Nível Superior

Então agora enviamos outra requisição para o servidor de nomes que conhece os endereços ".com" e perguntamos se ele sabe onde catzontheinterwebz.com está. O TLD não tem catzontheinterwebz.com em seus arquivos de zona, mas ele vê um registro para o servidor de nomes para catzontheinterwebz.com. Então ele nos dá o endereço IP desse servidor de nomes e nos diz para procurar lá.

### Servidor DNS Autoridade

Agora enviamos uma requisição final para o servidor DNS que realmente tem o registro que queremos. O servidor de nomes vê que ele tem um arquivo de zona para catzontheinterwebz.com, e há um registro de recurso para 'www' para este host. Ele então nos dá o endereço IP deste host, e finalmente podemos ver alguns gatos na Internet.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão da resolução e gerenciamento de DNS:

1. **[Consultar Registros DNS no Linux com dig e nslookup](https://labex.io/pt/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Aprenda a consultar registros DNS como A, PTR e MX, e identificar seu servidor DNS padrão, essencial para a solução de problemas de rede.
2. **[Configurar um Servidor DNS Autoridade Local no Linux](https://labex.io/pt/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Ganhe experiência prática instalando e configurando um servidor DNS autoridade local, definindo zonas e testando a resolução de DNS.
3. **[Gerenciar Resolução de Nome de Host Local no Linux](https://labex.io/pt/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Pratique o gerenciamento da resolução de nome de host local editando o arquivo `/etc/hosts`, uma habilidade chave para desenvolvimento web e testes de rede.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com DNS.

## Quiz Question

Qual é a abreviação para os servidores de nomes onde os endereços .com, .net, .org, etc., são encontrados?

## Quiz Answer

TLD
