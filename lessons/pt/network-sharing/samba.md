---
lesson_id: "samba"
course_id: "network-sharing"
lang: "pt"
order_index: 5
title: "Samba"
description: "Aprenda a configurar, validar, acessar e proteger um compartilhamento básico do Samba."
meta_title: "Samba - Compartilhamento de Rede"
meta_description: "Aprenda a configurar um compartilhamento de rede Samba no Linux. Este guia abrange o protocolo Samba, instalação, configuração e uso de clientes smb linux para conectar-se a compartilhamentos."
meta_keywords: "Samba, smb linux, linux smb, rede samba, protocolo samba, smb samba, compartilhamento de arquivos, smb.conf, cifs, smbclient, tutorial linux"
---

Samba implementa o protocolo Server Message Block em sistemas Unix-like, permitindo compartilhar arquivos e impressoras entre Linux, Windows, macOS e outros clientes. Implantações modernas usam dialetos SMB atuais; o termo antigo CIFS ainda aparece em ferramentas Linux, mas não é motivo para habilitar o obsoleto SMB1.

## Planejamento do compartilhamento

Antes de instalar ou mudar, defina clientes autorizados, identidades, leitura e escrita, zona de rede, proprietário dos dados, backup e dialeto exigido. Use um diretório dedicado, sem expor acidentalmente uma árvore pessoal ou do sistema.

O acesso é controlado pelas regras do Samba e pelas permissões do sistema de arquivos. Permitir escrita em `smb.conf` não concede acesso que a conta não possui localmente.

:::single-choice{#samba-two-permission-layers}
O que deve permitir a escrita por um compartilhamento Samba?

::option[Apenas o comentário exibido pelo compartilhamento.]{#samba-comment-permission explanation="Um comentário é texto descritivo e não concede acesso."}
::option[As regras do Samba e as permissões do sistema de arquivos.]{#samba-policy-and-filesystem .correct explanation="A solicitação precisa passar pela política do protocolo e pela autorização local."}
::option[Apenas o papel de parede do cliente.]{#samba-wallpaper explanation="A aparência do cliente não controla arquivos do servidor."}
:::

## Definição de um compartilhamento básico

A configuração principal costuma ser `/etc/samba/smb.conf`:

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

Crie o diretório com propriedade e permissões revisadas:

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

O bit set-group-ID ajuda novas entradas a herdar o grupo do diretório, mas o acesso colaborativo também pode exigir uma ACL ou uma máscara de criação escolhida cuidadosamente. Teste os resultados reais dos arquivos e diretórios em vez de presumir que a herança é suficiente.

:::single-choice{#samba-valid-users}
O que expressa `valid users = @teamshare`?

::option[Todo usuário anônimo recebe escrita.]{#samba-every-anonymous explanation="A regra restringe o acesso, em vez de habilitar guest."}
::option[O servidor deve renomear o share para `teamshare`.]{#samba-rename-share explanation="O nome visível continua sendo a seção `[team]`."}
::option[Apenas membros do grupo nomeado são permitidos pela regra.]{#samba-valid-group .correct explanation="A forma com `@` indica um grupo na sintaxe de usuários do Samba."}
:::

## Configuração da identidade

Num servidor standalone, a conta geralmente precisa de identidade Unix correspondente e credencial Samba habilitada:

```bash
$ sudo smbpasswd -a alice
```

Implantações em domínios de diretório usam outro projeto de identidade. Não coloque senhas no histórico do shell nem em configurações legíveis por usuários não relacionados e não presuma que uma senha do Samba seja automaticamente idêntica à senha da conta Unix.

:::single-choice{#samba-password-database}
O que `smbpasswd -a alice` costuma fazer num servidor standalone?

::option[Excluir o diretório pessoal do usuário Unix.]{#samba-delete-home explanation="O comando gerencia credenciais Samba e não remove o home."}
::option[Adicionar ou inicializar credenciais Samba da conta.]{#samba-add-credential .correct explanation="O banco SMB é gerenciado separadamente da simples criação do usuário Unix."}
::option[Montar todo compartilhamento visível como Alice.]{#samba-mount-all explanation="Cadastrar credenciais no servidor é separado de montar no cliente."}
:::

## Validação e aplicação

Verifique a configuração interpretada antes de recarregar:

```bash
$ testparm -s
```

Revise padrões inesperados e erros e, em seguida, recarregue o serviço Samba da distribuição por meio de seu gerenciador de serviços. Os nomes dos serviços variam e normalmente incluem `smbd.service` ou `smb.service`. Um reload causa menos interrupção do que um restart quando há suporte, mas ainda assim verifique o estado, os sockets em escuta, o escopo do firewall e os logs.

Teste a partir de um cliente com um usuário explícito:

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose}
Por que executar `testparm -s` antes de aplicar uma mudança?

::option[Ele copia todo arquivo compartilhado para backup.]{#samba-testparm-backup explanation="A ferramenta interpreta a configuração e não copia dados."}
::option[Ele valida e mostra a configuração efetiva do Samba.]{#samba-testparm-validate .correct explanation="A saída encontra erros e revela definições interpretadas antes do impacto."}
::option[Ele concede privilégios administrativos a todos.]{#samba-testparm-admin explanation="A validação não altera autorização."}
:::

## Montagem a partir do Linux

Clientes Linux usam o driver `cifs` e helpers. Evite senhas na linha de comando, pois vazam pelo histórico ou processos. Use arquivo de credenciais legível apenas pelo root ou mecanismo aprovado:

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

Proteja o arquivo de credenciais, confirme o dialeto aceito pelos dois lados e defina deliberadamente os requisitos de UID, GID, permissões e criptografia. Depois da montagem, verifique-a com `findmnt`, faça testes autorizados de leitura e escrita e desmonte após coordenar os usuários ativos.

:::single-choice{#samba-command-line-password}
Por que evitar `password=...` diretamente no comando mount?

::option[O segredo pode aparecer no histórico ou nos argumentos do processo.]{#samba-password-exposure .correct explanation="Uma fonte protegida reduz divulgação acidental, mas ainda exige permissões cuidadosas."}
::option[SMB não aceita nenhuma autenticação por senha.]{#samba-no-passwords explanation="Autenticação SMB por senha é comum, embora existam outros sistemas."}
::option[A opção torna o share permanentemente somente leitura.]{#samba-password-readonly explanation="A localização do segredo não define a política de escrita."}
:::

## Resumo

Agora você consegue configurar Samba considerando segurança do protocolo e do sistema de arquivos.

1. Definir clientes, identidades, rede e dados primeiro.
2. Restringir o share e alinhar permissões locais.
3. Gerenciar credenciais pelo modelo correto.
4. Validar com `testparm` e testar de ponta a ponta.
5. Proteger credenciais do cliente e verificar a montagem.
