---
lesson_id: "process-creation"
course_id: "processes"
lang: "pt"
order_index: 4
title: "Criação de Processos"
description: "Aprenda como fork, exec, PIDs e relações de parentesco participam da criação de processos no Linux."
meta_title: "Criação de Processos - Processos"
meta_description: "Conheça os fundamentos da criação de processos no Linux. Este guia aborda as chamadas de sistema fork e execve, as relações entre pais e filhos (PID e PPID) e a função do processo init."
meta_keywords: "criação de processos no Linux, criar processo Linux, criação de processos no sistema operacional, fork, execve, PID, PPID, processo init, processos Linux"
---

Os processos Linux formam relações entre pais e filhos. Um shell normalmente inicia um comando externo criando um processo filho e fazendo esse filho executar o programa solicitado. A explicação clássica separa esse trabalho nas operações `fork` e `exec`.

## Criação de um Filho com `fork`

A chamada de sistema `fork()` cria um processo filho com base no processo solicitante. O pai e o filho continuam a partir do ponto de retorno de `fork`, mas recebem valores de retorno diferentes e possuem PIDs distintos.

O filho recebe um estado de processo logicamente separado. Inicialmente, o Linux pode compartilhar páginas de memória física usando copy-on-write, copiando uma página somente quando um dos processos a modifica. Os descritores de arquivos abertos são herdados e apontam para as mesmas descrições de arquivos abertos subjacentes, portanto detalhes como os offsets dos arquivos podem continuar compartilhados.

:::single-choice{#process-creation-fork-result} O que uma chamada `fork()` bem-sucedida cria?

::option[Somente um programa substituto dentro do mesmo processo.]{#process-creation-fork-replacement explanation="Substituir a imagem do programa atual é a função de uma operação `exec`."}
::option[Um processo filho com um novo PID.]{#process-creation-fork-child .correct explanation="`fork()` estabelece um processo filho separado e uma relação entre pai e filho."}
::option[Uma cópia permanente e imediata de todas as páginas de memória física.]{#process-creation-fork-full-copy explanation="O Linux normalmente usa copy-on-write, em vez de duplicar antecipadamente todas as páginas físicas."}
:::

## Substituição de um Programa com `execve`

Uma chamada `execve()` carrega um novo programa no processo solicitante. Quando bem-sucedida, ela substitui a imagem do processo e não retorna ao programa antigo. O PID permanece o mesmo porque `execve()` não cria um novo processo.

Por isso, muitos comandos do shell seguem um padrão fork-exec:

1. O shell cria um processo filho.
2. O filho prepara redirecionamentos e outros estados de execução.
3. O filho executa o programa solicitado.
4. O shell aguarda ou continua, dependendo da execução em primeiro ou segundo plano.

Bibliotecas e aplicações podem expor interfaces de nível superior, como `posix_spawn()`, e o Linux possui primitivas adicionais, como `clone()`. O conhecido modelo fork-exec continua sendo útil sem ser a única interface possível.

:::single-choice{#process-creation-exec-pid} O que acontece com o PID de um processo após um `execve()` bem-sucedido?

::option[Ele se torna idêntico ao PID do pai.]{#process-creation-exec-parent-pid explanation="O pai e o filho mantêm IDs de processo separados."}
::option[Ele permanece o mesmo enquanto a imagem do programa é substituída.]{#process-creation-exec-same-pid .correct explanation="`execve()` transforma o processo solicitante, em vez de criar outro processo."}
::option[Ele é removido antes que o novo programa seja iniciado.]{#process-creation-exec-pid-removed explanation="O processo existente continua com seu PID e recebe novo código, dados, pilha e estados relacionados ao programa."}
:::

## Inspeção dos IDs de Pais e Filhos

`PID` identifica o processo, enquanto `PPID` identifica seu pai. Solicite esses campos explicitamente:

```bash
$ ps -o pid,ppid,stat,cmd
```

Se um shell iniciar `ps`, o PID do shell normalmente aparecerá como `PPID` desse processo `ps`. O momento importa: processos de curta duração podem terminar antes que uma observação separada os capture.

:::single-choice{#process-creation-ppid} O que `PPID` representa em uma listagem de processos?

::option[O PID anterior que já foi atribuído ao processo.]{#process-creation-previous-pid explanation="PIDs podem ser reutilizados, mas `PPID` não registra o histórico de identificadores."}
::option[O identificador da prioridade de escalonamento do processo.]{#process-creation-priority-id explanation="A prioridade de escalonamento é representada por outros campos, como priority ou nice."}
::option[O ID do processo pai.]{#process-creation-parent-pid .correct explanation="PPID registra a relação atual do processo com seu pai."}
:::

## PID 1 e Reparentalização

O kernel inicia o primeiro processo do espaço do usuário com o PID 1. Dependendo do sistema, ele pode ser `systemd`, outra implementação de init ou um init pequeno dentro de um contêiner ou namespace de PIDs. O PID 1 inicia e supervisiona partes do ambiente do espaço do usuário e possui responsabilidades especiais de sinais e coleta de processos órfãos.

Quando um pai termina antes de seu filho, o filho é reparentalizado para um subreaper apropriado ou para o processo init de seu namespace de PIDs. Ele não precisa terminar apenas porque seu pai original foi encerrado.

:::single-choice{#process-creation-pid-one} Qual afirmação sobre o PID 1 está correta?

::option[Ele sempre deve ser um programa cujo nome de executável seja exatamente `init`.]{#process-creation-pid-one-name explanation="A implementação pode ser `systemd`, outro init ou um programa específico do contêiner."}
::option[Ele é o pai que criou diretamente todos os processos atualmente em execução.]{#process-creation-pid-one-direct explanation="A maioria dos processos é criada por várias gerações de pais intermediários."}
::option[Ele é o primeiro processo de seu namespace de PIDs e possui responsabilidades semelhantes às de um init.]{#process-creation-pid-one-init .correct explanation="O PID 1 sustenta a supervisão e a coleta de processos do espaço do usuário dentro de um namespace de PIDs."}
:::

O laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) permite observar os IDs de pais e filhos durante a execução de comandos em primeiro e segundo plano.

## Resumo

Agora você sabe acompanhar a sequência clássica de criação de processos no Linux.

1. Use `fork()` para criar um filho com um PID distinto.
2. Use `execve()` para substituir a imagem de um processo sem alterar seu PID.
3. Leia PID e PPID para identificar relações entre pais e filhos.
4. Reconheça o PID 1 e os subreapers como destinos de filhos reparentalizados.
