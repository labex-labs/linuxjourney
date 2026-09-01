---
lesson_id: "managing-log-files"
course_id: "logging"
lang: "pt"
order_index: 6
title: "Gerenciamento de Arquivos de Log"
description: "Aprenda a configurar, testar e verificar com segurança a rotação de logs de texto usando logrotate."
meta_title: "Gerenciamento de Logs - Logrotate"
meta_description: "Domine o gerenciamento de logs Linux com este guia para iniciantes sobre logrotate. Aprenda como a rotação de logs economiza espaço em disco, como configurá-la e mantenha os logs do seu sistema organizados."
meta_keywords: "logrotate, logs Linux, gerenciamento de logs, rotação de logs, tutorial Linux, iniciante, guia, espaço em disco"
---

Logs de texto sem limite podem esgotar um sistema de arquivos; exclusões agressivas podem remover evidências operacionais ou obrigatórias. `logrotate` aplica políticas de tamanho, tempo, compressão, propriedade e retenção a logs baseados em arquivos.

## Entendendo a rotação

Uma rotação típica renomeia o arquivo ativo, cria outro, opcionalmente pede ao aplicativo que o reabra, comprime gerações antigas e remove as excedentes. Tudo depende da configuração. Rotação não é backup: cópias retidas ainda podem ser apagadas, corrompidas ou perdidas com o host.

:::single-choice{#logrotate-not-backup} Por que rotação não substitui backup ou arquivamento?

::option[Arquivos rotacionados continuam sujeitos à retenção local e a falhas do host.]{#logrotate-local-retention .correct explanation="A rotação controla gerações de trabalho, mas não cria uma cópia durável independente."}
::option[A rotação só processa arquivos de imagem.]{#logrotate-images explanation="A ferramenta foi projetada principalmente para logs."}
::option[Toda rotação mantém todas as gerações para sempre.]{#logrotate-forever explanation="Regras de retenção normalmente removem gerações antigas."}
:::

## Localização da configuração

O arquivo principal costuma ser `/etc/logrotate.conf`, com trechos de pacotes ou aplicações em `/etc/logrotate.d/`. Uma política simplificada pode ter esta aparência:

```text
/var/log/example/app.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 example adm
}
```

Isso solicita avaliação diária, sete rotações, compressão adiada por uma geração, tolerância a arquivo ausente ou vazio e um novo arquivo com modo e proprietário explícitos. A rotação real também depende do estado registrado e do agendador.

:::single-choice{#logrotate-rotate-seven} O que especifica `rotate 7`?

::option[Manter até sete gerações rotacionadas.]{#logrotate-seven-generations .correct explanation="Gerações mais antigas são removidas quando a retenção é excedida."}
::option[Executar o aplicativo sete vezes ao dia.]{#logrotate-run-seven explanation="A diretiva controla gerações, não a execução do aplicativo."}
::option[Definir a permissão de todo arquivo como 0007.]{#logrotate-mode-seven explanation="O modo é controlado por diretivas como `create`."}
:::

## Coordenação com o processo que escreve

Depois da renomeação, um daemon pode continuar escrevendo pelo descritor aberto. Um script `postrotate` costuma enviar um sinal documentado de reload ou reabertura. Confirme o comportamento do aplicativo e mantenha o script limitado.

`copytruncate` copia e trunca o original quando o aplicativo não consegue reabrir logs. Escritas podem ser perdidas ou duplicadas nessa janela; é um compromisso, não um padrão universalmente seguro.

:::single-choice{#logrotate-open-descriptor} Por que um aplicativo pode precisar reabrir o log após a rotação?

::option[Seu descritor aberto ainda pode apontar para o arquivo renomeado.]{#logrotate-descriptor-renamed .correct explanation="Reabrir faz novas escritas usarem o caminho ativo recém-criado."}
::option[A compressão encerra automaticamente todo aplicativo.]{#logrotate-compression-stops explanation="Compressão não gerencia o ciclo de vida do processo escritor."}
::option[O kernel proíbe criar um segundo arquivo de log.]{#logrotate-kernel-forbids explanation="Vários arquivos podem existir; a questão é qual inode está aberto."}
:::

## Teste antes da ativação

Use o modo debug para examinar decisões sem rotacionar:

```bash
$ sudo logrotate -d /etc/logrotate.conf
```

A saída de depuração não comprova que permissões, scripts, espaço livre ou a reabertura pela aplicação funcionarão durante uma execução real. Teste uma nova regra em um ambiente controlado e, depois da execução, examine o arquivo ativo, a geração rotacionada, a propriedade, a compressão, a saída da aplicação e o estado do logrotate. `-f` força uma rotação e altera o estado; não o confunda com uma execução de teste.

:::single-choice{#logrotate-debug-mode} O que `logrotate -d` oferece?

::option[Exclusão permanente de todos os logs vencidos.]{#logrotate-debug-delete explanation="O modo debug informa decisões sem executar a rotação."}
::option[Rotação forçada de produção independentemente da política.]{#logrotate-debug-force explanation="A opção de força é `-f` e altera o estado."}
::option[Avaliação diagnóstica sem modificar arquivos nem estado.]{#logrotate-debug-dry .correct explanation="É a primeira revisão de sintaxe e decisão, seguida por verificação real controlada."}
:::

## Outros armazenamentos

Logrotate gerencia arquivos nomeados por suas políticas. O journal tem configuração própria de tamanho e retenção; bancos e serviços remotos têm outros controles. Monitore capacidade e saúde do logging para detectar writers travados ou rotação falha antes de esgotar espaço.

:::single-choice{#logrotate-journal-retention} Uma regra logrotate aplica automaticamente a retenção do journal?

::option[Não; o journal tem configurações e limites próprios.]{#logrotate-journal-separate .correct explanation="Logrotate gerencia apenas caminhos selecionados por políticas de arquivo."}
::option[Sim; todos os logs compartilham um mecanismo.]{#logrotate-all-logs explanation="Rotação de arquivos e retenção do journal são mecanismos separados."}
::option[Sim, mas apenas quando não há logs de texto.]{#logrotate-journal-fallback explanation="A presença de arquivos não une os dois sistemas."}
:::

## Resumo

Agora você consegue projetar e verificar rotação de logs sem confundi-la com arquivamento.

1. Equilibrar espaço, operação e retenção.
2. Definir gerações, compressão, propriedade e arquivos vazios.
3. Coordenar aplicativos que mantêm descritores abertos.
4. Depurar antes de uma rotação real controlada.
5. Gerenciar journal e armazenamentos externos separadamente.
