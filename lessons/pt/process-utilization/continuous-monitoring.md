---
lesson_id: "continuous-monitoring"
course_id: "process-utilization"
lang: "pt"
order_index: 7
title: "Monitoramento Contínuo"
description: "Aprenda como a coleta do sysstat e os relatórios de sar apoiam a análise histórica do desempenho do Linux."
meta_title: "Monitoramento Contínuo - Utilização de Processos"
meta_description: "Aprenda a realizar o monitoramento contínuo de sistemas Linux com sar. Entenda a instalação, a coleta de dados e a análise histórica do uso de recursos."
meta_keywords: "sar, sysstat, monitoramento Linux, desempenho do sistema, monitoramento contínuo, iniciante, tutorial, guia"
---

As ferramentas interativas mostram o que acontece enquanto você as observa. O monitoramento histórico é necessário quando uma lentidão já terminou. O conjunto `sysstat` coleta periodicamente contadores do sistema, e `sar` lê os contadores atuais ou arquivos de atividade salvos.

## Ativação da Coleta de Dados

Instale o pacote `sysstat` da distribuição e depois confirme que seu coletor e seu mecanismo de retenção estejam ativados. Os serviços, temporizadores e caminhos de configuração exatos variam conforme a distribuição; instalar o pacote não garante que a coleta tenha começado.

Em um host com systemd, inspecione as unidades fornecidas pelo pacote, em vez de adivinhar seus nomes:

```bash
$ systemctl list-unit-files | grep sysstat
$ systemctl list-timers --all | grep sysstat
```

Verifique se novos arquivos de atividade estão sendo criados no diretório de dados do sysstat da distribuição e revise suas permissões e política de retenção.

:::single-choice{#sar-installation-verification} O que você deve verificar depois de instalar `sysstat`?

::option[Se a coleta está ativada e os arquivos de atividade estão sendo atualizados.]{#sar-collector-updating .correct explanation="A instalação do pacote e a coleta periódica ativa são condições distintas."}
::option[Se todos os processos foram reiniciados manualmente.]{#sar-restart-processes explanation="A instalação de um coletor de monitoramento não exige a reinicialização de todas as cargas de trabalho."}
::option[Se todos os arquivos históricos permitem escrita por todos.]{#sar-world-writable explanation="Os dados de monitoramento devem manter controles de acesso adequados."}
:::

## Leitura de Amostras Atuais

Solicite a `sar` três relatórios da CPU em intervalos de um segundo:

```bash
$ sar -u 1 3
```

Outros relatórios comuns incluem fila de execução e carga (`-q`), memória (`-r`), paginação (`-B`), dispositivos de bloco (`-d`) e atividade por CPU (`-P ALL`). As opções e os campos variam conforme a versão do sysstat, portanto consulte `sar --help` ou o manual local.

:::single-choice{#sar-one-second-count} O que `sar -u 1 3` solicita?

::option[Três relatórios da CPU em intervalos de um segundo.]{#sar-three-cpu-samples .correct explanation="O primeiro número é o intervalo em segundos, e o segundo é a quantidade de relatórios."}
::option[Um relatório que abrange exatamente três dias.]{#sar-three-days explanation="Os operandos especificam o intervalo e a quantidade das amostras, não um intervalo de datas."}
::option[A exclusão de três arquivos de CPU salvos.]{#sar-delete-files explanation="O comando lê contadores e não solicita exclusões."}
:::

## Leitura de Arquivos Históricos

Os locais e nomes dos arquivos salvos variam, muitas vezes ficando em `/var/log/sysstat` ou `/var/log/sa`. Forneça um arquivo de atividade selecionado com `-f`:

```bash
$ sar -q -f /var/log/sysstat/sa02
```

Confirme a data completa do arquivo nos cabeçalhos do relatório; um sufixo de dois dígitos normalmente indica o dia do mês e pode ser ambíguo entre períodos de retenção. Os formatos binários salvos também podem exigir uma versão compatível do sysstat.

:::single-choice{#sar-historical-file-option} Qual opção solicita que `sar` leia um arquivo de atividade especificado?

::option[`-P`]{#sar-option-p explanation="Essa opção seleciona relatórios de processadores, não um arquivo de entrada."}
::option[`-q`]{#sar-option-q explanation="Essa opção seleciona relatórios de fila e carga."}
::option[`-f`]{#sar-option-f .correct explanation="A opção de arquivo seleciona os dados de atividade salvos que serão lidos."}
:::

## Relação com um Incidente

Determine o horário e o fuso do incidente e depois compare vários sinais no mesmo intervalo. Procure alterações na carga, CPU, fila de execução, paginação, atividade dos dispositivos, tráfego de rede e latência da aplicação. As alterações nos contadores mostram correlação, não necessariamente causalidade; os registros de implantações e logs da aplicação podem explicar o fator desencadeante.

As lacunas podem significar que o host estava desligado, que o coletor falhou ou que a retenção removeu os dados. Monitore o próprio pipeline de monitoramento para que as evidências ausentes sejam percebidas antes de um incidente.

:::single-choice{#sar-incident-method} Como os dados históricos de `sar` devem ser usados durante a revisão de um incidente?

::option[Tratar o maior contador isolado como a causa raiz comprovada.]{#sar-single-root explanation="Uma única correlação não estabelece causalidade."}
::option[Comparar várias métricas no mesmo intervalo de tempo verificado.]{#sar-correlate-window .correct explanation="Sinais alinhados ajudam a diferenciar hipóteses e conectar o comportamento do sistema ao incidente."}
::option[Ignorar as lacunas porque a coleta é garantida após a instalação.]{#sar-ignore-gaps explanation="A coleta pode falhar ou estar desativada, e as lacunas exigem uma explicação."}
:::

## Resumo

Agora você sabe usar `sar` para investigar o desempenho fora de uma sessão interativa.

1. Verifique se a coleta e a retenção estão realmente ativas.
2. Solicite amostras atuais limitadas por um intervalo e uma quantidade.
3. Selecione explicitamente os arquivos históricos de atividade.
4. Alinhe várias métricas ao horário do incidente e às evidências da carga de trabalho.
