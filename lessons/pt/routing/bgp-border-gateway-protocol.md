---
index: 7
lang: "pt"
title: "Protocolo de Gateway de Borda"
meta_title: "Protocolo de Gateway de Borda - Roteamento"
meta_description: "Explore os fundamentos do Protocolo de Gateway de Borda (BGP), o protocolo central que possibilita o roteamento na internet. Aprenda como o BGP facilita a comunicação entre sistemas autônomos e os princípios do roteamento do protocolo de gateway de borda."
meta_keywords: "BGP, Protocolo de Gateway de Borda, roteamento de protocolo de gateway de borda, roteamento de internet, sistemas autônomos, rede Linux, tutorial BGP, protocolos de rede"
---

## Lesson Content

### A Espinha Dorsal da Internet

O último protocolo importante que abordaremos é o Border Gateway Protocol (BGP). O BGP é o protocolo fundamental que permite que a internet funcione, gerenciando como os pacotes de dados são roteados através de sua vasta coleção de redes. Ele é especificamente projetado para trocar informações de roteamento e alcançabilidade entre diferentes Sistemas Autônomos (AS).

### O que é um Sistema Autônomo?

Um Sistema Autônomo (AS) é uma grande rede ou um grupo de redes gerenciado por uma única entidade administrativa. Exemplos incluem provedores de serviços de internet (ISPs), grandes corporações, universidades e agências governamentais. Sem o BGP, esses sistemas estariam isolados e incapazes de se comunicar entre si. Enquanto outros protocolos gerenciam o roteamento _dentro_ de um AS, o BGP é responsável pelo roteamento _entre_ eles.

### O Processo de Roteamento do Border Gateway Protocol

A função principal do BGP é o **roteamento do Border Gateway Protocol**. Vamos considerar um exemplo. Imagine que você está em sua rede doméstica e um amigo está usando o Wi-Fi em uma cafeteria. Quando seu amigo lhe envia uma mensagem, o pacote de dados primeiro viaja pela rede local da cafeteria. Ele segue as tabelas de roteamento internas até atingir um roteador de "fronteira" na borda dessa rede.

Esse roteador de fronteira usa o BGP para determinar o melhor caminho para o pacote sair de seu próprio AS e viajar através de outros sistemas autônomos para, eventualmente, alcançar o AS da sua rede doméstica. O BGP não apenas encontra um caminho; ele toma decisões de política para encontrar o caminho _melhor_ com base em regras configuradas por administradores de rede, garantindo uma troca de dados eficiente e confiável em toda a internet global.

## Exercise

Embora não haja laboratórios específicos para este tópico, recomendamos explorar o abrangente [Trilha de Aprendizagem do Linux](https://labex.io/pt/learn/linux) para praticar habilidades e conceitos relacionados ao Linux.

## Quiz Question

Qual protocolo basicamente faz a internet funcionar? Por favor, responda usando a sigla em inglês em letras maiúsculas.

## Quiz Answer

BGP
