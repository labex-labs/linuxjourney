---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "pt"
order_index: 5
title: "Rollbacks"
description: "Aprenda a escolher uma versão que já funcionou e a verificar se basta reverter a aplicação."
meta_title: "Rollbacks - Implantação"
meta_description: "Aprenda a escolher uma versão que já funcionou e a verificar se basta reverter a aplicação."
meta_keywords: "rollback, reversão, implantação, DevOps, Linux Journey"
---

Um **rollback** devolve o serviço a uma release anterior cujo funcionamento já foi verificado. Consulte o histórico de implantações para escolher a versão. Antes de reverter, verifique se a release também alterou dados ou configurações compartilhados.

## Escolhendo uma release anterior

O exemplo mostra uma nova release seguida de uma requisição com falha. A última versão verificada foi a 2. Em um registro real, os identificadores abaixo seriam digests completos das imagens.

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

A versão 2 é uma candidata ao rollback se ainda for compatível com o ambiente. Use a identificação registrada do artefato para encontrá-la.

:::single-choice{#deployment-rollbacks-previous-version} Qual imagem você examinaria primeiro para o rollback?

::option[A imagem mais recente no cache do host.]{#deployment-rollbacks-previous-version-a explanation="A ordem do cache não indica qual release funcionava."}
::option[Digest-C, pois corresponde à implantação mais recente.]{#deployment-rollbacks-previous-version-c explanation="O registro associa esse artefato à verificação que falhou."}
::option[Digest-B, que já passou pelas verificações pertinentes.]{#deployment-rollbacks-previous-version-b .correct explanation="O registro associa esse artefato à última versão verificada."}
:::

## Verificando a compatibilidade dos dados

Uma release também pode alterar um banco de dados ou outro recurso compartilhado. Ao iniciar uma imagem anterior, o estado externo à aplicação continua como estava. Verifique se a versão anterior consegue ler os dados atuais. Se precisar restaurar dados, siga o plano de recuperação da equipe e leve em conta as alterações feitas após o backup.

:::single-choice{#deployment-rollbacks-external-state} A versão 3 mudou o formato do banco de dados. O que você precisa confirmar antes de colocar a versão 2 para usar esse banco?

::option[Se a versão 2 passou na verificação anterior da página inicial.]{#deployment-rollbacks-external-state-b explanation="A verificação anterior faz da versão 2 uma candidata. A compatibilidade com o formato atual ainda precisa ser confirmada."}
::option[Se a versão 2 é compatível com o formato atual.]{#deployment-rollbacks-external-state-a .correct explanation="Trocar a imagem da aplicação não reverte os dados compartilhados."}
::option[Se o nome do banco aparece nas notas da release.]{#deployment-rollbacks-external-state-c explanation="O que importa é se o código anterior consegue usar os dados atuais."}
:::

## Confirmando o resultado

Depois do rollback, confirme a versão em execução e repita a verificação que falhou no caminho usado pelos usuários. Examine novamente as dependências importantes. Registre o horário, a versão restaurada e os resultados para que outra pessoa consiga distinguir a falha original da recuperação.

:::single-choice{#deployment-rollbacks-rollback-proof} O comando de rollback terminou. Qual par de observações indica que o serviço se recuperou?

::option[O endpoint informa a versão 2 e a verificação que falhou agora funciona.]{#deployment-rollbacks-rollback-proof-c .correct explanation="Essas observações confirmam a versão desejada e o comportamento afetado."}
::option[Dois downloads de imagem bem-sucedidos.]{#deployment-rollbacks-rollback-proof-a explanation="Os downloads disponibilizam os arquivos. O serviço em execução ainda precisa ser testado."}
::option[Uma captura de tela antiga da versão 2.]{#deployment-rollbacks-rollback-proof-b explanation="A captura mostra como o serviço estava antes."}
:::

## Resumo

Agora você consegue planejar um rollback com base em evidências.

1. Escolha uma release cujo funcionamento já foi verificado.
2. Confirme a compatibilidade com os dados e as configurações compartilhados.
3. Verifique a versão restaurada e o comportamento que afetou os usuários.
