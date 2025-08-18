---
lang: "pt"
title: "Terminação de Processos"
meta_title: "Terminação de Processos - Processos"
meta_description: "Aprenda sobre a terminação de processos Linux, incluindo processos órfãos e zumbis. Entenda as chamadas de sistema _exit e wait para um gerenciamento eficaz de processos."
meta_keywords: "terminação de processo Linux, processos zumbis, processos órfãos, chamada de sistema wait, _exit, tutorial Linux, Linux para iniciantes"
---

## Lesson Content

Agora que sabemos o que acontece quando um processo é criado, o que acontece quando não precisamos mais dele? Esteja avisado, às vezes o Linux pode ficar um pouco sombrio...

Um processo pode sair usando a chamada de sistema `_exit`. Isso liberará os recursos que o processo estava usando para realocação. Então, quando um processo está pronto para terminar, ele informa ao kernel o motivo de sua terminação com algo chamado status de terminação. Mais comumente, um status de 0 significa que o processo foi bem-sucedido. No entanto, isso não é suficiente para encerrar completamente um processo. O processo pai deve reconhecer a terminação do processo filho usando a chamada de sistema `wait`, e o que isso faz é verificar o status de terminação do processo filho. Eu sei que é horrível pensar nisso, mas a chamada `wait` é uma necessidade; afinal, qual pai não gostaria de saber como seu filho morreu?

Existe outra maneira de encerrar um processo, e isso envolve o uso de sinais, que discutiremos em breve.

### Orphan Processes

Quando um processo pai morre antes de um processo filho, o kernel sabe que não receberá uma chamada `wait`, então, em vez disso, ele torna esses processos "órfãos" e os coloca sob os cuidados de `init` (lembre-se, a mãe de todos os processos). O `init` eventualmente executará a chamada de sistema `wait` para esses órfãos para que eles possam morrer.

### Zombie Processes

O que acontece quando um filho termina e o processo pai ainda não chamou `wait`? Ainda queremos ser capazes de ver como um processo filho terminou, então, embora o processo filho tenha terminado, o kernel transforma o processo filho em um processo zumbi. Os recursos que o processo filho usou ainda são liberados para outros processos; no entanto, ainda há uma entrada na tabela de processos para este zumbi. Processos zumbis também não podem ser mortos, já que estão tecnicamente "mortos", então você não pode usar sinais para matá-los. Eventualmente, se o processo pai chamar a chamada de sistema `wait`, o zumbi desaparecerá; isso é conhecido como "reaping". Se o pai não executar uma chamada `wait`, o `init` adotará o zumbi e executará automaticamente `wait` e removerá o zumbi. Pode ser ruim ter muitos processos zumbis, pois eles ocupam espaço na tabela de processos; se ela encher, impedirá que outros processos sejam executados.

## Exercise

No exercises for this lesson.

## Quiz Question

Qual é o status de terminação mais comum para um processo bem-sucedido?

## Quiz Answer

0
