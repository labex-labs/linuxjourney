---
index: 2
lang: "es"
title: "Componentes de DNS"
meta_title: "Componentes de DNS - DNS"
meta_description: "Aprende sobre los componentes de DNS: name servers, zone files y resource records. Entiende cómo funciona DNS para principiantes. ¡Comienza tu viaje en redes Linux!"
meta_keywords: "componentes DNS, name server, zone file, resource records, tutorial DNS, redes Linux, guía para principiantes"
---

## Lesson Content

La base de datos DNS de Internet se basa en que los sitios y las organizaciones proporcionan parte de esa base de datos. Para ello, necesitan:

### Name Server

Configuramos DNS a través de "name servers". Los name servers cargan nuestra configuración DNS y responden a cualquier pregunta de clientes u otros servidores que quieran saber cosas como "¿Quién es google.com?". Si el name server no sabe la respuesta a esa consulta, redirigirá la solicitud a otros name servers. Los name servers pueden ser "autoritativos", lo que significa que contienen los registros DNS reales que estás buscando, o "recursivos", lo que significa que preguntarían a otros servidores, y esos servidores preguntarían a otros servidores hasta que encontraran un servidor autoritativo que contuviera los registros DNS. Los servidores recursivos también pueden tener la información que queremos en caché en lugar de contactar con un servidor autoritativo.

### Zone File

Dentro de un name server vive algo llamado zone files. Los zone files son la forma en que el name server almacena información sobre el dominio o cómo llegar al dominio si no lo sabe.

### Resource Records

Un zone file se compone de entradas de resource records. Cada línea es un registro y contiene información sobre hosts, name servers, otros recursos, etc. Los campos consisten en lo siguiente:

- Record name
- TTL - El tiempo después del cual descartamos el registro y obtenemos uno nuevo. En DNS, TTL se denota por tiempo, por lo que los registros podrían tener un TTL de una hora. La razón por la que hacemos esto es porque Internet está en constante cambio; en un minuto un host puede estar mapeado a la dirección IP X, y al siguiente puede estar en la dirección IP Y.
- Class - Espacio de nombres de la información del registro. Más comúnmente, IN se usa para Internet.
- Type - Tipo de información almacenada en los datos del registro. No entraremos en los tipos de registro, pero probablemente hayas visto los comunes como A para address, MX para mail exchanger, etc.
- Data - Este campo puede contener una dirección IP si es un registro A o algo más dependiendo del tipo de registro.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

No hay ejercicios para esta lección.

## Quiz Question

¿Qué tipo de registro de recurso se utiliza para los mail exchangers?

## Quiz Answer

MX
