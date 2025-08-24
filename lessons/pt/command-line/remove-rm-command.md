---
index: 13
lang: "pt"
title: "rm (Remover)"
meta_title: "rm (Remover) - Linha de Comando"
meta_description: "Aprenda a usar o comando `rm` no Linux para excluir arquivos e diretórios com segurança. Entenda as opções como -f, -i, -r e rmdir. Comece sua jornada no Linux!"
meta_keywords: "comando rm, excluir arquivos Linux, remover diretórios, tutorial Linux, Linux para iniciantes, rmdir, guia Linux"
---

## Lesson Content

Agora, acho que temos muitos arquivos; vamos remover alguns. Para remover arquivos, você pode usar o comando `rm`. O comando `rm` (remove) é usado para excluir arquivos e diretórios.

```bash
rm file1
```

Tome cuidado ao usar `rm`; não há uma lixeira mágica de onde você possa recuperar arquivos removidos. Uma vez que eles se foram, eles se foram para sempre, então seja cuidadoso.

Felizmente, existem algumas medidas de segurança em vigor, para que o usuário médio não possa simplesmente remover um monte de arquivos importantes. Arquivos protegidos contra gravação solicitarão confirmação antes de serem excluídos. Se um diretório for protegido contra gravação, ele também não será facilmente removido.

Agora, se você não se importa com nada disso, você pode absolutamente remover um monte de arquivos.

```bash
rm -f file1
```

A opção `-f` ou force diz ao `rm` para remover todos os arquivos, sejam eles protegidos contra gravação ou não, sem solicitar ao usuário (desde que você tenha as permissões apropriadas).

```bash
rm -i file
```

Adicionar a flag `-i`, como muitos dos outros comandos, lhe dará um prompt sobre se você realmente deseja remover os arquivos ou diretórios.

```bash
rm -r directory
```

Você não pode simplesmente `rm` um diretório por padrão; você precisará adicionar a flag `-r` (recursive) para remover todos os arquivos e quaisquer subdiretórios que ele possa ter.

Você pode remover um diretório com o comando `rmdir`.

```bash
rmdir directory
```

## Exercise

Para prática interativa com o comando `rm`, experimente este laboratório interativo:

- [Linux rm Command: File Removing](https://labex.io/pt/labs/linux-linux-rm-command-file-removing-209741)

## Quiz Question

Como você remove um arquivo chamado `myfile`?

## Quiz Answer

rm myfile
