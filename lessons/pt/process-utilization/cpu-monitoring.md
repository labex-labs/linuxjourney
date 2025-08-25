---
index: 4
lang: "pt"
title: "Monitoramento da CPU"
meta_title: "Monitoramento da CPU - Utilização do Processo"
meta_description: "Aprenda o monitoramento da CPU com o comando uptime. Entenda o load average, o uso da CPU e como interpretar o desempenho do sistema para iniciantes em Linux."
meta_keywords: "comando uptime, monitoramento de CPU Linux, load average, desempenho do sistema, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Vamos analisar um comando útil, o **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Falamos sobre o uptime na primeira lição deste curso, mas não abordamos o campo de load average. Os load averages são uma boa maneira de ver a carga da CPU no seu sistema. Esses números representam a carga média da CPU em intervalos de 1, 5 e 15 minutos. O que quero dizer com carga da CPU? A carga da CPU é o número médio de processos que estão esperando para serem executados pela CPU.

Digamos que você tenha uma CPU de um único núcleo; pense neste núcleo como uma única faixa de tráfego. Se for hora do rush na autoestrada, esta faixa estará muito movimentada, e o tráfego estará em 100% ou uma carga de 1. Agora o tráfego ficou tão ruim que está congestionando a autoestrada e deixando as estradas regulares duas vezes mais movimentadas; podemos dizer que sua carga é de 200% ou uma carga de 2. Agora digamos que melhore um pouco e haja apenas metade dos carros na faixa da autoestrada; podemos dizer que a carga da faixa é de 0.5. Quando o tráfego é inexistente e podemos chegar em casa mais rápido, a carga deve ser idealmente muito baixa, como o tráfego das 2 da manhã. Os carros, neste caso, são processos, e esses processos estão apenas esperando para sair da autoestrada e chegar em casa.

Agora, só porque você tem um load average de 1 não significa que seu computador está lento. A maioria das máquinas modernas hoje em dia tem vários núcleos. Se você tivesse um processador quad-core (4 núcleos) e seu load average fosse 1, isso estaria realmente afetando apenas 25% da sua CPU. Pense em cada núcleo como uma faixa de tráfego. Você pode ver a quantidade de núcleos que você tem em seu sistema com `cat /proc/cpuinfo`.

Ao observar o load average, você deve levar em consideração o número de núcleos. Se você descobrir que sua máquina está sempre usando uma carga acima da média, pode haver algo errado acontecendo.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre o monitoramento do desempenho do sistema Linux e da carga da CPU:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação e inspeção de processos, e o monitoramento de recursos com ferramentas como `ps` e `top`, o que se relaciona diretamente com a compreensão da carga da CPU.
2. **[Comando Linux top: Monitoramento de Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar o comando `top` para monitoramento de sistema em tempo real, incluindo a classificação e filtragem de processos, proporcionando um mergulho mais profundo na atividade da CPU e dos processos.
3. **[Comando Linux free: Monitorando a Memória do Sistema](https://labex.io/pt/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a monitorar e analisar o uso da memória do sistema, que é frequentemente um fator crítico, juntamente com a carga da CPU, no desempenho geral do sistema.

Esses laboratórios o ajudarão a aplicar os conceitos de monitoramento de sistema e gerenciamento de recursos em cenários reais e a construir confiança na análise do desempenho do sistema.

## Quiz Question

Qual comando você pode usar para ver o load average?

## Quiz Answer

uptime
