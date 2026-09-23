---
nome: Claude Opus 5.5
provedor: Anthropic
id: claude-opus-5-5
preco_1m: "$4 entrada / $20 saída (fast mode $8/$40)"
contexto: 1M
status: ativo
papel: uso geral, projetos complexos
melhor_para: [uso geral, projeto complexo, SaaS, Remotion, Hyperframes, código]
evitar_para: []
esforco_recomendado: low
custo_tokens: baixo
fonte: observações de terceiros (2026-09-23) + claude-api skill (id/preço)
data_fonte: 2026-09-23
testado_inema: não
reavaliar_em: 2026-09-30
---

# Opus 5.5 — o principal

**Use como modelo padrão.** Rápido, direto, econômico em tokens, pede pouca instrução.

- Rodar em esforço **baixo** como "sistema operacional" do dia a dia.
- Aguenta projeto complexo sem prompt longo — não superespecifique.
- Segunda opinião barata em caso ambíguo (junto com Astra).

**Notas técnicas (API):** thinking não pode ser desligado; controle é só por `effort`
(default `medium` — setar `low` explicitamente). `tool_choice` forçado dá 400.

**Teste comparativo Opus 5.5 × Sol (10 casos, 2026-09-23):** venceu 7 de 8 — site, reel, sizzle, mundo 3D,
pesquisa/roteiro, browser (Skool, Canva). Custa ~2–4× mais que o Sol por tarefa (até 20× em código),
mas acerta de primeira em criativo/design/julgamento. Perdeu em conserto de codebase grande.
Não travou no filtro de segurança onde o Sol travou.

**Papel extra:** orquestrador que despacha workers baratos (Sol/Luna) — ver `prompts/orquestrador-workers.md`.

**Evidência própria:** nenhuma ainda com o 5.5.
