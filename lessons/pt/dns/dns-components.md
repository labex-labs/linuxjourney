---
lang: "pt"
title: "Componentes DNS"
description: "Aprenda sobre os componentes do DNS: servidores de nomes, arquivos de zona e registros de recursos. Entenda como o DNS funciona para iniciantes. Comece sua jornada de rede Linux!"
keywords: "componentes DNS, servidor de nomes, arquivo de zona, registros de recursos, tutorial DNS, rede Linux, guia para iniciantes"
---

## Lesson Content

O banco de dados DNS da Internet depende de sites e organizações que fornecem parte desse banco de dados. Para fazer isso, eles precisam:

### Name Server

Configuramos o DNS via "servidores de nomes" (name servers). Os servidores de nomes carregam nossas configurações de DNS e respondem a quaisquer perguntas de clientes ou outros servidores que desejam saber coisas como "Quem é google.com?". Se o servidor de nomes não souber a resposta a essa consulta, ele redirecionará a solicitação para outros servidores de nomes. Os servidores de nomes podem ser "autoritativos", o que significa que eles contêm os registros DNS reais que você está procurando, ou "recursivos", o que significa que eles perguntariam a outros servidores, e esses servidores perguntariam a outros servidores até encontrarem um servidor autoritativo que contivesse os registros DNS. Servidores recursivos também podem ter as informações que queremos em cache, em vez de alcançar um servidor autoritativo.

### Zone File

Dentro de um servidor de nomes existe algo chamado arquivos de zona (zone files). Os arquivos de zona são a forma como o servidor de nomes armazena informações sobre o domínio ou como chegar ao domínio se ele não souber.

### Resource Records

Um arquivo de zona é composto por entradas de registros de recursos (resource records). Cada linha é um registro e contém informações sobre hosts, servidores de nomes, outros recursos, etc. Os campos consistem no seguinte:

- Record name
- TTL - O tempo após o qual descartamos o registro e obtemos um novo. No DNS, TTL é denotado por tempo, então os registros podem ter um TTL de uma hora. A razão pela qual fazemos isso é porque a Internet está em constante mudança; em um minuto um host pode ser mapeado para o endereço IP X, e no próximo ele pode estar no endereço IP Y.
- Class - Namespace das informações do registro. Mais comumente, IN é usado para Internet.
- Type - Tipo de informação armazenada nos dados do registro. Não entraremos em tipos de registro, mas você provavelmente já viu os comuns como A para endereço, MX para mail exchanger, etc.
- Data - Este campo pode conter um endereço IP se for um registro A ou outra coisa dependendo do tipo de registro.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

No exercises for this lesson.

## Quiz Question

Qual tipo de registro de recurso é usado para mail exchangers?

## Quiz Answer

MX
