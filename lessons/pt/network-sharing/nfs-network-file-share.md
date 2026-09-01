---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "pt"
order_index: 4
title: "NFS"
description: "Aprenda a descobrir, montar, validar e automatizar com segurança uma montagem de cliente NFS."
meta_title: "NFS - Compartilhamento de Rede"
meta_description: "Descubra como usar o Sistema de Arquivos de Rede (NFS) no Linux. Esta lição aborda a configuração de um cliente NFS, o uso do comando mount e a configuração do automount para acesso contínuo a compartilhamentos de rede."
meta_keywords: "NFS, cliente NFS, automount, Sistema de Arquivos de Rede, rede Linux, comando mount, tutorial Linux, iniciante"
---

Network File System permite que um cliente acesse um export do servidor pelo namespace local de arquivos. O servidor controla os exports e boa parte da política; o cliente controla onde e quando um export autorizado é montado.

## Preparação do cliente

Instale os utilitários de cliente NFS da distribuição, normalmente empacotados como `nfs-common` em sistemas da família Debian ou `nfs-utils` em sistemas da família Red Hat. Confirme a acessibilidade pelo DNS ou endereço, as versões NFS permitidas, a política do firewall e o caminho exato da exportação com o administrador do servidor.

`showmount -e SERVER` pode listar exports pelo protocolo antigo de montagem, mas não é autoridade para todo servidor somente NFSv4. Uma falha não prova que não exista export NFSv4 autorizado.

:::single-choice{#nfs-showmount-limit} Por que `showmount -e` pode ser incompleto para NFSv4?

::option[Ele consulta um protocolo antigo de listagem que pode não estar exposto.]{#nfs-showmount-protocol .correct explanation="NFSv4 pode funcionar sem disponibilizar esse serviço separado."}
::option[Ele mostra apenas a temperatura da CPU local.]{#nfs-showmount-temperature explanation="O comando consulta exports de um servidor NFS."}
::option[Ele desativa permanentemente todo export listado.]{#nfs-showmount-disables explanation="A listagem é uma solicitação somente leitura."}
:::

## Montagem de um export

Crie um ponto vazio e dedicado e monte o export aprovado:

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

Especifique uma versão somente quando a política ou a compatibilidade exigirem, por exemplo, `-o vers=4.2`. Não tente adivinhar opções de desempenho nem de segurança. Confirme a origem, o tipo e as opções resultantes:

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands} No comando, o que é `server.example.net:/srv/team`?

::option[O diretório local que oculta o export remoto.]{#nfs-local-mountpoint explanation="O ponto local é `/mnt/team`."}
::option[O nome do pacote cliente a instalar.]{#nfs-package-name explanation="Nomes de pacote variam e não são operandos de fonte."}
::option[O servidor e o caminho remoto exportado.]{#nfs-remote-export .correct explanation="Host e caminho após dois-pontos identificam a fonte NFS."}
:::

## Identidade e permissões

O acesso combina regras do export, segurança do protocolo, identidades numéricas ou serviços de diretório e permissões. Nomes iguais nos dois hosts não garantem IDs iguais. `AUTH_SYS` envia IDs fornecidos pelo cliente e depende de confiança no cliente e na rede; ambientes mais fortes podem usar Kerberos configurado de ponta a ponta.

O servidor costuma mapear root remoto para identidade sem privilégio por root squashing. Não desative essa proteção para corrigir um erro; examine IDs, propriedade, política e modelo de segurança.

:::single-choice{#nfs-name-versus-id} Por que usuários com o mesmo nome podem receber permissões NFS diferentes?

::option[As permissões podem depender do mapeamento numérico de identidade.]{#nfs-numeric-mapping .correct explanation="Nomes iguais não provam que cliente e servidor resolvam o mesmo UID e grupos."}
::option[NFS ignora todas as permissões de arquivos.]{#nfs-ignores-permissions explanation="Permissões do sistema e do export continuam na autorização."}
::option[Toda montagem altera as contas do servidor.]{#nfs-changes-accounts explanation="Uma montagem cliente não reescreve identidades do servidor."}
:::

## Automação de montagens de rede

Uma montagem simples de inicialização em `/etc/fstab` pode atrasar a inicialização quando a rede ou o servidor estão indisponíveis. Dependendo do host, use `autofs` para mapas sob demanda ou opções de montagem do systemd como `_netdev,nofail,x-systemd.automount`, depois de testar a semântica exata delas:

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

Antes de editar fstab, preserve recuperação e valide com parser não destrutivo ou teste controlado. Automount melhora disponibilidade, mas não corrige autorização, DNS ou indisponibilidade.

:::single-choice{#nfs-automount-benefit} Qual é um benefício principal do automount sob demanda?

::option[Ele concede root a todo cliente.]{#nfs-automount-root explanation="O momento da montagem não ignora autorização."}
::option[Ele evita exigir o servidor durante a inicialização inicial.]{#nfs-automount-boot .correct explanation="A conexão ocorre no acesso, em vez de bloquear necessariamente o boot."}
::option[Ele copia todo o servidor para o disco local.]{#nfs-automount-copy explanation="Uma montagem apresenta acesso remoto, não cópia completa."}
:::

## Desmontagem e verificação

Antes de desmontar, coordene processos que usam o compartilhamento e conclua escritas. Depois desmonte e confirme:

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

Desmontagem forçada ou lazy pode ocultar referências ativas e causar erros; reserve-a para falha diagnosticada com plano explícito.

:::single-choice{#nfs-safe-unmount} O que deve preceder uma desmontagem NFS normal?

::option[Coordenar processos usuários e concluir escritas importantes.]{#nfs-coordinate-writers .correct explanation="Remover um sistema ativo pode interromper I/O ou deixar trabalho incompleto."}
::option[Excluir o diretório exportado no servidor.]{#nfs-delete-export explanation="Desmontar no cliente não exige destruir dados."}
::option[Desativar todas as interfaces do cliente.]{#nfs-disable-network explanation="Isso dificulta a conclusão ordenada e não é a sequência normal."}
:::

## Resumo

Agora você consegue operar uma montagem NFS com premissas explícitas de identidade e disponibilidade.

1. Confirmar ferramentas, caminho, protocolo e política de rede.
2. Montar em caminho dedicado e verificar fonte e opções.
3. Diagnosticar permissões por identidade e política do export.
4. Usar montagem sob demanda testada quando o boot importa.
5. Coordenar usuários, desmontar normalmente e verificar.
