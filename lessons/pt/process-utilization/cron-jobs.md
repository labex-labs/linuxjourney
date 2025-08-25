---
index: 8
lang: "pt"
title: "Cron Jobs"
meta_title: "Cron Jobs - Utilização de Processos"
meta_description: "Aprenda a agendar tarefas Linux com cron jobs. Entenda a sintaxe do crontab e automatize scripts para operações diárias. Comece com este guia para iniciantes!"
meta_keywords: "cron jobs, crontab, agendar tarefas, automação Linux, comandos Linux, Linux para iniciantes, tutorial Linux, crontab -e"
---

## Lesson Content

Embora tenhamos falado sobre utilização de recursos, acho que este seria um bom momento para mencionar uma ferramenta útil no Linux que é usada para agendar tarefas usando cron. Existe um serviço que executa programas para você no horário que você agendar. Isso é realmente útil se você tem um script que deseja executar uma vez por dia e que precisa executar algo para você.

Por exemplo, digamos que eu tenha um script localizado em `/home/pete/scripts/change_wallpaper`. Eu uso este script todas as manhãs para mudar a imagem que uso como papel de parede, mas todas as manhãs tenho que executar este script manualmente. Em vez disso, o que posso fazer é criar um cron job que executa meu script através do cron. Posso especificar a hora em que quero que este cron job seja executado e execute meu script.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Os campos são os seguintes, da esquerda para a direita:

- Minuto - (0-59)
- Hora - (0-23)
- Dia do mês - (1-31)
- Mês - (1-12)
- Dia da semana - (0-7). 0 e 7 são denotados como Domingo

O asterisco no campo significa corresponder a todos os valores. Então, no meu exemplo acima, quero que isso seja executado todos os dias em todos os meses às 8:30 AM.

Para criar um cron job, basta editar o arquivo crontab:

```bash
crontab -e
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre o agendamento de tarefas no Linux:

1. **[Agendar Tarefas com at e cron no Linux](https://labex.io/pt/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Pratique a criação, gerenciamento e remoção de jobs com `at`, `atq`, `atrm` e `crontab`, ganhando experiência prática na automação de tarefas de administração de sistema.

Este laboratório o ajudará a aplicar os conceitos em cenários reais e a construir confiança com o agendamento de tarefas.

## Quiz Question

Qual é o comando para editar seus cron jobs?

## Quiz Answer

crontab -e
