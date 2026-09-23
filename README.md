# modelos — qual modelo usar, direto ao ponto

Catálogo prático dos modelos recentes (Claude, GPT-6, Grok) para decidir **qual usar em cada tarefa**
e servir de base para skills, prompts e orientações.

> **Status:** baseado em observações de terceiros de 2026-09-23, incluindo um teste comparativo
> Opus 5.5 × GPT-6 Sol em 10 casos reais.
> Nada aqui foi testado pelo INEMA ainda. Reavaliar em **2026-09-30** (fim da "lua de mel").
> Bateria de teste própria: [avaliacao/bateria.md](avaliacao/bateria.md).
> **Uso e testes via assinatura** (plano Claude + plano Codex), não API: "custo" = consumo da cota.

## Pilha atual (sem lealdade a plataforma)

| Tarefa | Modelo | Esforço | Por quê |
|---|---|---|---|
| Planejar, problema difícil, "jogar guerra" | **Astra** | médio–alto | Melhor em tarefa exigente |
| Uso geral, projeto complexo | **Opus 5.5** | baixo | Rápido, direto, econômico, pede pouca instrução |
| Criativo, design, vídeo, browser, pesquisa | **Opus 5.5** | baixo–médio | Venceu 7×1 no teste comparativo; acerta de primeira |
| Executar plano já definido | **GPT-6 Sol** | médio–alto | Bom custo; abaixo do Astra no difícil |
| Consertar/revisar código com critério claro | **GPT-6 Sol** | médio–alto | Venceu Opus nisso a ~1/20 do custo |
| Muitas subtarefas em paralelo | **Opus 5.5 orquestra + Sol/Luna executam** | — | Julgamento caro 1×, execução barata N× |
| Braçal simples e rápido | **GPT-6 Luna Low** | low | Tarefa clara, sem ambiguidade |
| Braçal pesado/operacional | **GPT-6 Luna High / X-High** | high | Substitui o papel do Sonnet |
| Caso ambíguo | **Astra + Opus 5.5** (2ª opinião) | — | Duas visões baratas > uma cara |

**Fora da pilha:** Grok 4.7 (pior que 4.6) · Fable 5.1 (caro, superado pelo Opus 5.5) ·
Sonnet 5 e Haiku 4.5 (custo/benefício fraco na pilha Claude).

## 4 regras

1. **Melhor modelo por tarefa**, sem lealdade a nenhuma plataforma.
2. **Teste nas suas tarefas**, não confie só em benchmark.
3. **Lua de mel:** modelo novo parece ótimo nos primeiros dias. Espere 1 semana antes de trocar a pilha.
4. **Não pague pelo topo:** acima do nível "alto" de esforço não houve ganho real.
5. **Meça cota gasta por resultado bom**, não preço por token (o mais "caro" pode render mais se acerta de primeira).

Detalhe e protocolo de teste em [regras.md](regras.md).

## Estrutura

```
README.md            esta página — a orientação rápida
regras.md            regras + protocolo de teste de 1 semana
log.md               observações datadas (mais recente no topo)
avaliacao/           bateria de teste própria (para a sessão extra)
modelos/<slug>.md    uma ficha por modelo (frontmatter YAML)
prompts/             padrões prontos: planejar→executar, 2ª opinião, braçal
skills/              como virar skill + rascunho da skill escolher-modelo
```

## Relação com outras ferramentas

- **`/maestro-roteador`** (skill já instalada) decide **modelo × esforço** dentro da pilha Claude.
  Este repo é o **catálogo multi-provedor**. Atenção: o maestro ainda recomenda Sonnet/Haiku/Fable,
  o que conflita com a pilha acima — ver [log.md](log.md).
- Evidência própria sobre comportamento Fable vs Opus (modelos anteriores):
  `~/.claude/runbooks/fable-analise-completa.md`.
