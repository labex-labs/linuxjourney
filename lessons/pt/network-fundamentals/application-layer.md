---
lang: "pt"
title: "Camada de Aplicação"
meta_description: "Aprenda sobre a Camada de Aplicação no modelo TCP/IP, como ela lida com dados para e-mail (SMTP) e seu papel na comunicação de rede. Entenda as camadas de rede."
meta_keywords: "Camada de Aplicação, modelo TCP/IP, SMTP, camadas de rede, rede Linux, tutorial para iniciantes, comunicação de rede"
---

## Lesson Content

Digamos que eu queira enviar um e-mail para a Patty. Vamos percorrer cada uma das camadas TCP/IP para ver isso em ação.

Lembre-se de que os pacotes são usados para transmitir dados através de redes. Um pacote consiste em um cabeçalho e um payload. O cabeçalho contém informações sobre para onde o pacote está indo e de onde ele veio. O payload é os dados reais que estão sendo transferidos. À medida que nosso pacote atravessa a rede, cada camada adiciona um pouco de informação ao cabeçalho do pacote. Além disso, tenha em mente que diferentes camadas usam um termo diferente para o nosso "pacote". Na camada de transporte, essencialmente encapsulamos nossos dados em um segmento, e na camada de enlace, nos referimos a isso como um frame, mas saiba que "pacote" pode ser usado em relação à mesma coisa.

Primeiro, começamos na camada de aplicação. Quando enviamos nosso e-mail através do nosso cliente de e-mail, a camada de aplicação encapsulará esses dados. A camada de aplicação se comunica com a camada de transporte através de uma porta especificada, e através desta porta, ela envia seus dados. Queremos enviar um e-mail através do protocolo da camada de aplicação SMTP (Simple Mail Transfer Protocol). Os dados são enviados através do nosso protocolo de transporte, que abre uma conexão para esta porta (a porta 25 é usada para SMTP). Então, esses dados são enviados através desta porta, e esses dados são enviados para a camada de Transporte para serem encapsulados em segmentos.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual camada é usada para apresentar os dados do pacote em um formato amigável ao usuário?

## Quiz Answer

Application
