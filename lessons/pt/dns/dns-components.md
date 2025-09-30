---
index: 2
lang: "pt"
title: "Componentes DNS"
meta_title: "Componentes DNS - DNS"
meta_description: "Aprenda sobre os componentes do DNS: servidores de nomes, arquivos de zona e registros de recursos. Entenda como o DNS funciona para iniciantes. Comece sua jornada de rede Linux!"
meta_keywords: "componentes DNS, servidor de nomes, arquivo de zona, registros de recursos, tutorial DNS, rede Linux, guia para iniciantes"
---

## Lesson Content

O banco de dados DNS da Internet depende de sites e organizações que fornecem parte desse banco de dados. Para fazer isso, eles precisam:

### Servidor de Nomes

Configuramos o DNS através de "servidores de nomes". Os servidores de nomes carregam nossas configurações de DNS e respondem a quaisquer perguntas de clientes ou outros servidores que queiram saber coisas como "Quem é google.com?". Se o servidor de nomes não souber a resposta a essa consulta, ele redirecionará a solicitação para outros servidores de nomes. Os servidores de nomes podem ser "autoritativos", o que significa que eles contêm os registros DNS reais que você está procurando, ou "recursivos", o que significa que eles perguntariam a outros servidores, e esses servidores perguntariam a outros servidores até encontrarem um servidor autoritativo que contivesse os registros DNS. Servidores recursivos também podem ter as informações que queremos em cache em vez de alcançar um servidor autoritativo.

### Arquivo de Zona

Dentro de um servidor de nomes existe algo chamado arquivos de zona. Os arquivos de zona são a forma como o servidor de nomes armazena informações sobre o domínio ou como chegar ao domínio se ele não souber.

### Registros de Recurso

Um arquivo de zona é composto por entradas de registros de recurso. Cada linha é um registro e contém informações sobre hosts, servidores de nomes, outros recursos, etc. Os campos consistem no seguinte:

- Nome do registro
- TTL - O tempo após o qual descartamos o registro e obtemos um novo. No DNS, o TTL é denotado por tempo, então os registros podem ter um TTL de uma hora. A razão pela qual fazemos isso é porque a Internet está em constante mudança; em um minuto um host pode ser mapeado para o endereço IP X, no próximo ele pode estar no endereço IP Y.
- Class - Espaço de nomes das informações do registro. Mais comumente, IN é usado para Internet.
- Type - Tipo de informação armazenada nos dados do registro. Não entraremos em tipos de registro, mas você provavelmente já viu os comuns como A para endereço, MX para mail exchanger, etc.
- Data - Este campo pode conter um endereço IP se for um registro A ou outra coisa dependendo do tipo de registro.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of DNS and hostname resolution:

1. **[Configurar um Servidor DNS Autoritativo Local no Linux](https://labex.io/pt/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803-592803)** - Pratique a instalação e configuração de um servidor DNS local (`bind9`), definindo zonas e validando sua configuração.
2. **[Consultar Registros DNS no Linux com dig e nslookup](https://labex.io/pt/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Aprenda a usar ferramentas essenciais de linha de comando (`dig`, `nslookup`) para consultar vários tipos de registros DNS e solucionar problemas de DNS.
3. **[Gerenciar Resolução de Nome de Host Local no Linux](https://labex.io/pt/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Entenda como gerenciar a resolução de nome de host local editando o arquivo `/etc/hosts`, uma habilidade fundamental para desenvolvimento e testes.

Esses laboratórios o ajudarão a aplicar os conceitos de DNS e resolução de nome de host em cenários reais e a construir confiança com os serviços de rede.

## Quiz Question

Qual tipo de registro de recurso é usado para mail exchangers?

## Quiz Answer

MX
