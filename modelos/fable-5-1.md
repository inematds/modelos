---
nome: Claude Fable 5.1
provedor: Anthropic
id: claude-fable-5-1
preco_1m: "$10 entrada / $50 saída"
contexto: 1M
status: evitar
papel: —
melhor_para: []
evitar_para: [uso geral — Opus 5.5 entrega igual ou melhor por menos]
esforco_recomendado: ""
custo_tokens: alto
fonte: observações de terceiros (2026-09-23) + claude-api skill (id/preço)
data_fonte: 2026-09-23
testado_inema: parcial (Fable 5 vs Opus 4.8 — ver abaixo)
reavaliar_em: 2026-09-30
---

# Fable 5.1 — perdeu espaço

- Consome muito token (pode consumir metade do orçamento).
- Opus 5.5 é melhor para uso geral e 2,5× mais barato por token.
- Caso ambíguo: prefira **Astra + Opus 5.5 como segunda opinião**.

**Evidência própria (modelos anteriores):** `~/.claude/runbooks/fable-analise-completa.md` —
Fable 5 pensava antes de agir em 85% dos turnos (Opus 4.8: 54%) e testava após editar em 41% (Opus 4.8: 2%).
Não medido ainda contra o Opus 5.5. Esses hábitos podem ser pedidos via prompt a qualquer modelo.
