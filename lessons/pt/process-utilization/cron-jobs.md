---
title: "Cron Jobs"
description: "Aprenda a agendar tarefas Linux com cron jobs. Entenda a sintaxe do crontab e automatize scripts para operações diárias. Comece com este guia para iniciantes!"
keywords: "cron jobs, crontab, agendar tarefas, automação Linux, comandos Linux, Linux para iniciantes, tutorial Linux, crontab -e"
---

## Lesson Content

Embora tenhamos falado sobre a utilização de recursos, acho que este seria um bom momento para mencionar uma ferramenta útil no Linux que é usada para agendar tarefas usando cron. Existe um serviço que executa programas para você no horário que você agendar. Isso é realmente útil se você tiver um script que deseja executar uma vez por dia e que precise executar algo para você.

Por exemplo, digamos que eu tenha um script localizado em `/home/pete/scripts/change_wallpaper`. Eu uso este script todas as manhãs para mudar a imagem que uso como papel de parede, mas todas as manhãs tenho que executar este script manualmente. Em vez disso, o que posso fazer é criar um cron job que executa meu script através do cron. Posso especificar a hora em que quero que este cron job seja executado e execute meu script.

```plaintext
30 08 * * * /home/pete/scripts/change_wallpaper
```

Os campos são os seguintes, da esquerda para a direita:

- Minute - (0-59)
- Hour - (0-23)
- Day of the month - (1-31)
- Month - (1-12)
- Day of the week - (0-7). 0 e 7 são denotados como Sunday

O asterisco no campo significa corresponder a todos os valores. Então, no meu exemplo acima, quero que isso seja executado todos os dias em todos os meses às 8:30 AM.

Para criar um cron job, basta editar o arquivo crontab:

```bash
crontab -e
```

## Exercise

Crie um cron job que você deseja executar em um horário agendado.

## Quiz Question

Qual é o comando para editar seus cron jobs?

## Quiz Answer

crontab -e
