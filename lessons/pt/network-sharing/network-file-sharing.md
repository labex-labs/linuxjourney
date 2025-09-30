---
index: 1
lang: "pt"
title: "Visão Geral do Compartilhamento de Arquivos"
meta_title: "Visão Geral do Compartilhamento de Arquivos - Compartilhamento de Rede"
meta_description: "Aprenda sobre compartilhamento de arquivos Linux e o comando secure copy (scp). Transfira arquivos entre hosts em sua rede. Comece com este guia amigável para iniciantes!"
meta_keywords: "compartilhamento de arquivos Linux, comando scp, cópia segura, transferência de arquivos em rede, tutorial Linux, Linux para iniciantes, guia Linux"
---

## Lesson Content

Você geralmente não é o único computador em sua rede, especialmente se estiver trabalhando em um ambiente comercial. Quando queremos transferir dados de uma máquina para outra, às vezes pode ser mais fácil conectar um drive USB e copiá-los manualmente. Mas, na maioria das vezes, se você estiver trabalhando com máquinas na mesma rede, a maneira de transferir dados é através do compartilhamento de arquivos em rede.

Neste curso, abordaremos alguns métodos diferentes para copiar dados de e para diferentes máquinas em sua rede. Discutiremos algumas cópias de arquivos simples e, em seguida, falaremos sobre a montagem de diretórios inteiros em sua máquina que funcionam como um drive separado.

Uma ferramenta simples de compartilhamento de arquivos é o comando **scp**. O comando scp significa secure copy (cópia segura); ele funciona exatamente da mesma forma que o comando cp, mas permite copiar de um host para outro host na mesma rede. Ele funciona via ssh, então todas as suas ações usam a mesma autenticação e segurança do ssh.

### Para copiar um arquivo de um host local para um host remoto

```bash
scp myfile.txt username@remotehost.com:/remote/directory
```

### Para copiar um arquivo de um host remoto para o seu host local

```bash
scp username@remotehost.com:/remote/directory/myfile.txt /local/directory
```

### Para copiar um diretório do seu host local para um host remoto

```bash
scp -r mydir username@remotehost.com:/remote/directory
```

## Exercise

A prática leva à perfeição! Aqui está um laboratório prático para reforçar sua compreensão da transferência segura de arquivos em rede:

1. **[Acesso Remoto Seguro no Linux com SSH](https://labex.io/pt/labs/comptia-secure-remote-access-in-linux-with-ssh-592816)** - Pratique a autenticação baseada em chave, a transferência segura de arquivos com `scp` e a criação de túneis SSH para encaminhamento de portas.

Este laboratório o ajudará a aplicar os conceitos de acesso remoto seguro e transferência de arquivos em um cenário real e a construir confiança com `scp`.

## Quiz Question

Qual comando você pode usar para copiar arquivos de forma segura de um host para outro?

## Quiz Answer

scp
