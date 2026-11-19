---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "pt"
order_index: 3
title: "Integridade de arquivos"
description: "Aprenda a comparar o conteúdo e as permissões de um arquivo usando um hash e metadados."
meta_title: "Integridade de arquivos - Auditoria de sistemas"
meta_description: "Aprenda a comparar o conteúdo e as permissões de um arquivo usando um hash e metadados."
meta_keywords: "integridade de arquivos, hash, metadados, auditoria de sistemas, cibersegurança, Linux Journey"
---

Uma verificação de integridade determina se um arquivo ainda corresponde a uma referência. Confira o conteúdo e os metadados separadamente. O conteúdo são os bytes dentro do arquivo. Os **metadados** incluem detalhes como as permissões de acesso.

## Registrando um hash do conteúdo

Em uma pasta de prática vazia, crie um arquivo de configuração pequeno. O redirecionamento substitui um arquivo existente com o mesmo nome, por isso use uma pasta nova.

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

O primeiro campo é o **hash**, um valor de tamanho fixo calculado com os bytes do arquivo. Mais tarde, aplique o mesmo método ao mesmo arquivo. Se o hash mudou, os bytes usados no cálculo são diferentes.

:::single-choice{#host-file-integrity-changed-hash} O valor SHA-256 muda depois que o arquivo é editado. O que a comparação mostra?

::option[Seu conteúdo difere dos bytes medidos anteriormente.]{#host-file-integrity-changed-hash-a .correct explanation="O hash muda com o conteúdo fornecido ao cálculo."}
::option[A edição foi necessariamente feita sem autorização.]{#host-file-integrity-changed-hash-b explanation="A autorização precisa ser verificada à parte."}
::option[As permissões de uma conta certamente mudaram.]{#host-file-integrity-changed-hash-c explanation="Um hash de conteúdo não registra permissões."}
:::

## Registrando as permissões

No Linux, `stat -c` imprime os metadados selecionados. O campo `%a` mostra as permissões em formato numérico e `%n` mostra o nome.

```bash
$ stat -c '%a %n' site.conf
```

As permissões iniciais podem variar conforme a forma de criação do arquivo. Registre o valor junto com o hash do conteúdo para comparar as duas propriedades depois.

:::single-choice{#host-file-integrity-mode-vs-content} O hash corresponde à referência e stat indica permissões diferentes. O que mudou segundo essas verificações?

::option[Os bytes do arquivo mudaram e as permissões continuaram iguais.]{#host-file-integrity-mode-vs-content-a explanation="O hash é o mesmo, mas as permissões são diferentes."}
::option[O arquivo necessariamente foi excluído.]{#host-file-integrity-mode-vs-content-c explanation="As duas verificações retornaram informações sobre o arquivo."}
::option[As permissões mudaram e o hash do conteúdo observado continuou igual.]{#host-file-integrity-mode-vs-content-b .correct explanation="As duas ferramentas medem propriedades diferentes."}
:::

## Testando uma alteração nas permissões

O próximo comando define as permissões desse arquivo descartável como `640`. Isso dá ao proprietário acesso de leitura e escrita e ao grupo acesso de leitura. Repita as duas verificações e compare os resultados.

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

As permissões devem aparecer como 640 e o hash do conteúdo deve corresponder à primeira medição.

:::single-choice{#host-file-integrity-repeat-check} Qual verificação detectaria uma edição posterior de mode=preview dentro do arquivo?

::option[Somente o nome do arquivo exibido por stat.]{#host-file-integrity-repeat-check-a explanation="O nome pode continuar igual após a edição."}
::option[Um novo cálculo SHA-256 comparado ao original.]{#host-file-integrity-repeat-check-c .correct explanation="Uma mudança no conteúdo produziria um hash diferente."}
::option[Somente o número da permissão do proprietário.]{#host-file-integrity-repeat-check-b explanation="As permissões podem permanecer iguais após uma alteração no conteúdo."}
:::

![Saída da LabEx mostrando permissões alteradas para 640 e o mesmo hash de conteúdo](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## Resumo

Agora você consegue comparar o conteúdo e as permissões de acesso de um arquivo de forma independente.

1. Registre um hash SHA-256 do conteúdo.
2. Leia as permissões com stat.
3. Verifique o efeito de uma mudança nas permissões.
