---
index: 7
lang: "pt"
title: "Monitoramento Contínuo"
meta_title: "Monitoramento Contínuo - Utilização de Processos"
meta_description: "Aprenda o monitoramento contínuo de sistemas Linux com sar. Entenda a instalação, coleta de dados e como analisar o uso histórico de recursos para desempenho. Comece já!"
meta_keywords: "sar, sysstat, monitoramento Linux, desempenho do sistema, monitoramento contínuo, iniciante, tutorial, guia"
---

## Lesson Content

Essas ferramentas de monitoramento são boas para verificar quando sua máquina está com problemas, mas e as máquinas que estão com problemas quando você não está olhando? Para essas, você precisará usar uma ferramenta de monitoramento contínuo, algo que coletará, relatará e salvará as informações de atividade do seu sistema. Nesta lição, abordaremos uma ótima ferramenta para usar: o **sar**.

### Instalando o sar

Sar é uma ferramenta usada para fazer análises históricas em seu sistema. Primeiro, certifique-se de tê-lo instalado instalando o pacote `sysstat`: `sudo apt install sysstat`.

### Configurando a coleta de dados

Normalmente, depois de instalar o `sysstat`, seu sistema começará automaticamente a coletar dados. Se não o fizer, você pode habilitá-lo modificando o campo `ENABLED` em `/etc/default/sysstat`.

### Usando o sar

```bash
sudo sar -q
```

Este comando listará os detalhes desde o início do dia.

```bash
sudo sar -r
```

Isso listará os detalhes do uso da memória desde o início do dia.

```bash
sudo sar -P
```

Isso listará os detalhes do uso da CPU.

Para ver uma visualização de um dia diferente, você pode ir para `/var/log/sysstat/saXX` onde `XX` é o dia que você deseja visualizar.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão sobre monitoramento de sistema e análise de recursos:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Pratique a interação com processos em primeiro e segundo plano, inspecionando-os com `ps`, monitorando recursos com `top` e encerrando-os com `kill`.
2. **[Comando Linux top: Monitoramento de Sistema em Tempo Real](https://labex.io/pt/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar várias opções com o comando `top` para classificar processos, ajustar intervalos de atualização, filtrar por usuário e focar em processos ativos para monitorar efetivamente o desempenho do sistema.
3. **[Comando Linux df: Relatório de Espaço em Disco](https://labex.io/pt/labs/linux-linux-df-command-disk-space-reporting-219188)** - Este laboratório apresenta o comando `df` no Linux, um utilitário que exibe informações sobre o uso do espaço em disco em sistemas de arquivos montados, que é um aspecto chave do monitoramento do sistema.

Esses laboratórios o ajudarão a aplicar os conceitos de monitoramento de recursos do sistema em cenários reais e a construir confiança na análise da atividade do sistema.

## Quiz Question

Qual é uma boa ferramenta para usar para monitorar os recursos do sistema?

## Quiz Answer

sar
