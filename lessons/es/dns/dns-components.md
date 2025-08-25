---
index: 2
lang: "es"
title: "Componentes DNS"
meta_title: "Componentes DNS - DNS"
meta_description: "Aprende sobre los componentes de DNS: servidores de nombres, archivos de zona y registros de recursos. Comprende cómo funciona DNS para principiantes. ¡Comienza tu viaje en redes Linux!"
meta_keywords: "componentes DNS, servidor de nombres, archivo de zona, registros de recursos, tutorial DNS, redes Linux, guía para principiantes"
---

## Lesson Content

La base de datos DNS de Internet se basa en que los sitios y las organizaciones proporcionan parte de esa base de datos. Para ello, necesitan:

### Servidor de Nombres

Configuramos DNS a través de "servidores de nombres". Los servidores de nombres cargan nuestra configuración DNS y responden a cualquier pregunta de clientes u otros servidores que quieran saber cosas como "¿Quién es google.com?". Si el servidor de nombres no sabe la respuesta a esa consulta, redirigirá la solicitud a otros servidores de nombres. Los servidores de nombres pueden ser "autoritativos", lo que significa que contienen los registros DNS reales que estás buscando, o "recursivos", lo que significa que preguntarían a otros servidores, y esos servidores preguntarían a otros servidores hasta que encontraran un servidor autoritativo que contuviera los registros DNS. Los servidores recursivos también pueden tener la información que queremos en caché en lugar de llegar a un servidor autoritativo.

### Archivo de Zona

Dentro de un servidor de nombres reside algo llamado archivos de zona. Los archivos de zona son la forma en que el servidor de nombres almacena información sobre el dominio o cómo llegar al dominio si no lo sabe.

### Registros de Recursos

Un archivo de zona se compone de entradas de registros de recursos. Cada línea es un registro y contiene información sobre hosts, servidores de nombres, otros recursos, etc. Los campos consisten en lo siguiente:

- Nombre del registro
- TTL - El tiempo después del cual descartamos el registro y obtenemos uno nuevo. En DNS, TTL se denota por tiempo, por lo que los registros podrían tener un TTL de una hora. La razón por la que hacemos esto es porque Internet está cambiando constantemente; en un minuto un host puede estar mapeado a una dirección IP X, y al siguiente puede estar en una dirección IP Y.
- Clase - Espacio de nombres de la información del registro. Más comúnmente, IN se usa para Internet.
- Tipo - Tipo de información almacenada en los datos del registro. No entraremos en los tipos de registros, pero probablemente hayas visto los comunes como A para dirección, MX para intercambiador de correo, etc.
- Datos - Este campo puede contener una dirección IP si es un registro A o algo más dependiendo del tipo de registro.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de DNS y la resolución de nombres de host:

1. **[Configurar un servidor DNS autoritativo local en Linux](https://labex.io/es/labs/linux-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Practica la instalación y configuración de un servidor DNS local (`bind9`), la definición de zonas y la validación de tu configuración.
2. **[Consultar registros DNS en Linux con dig y nslookup](https://labex.io/es/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Aprende a usar herramientas esenciales de línea de comandos (`dig`, `nslookup`) para consultar varios tipos de registros DNS y solucionar problemas de DNS.
3. **[Administrar la resolución local de nombres de host en Linux](https://labex.io/es/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Comprende cómo administrar la resolución local de nombres de host editando el archivo `/etc/hosts`, una habilidad clave para el desarrollo y las pruebas.

Estos laboratorios te ayudarán a aplicar los conceptos de DNS y resolución de nombres de host en escenarios reales y a generar confianza con los servicios de red.

## Quiz Question

¿Qué tipo de registro de recurso se utiliza para los intercambiadores de correo?

## Quiz Answer

MX
