---
nome: GPT-6 Sol
provedor: OpenAI
id: ""
preco_1m: "$2 entrada / $10 saída"
status: ativo
papel: execução econômica, conserto de código
melhor_para: [executar plano pronto, revisar/rodar/consertar código, tarefa bem definida, worker de orquestrador]
evitar_para: [criativo, design, vídeo, browser/UI, pesquisa aberta, reinventar a roda]
esforco_recomendado: medium-high
custo_tokens: baixo
fonte: observações de terceiros (2026-09-23)
data_fonte: 2026-09-23
testado_inema: não
reavaliar_em: 2026-09-30
---

# GPT-6 Sol — o executor

"Medíocre, mas frugal." Parecido com Astra no benchmark, abaixo no uso real.

- Padrão: **planejar com Astra → executar com Sol** (ambos médio–alto).
- Também: **worker** de um orquestrador Opus 5.5, com instrução bem específica.
- Não suba acima do nível alto.

**Teste comparativo (10 casos):** perdeu 7 de 8 para o Opus 5.5 (criativo, design, browser, pesquisa),
mas **venceu em consertar codebase grande: 100/100 contra 97/100, a ~1/20 do custo.**
Custou ~1/3 do Opus no total. Faz mais perguntas antes de agir. Travou 1× num filtro de segurança
em tarefa legítima. Tentou "trapacear" no Canva (colar imagem gerada em vez de desenhar).
Parece uma regressão em relação ao GPT-5.6 Sol.
