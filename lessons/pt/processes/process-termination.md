---
lesson_id: "process-termination"
course_id: "processes"
lang: "pt"
order_index: 5
title: "Encerramento de Processos"
description: "Aprenda como status de saída, espera, zumbis e reparentalização completam o ciclo de vida dos processos Linux."
meta_title: "Encerramento de Processos - Processos"
meta_description: "Conheça o encerramento de processos Linux, a chamada de sistema wait e as principais diferenças entre processos zumbis e órfãos."
meta_keywords: "encerramento de processos Linux, processo zumbi, processo órfão, zumbi versus órfão, encerrar processo filho Linux, chamada de sistema wait, _exit, gerenciamento de processos"
---

Um processo pode terminar retornando de sua função principal, chamando uma interface de saída ou sendo encerrado por um sinal. O kernel libera a maioria de seus recursos, mas a contabilização entre pai e filho continua até que o pai colete as informações de encerramento.

## Status de Saída

Um programa que termina normalmente fornece um status inteiro. Por convenção, o status `0` significa sucesso, enquanto um valor diferente de zero informa algum tipo de falha ou resultado alternativo. Os significados exatos dos valores diferentes de zero pertencem à interface do programa.

Em um shell, inspecione o status do pipeline em primeiro plano mais recente com:

```bash
$ command
$ printf '%s\n' "$?"
```

Os shells expõem um intervalo limitado de status codificados e também representam o encerramento por sinais, portanto esse valor não é um registro de diagnóstico completo. Os programas devem documentar seus próprios códigos de saída.

:::single-choice{#process-termination-success-status}
Pela convenção Unix, qual status de saída normal indica sucesso?

::option[`1`]{#process-termination-status-one explanation="Muitos programas usam `1` para uma falha geral, embora os significados sejam específicos do comando."}
::option[`0`]{#process-termination-status-zero .correct explanation="Um status normal zero indica convencionalmente a conclusão bem-sucedida."}
::option[`255`]{#process-termination-status-255 explanation="Esse valor é diferente de zero e não representa convencionalmente o sucesso."}
:::

## Espera e Coleta

O kernel registra como um filho terminou e notifica seu pai. O pai usa uma função da família de chamadas de sistema `wait()` para recuperar essas informações. A coleta do registro é chamada de reaping.

A espera também pode coordenar a execução: um shell aguarda um comando em primeiro plano antes de exibir outro prompt, mas pode adiar a espera por uma tarefa em segundo plano. Um pai de longa duração bem projetado deve se organizar para coletar seus filhos sem bloquear trabalhos não relacionados.

:::single-choice{#process-termination-wait-purpose}
O que uma operação wait bem-sucedida permite que um pai recupere?

::option[As informações de encerramento do filho.]{#process-termination-wait-status .correct explanation="A família wait informa como um filho foi interrompido ou terminou e coleta um filho concluído."}
::option[Uma cópia do antigo espaço de endereços do filho.]{#process-termination-wait-memory explanation="A maior parte da memória do processo já foi liberada e não é devolvida ao pai por `wait()`."}
::option[A propriedade de todos os arquivos que o filho abriu.]{#process-termination-wait-files explanation="A espera não transfere metadados de propriedade do sistema de arquivos."}
:::

## Processos Zumbis

Depois que um filho termina, mas antes que seu registro de encerramento seja coletado, ele aparece como zumbi, normalmente com o estado `Z` em `ps`. Ele não executa mais nem mantém um espaço de endereços comum, mas uma entrada mínima na tabela de processos e informações de contabilização permanecem.

Enviar um sinal a um zumbi não pode fazê-lo terminar novamente. Corrija o acúmulo persistente de zumbis diagnosticando o pai que não está aguardando, reiniciando ou corrigindo esse pai por um procedimento operacional adequado ou permitindo a reparentalização para um processo que fará a coleta. Grandes quantidades podem esgotar a capacidade de PIDs ou da tabela de processos.

:::single-choice{#process-termination-zombie-definition}
Qual descrição corresponde a um processo zumbi?

::option[Um filho em execução cujo pai já terminou.]{#process-termination-zombie-orphan explanation="Isso descreve um filho órfão, não um estado zumbi."}
::option[Um filho concluído cujo registro de encerramento ainda não foi coletado.]{#process-termination-zombie-unreaped .correct explanation="O processo deixou de executar, mas o kernel mantém um estado mínimo para seu pai."}
::option[Um processo que consome CPU em um loop ininterrupto.]{#process-termination-zombie-cpu explanation="Um zumbi não executa instruções nem consome tempo de CPU."}
:::

## Órfãos e Reparentalização

Se um pai termina enquanto seu filho continua, o kernel reparentaliza esse filho para um subreaper elegível ou para o processo init do namespace de PIDs relevante. O filho pode estar em execução, dormindo, interrompido ou tornar-se um zumbi mais tarde; “órfão” descreve a perda da relação com o pai original, não um estado de execução.

O processo adotante passa a ser responsável por coletar o status de encerramento. Gerenciadores de serviços modernos e ambientes de contêineres tornam importante não presumir que o novo pai sempre seja o PID 1 do host.

:::single-choice{#process-termination-orphan-definition}
O que acontece quando um processo sobrevive a seu pai original?

::option[Ele é reparentalizado para um subreaper elegível ou para o processo init do namespace.]{#process-termination-orphan-reparented .correct explanation="O kernel preserva uma relação válida de parentesco atribuindo um processo adotante."}
::option[Ele se torna imediatamente um zumbi, mesmo que ainda não tenha terminado.]{#process-termination-orphan-zombie explanation="O estado zumbi começa somente depois que a execução termina e o status aguarda a coleta."}
::option[Ele perde permanentemente seu PID e continua anonimamente.]{#process-termination-orphan-no-pid explanation="Um órfão ativo mantém sua identidade de processo enquanto a relação de parentesco muda."}
:::

Use o laboratório [Gerenciamento e Monitoramento de Processos Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) para observar códigos de saída e estados de processos sem afetar uma carga de trabalho de produção.

## Resumo

Agora você sabe diferenciar o fim da execução da limpeza realizada pelo pai.

1. Interprete zero como sucesso convencional e os status diferentes de zero pela documentação do programa.
2. Use a espera para coletar as informações de encerramento de um filho.
3. Reconheça um zumbi como encerrado, mas ainda não coletado.
4. Reconheça um órfão como um filho reparentalizado depois que seu pai original termina.
