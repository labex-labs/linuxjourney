---
lesson_id: "filesystem-repair"
course_id: "filesystem"
lang: "pt"
order_index: 10
title: "Reparo de Sistemas de Arquivos"
description: "Aprenda a diagnosticar danos no sistema de arquivos e escolher um fluxo de reparo offline, específico do tipo e com backups."
meta_title: "Reparo de Sistemas de Arquivos - O Sistema de Arquivos"
meta_description: "Aprenda a usar fsck para reparar sistemas de arquivos Linux e recuperar dados. Entenda como verificar e corrigir erros de disco com as ferramentas apropriadas."
meta_keywords: "fsck, reparo de sistemas de arquivos, comandos Linux, erros de disco, recuperação de dados, tutorial Linux, guia para iniciantes"
---

O reparo de um sistema de arquivos reescreve metadados para restaurar sua consistência interna. Ele pode descartar referências ou dados danificados e agravar a perda quando o hardware de armazenamento está falhando. Trate o reparo como uma operação de recuperação: preserve primeiro as evidências e os dados recuperáveis e só então use a ferramenta documentada para o sistema de arquivos exato.

## Diagnóstico antes do Reparo

Sintomas como erros de E/S, remontagens somente para leitura, arquivos ausentes ou falhas de montagem não comprovam todos uma corrupção do sistema de arquivos. Primeiro, reúna evidências somente para leitura:

```bash
$ findmnt --target /affected/path
$ lsblk -f
$ journalctl -k -b
```

Verifique a pilha de armazenamento, a integridade do dispositivo, os cabos ou o caminho de rede, o estado do RAID, a criptografia e os eventos recentes. Se o dispositivo estiver falhando, verificações repetidas podem consumir sua vida útil restante. Quando possível, capture uma imagem ou um clone com uma ferramenta voltada à recuperação e trabalhe sobre a cópia.

:::single-choice{#filesystem-repair-first-response}
O que deve preceder um reparo do sistema de arquivos capaz de gravar quando uma falha de hardware é possível?

::option[Executar repetidamente todas as ferramentas de reparo até uma delas retornar zero.]{#filesystem-repair-repeat-tools explanation="Usar ferramentas incompatíveis e realizar gravações repetidas pode agravar os danos."}
::option[Criar imediatamente uma nova tabela de partições sobre o dispositivo.]{#filesystem-repair-new-table explanation="Sobrescrever os metadados do layout destrói evidências e pode dificultar a recuperação."}
::option[Preservar os dados recuperáveis ou uma imagem e investigar a integridade do dispositivo.]{#filesystem-repair-preserve-first .correct explanation="O reparo modifica metadados, enquanto uma mídia com falha pode se deteriorar durante acessos repetidos."}
:::

## Identificação do Sistema de Arquivos e do Dispositivo Exatos

Determine se o sistema de arquivos reside em uma partição, volume lógico, dispositivo RAID, mapeamento criptografado ou disco inteiro. Não execute um verificador em `/dev/sda` apenas porque uma partição filha como `/dev/sda1` está afetada.

Use `lsblk -f`, `blkid`, `findmnt` e ferramentas das camadas de armazenamento para mapear o destino. As assinaturas de detecção podem estar desatualizadas, portanto compare-as com a configuração conhecida e os backups.

:::single-choice{#filesystem-repair-target-layer}
Se o ext4 estiver armazenado em `/dev/sda1`, qual camada seu verificador de ext4 normalmente deve receber?

::option[`/dev/sda`, independentemente de sua tabela de partições.]{#filesystem-repair-whole-disk explanation="O disco inteiro contém a tabela de partições e possivelmente várias regiões filhas, não diretamente a instância ext4."}
::option[`/dev/sda1`, depois de ficar offline com segurança.]{#filesystem-repair-partition-target .correct explanation="O verificador atua sobre o dispositivo de bloco que contém diretamente esse sistema de arquivos."}
::option[`/mnt/data`, enquanto as aplicações continuam gravando nele.]{#filesystem-repair-live-mount explanation="O caminho do ponto de montagem não é o destino offline de dispositivo de bloco esperado pelo verificador."}
:::

## Colocação do Sistema de Arquivos Offline

A maioria dos verificadores tradicionais de consistência exige que o sistema de arquivos esteja desmontado. Um sistema montado muda enquanto o verificador o lê, e as gravações de reparo podem entrar em conflito com o estado em cache do kernel, causando corrupção.

Interrompa os serviços dependentes, desmonte os sistemas de arquivos aninhados, mova os diretórios de trabalho dos processos e desative as camadas superiores conforme necessário. Para o sistema de arquivos raiz, inicialize um ambiente de resgate ou use o mecanismo documentado de verificação offline da distribuição. Confirme com `findmnt` que o destino não esteja montado no namespace relevante.

:::single-choice{#filesystem-repair-mounted-risk}
Por que um sistema de arquivos normalmente deve estar desmontado antes que um verificador de reparo grave nele?

::option[Atualizações simultâneas do kernel e do verificador podem entrar em conflito e corromper metadados.]{#filesystem-repair-concurrent-writes .correct explanation="Uma visão offline impede que o sistema de arquivos mude durante a operação de reparo."}
::option[A desmontagem restaura automaticamente todos os arquivos danificados a partir do backup.]{#filesystem-repair-unmount-restores explanation="O desanexo oferece consistência para a verificação, mas não restaura dados."}
::option[As ferramentas de sistemas de arquivos só podem ler diretórios, nunca dispositivos de bloco.]{#filesystem-repair-tools-directories explanation="As ferramentas de reparo normalmente atuam diretamente sobre dispositivos de bloco offline."}
:::

## Uso da Ferramenta Específica do Sistema de Arquivos

`fsck` é uma interface capaz de invocar auxiliares específicos de sistemas de arquivos. Ele não é um único mecanismo universal de reparo. Alguns exemplos de fluxos distintos são `e2fsck` para sistemas ext, `xfs_repair` para XFS e as ferramentas de diagnóstico e recuperação específicas do Btrfs.

Opções com nomes semelhantes podem possuir semânticas diferentes. Em particular, não aplique opções `--repair` ou de força copiadas do guia de outro sistema de arquivos. Leia o manual instalado e a documentação atual do projeto ou da distribuição sobre recuperação. Comece por um modo sem modificações ou de diagnóstico quando a implementação oferecer um modo confiável, capture a saída e compreenda os reparos propostos.

:::single-choice{#filesystem-repair-fsck-role}
Pelo que `fsck` normalmente é responsável no Linux?

::option[Encaminhar verificações a um auxiliar apropriado ao tipo do sistema de arquivos.]{#filesystem-repair-fsck-dispatch .correct explanation="A lógica real de validação e reparo pertence a ferramentas e fluxos específicos do formato."}
::option[Converter todos os sistemas de arquivos para ext4 antes de verificá-los.]{#filesystem-repair-fsck-convert explanation="Um verificador precisa preservar e compreender o formato existente."}
::option[Reparar setores de hardware com falha e garantir que não haja perda de dados.]{#filesystem-repair-fsck-hardware explanation="As ferramentas de consistência do sistema de arquivos não podem reparar o hardware físico nem garantir a recuperação dos dados."}
:::

## Verificação e Restauração do Serviço

Registre a ferramenta de reparo, a versão, as opções, a saída e o status de retorno. Após o reparo, repita as verificações da integridade do dispositivo, monte primeiro somente para leitura quando for apropriado, inspecione os dados essenciais e compare-os com backups conhecidos. Depois, restaure gradualmente as montagens e os serviços normais enquanto monitora os logs do kernel e das aplicações.

Um sistema de arquivos voltar a ser montável não comprova que todos os arquivos estejam corretos. Restaure a partir dos backups os dados de aplicações perdidos ou danificados e valide-os no nível da aplicação.

:::single-choice{#filesystem-repair-mountable-proof}
Uma montagem bem-sucedida após o reparo comprova que todos os dados das aplicações estão corretos?

::option[Não; o reparo de consistência e a validação de dados no nível da aplicação são diferentes.]{#filesystem-repair-not-data-proof .correct explanation="O sistema de arquivos pode estar estruturalmente montável enquanto arquivos ou transações continuam ausentes ou danificados."}
::option[Sim; a montagem verifica criptograficamente todos os arquivos em relação a um backup.]{#filesystem-repair-mount-verifies explanation="Uma montagem comum não realiza uma comparação completa com o backup."}
::option[Sim; as ferramentas de reparo recriam automaticamente todo conteúdo desconhecido.]{#filesystem-repair-recreates-data explanation="O reparo de metadados não pode deduzir dados arbitrários perdidos dos usuários."}
:::

## Resumo

Agora você sabe planejar o reparo de um sistema de arquivos como um procedimento de recuperação em etapas.

1. Diagnostique o hardware e preserve os dados recuperáveis antes de gravar.
2. Mapeie a camada exata de blocos que contém o sistema de arquivos.
3. Coloque o sistema de arquivos offline no namespace relevante.
4. Use a ferramenta documentada de diagnóstico e reparo específica do sistema de arquivos.
5. Valide separadamente a integridade do dispositivo, o estado do sistema de arquivos e os dados das aplicações.
