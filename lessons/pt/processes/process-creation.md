---
lang: "pt"
title: "Criação de Processos"
meta_title: "Criação de Processos - Processos"
meta_description: "Aprenda sobre a criação de processos Linux, fork e processos pai/filho. Entenda PID, PPID e o processo init. Obtenha um guia para iniciantes em gerenciamento de processos Linux."
meta_keywords: "criação de processo Linux, fork, PID, PPID, processo init, processos Linux, iniciante, tutorial, guia"
---

## Lesson Content

Novamente, esta lição e a próxima são puramente informativas para que você possa ver o que está por baixo do capô. Sinta-se à vontade para revisitar isso depois de ter trabalhado um pouco mais com processos.

Quando um novo processo é criado, um processo existente basicamente se clona usando algo chamado chamada de sistema `fork` (chamadas de sistema serão discutidas muito no futuro). A chamada de sistema `fork` cria um processo filho quase idêntico. Este processo filho assume um novo ID de processo (PID), e o processo original se torna seu processo pai e tem algo chamado ID de processo pai **PPID**. Depois, o processo filho pode continuar a usar o mesmo programa que seu pai estava usando antes ou, mais frequentemente, usar a chamada de sistema `execve` para iniciar um novo programa. Esta chamada de sistema destrói o gerenciamento de memória que o kernel colocou em prática para esse processo e configura novos para o novo programa.

Podemos ver isso em ação:

```bash
ps l
```

A opção `l` nos dá um "formato longo" ou uma visão ainda mais detalhada de nossos processos em execução. Você verá uma coluna rotulada **PPID**; este é o ID do pai. Agora olhe para o seu terminal; você verá um processo em execução que é o seu shell. Então, no meu sistema, tenho um processo executando `bash`. Agora, lembre-se de que quando você executou o comando `ps l`, você o estava executando a partir do processo que estava executando `bash`. Você verá que o **PID** do shell `bash` é o **PPID** do comando `ps l`.

Então, se todo processo tem que ter um pai e eles são apenas forks um do outro, deve haver uma mãe de todos os processos, certo? Você está correto. Quando o sistema inicializa, o kernel cria um processo chamado **init**; ele tem um PID de 1. O processo `init` não pode ser encerrado a menos que o sistema seja desligado. Ele é executado com privilégios de root e executa muitos processos que mantêm o sistema funcionando. Analisaremos mais de perto o `init` no curso de inicialização do sistema; por enquanto, saiba apenas que é o processo que gera todos os outros processos.

## Exercise

Observe seus processos em execução. Você consegue ver quais outros processos têm pais?

## Quiz Question

Qual chamada de sistema cria um novo processo?

## Quiz Answer

fork
