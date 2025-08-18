---
lang: "pt"
title: "Níveis de Privilégio"
meta_description: "Aprenda sobre os níveis de privilégio do Linux, modo kernel e modo de usuário. Entenda os anéis de proteção e as chamadas de sistema para acesso seguro ao hardware. Comece sua jornada no Linux!"
meta_keywords: "níveis de privilégio Linux, modo kernel, modo de usuário, anéis de proteção, chamadas de sistema, segurança Linux, Linux para iniciantes, tutorial Linux"
---

## Lesson Content

As próximas lições serão bastante teóricas, então se você estiver procurando por algo mais prático, pode pular e voltar depois.

Por que temos diferentes camadas de abstração para o espaço do usuário e o kernel? Por que não podemos combinar ambos os poderes em uma única camada? Bem, há uma razão muito boa para que essas duas camadas existam separadamente. Ambas operam em modos diferentes: o kernel opera em kernel mode, e o espaço do usuário opera em user mode.

Em kernel mode, o kernel tem acesso completo ao hardware; ele controla tudo. Em user mode, há uma quantidade muito pequena de memória segura e CPU que você tem permissão para acessar. Basicamente, quando queremos fazer qualquer coisa que envolva hardware — ler dados de nossos discos, gravar dados em nossos discos, controlar nossa rede, etc. — tudo é feito em kernel mode. Por que isso é necessário? Imagine se sua máquina fosse infectada com spyware; você não gostaria que ele tivesse acesso direto ao hardware do seu sistema. Ele poderia acessar todos os seus dados, sua webcam, etc., e isso não é bom.

Esses diferentes modos são chamados de níveis de privilégio (nome apropriado para os níveis de privilégio que você obtém) e são frequentemente descritos como anéis de proteção. Para tornar essa imagem mais fácil de pintar, digamos que você descubra que Britney Spears está na cidade em seu clube local. Ela está protegida por suas groupies, depois por seus guarda-costas pessoais, e depois pelo segurança na porta do clube. Você quer pegar o autógrafo dela (porque não?), mas não consegue chegar até ela porque ela está fortemente protegida. Os anéis funcionam da mesma forma: o anel mais interno corresponde ao nível de privilégio mais alto. Existem dois níveis ou modos principais em uma arquitetura de computador x86. O Anel #3 é o privilégio em que as aplicações em user mode são executadas; o Anel #0 é o privilégio em que o kernel é executado. O Anel #0 pode executar qualquer instrução do sistema e recebe total confiança. Então, agora que sabemos como esses níveis de privilégio funcionam, como podemos escrever qualquer coisa em nosso hardware? Não estaremos sempre em um modo diferente do kernel?

A resposta está nas chamadas de sistema. As chamadas de sistema nos permitem executar uma instrução privilegiada em kernel mode e depois voltar para user mode.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual número de anel tem os maiores privilégios?

## Quiz Answer

0
