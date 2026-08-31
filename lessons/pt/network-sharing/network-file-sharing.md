---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "pt"
order_index: 1
title: "Visão Geral do Compartilhamento de Arquivos"
description: "Aprenda a escolher e executar com segurança uma transferência de arquivos por SSH usando scp."
meta_title: "Compartilhamento de Arquivos - Compartilhamento de Rede"
meta_description: "Explore o compartilhamento de arquivos Linux com nosso curso online gratuito. Aprenda uma das melhores formas de usar comandos Linux como scp para transferências seguras de arquivos em rede. Um recurso essencial para codificação em Linux."
meta_keywords: "compartilhamento de arquivos linux, comando scp, cópia segura, aprender comandos linux, melhor curso linux online grátis, codificação em linux, transferência de arquivos de rede, melhores recursos para aprender linux"
---

A movimentação de arquivos em rede varia de cópias únicas a compartilhamentos montados continuamente e árvores sincronizadas. Escolha conforme direção, tamanho, frequência, modelo de identidade, confiança da rede, metadados e necessidade de acesso compartilhado ativo.

## Escolha do método de transferência

- `scp` ou SFTP oferece cópia autenticada por SSH ou transferência interativa.
- `rsync` reconcilia árvores eficientemente, localmente ou por SSH.
- NFS apresenta exports como sistemas montados, normalmente entre hosts Unix-like.
- SMB, implementado pelo Samba, oferece acesso compartilhado entre vários sistemas.
- HTTP fornece downloads simples, mas não é um sistema montado geral.

Uma cópia não é automaticamente um backup. Backup também exige retenção independente, testes de restauração, integridade e proteção contra a mesma exclusão ou invasão.

:::single-choice{#file-sharing-one-time-ssh-copy}
Qual ferramenta é adequada a uma cópia única por SSH?

::option[`scp`]{#file-sharing-scp .correct explanation="SCP usa autenticação e transporte SSH para copiar arquivos."}
::option[`uptime`]{#file-sharing-uptime explanation="Uptime informa tempo de atividade e carga, não transfere arquivos."}
::option[`logrotate`]{#file-sharing-logrotate explanation="Logrotate gerencia gerações de logs no host."}
:::

## Compreensão dos caminhos do scp

A forma geral é `scp SOURCE DESTINATION`. Um operando remoto costuma usar `user@host:path`:

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

O primeiro envia um arquivo local; o segundo busca um remoto. Dois-pontos separam host e caminho. Coloque entre aspas caminhos com caracteres do shell e evite nomes não confiáveis ambíguos.

:::single-choice{#file-sharing-scp-pull-source}
Em um pull com `scp`, onde aparece a especificação remota?

::option[Como origem antes do destino local.]{#file-sharing-pull-source .correct explanation="A direção segue a ordem origem-destino dos operandos."}
::option[Como destino local depois de toda opção.]{#file-sharing-pull-destination explanation="O objeto remoto recuperado é a origem."}
::option[Apenas dentro da configuração SSH.]{#file-sharing-pull-config explanation="A configuração fornece padrões, mas o caminho copiado continua sendo operando."}
:::

## Cópia de um diretório

Use modo recursivo para uma árvore:

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

Antes de copiar, examine o tamanho dos dados, os links simbólicos, as permissões, os requisitos de propriedade, o espaço livre e os nomes no destino. O SCP não é uma política de sincronização; cópias repetidas de diretórios podem deixar no destino arquivos que já não existem na origem.

:::single-choice{#file-sharing-scp-recursive}
O que `scp -r` solicita?

::option[Remover o destino remoto antes da cópia.]{#file-sharing-scp-remove explanation="O modo recursivo percorre diretórios e não define limpeza."}
::option[Copiar recursivamente uma árvore de diretórios.]{#file-sharing-scp-tree .correct explanation="A opção é necessária quando a origem é um diretório."}
::option[Acesso somente leitura à configuração SSH.]{#file-sharing-scp-readonly explanation="A opção trata do percurso de diretórios."}
:::

## Verificação da identidade e dos resultados

A verificação da chave do host SSH protege contra conexão ao servidor errado. Trate uma chave alterada como evento a confirmar por canal confiável, sem ignorar o aviso. Use contas de privilégio mínimo e proteja as chaves.

Depois da transferência, verifique o status de saída, os arquivos esperados, os tamanhos, os metadados e, quando os requisitos de integridade exigirem, hashes calculados independentemente nos dois lados. Confirme que a aplicação de destino realmente consegue ler os dados.

:::single-choice{#file-sharing-host-key-change}
O que fazer quando o SSH informa uma mudança inesperada na chave do host?

::option[Desativar a verificação em toda transferência futura.]{#file-sharing-disable-checking explanation="Isso remove um controle importante de identidade."}
::option[Verificar a nova chave por uma fonte confiável antes de continuar.]{#file-sharing-verify-key .correct explanation="O aviso pode indicar host reconstruído, destino errado ou interceptação."}
::option[Publicar a chave privada na saída do comando.]{#file-sharing-publish-key explanation="Credenciais privadas nunca devem ser expostas."}
:::

## Resumo

Agora você consegue selecionar e verificar uma cópia segura e pontual pela rede.

1. Combinar o método às necessidades de acesso e retenção.
2. Ler operandos locais e remotos por origem e destino.
3. Usar modo recursivo deliberadamente para árvores.
4. Verificar identidade, resultados e uso no destino.
