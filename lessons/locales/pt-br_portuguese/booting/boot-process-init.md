# Processo de inicialização: Init

## Conteúdo da lição

Nós discutimos o init nas lições anteriores e sabemos que este é o primeiro processo que começa e inicia todos os outros serviços essenciais em nosso sistema. Mas como?

Na verdade, existem três principais implementações do init no Linux:

<b> init do System V (sysv) </ b>

Este é o sistema tradicional de inicialização. Ele inicia e interrompe sequencialmente os processos, com base nos scripts de inicialização. O estado da máquina é denotado por níveis de execução, cada nível de execução inicia ou interrompe uma máquina de maneira diferente.

<b> Upstart </ b>

Este é o init que você encontrará em instalações antigas do Ubuntu. O Upstart usa a ideia de jobs e eventos e funciona iniciando jobs que executam determinadas ações em resposta a eventos.

<b> Systemd </ b>

Este é o novo padrão para o init, é orientado por objetivos. Basicamente, você tem um objetivo que deseja alcançar e o systemd tenta satisfazer as dependências do objetivo para completar o objetivo.

Temos um curso completo sobre sistemas de inicialização, onde vamos mergulhar em cada um desses sistemas com mais detalhes.

## Exercício

Nenhum exercício para esta lição.

## Questionário

Qual é o mais novo padrão para o init?

## resposta do questionário

systemd
