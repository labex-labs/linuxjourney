---
lang: "pt"
title: "Monitoramento Contínuo"
meta_description: "Aprenda o monitoramento contínuo de sistemas Linux com sar. Entenda a instalação, coleta de dados e como analisar o uso histórico de recursos para desempenho. Comece já!"
meta_keywords: "sar, sysstat, monitoramento Linux, desempenho do sistema, monitoramento contínuo, iniciante, tutorial, guia"
---

## Lesson Content

Essas ferramentas de monitoramento são boas para consultar quando sua máquina está com problemas, mas e as máquinas que estão com problemas quando você não está olhando? Para essas, você precisará usar uma ferramenta de monitoramento contínuo, algo que coletará, relatará e salvará as informações de atividade do seu sistema. Nesta lição, abordaremos uma ótima ferramenta para usar: o **sar**.

### Installing sar

Sar é uma ferramenta usada para fazer análise histórica em seu sistema. Primeiro, certifique-se de tê-lo instalado instalando o pacote `sysstat`: `sudo apt install sysstat`.

### Setting up data collection

Normalmente, depois de instalar o `sysstat`, seu sistema começará automaticamente a coletar dados. Se não o fizer, você pode habilitá-lo modificando o campo `ENABLED` em `/etc/default/sysstat`.

### Using sar

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

Instale o sar em seu sistema e comece a coletar e analisar a utilização dos recursos do seu sistema.

## Quiz Question

Qual é uma boa ferramenta para usar para monitorar os recursos do sistema?

## Quiz Answer

sar
