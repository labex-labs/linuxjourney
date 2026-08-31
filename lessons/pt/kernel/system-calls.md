---
lesson_id: "system-calls"
course_id: "kernel"
lang: "pt"
order_index: 3
title: "Chamadas de Sistema"
description: "Aprenda como o código do espaço do usuário invoca serviços do kernel Linux e como inspecionar chamadas com segurança usando `strace`."
meta_title: "Chamadas de Sistema - Kernel"
meta_description: "Explore os fundamentos de uma chamada de sistema no Linux. Aprenda como processos em espaço de usuário usam chamadas de sistema (syscalls) para solicitar serviços do kernel, mudar de modo e como a tabela de syscalls funciona. Use `strace` para ver chamadas de sistema em ação."
meta_keywords: "chamada de sistema linux, chamadas de sistema, tabela syscall, modo kernel, modo usuário, strace, kernel linux, API syscall"
---

Uma chamada de sistema é uma entrada definida no kernel pela qual o código do espaço do usuário solicita uma operação, como abrir um arquivo, mapear memória, criar um processo ou enviar dados pela rede. Antes de agir, o kernel valida argumentos, credenciais, estado do objeto e política de segurança.

## Bibliotecas e a ABI de chamadas de sistema

Aplicativos costumam chamar funções da biblioteca C, em vez de escrever instruções de entrada específicas da arquitetura. Um wrapper prepara registradores e memória conforme a ABI, entra no kernel e traduz o resultado para a convenção da linguagem.

A relação nem sempre é de uma função para uma syscall:

- uma função de biblioteca pode combinar várias chamadas
- algumas funções trabalham inteiramente no espaço do usuário
- uma função vDSO otimizada pode obter certos dados mantidos pelo kernel sem uma transição completa
- uma chamada pode sustentar várias APIs de alto nível

:::single-choice{#system-calls-library-wrapper}
O que um wrapper típico da libc faz?

::option[Prepara argumentos da ABI, entra no kernel e traduz o resultado.]{#system-calls-wrapper-role .correct explanation="O wrapper oculta convenções específicas da arquitetura atrás de uma interface comum de biblioteca."}
::option[Concede ao aplicativo acesso irrestrito à memória do kernel.]{#system-calls-wrapper-unrestricted explanation="A entrada continua controlada, e o kernel valida a solicitação."}
::option[Recompila o kernel sempre que a função é chamada.]{#system-calls-wrapper-compile explanation="A chamada em tempo de execução usa o kernel que já está em execução."}
:::

## Entrada e retorno do kernel

O wrapper coloca o número da chamada e seus argumentos nos locais definidos pela arquitetura, depois executa uma instrução como `syscall` em x86-64 ou `svc` em AArch64. O processador muda para um ponto privilegiado configurado e o kernel despacha a solicitação.

Ao terminar, o kernel retorna um valor ou indicação de erro. Wrappers da biblioteca C normalmente retornam `-1` e definem o `errno` local da thread. Outras linguagens expõem erros de formas diferentes.

Chamar toda entrada de “interrupção de software” é impreciso em arquiteturas atuais; traps, instruções rápidas e supervisor calls implementam transições controladas relacionadas, mas diferentes.

:::single-choice{#system-calls-entry-result}
Quem valida os argumentos e a autorização de uma chamada de sistema?

::option[O prompt do shell antes de o processo iniciar.]{#system-calls-shell-validates explanation="Um processo pode fazer chamadas sem shell, e as verificações do kernel continuam necessárias."}
::option[A implementação do serviço solicitado no kernel.]{#system-calls-kernel-validates .correct explanation="O handler privilegiado verifica ponteiros, estado, credenciais e política antes de agir."}
::option[A tabela de partições do disco.]{#system-calls-partition-validates explanation="Metadados de armazenamento não autorizam serviços arbitrários do kernel."}
:::

## Números e compatibilidade

Números e convenções de chamadas são específicos da arquitetura. A mesma chamada simbólica pode ter outro número ou layout em outra ABI. Versões do kernel podem acrescentar syscalls, enquanto ABIs estáveis procuram preservar comportamentos existentes.

Um processo não privilegiado não insere handlers arbitrários na tabela do kernel em execução. Ampliar a interface exige código do kernel e projeto cuidadoso da ABI. O seccomp pode filtrar chamadas permitidas, mas não cria novas implementações.

:::single-choice{#system-calls-number-portability}
Por que um aplicativo não deve fixar números de syscall de outra arquitetura?

::option[Os números e as convenções são específicos da ABI.]{#system-calls-abi-specific .correct explanation="Um número válido em uma arquitetura pode indicar outra operação ou não existir em outra."}
::option[As chamadas recebem nomes do diretório de trabalho atual.]{#system-calls-directory-names explanation="Caminhos não definem a numeração da ABI."}
::option[Cada processo recebe uma tabela aleatória ao iniciar.]{#system-calls-random-table explanation="A ABI do kernel é estável para uma arquitetura, não aleatória por processo."}
:::

## Rastreamento com `strace`

Rastreie um comando simples e salve a saída separadamente:

```bash
$ strace -o trace.log -- ls
```

Siga processos-filhos autorizados com `-f` ou filtre a saída:

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace` pode revelar caminhos, argumentos, dados do ambiente, endereços de rede, fragmentos de arquivos e credenciais passadas indevidamente. Proteja os traces e remova-os conforme a política de dados.

:::single-choice{#system-calls-strace-purpose}
O que o `strace` observa principalmente?

::option[Apenas linhas do código-fonte executadas no aplicativo.]{#system-calls-strace-source-lines explanation="Rastreamento de fonte exige depuradores ou instrumentação com símbolos."}
::option[Chamadas de sistema e sinais no limite entre usuário e kernel.]{#system-calls-strace-boundary .correct explanation="Ele informa solicitações, argumentos, resultados e sinais dos processos rastreados."}
::option[A tensão física de cada núcleo da CPU.]{#system-calls-strace-voltage explanation="Telemetria de hardware está fora do rastreamento de syscalls."}
:::

## Interpretação cuidadosa dos traces

O rastreamento altera o tempo e pode causar sobrecarga. Uma chamada com falha pode ser uma sondagem esperada, e o erro final pode resultar de operação anterior ou política do aplicativo. Interprete descritores, relações entre processos e logs em conjunto.

Permissões e políticas de ptrace limitam os processos rastreáveis. Não anexe a processos de outro usuário ou de produção sem autorização; pausas e mudanças de tempo podem afetar o serviço.

:::single-choice{#system-calls-strace-failure}
Uma syscall com falha necessariamente significa que o aplicativo está quebrado?

::option[Sim; todo retorno diferente de zero encerra o Linux.]{#system-calls-nonzero-terminates explanation="Aplicativos tratam rotineiramente erros sem provocar falha do sistema."}
::option[Não; programas frequentemente testam alternativas e tratam erros esperados.]{#system-calls-expected-failure .correct explanation="Interprete o retorno no fluxo de controle e no contexto do aplicativo."}
::option[Sim; o kernel nunca retorna erros esperados.]{#system-calls-no-expected-errors explanation="Caminhos ausentes e operações incompatíveis são resultados normais de uma API."}
:::

## Resumo

Agora você consegue acompanhar uma chamada desde a API da biblioteca até o trabalho validado pelo kernel.

1. Separar funções de alto nível da ABI de syscalls.
2. Relacionar instruções de entrada ao despacho controlado do kernel.
3. Tratar números e estruturas como específicos da arquitetura.
4. Usar `strace` filtrado protegendo dados sensíveis.
5. Interpretar falhas e sobrecarga no contexto do aplicativo.
