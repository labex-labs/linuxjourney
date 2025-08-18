---
lang: "pt"
title: "Monitoramento da CPU"
meta_title: "Monitoramento da CPU - Utilização de Processos"
meta_description: "Aprenda o monitoramento da CPU com o comando uptime. Entenda a média de carga, o uso da CPU e como interpretar o desempenho do sistema para iniciantes em Linux."
meta_keywords: "comando uptime, monitoramento de CPU Linux, média de carga, desempenho do sistema, tutorial Linux, guia para iniciantes"
---

## Lesson Content

Vamos analisar um comando útil, o **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Falamos sobre o uptime na primeira lição deste curso, mas não abordamos o campo load average. Os load averages são uma boa maneira de ver a carga da CPU no seu sistema. Esses números representam a carga média da CPU em intervalos de 1, 5 e 15 minutos. O que quero dizer com carga da CPU? A carga da CPU é o número médio de processos que estão esperando para serem executados pela CPU.

Digamos que você tenha uma CPU de núcleo único; pense neste núcleo como uma única faixa de tráfego. Se for hora do rush na rodovia, esta faixa estará muito movimentada, e o tráfego estará em 100% ou uma carga de 1. Agora o tráfego ficou tão ruim que está congestionando a rodovia e deixando as ruas normais movimentadas com o dobro de carros; podemos dizer que sua carga é de 200% ou uma carga de 2. Agora digamos que melhore um pouco e haja apenas metade dos carros na faixa da rodovia; podemos dizer que a carga da faixa é de 0.5. Quando o tráfego é inexistente e podemos chegar em casa mais rápido, a carga deve ser idealmente muito baixa, como o tráfego das 2 da manhã. Os carros, neste caso, são processos, e esses processos estão apenas esperando para sair da rodovia e chegar em casa.

Agora, só porque você tem um load average de 1 não significa que seu computador está lento. A maioria das máquinas modernas hoje em dia tem vários núcleos. Se você tivesse um processador quad-core (4 núcleos) e seu load average fosse 1, isso estaria realmente afetando apenas 25% da sua CPU. Pense em cada núcleo como uma faixa de tráfego. Você pode ver a quantidade de núcleos que você tem no seu sistema com **cat /proc/cpuinfo**.

Ao observar o load average, você deve levar em consideração o número de núcleos. Se você descobrir que sua máquina está sempre usando uma carga acima da média, pode haver algo errado acontecendo.

## Exercise

Verifique o load average do seu sistema e veja o que ele está fazendo.

## Quiz Question

Qual comando você pode usar para ver o load average?

## Quiz Answer

uptime
