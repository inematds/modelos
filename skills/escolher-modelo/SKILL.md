---
name: escolher-modelo
description: Escolhe o modelo de IA (Claude, GPT-6, Grok) certo para uma tarefa com base na pilha atual do INEMA. Use quando o usuário perguntar "qual modelo uso", "Opus ou GPT", "vale usar Fable/Sonnet/Haiku", "quem planeja e quem executa", ou antes de montar um fluxo com mais de um modelo.
---

# Escolher modelo

Fonte da verdade: `~/projetos/modelos` (README + `modelos/*.md`). Se divergir, o repo vence.

## Procedimento
1. Classifique a tarefa pelo **passo mais difícil**:
   - Planejar / difícil / arquitetura → **Astra** (médio–alto)
   - Uso geral / projeto complexo → **Opus 5.5** (esforço baixo)
   - Executar plano já pronto → **GPT-6 Sol** (médio–alto)
   - Braçal inequívoco: simples → **Luna Low**; pesado → **Luna High/X-High**
   - Ambíguo e caro de errar → **Astra propõe + Opus 5.5 revisa**
2. Esforço: o menor que resolve; acima de "alto" não compensa.
3. Evitar: Grok 4.7, Fable 5.1, Sonnet 5, Haiku 4.5 (ver fichas para o motivo).
4. Se a tarefa usar dois modelos, entregue o prompt de `prompts/` correspondente.

## Resposta
Uma linha: **modelo + esforço + motivo**. Se houver fluxo em 2 etapas, uma linha por etapa.

## Cuidados
- A pilha vem de observações de terceiros (2026-09-23), ainda não testada. Diga isso se a decisão for cara.
- Modelo lançado há menos de 1 semana: avise sobre a "lua de mel".
