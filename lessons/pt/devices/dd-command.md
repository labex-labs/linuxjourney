---
lesson_id: "dd-command"
course_id: "devices"
lang: "pt"
order_index: 7
title: "dd"
description: "Aprenda como `dd` copia fluxos de blocos e como evitar erros destrutivos de entrada, saída e tamanho."
meta_title: "dd - Dispositivos"
meta_description: "Conheça a poderosa ferramenta dd do Linux. Este guia explica como usar o comando dd para copiar dados, criar imagens de discos e backups, incluindo opções como if, of e bs."
meta_keywords: "comando dd, dd Linux, ferramenta dd, copiar dados, imagem de disco, tutorial Linux, iniciante, guia, backup de dados"
---

`dd` copia dados de um fluxo de entrada para um fluxo de saída enquanto aplica os tamanhos de blocos e as conversões solicitados. Ele não compreende sistemas de arquivos, limites de partições nem se um destino de saída contém dados valiosos. Isso o torna útil para imagens e dispositivos brutos — e imediatamente destrutivo quando o destino está errado.

## Entrada, Saída e Tamanho de Bloco

Um comando possui este formato geral:

```bash
$ dd if=input.img of=output.img bs=4M status=progress
```

- `if=` seleciona a entrada; sem ele, `dd` lê da entrada padrão.
- `of=` seleciona a saída; sem ele, `dd` grava na saída padrão.
- `bs=` define o tamanho dos blocos de entrada e saída para uma cópia comum.
- `status=progress` solicita que o `dd` do GNU informe periodicamente o progresso da transferência.

`dd` copia blocos, não necessariamente um byte por vez. Um `bs` maior pode reduzir a sobrecarga das chamadas de sistema, mas o valor ideal depende dos dispositivos, do alinhamento, do cache e da carga de trabalho. Ele não altera os dados lógicos copiados.

:::single-choice{#dd-command-output-operand} Qual operando seleciona o destino gravado por `dd`?

::option[`if=`]{#dd-command-input-file explanation="`if` identifica a origem de entrada."}
::option[`of=`]{#dd-command-output-file .correct explanation="`of` nomeia o fluxo ou arquivo de saída que recebe os dados copiados."}
::option[`bs=`]{#dd-command-block-size explanation="`bs` escolhe um tamanho de bloco de transferência, não um caminho."}
:::

## Limitação da Cópia

`count=` limita o número de blocos de entrada processados. Para um arquivo de entrada comum:

```bash
$ dd if=source.img of=prefix.img bs=1M count=2 status=progress
```

Isso solicita dois blocos de entrada de até 1 MiB cada, portanto copia no máximo 2 MiB. Leituras curtas podem complicar a multiplicação simples em fluxos como pipes; o `dd` do GNU oferece `iflag=fullblock` quando são necessários blocos de entrada completos. Diferencie unidades binárias e a sintaxe dos sufixos conforme a implementação local.

:::single-choice{#dd-command-count-result} Para um arquivo comum, qual quantidade máxima `bs=1M count=2` solicita?

::option[1 MiB.]{#dd-command-one-mib explanation="Isso corresponderia a um bloco do tamanho selecionado."}
::option[2 MiB.]{#dd-command-two-mib .correct explanation="Dois blocos de entrada multiplicados por 1 MiB por bloco resultam em um máximo de 2 MiB."}
::option[2 GiB.]{#dd-command-two-gib explanation="No `dd` do GNU, o sufixo `M` indica blocos com tamanho de mebibytes, não gibibytes."}
:::

## Gravação de uma Imagem em um Dispositivo de Bloco

Uma restauração bruta pode se parecer com esta:

```bash
$ sudo dd if=backup.img of=/dev/sdX bs=4M status=progress conv=fsync
```

`/dev/sdX` é deliberadamente um marcador, não um comando para copiar. Antes de substituí-lo:

1. Mantenha um backup testado de todos os dados valiosos.
2. Identifique o destino pelo modelo, número de série, tamanho, transporte e link persistente usando `lsblk`, `udevadm` ou ferramentas equivalentes.
3. Confirme que nenhuma partição do destino esteja montada, usada como swap, integrada a RAID ou LVM ou aberta por outro serviço.
4. Verifique novamente o dispositivo após qualquer desconexão, reinicialização ou alteração da topologia.
5. Garanta que a imagem caiba e que a gravação de todo o dispositivo seja realmente pretendida.

O dispositivo de saída é sobrescrito desde o início. Inverter `if` e `of`, selecionar o disco do sistema ou usar um disco inteiro quando a intenção era uma partição pode destruir dados sem uma solicitação de confirmação.

:::single-choice{#dd-command-target-verification} Qual é o motivo mais importante para verificar o modelo, o número de série, o tamanho e o uso ativo antes de uma gravação bruta em um dispositivo?

::option[As letras dos dispositivos podem mudar, e `dd` sobrescreve o destino selecionado sem compreender seu conteúdo.]{#dd-command-target-can-change .correct explanation="As verificações de identidade e uso reduzem o risco de destruir outro disco ou uma pilha de armazenamento ativa."}
::option[`dd` se recusa a gravar se o rótulo do sistema de arquivos não corresponder à imagem.]{#dd-command-label-check explanation="A ferramenta não realiza essa verificação de segurança baseada no sistema de arquivos."}
::option[Dispositivos de bloco não podem ser abertos enquanto existir qualquer backup.]{#dd-command-backup-prevents-open explanation="Um backup não impede tecnicamente as gravações; quando mantido e testado, ele oferece recuperação."}
:::

## Criação de uma Imagem Consistente

Ler um dispositivo de bloco ativo enquanto seu sistema de arquivos está sendo alterado pode produzir uma imagem internamente inconsistente. Prefira um sistema de arquivos desmontado, um snapshot consistente com a aplicação ou um fluxo documentado de congelamento e snapshot. Bancos de dados e máquinas virtuais podem exigir seus próprios procedimentos de suspensão das alterações.

Uma imagem bruta do dispositivo copia blocos, incluindo os metadados do sistema de arquivos e regiões não utilizadas. Por isso, ela pode ser muito maior que um backup no nível dos arquivos e pode reproduzir identificadores que precisam ser alterados antes de montar um clone junto do original.

:::single-choice{#dd-command-live-filesystem-image} Por que criar a imagem de um sistema de arquivos montado e em alteração pode não ser confiável?

::option[Sistemas de arquivos montados nunca permitem leituras do dispositivo de bloco.]{#dd-command-mounted-no-read explanation="Leituras brutas podem ser possíveis, por isso a consistência precisa ser planejada, não presumida."}
::option[Blocos diferentes podem ser lidos em momentos diferentes do estado do sistema de arquivos.]{#dd-command-inconsistent-moments .correct explanation="Alterações simultâneas podem fazer a imagem de blocos coletada não representar um único ponto consistente no tempo."}
::option[`dd` converte automaticamente o sistema de arquivos em um arquivo tar.]{#dd-command-converts-tar explanation="A ferramenta copia dados brutos e não cria um arquivo compactado com conhecimento do sistema de arquivos."}
:::

## Conclusão e Verificação

O comando terminar sem um erro de E/S não comprova que a origem e o destino pretendidos foram selecionados nem que a imagem possa ser usada. Registre as identidades e os tamanhos exatos, garanta que a saída em buffer tenha chegado ao armazenamento, compare uma leitura posterior com limites apropriados ou hashes criptográficos e teste a recuperação conforme o plano de backup.

Não divulgue passagens de sobrescrita com `dd` como apagamento seguro garantido para SSDs, camadas de tradução de flash, armazenamento com provisionamento dinâmico, snapshots ou setores remapeados. Use a sanitização compatível com o dispositivo e a plataforma junto com uma política explícita de destruição de dados.

:::single-choice{#dd-command-success-meaning} O que um status de saída zero de `dd` não comprova por si só?

::option[Que o comando interpretou todos os operandos fornecidos.]{#dd-command-parsed-operands explanation="Operandos inválidos normalmente causam um erro, não uma conclusão bem-sucedida."}
::option[Que o operador selecionou a origem e o destino pretendidos.]{#dd-command-does-not-prove-intent .correct explanation="A ferramenta pode copiar com sucesso para o destino errado, pois não consegue deduzir a intenção do operador."}
::option[Que o processo chegou ao caminho normal de encerramento.]{#dd-command-normal-exit explanation="Um status zero indica sucesso no nível do comando, mas não a correção semântica dos destinos escolhidos."}
:::

Pratique somente com arquivos comuns ou discos virtuais descartáveis antes de trabalhar com hardware bruto. Os conceitos de partições e sistemas de arquivos em [Gerenciamento de Partições e Sistemas de Arquivos Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) fornecem um contexto essencial.

## Resumo

Agora você sabe analisar `dd` como uma ferramenta de cópia bruta de blocos sem conhecimento da intenção.

1. Diferencie `if`, `of`, `bs` e `count`.
2. Verifique a identidade persistente do destino e todos os seus consumidores ativos.
3. Crie imagens a partir de um estado de armazenamento consistente.
4. Sincronize, verifique e teste a recuperação após uma cópia.
5. Trate toda saída para um dispositivo bruto como potencialmente destrutiva.
