---
lesson_id: "tracking-processes-lsof-fuser"
course_id: "process-utilization"
lang: "pt"
order_index: 2
title: "lsof e fuser"
description: "Aprenda a identificar processos que usam arquivos, diretórios, pontos de montagem e sockets de rede."
meta_title: "lsof e fuser - Utilização de Processos"
meta_description: "Conheça os comandos lsof e fuser do Linux para identificar quais processos usam determinados arquivos. Aprenda a resolver erros de dispositivo ocupado e compare fuser e lsof."
meta_keywords: "lsof, fuser, comando fuser, Linux fuser, fuser versus lsof, lsof versus fuser, fuser -k Linux, arquivos abertos, gerenciamento de processos, dispositivo ocupado"
---

Um sistema de arquivos pode continuar ocupado porque um processo possui um arquivo aberto, mapeia um arquivo na memória ou usa um diretório como seu diretório de trabalho atual. `lsof` e `fuser` ajudam a identificar essas relações. Inspecione primeiro; interromper processos é uma decisão separada, com consequências operacionais.

## Listagem de Arquivos Abertos com lsof

`lsof` significa “list open files”. Consulte um caminho para ver os registros correspondentes de arquivos abertos:

```bash
$ sudo lsof -- /mnt/usb
```

Para uma árvore inteira de diretórios no mesmo sistema de arquivos, as implementações normalmente oferecem `+D`, mas as verificações recursivas podem ser caras:

```bash
$ sudo lsof +D /mnt/usb
```

As colunas úteis incluem `COMMAND`, `PID`, `USER`, descritor de arquivo (`FD`), tipo, dispositivo e `NAME`. Um registro cujo `FD` seja `cwd` indica que o processo usa o diretório como seu diretório de trabalho atual. A saída sem privilégios pode ser incompleta para processos de outros usuários.

:::single-choice{#lsof-cwd-record}
O que `cwd` na coluna `FD` indica?

::option[O processo usa esse diretório como seu diretório de trabalho atual.]{#lsof-current-directory .correct explanation="O diretório atual de um processo pode manter um sistema de arquivos montado ocupado."}
::option[O arquivo foi fechado durante uma gravação.]{#lsof-closed-write explanation="O marcador descreve uma relação com um diretório, não um evento de fechamento."}
::option[O processo é proprietário do dispositivo do sistema de arquivos.]{#lsof-device-owner explanation="A propriedade do sistema de arquivos não é representada pelo rótulo de descritor `cwd`."}
:::

## Identificação dos Usuários com fuser

`fuser` informa os IDs dos processos que usam determinado arquivo ou sistema de arquivos. A saída detalhada acrescenta usuários, tipos de acesso e nomes de comandos:

```bash
$ sudo fuser -v /mnt/usb
```

Para tratar o argumento como um sistema de arquivos montado e localizar processos que acessam arquivos dentro dele, use a opção de montagem oferecida pelo `fuser` do procps:

```bash
$ sudo fuser -vm /mnt/usb
```

Verifique se o caminho é o ponto de montagem pretendido com ferramentas como `findmnt --target /mnt/usb`. Montagens bind, namespaces, permissões e condições de corrida podem afetar o que uma única consulta revela.

:::single-choice{#fuser-verbose-purpose}
Por que usar `fuser -v` em vez de `fuser` sem opções durante uma investigação?

::option[Ele desmonta automaticamente o sistema de arquivos selecionado.]{#fuser-verbose-unmount explanation="O modo detalhado informa dados e não solicita uma desmontagem."}
::option[Ele acrescenta contexto, como usuário, tipo de acesso e comando.]{#fuser-verbose-details .correct explanation="As colunas adicionais ajudam a avaliar quais processos podem ser coordenados ou interrompidos com segurança."}
::option[Ele impede permanentemente que os processos reabram os arquivos.]{#fuser-verbose-prevent explanation="A apresentação de um relatório não cria uma regra de controle de acesso."}
:::

## Tratamento de um Sistema de Arquivos Ocupado

Use uma sequência deliberada, em vez de encerrar imediatamente todos os PIDs correspondentes:

1. Confirme o host, o caminho, a origem da montagem e a manutenção pretendida.
2. Identifique os processos com as duas ferramentas quando for viável.
3. Determine se cada processo pode ser interrompido, movido para fora do diretório ou deixado terminar.
4. Interrompa-o pelo gerenciador de serviços ou pela interface da aplicação quando disponível.
5. Consulte novamente, desmonte e verifique o resultado.

`fuser -k` envia um sinal aos processos correspondentes. Seu sinal padrão é `SIGKILL` nas implementações comuns do procps, portanto ele não oferece um encerramento ordenado. Se um encerramento explicitamente aprovado for necessário, selecione um sinal adequado, verifique o PID e o proprietário e considere que o conjunto de processos pode mudar entre a inspeção e a ação.

:::single-choice{#fuser-k-risk}
Por que `fuser -k /mnt/usb` é uma primeira medida inadequada de solução de problemas?

::option[Ele só informa o espaço livre do sistema de arquivos.]{#fuser-k-space explanation="A opção atua sobre processos, em vez de informar a capacidade."}
::option[Ele pode encerrar vários processos correspondentes sem uma limpeza ordenada.]{#fuser-k-kills .correct explanation="A ação ampla do sinal pode interromper gravações ou serviços, portanto a investigação e a coordenação devem vir primeiro."}
::option[Ele altera o diretório de trabalho de todos os processos correspondentes.]{#fuser-k-chdir explanation="Ele envia um sinal e não muda os diretórios dos processos."}
:::

## Escolha da Ferramenta

Use `lsof` quando precisar de registros detalhados de arquivos abertos, descritores ou informações de sockets. Use `fuser` para uma visão orientada a caminhos dos PIDs e tipos de acesso correspondentes. Nenhum resultado, sozinho, informa se é seguro encerrar um processo.

Para sockets de rede, use um namespace de protocolo explícito com `fuser` ou uma ferramenta voltada a sockets, como `ss`:

```bash
$ sudo fuser -v 22/tcp
$ sudo ss -lntp
```

:::single-choice{#lsof-fuser-tool-choice}
Qual ferramenta é adequada para obter uma lista detalhada de descritores de arquivos abertos e seus processos proprietários?

::option[`lsof`]{#lsof-detailed-records .correct explanation="Sua saída é organizada em torno dos registros de arquivos abertos e dos metadados de seus processos."}
::option[`uptime`]{#lsof-uptime explanation="Uptime informa o tempo em atividade e as médias de carga, não descritores abertos."}
::option[`free`]{#lsof-free explanation="Free resume a memória, não o uso de arquivos."}
:::

## Resumo

Agora você sabe investigar o uso de arquivos e sistemas de arquivos sem tratar o encerramento como resposta padrão.

1. Use `lsof` para registros detalhados de arquivos abertos.
2. Use `fuser` para informações de PIDs e acessos orientadas a caminhos.
3. Confirme a montagem e considere permissões e condições de corrida.
4. Coordene uma interrupção ordenada antes de considerar um sinal.
5. Consulte novamente e verifique o resultado da desmontagem ou do serviço.
