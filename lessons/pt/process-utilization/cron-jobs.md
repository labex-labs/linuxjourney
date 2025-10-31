---
index: 8
lang: "pt"
title: "Trabalhos Cron"
meta_title: "Trabalhos Cron - Utilização de Processos"
meta_description: "Aprenda a agendar tarefas e automatizar scripts no Linux usando trabalhos cron. Este guia abrange a sintaxe do crontab, comandos essenciais como crontab -e e exemplos práticos para iniciantes."
meta_keywords: "trabalhos cron, crontab, agendar tarefas, automação Linux, comandos Linux, Linux para iniciantes, tutorial Linux, crontab -e, cron"
---

## Lesson Content

Embora a utilização de processos seja importante, é também um ótimo momento para introduzir uma ferramenta poderosa para a `automação Linux`: o daemon `cron`. Este serviço em segundo plano permite-lhe `agendar tarefas` para serem executadas automaticamente em horários ou intervalos específicos. Estas tarefas agendadas são comumente conhecidas como `tarefas cron` (cron jobs).

Isso é incrivelmente útil para automatizar ações rotineiras, como executar um script de backup todas as noites ou limpar arquivos temporários uma vez por semana.

### O que são Tarefas Cron

Imagine que tem um script em `/home/pete/scripts/change_wallpaper` que executa todas as manhãs para definir um novo fundo de ecrã. Em vez de o executar manualmente todos os dias, pode criar uma `tarefa cron` para o executar por si. Ao definir um horário, pode dizer ao serviço `cron` exatamente quando executar o seu script, tornando-o uma verdadeira solução de "configurar e esquecer".

### Compreender a Sintaxe Crontab

Para criar uma `tarefa cron`, precisa de especificar o horário e o comando a executar. O horário é definido por cinco campos, seguidos pelo comando.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Os cinco campos de hora e data são, da esquerda para a direita:

- **Minuto:** 0-59
- **Hora:** 0-23 (em formato de 24 horas)
- **Dia do mês:** 1-31
- **Mês:** 1-12
- **Dia da semana:** 0-7 (onde 0 e 7 representam Domingo)

Um asterisco (`*`) num campo funciona como um curinga, significando "todos". No exemplo acima, o horário `30 08 * * *` diz ao `cron` para executar o comando às 8:30 da manhã, todos os dias do mês, todos os meses e todos os dias da semana.

### Gerir Tarefas Cron com Crontab

Você gere as suas `tarefas cron` pessoais usando o comando `crontab`, que permite editar o seu ficheiro crontab específico do utilizador. Este ficheiro contém todas as `tarefas cron` que agendou.

Para adicionar ou editar as suas `tarefas cron`, use a flag `-e` (editar). Isto abrirá o seu ficheiro crontab no seu editor de texto predefinido.

```bash
crontab -e
```

Depois de adicionar a definição da sua tarefa e guardar o ficheiro, o `cron` lerá automaticamente o novo horário. Também pode listar as suas `tarefas cron` ativas com `crontab -l` ou remover todas com `crontab -r`. Usar `tarefas cron` é uma competência fundamental para qualquer pessoa interessada em `automação Linux`.

## Exercise

A prática leva à perfeição! Este laboratório prático ajudará a reforçar a sua compreensão sobre como `agendar tarefas` no Linux.

1. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Pratique a criação, gestão e remoção de tarefas com `at`, `atq`, `atrm` e `crontab`, ganhando experiência prática na automação de tarefas de administração do sistema.

Este laboratório irá ajudá-lo a aplicar os conceitos desta lição num cenário do mundo real e a aumentar a sua confiança com a `automação Linux`.

## Quiz Question

Qual é o comando para editar as suas tarefas cron pessoais? (Por favor, responda usando o comando exato em minúsculas e a sua opção.)

## Quiz Answer

crontab -e
