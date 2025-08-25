---
index: 2
lang: "pt"
title: "Níveis de Privilégio"
meta_title: "Níveis de Privilégio - Kernel"
meta_description: "Aprenda sobre os níveis de privilégio do Linux, modo kernel e modo usuário. Entenda os anéis de proteção e as chamadas de sistema para acesso seguro ao hardware. Comece sua jornada no Linux!"
meta_keywords: "níveis de privilégio Linux, modo kernel, modo usuário, anéis de proteção, chamadas de sistema, segurança Linux, Linux para iniciantes, tutorial Linux"
---

## Lesson Content

As próximas lições serão bastante teóricas, então se você estiver procurando por algo mais prático, pode pular e voltar depois.

Por que temos diferentes camadas de abstração para o espaço do usuário e o kernel? Por que não podemos combinar ambos os poderes em uma única camada? Bem, há uma razão muito boa pela qual essas duas camadas existem separadamente. Ambas operam em modos diferentes: o kernel opera no modo kernel, e o espaço do usuário opera no modo usuário.

No modo kernel, o kernel tem acesso completo ao hardware; ele controla tudo. No modo de espaço do usuário, há uma quantidade muito pequena de memória e CPU seguras que você tem permissão para acessar. Basicamente, quando queremos fazer qualquer coisa que envolva hardware — ler dados de nossos discos, gravar dados em nossos discos, controlar nossa rede, etc. — tudo é feito no modo kernel. Por que isso é necessário? Imagine se sua máquina fosse infectada com spyware; você não gostaria que ele tivesse acesso direto ao hardware do seu sistema. Ele poderia acessar todos os seus dados, sua webcam, etc., e isso não é bom.

Esses diferentes modos são chamados de níveis de privilégio (nomeados apropriadamente pelos níveis de privilégio que você obtém) e são frequentemente descritos como anéis de proteção. Para tornar essa imagem mais fácil de pintar, digamos que você descubra que Britney Spears está na cidade em seu clube local. Ela está protegida por suas groupies, depois por seus guarda-costas pessoais, depois pelo segurança na porta do clube. Você quer pegar o autógrafo dela (porque não?), mas não consegue chegar até ela porque ela está fortemente protegida. Os anéis funcionam da mesma forma: o anel mais interno corresponde ao nível de privilégio mais alto. Existem dois níveis ou modos principais em uma arquitetura de computador x86. O Anel #3 é o privilégio em que os aplicativos do modo de usuário são executados; o Anel #0 é o privilégio em que o kernel é executado. O Anel #0 pode executar qualquer instrução do sistema e recebe total confiança. Então, agora que sabemos como esses níveis de privilégio funcionam, como podemos escrever qualquer coisa em nosso hardware? Não estaremos sempre em um modo diferente do kernel?

A resposta está nas chamadas de sistema. As chamadas de sistema nos permitem executar uma instrução privilegiada no modo kernel e depois voltar para o modo usuário.

## Exercise

Prática leva à perfeição! Compreender os conceitos teóricos de espaço de usuário, espaço de kernel e níveis de privilégio é crucial, mas a experiência prática ajuda a solidificar como esses conceitos se manifestam na administração prática do Linux. Aqui estão alguns laboratórios práticos para reforçar sua compreensão de como as ações de nível de usuário interagem com o sistema subjacente:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique a criação, modificação e exclusão de contas de usuário, o que se relaciona diretamente com o gerenciamento de entidades que operam no espaço do usuário e exigem interação do kernel para ações privilegiadas.
2. **[Gerenciar Permissões de Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Aprenda a controlar o acesso a arquivos e diretórios, um conceito de segurança central que depende do kernel para impor permissões com base nos privilégios do usuário.
3. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Explore como interagir e monitorar processos, que são aplicativos de espaço de usuário que fazem chamadas de sistema para o kernel para gerenciamento de recursos e execução.

Esses laboratórios o ajudarão a aplicar os conceitos de interação do usuário com o sistema Linux, onde o papel do kernel no gerenciamento de recursos e na imposição de privilégios é primordial, e a construir confiança com tarefas fundamentais de administração do Linux.

## Quiz Question

Qual número de anel tem os privilégios mais altos?

## Quiz Answer

0
