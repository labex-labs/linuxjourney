---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "pt"
order_index: 3
title: "Ambiente de homologação"
description: "Aprenda o que é possível verificar em homologação e por que o mesmo artefato pode se comportar de forma diferente em cada ambiente."
meta_title: "Ambiente de homologação - Implantação"
meta_description: "Aprenda o que é possível verificar em homologação e por que o mesmo artefato pode se comportar de forma diferente em cada ambiente."
meta_keywords: "homologação, staging, implantação, DevOps, Linux Journey"
---

Uma release está quase pronta. Execute o artefato em **homologação** (staging), um ambiente de teste que procura reproduzir o serviço usado pelas pessoas. Assim você testa a release com configurações próximas das reais antes que ela receba tráfego de produção.

## Promovendo o mesmo artefato

Use a imagem que passou pelos testes e foi aprovada. Refazer o build com dependências que podem mudar pode gerar outro artefato. Anote a referência completa da imagem em cada implantação.

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

O exemplo usa um digest simbólico. O artefato é idêntico, mas as configurações variam.

:::single-choice{#deployment-staging-same-artifact} O que indica que o mesmo código empacotado pode seguir para produção?

::option[A referência do artefato é a mesma nos dois registros de implantação.]{#deployment-staging-same-artifact-b .correct explanation="A referência exata liga ambos os ambientes ao mesmo build."}
::option[Os dois ambientes usam o mesmo rótulo para uma porta.]{#deployment-staging-same-artifact-a explanation="Uma configuração em comum é insuficiente para identificar o artefato."}
::option[Os dois ambientes receberam uma implantação no mesmo dia.]{#deployment-staging-same-artifact-c explanation="A data não identifica o que foi implantado."}
:::

## Escolhendo verificações representativas

A homologação deve permitir que você verifique funções importantes, como abrir a página e ler dados de uma dependência de teste. Use contas de teste autorizadas e dados de teste. Se a verificação passar, você terá mais confiança no cenário que verificou. Diferenças de tráfego, dados ou configuração ainda podem afetar o resultado em produção.

:::single-choice{#deployment-staging-staging-scope} A página de homologação abre usando um banco de teste. O que ainda é preciso verificar após uma implantação real?

::option[Se o artefato deixou de precisar de uma versão.]{#deployment-staging-staging-scope-b explanation="Os registros de versão continuam úteis para verificar ou recuperar o serviço."}
::option[Se todas as requisições em produção vão funcionar.]{#deployment-staging-staging-scope-c explanation="Uma pequena amostra de teste não garante todos os resultados futuros."}
::option[Se o caminho em produção funciona com as configurações aprovadas.]{#deployment-staging-staging-scope-a .correct explanation="A requisição de homologação não passou pelo ambiente de produção."}
:::

## Conferindo o destino antes da mudança

Confira o nome e o endereço do destino antes de implantar. Depois, use o mesmo endereço para confirmar a nova versão e o funcionamento das partes importantes. Registre claramente a qual ambiente pertence cada resultado, seja homologação ou produção.

:::single-choice{#deployment-staging-correct-target} Você pretende implantar em homologação, mas o comando mostra o endereço de produção. O que fazer primeiro?

::option[Continuar e registrar o resultado como homologação.]{#deployment-staging-correct-target-a explanation="O endereço determina qual serviço recebe a mudança."}
::option[Parar e confirmar o destino pretendido.]{#deployment-staging-correct-target-c .correct explanation="Assim você evita aplicar a mudança no ambiente errado."}
::option[Testar em outro navegador após implantar.]{#deployment-staging-correct-target-b explanation="É preciso corrigir o destino antes de iniciar a mudança."}
:::

Para praticar CI/CD, veja [Implantação contínua em homologação](https://labex.io/tutorials/cd-deployment-to-staging-636593).

## Resumo

Agora você consegue usar a homologação para verificar um artefato aprovado antes de promovê-lo.

1. Use o mesmo artefato nos diferentes ambientes.
2. Escolha verificações que representem ações importantes dos usuários.
3. Confirme o ambiente antes de aplicar a mudança.
