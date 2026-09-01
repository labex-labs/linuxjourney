---
lesson_id: "etc-fstab-file-system-table"
course_id: "filesystem"
lang: "pt"
order_index: 7
title: "/etc/fstab"
description: "Aprenda a definir associações persistentes de sistemas de arquivos e swap em `/etc/fstab` e validá-las com segurança."
meta_title: "/etc/fstab - O Sistema de Arquivos"
meta_description: "Aprenda a usar o arquivo /etc/fstab no Linux para montar sistemas de arquivos automaticamente durante o boot. Este guia aborda a sintaxe, a edição segura e sua função na inicialização."
meta_keywords: "fstab, fstab Linux, etc fstab, /etc/fstab, arquivo fstab, montar sistemas de arquivos, boot Linux, tutorial fstab"
---

`/etc/fstab`, a tabela de sistemas de arquivos, declara sistemas de arquivos, áreas de swap, montagens bind, origens de rede e outras associações que as ferramentas do sistema podem montar ou ativar. As entradas podem participar da inicialização, mas opções como `noauto`, a integração com montagens automáticas e a política do gerenciador de serviços afetam quando ou se isso acontece.

## Os Seis Campos

Uma entrada convencional possui seis campos separados por espaços em branco:

```text
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /data ext4 defaults,nosuid,nodev 0 2
```

1. **Origem**: um caminho de dispositivo, `UUID=`, `LABEL=`, uma origem de rede ou outra especificação compatível.
2. **Destino**: o ponto de montagem, ou `none` para usos como swap quando apropriado.
3. **Tipo**: o tipo do sistema de arquivos, `swap`, `none` ou um tipo automático aceito.
4. **Opções**: uma lista separada por vírgulas interpretada pelos auxiliares de montagem e camadas de integração.
5. **Campo dump**: controla historicamente o utilitário de backup `dump`; `0` normalmente desabilita a participação.
6. **Campo pass**: controla a ordem de `fsck` durante o boot quando aplicável; `0` desabilita a verificação automática por esse mecanismo.

Os espaços em branco dentro de um campo devem ser escapados com a sintaxe do fstab, como `\040` para um espaço. Um `#` inicia um comentário fora de um campo.

:::single-choice{#fstab-field-count} Quantos campos uma entrada normal de `/etc/fstab` contém?

::option[Quatro.]{#fstab-four-fields explanation="Origem, destino, tipo e opções são seguidos pelos campos dump e pass."}
::option[Oito.]{#fstab-eight-fields explanation="Oito não é a quantidade padrão de campos de um registro do fstab."}
::option[Seis.]{#fstab-six-fields .correct explanation="O formato tradicional contém os campos origem, destino, tipo, opções, dump e pass."}
:::

## Identificadores Estáveis da Origem

Para sistemas de arquivos locais, um UUID de sistema de arquivos costuma ser mais estável que a enumeração `/dev/sdX`:

```bash
$ lsblk -f
$ sudo blkid
```

Use `UUID=...` somente depois de confirmar que o identificador pertence ao sistema de arquivos pretendido. A reformatação cria um novo UUID, e clones no nível dos blocos podem duplicá-lo. Por sua vez, `PARTUUID=` identifica uma entrada da tabela de partições e possui uma semântica diferente.

:::single-choice{#fstab-uuid-source} O que `UUID=...` no campo de origem normalmente identifica?

::option[A conta de usuário proprietária do ponto de montagem.]{#fstab-user-uuid explanation="A identidade da conta não é selecionada pela sintaxe de origem com UUID do sistema de arquivos."}
::option[Os metadados do sistema de arquivos que contêm esse UUID.]{#fstab-filesystem-uuid .correct explanation="Mount resolve o identificador do sistema de arquivos para um dispositivo de bloco disponível, em vez de depender do nome de enumeração."}
::option[O processo que desmontou o sistema de arquivos pela última vez.]{#fstab-process-uuid explanation="O histórico dos processos não é codificado por esse campo de origem."}
:::

## Opções de Montagem e Campos de Verificação

`defaults` se expande para um conjunto convencional de opções definido pela implementação; ele não é necessariamente a política mais segura para todas as montagens. Adicione opções com base na confiança e na carga de trabalho, como acesso somente para leitura ou restrições a nós de dispositivos e ao comportamento setuid. Sistemas de arquivos de rede e removíveis podem exigir políticas de timeout, dependências ou tolerância a falhas para que o boot não fique bloqueado inesperadamente.

Nos sistemas de arquivos compatíveis com `fsck`, o sistema de arquivos raiz usa convencionalmente pass `1`, e outros sistemas de arquivos locais verificados usam pass `2`. As práticas específicas de cada sistema podem ser diferentes — por exemplo, alguns tipos não usam o fsck genérico durante o boot — portanto siga a documentação do sistema de arquivos instalado e da distribuição, em vez de atribuir `2` mecanicamente.

:::single-choice{#fstab-pass-zero} O que um valor `0` no sexto campo solicita?

::option[Ignorar para essa entrada a ordenação automática do fsck realizada por meio do fstab.]{#fstab-pass-zero-skip .correct explanation="Pass zero exclui a entrada da sequência de verificação durante o boot controlada por esse campo."}
::option[Montar o sistema de arquivos somente para leitura em todas as circunstâncias.]{#fstab-pass-zero-readonly explanation="O comportamento somente para leitura pertence ao campo de opções de montagem."}
::option[Apagar o sistema de arquivos antes de cada inicialização.]{#fstab-pass-zero-erase explanation="O campo pass não formata nem apaga um sistema de arquivos."}
:::

## Edição com um Caminho de Recuperação

Uma entrada inválida para a raiz, o boot ou uma rede obrigatória pode interromper a inicialização. Antes de editar:

1. Confirme um backup atual e o acesso pelo console ou por um modo de resgate.
2. Copie o arquivo existente preservando as permissões.
3. Verifique a identidade da origem e crie o ponto de montagem pretendido.
4. Faça uma única alteração de escopo restrito.
5. Valide e teste antes de reiniciar.

Não coloque credenciais diretamente em uma entrada do fstab legível por todos. Use o mecanismo protegido de credenciais do auxiliar de montagem correspondente.

:::single-choice{#fstab-editing-recovery} Por que o acesso de resgate deve ser confirmado antes de alterar uma entrada essencial do fstab?

::option[As edições do fstab sempre apagam a tabela de partições imediatamente.]{#fstab-no-partition-erase explanation="A edição do texto não reescreve as partições do disco, embora montagens posteriores possam ter efeitos."}
::option[O arquivo só pode ser editado a partir de outro sistema operacional.]{#fstab-other-os-only explanation="Ele pode ser editado no Linux com os privilégios e as proteções adequados."}
::option[Uma entrada incorreta pode impedir que o boot normal chegue a um sistema utilizável.]{#fstab-boot-failure .correct explanation="Falhas em montagens essenciais podem entrar no modo de emergência ou bloquear serviços dependentes."}
:::

## Validação sem Presumir o Sucesso

Comece com uma verificação estática quando houver suporte:

```bash
$ sudo findmnt --verify --verbose
```

Em seguida, teste a nova entrada específica sob condições controladas, confirme-a com `findmnt` e desmonte se o teste for temporário. `mount -a` tenta várias entradas elegíveis e pode acessar redes ou anexar origens não pretendidas; ele também ignora entradas já montadas e com `noauto`, portanto não é um verificador inofensivo de sintaxe nem uma prova completa.

Em sistemas baseados no systemd, recarregue a configuração do gerenciador após editar o fstab para atualizar as unidades de montagem geradas e verifique as dependências e o comportamento do boot conforme a documentação local.

:::single-choice{#fstab-mount-a-limit} Por que `mount -a` não é, sozinho, uma validação completa do fstab?

::option[Ele sempre reformata todos os dispositivos listados antes de montá-los.]{#fstab-mount-a-formats explanation="Mount normalmente não cria sistemas de arquivos."}
::option[Ele pode ignorar entradas e realizar operações reais amplas de montagem, em vez de verificar apenas a sintaxe.]{#fstab-mount-a-incomplete .correct explanation="Registros já montados ou com `noauto` podem não ser testados, enquanto origens elegíveis podem causar efeitos ativos."}
::option[Ele lê somente o histórico do shell e ignora o fstab.]{#fstab-mount-a-history explanation="O comando consulta o fstab para as entradas elegíveis."}
:::

Pratique no laboratório [Gerenciamento de Partições e Sistemas de Arquivos Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) com o armazenamento secundário seguro para recuperação fornecido pelo laboratório.

## Resumo

Agora você sabe ler e validar uma entrada persistente da tabela de sistemas de arquivos.

1. Interprete os campos origem, destino, tipo, opções, dump e pass.
2. Selecione um identificador verificado com a semântica de identidade pretendida.
3. Escolha a política de montagem e verificação para o sistema de arquivos real.
4. Preserve o acesso de resgate e faça uma alteração de escopo restrito por vez.
5. Combine a validação estática, a montagem específica e as verificações da política de boot.
