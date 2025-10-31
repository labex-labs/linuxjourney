---
index: 2
lang: "pt"
title: "Níveis de Privilégio"
meta_title: "Níveis de Privilégio - Kernel"
meta_description: "Explore os conceitos centrais dos níveis de privilégio do Linux. Esta lição explica a diferença entre modo kernel e modo usuário, o papel dos anéis de proteção e como as chamadas de sistema fornecem acesso privilegiado ao hardware. Entenda como o kernel gerencia a segurança e os privilégios do kernel."
meta_keywords: "Níveis de privilégio Linux, modo kernel, modo usuário, anéis de proteção, chamadas de sistema, acesso privilegiado, privilégios do kernel, qual a diferença entre modo kernel e modo usuário, segurança Linux"
---

## Lesson Content

As próximas lições cobrem conceitos mais teóricos. Se você prefere prática, sinta-se à vontade para pular e retornar a esses tópicos mais tarde.

Um aspecto fundamental da arquitetura Linux é a separação entre o espaço do usuário (user space) e o kernel. Mas por que não podemos combinar seus poderes em uma única camada? A razão é a segurança e a estabilidade, o que é alcançado fazendo com que operem em modos diferentes.

### Qual é a Diferença Entre Modo Kernel e Modo Usuário

O sistema opera em dois modos distintos: modo kernel e modo usuário. Essa separação é crucial para proteger o hardware e os recursos do sistema contra acesso direto e descontrolado por aplicações.

Em **modo kernel**, o kernel tem acesso completo e irrestrito ao hardware; ele controla tudo. Este é o nível mais alto de privilégio.

Em **modo usuário**, as aplicações têm acesso muito limitado a uma pequena e segura porção da memória e dos recursos da CPU.

Quando uma aplicação de usuário precisa realizar uma ação envolvendo hardware — como ler de um disco, enviar dados pela rede ou acessar um periférico — ela não pode fazer isso diretamente. Essas operações devem ser tratadas pelo kernel em modo kernel. Esse design impede que um programa com falha ou malicioso comprometa todo o sistema. Por exemplo, você não gostaria que um spyware tivesse acesso direto ao hardware, pois ele poderia ler todos os seus dados ou controlar sua webcam.

### Anéis de Proteção e Acesso Privilegiado

Esses modos diferentes são frequentemente descritos como **níveis de privilégio** ou **anéis de proteção**. Imagine uma fortaleza com paredes concêntricas: a área mais interna é a mais segura e possui a maior autoridade. Os anéis de proteção em um computador funcionam de forma semelhante, com o anel mais interno correspondendo ao nível de privilégio mais alto.

Em uma arquitetura de computador x86 padrão, existem dois níveis principais:

- **Anel 0 (Ring 0):** É onde o kernel é executado. Ele possui o mais alto nível de **privilégios de kernel**, pode executar qualquer instrução do sistema e recebe total confiança para gerenciar o hardware. Este é o cerne do **acesso privilegiado**.
- **Anel 3 (Ring 3):** É o nível onde as aplicações em modo usuário são executadas. É o anel com menos privilégios e não tem acesso direto ao hardware.

Este modelo de segurança baseado em anéis garante que as aplicações de usuário fiquem isoladas dos componentes críticos do sistema. Mas se as aplicações estão sempre em um modo diferente do kernel, como elas podem realizar as operações de hardware necessárias?

### Chamadas de Sistema e Privilégios de Kernel

A ponte entre o modo usuário e o modo kernel é a **chamada de sistema (system call)**. Quando uma aplicação de usuário precisa realizar uma tarefa privilegiada, ela faz uma chamada de sistema para solicitar que o kernel execute a ação em seu nome.

Esse processo permite que a aplicação transite temporária e seguramente do modo usuário para o modo kernel para executar uma instrução específica e controlada. Assim que a tarefa é concluída, o sistema retorna ao modo usuário. Esse mecanismo garante que as aplicações possam obter os serviços de que precisam sem ganhar acesso privilegiado direto e perigoso ao hardware.

## Exercise

Praticar é fundamental! Entender os conceitos teóricos de espaço do usuário, espaço do kernel e níveis de privilégio é crucial, mas a experiência prática ajuda a solidificar como esses conceitos se manifestam na administração prática do Linux. Aqui estão alguns laboratórios práticos para reforçar sua compreensão de como as ações de nível de usuário interagem com o sistema subjacente:

1. **[Gerenciar Contas de Usuário Linux com useradd, usermod e userdel](https://labex.io/pt/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratique a criação, modificação e exclusão de contas de usuário, o que se relaciona diretamente com o gerenciamento de entidades que operam no espaço do usuário e requerem interação com o kernel para ações privilegiadas.
2. **[Gerenciar Permissões de Arquivos e Diretórios no Linux](https://labex.io/pt/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Aprenda a controlar o acesso a arquivos e diretórios, um conceito central de segurança que depende do kernel para impor permissões com base nos privilégios do usuário.
3. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Explore como interagir e monitorar processos, que são aplicações em espaço de usuário que fazem chamadas de sistema para o kernel para gerenciamento de recursos e execução.

Esses laboratórios ajudarão você a aplicar os conceitos de interação do usuário com o sistema Linux, onde o papel do kernel no gerenciamento de recursos e na imposição de privilégios é fundamental, e a construir confiança com tarefas fundamentais de administração Linux.

## Quiz Question

Qual número de anel possui os maiores privilégios?

## Quiz Answer

0
