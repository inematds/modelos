# 🧭 modelos — qual modelo de IA usar em cada tarefa

[![Qual modelo de IA usar](guia/assets/banner.jpg)](https://inematds.github.io/modelos/guia/)

Muitos modelos chegaram ao mesmo tempo. A resposta prática é simples:
**use o melhor modelo para cada tarefa, sem lealdade a nenhuma plataforma.**

📖 **Guia:** [Português](https://inematds.github.io/modelos/guia/) · [English](https://inematds.github.io/modelos/guia/en/) · [Español](https://inematds.github.io/modelos/guia/es/)
🧩 **Modelos explicados de forma simples:** [PT](https://inematds.github.io/modelos/guia/modelos/) · [EN](https://inematds.github.io/modelos/guia/en/modelos/) · [ES](https://inematds.github.io/modelos/guia/es/modelos/)

---

## Visão rápida dos modelos

### 🟠 Claude Opus 5.5 — o melhor para uso geral
- Rápido, direto e econômico em tokens.
- Excelente em projetos complexos; precisa de poucas instruções.
- Forte em criativo, design, vídeo, pesquisa e navegador.
- **Modelo principal para o dia a dia**, em esforço baixo.

### 🔷 GPT-6 Astra — planejamento e problemas difíceis
- Pensar antes de fazer: planejar, decidir arquitetura, simular cenários.
- Esforço médio a alto (acima disso não houve ganho).

### ☀️ GPT-6 Sol — execução com bom custo
- Bom e econômico, mas abaixo do Astra no que é exigente.
- Faz sentido para tarefas **já bem definidas** e para consertar código com testes.
- Estratégia: **planejar com Astra → executar com Sol**.

### 🌙 GPT-6 Luna — trabalho braçal
- Tarefas repetitivas, claras e sem ambiguidade.
- **Luna Low:** simples e rápido. **Luna High / X-High:** pesado e operacional.

### ✖️ Grok 4.7 — fora
- Experiência ruim; inferior ao 4.6. Não entrou na pilha.

### 💎 Claude Fable 5.1 — perdeu espaço
- Consome muitos tokens; o Opus 5.5 entrega o mesmo ou mais por menos.
- Para caso ambíguo, prefira **Astra + Opus 5.5 como segunda opinião**.

### ➖ Claude Sonnet 5 e Haiku 4.5 — pular
- Sonnet 5 gasta demais por tarefa; o Haiku atual é fraco. Dentro do Claude, use o Opus 5.5 em esforço baixo.

---

## A pilha hoje

| Papel | Modelo | Esforço |
|---|---|---|
| Planejamento e problemas difíceis | **GPT-6 Astra** | médio–alto |
| Uso geral e projetos complexos | **Claude Opus 5.5** | baixo |
| Criativo, design, vídeo, navegador | **Claude Opus 5.5** | baixo–médio |
| Execução econômica / consertar código | **GPT-6 Sol** | médio–alto |
| Tarefas repetitivas | **GPT-6 Luna** (Low ou High/X-High) | conforme o peso |
| Muitas subtarefas em paralelo | **Opus 5.5 orquestra + Sol/Luna executam** | — |
| Caso ambíguo | **Astra propõe + Opus 5.5 revisa** | — |

Uso e testes **via assinaturas** (plano Claude + plano Codex), não API: "custo" = quanto da cota cada modelo consome.

## Regra principal

**Não confie apenas em benchmarks. Teste os modelos nas suas próprias tarefas.**

⚠️ **Efeito lua de mel:** modelos novos parecem incríveis nos primeiros dias. Espere uma semana,
observe estabilidade, qualidade e custo antes de mudar toda a pilha.
Próxima revisão: **2026-09-30**.

---

## Como usar este repositório

| Quero… | Abra |
|---|---|
| Decidir rápido | a tabela acima |
| Detalhe de um modelo | [`modelos/`](modelos/) — uma ficha por modelo (YAML: status, melhor para, evitar para, esforço) |
| Usar dois modelos juntos | [`prompts/`](prompts/) — planejar→executar, segunda opinião, orquestrador+workers, tarefa braçal |
| Entender as regras | [`regras.md`](regras.md) — sem lealdade, lua de mel, cota por resultado, um agente por pasta, teste de 30 min |
| Testar nas minhas tarefas | [`avaliacao/bateria.md`](avaliacao/bateria.md) — 8 casos reais com nota 0–3 |
| Registrar o que observei | [`log.md`](log.md) — uma linha por observação |
| Virar skill | [`skills/`](skills/) — rascunho `escolher-modelo` (ainda não instalado) |

O guia (landing) é gerado por `python3 guia/_src/build.py` — o texto das 3 línguas fica nesse script.

## Relação com outras ferramentas

- **`/maestro-roteador`** decide modelo × esforço dentro da pilha Claude. Este repositório é o catálogo multi-provedor.
  O maestro ainda recomenda Sonnet/Haiku/Fable, o que conflita com a pilha acima — revisar após 2026-09-30 (ver [`log.md`](log.md)).
