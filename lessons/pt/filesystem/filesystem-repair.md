---
title: "Reparo do Sistema de Arquivos"
description: "Aprenda a usar o fsck para reparo de sistema de arquivos Linux e recuperação de dados. Entenda como verificar e corrigir erros de disco com este comando essencial. Comece sua jornada no Linux!"
keywords: "fsck, reparo de sistema de arquivos, comandos Linux, erros de disco, recuperação de dados, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Às vezes, nosso sistema de arquivos nem sempre está nas melhores condições. Se tivermos um desligamento repentino, nossos dados podem ser corrompidos. Cabe ao sistema tentar nos colocar de volta em um estado funcional (embora certamente possamos tentar nós mesmos).

O comando **fsck** (filesystem check) é usado para verificar a consistência de um sistema de arquivos e pode até tentar repará-lo para nós. Geralmente, quando você inicializa um disco, o fsck será executado antes que seu disco seja montado para garantir que tudo esteja bem. Às vezes, porém, seu disco está tão danificado que você precisará fazer isso manualmente. No entanto, certifique-se de fazer isso enquanto estiver em um disco de resgate ou em algum lugar onde você possa acessar seu sistema de arquivos sem que ele esteja montado.

```bash
sudo fsck /dev/sda
```

## Exercise

Look at the manpage for fsck to see what else it can do.

## Quiz Question

Qual comando é usado para verificar a integridade de um sistema de arquivos?

## Quiz Answer

fsck
