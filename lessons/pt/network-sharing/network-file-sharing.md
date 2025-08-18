---
lang: "pt"
title: "Visão Geral do Compartilhamento de Arquivos"
meta_description: "Aprenda sobre compartilhamento de arquivos Linux e o comando secure copy (scp). Transfira arquivos entre hosts em sua rede. Comece com este guia para iniciantes!"
meta_keywords: "compartilhamento de arquivos Linux, comando scp, cópia segura, transferência de arquivos em rede, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Você geralmente não é o único computador em sua rede, especialmente se estiver trabalhando em um ambiente comercial. Quando queremos transferir dados de uma máquina para outra, às vezes pode ser mais fácil conectar um drive USB e copiá-los manualmente. Mas, na maioria das vezes, se você estiver trabalhando com máquinas na mesma rede, a maneira de transferir dados é através do compartilhamento de arquivos em rede.

Neste curso, abordaremos alguns métodos diferentes para copiar dados de e para diferentes máquinas em sua rede. Discutiremos algumas cópias de arquivos simples e, em seguida, falaremos sobre montar diretórios inteiros em sua máquina que atuam como um drive separado.

Uma ferramenta simples de compartilhamento de arquivos é o comando **scp**. O comando scp significa secure copy (cópia segura); ele funciona exatamente da mesma forma que o comando cp, mas permite copiar de um host para outro host na mesma rede. Ele funciona via ssh, então todas as suas ações usam a mesma autenticação e segurança do ssh.

### To copy a file from a local host to a remote host

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### To copy a file from a remote host to your local host

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### To copy a directory from your local host to a remote host

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

Try to copy a file over with scp from one machine to another.

## Quiz Question

Qual comando você pode usar para copiar arquivos com segurança de um host para outro?

## Quiz Answer

scp
