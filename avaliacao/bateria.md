# Bateria INEMA — teste próprio dos modelos

Objetivo: trocar "o que os outros acharam" por evidência nas **nossas** tarefas.
Rodar 1× agora (lua de mel) e repetir a partir de **2026-09-30**.

## Regras da rodada
- Mesmo prompt, mesma entrada, **pasta separada por modelo** (`runs/<data>/<caso>/<modelo>/`).
- Tudo via **assinatura** (Claude Code no plano Claude; Codex no plano ChatGPT/Codex) — nada de API.
- Anotar: acertou de primeira? retrabalho (nº de correções)? tempo? **consumo da cota** (% do limite de 5h/semana antes e depois; `/usage` no Claude Code, painel de uso no Codex)?
- Nota 0–3: 0 inutilizável · 1 precisa refazer · 2 ajustes pequenos · 3 publicável.
- Resultado vai em `log.md` (uma linha por caso × modelo) e o resumo nas fichas.

## Casos (do mais barato ao mais caro)

| # | Caso INEMA | Tipo | Modelos | Critério de "bom" |
|---|---|---|---|---|
| 1 | Renomear/extrair dados de um lote de arquivos | braçal | Luna Low, Haiku 4.5, Opus 5.5 low | 100% certo, nada fora do pedido |
| 2 | Corrigir bug real de um projeto (com teste que falha) | código | Sol, Opus 5.5 | teste passa, diff pequeno |
| 3 | Roteiro de reel a partir de ideia bruta | criativo/texto | Opus 5.5, Sol | gancho forte, tom INEMA, pronto pra gravar |
| 4 | Guia landing de um repo (`projetos-landing-guia`) | design | Opus 5.5, Sol | publicável sem retoque visual |
| 5 | Módulo de curso v5 | conteúdo longo | Opus 5.5, Sol | didático p/ público 40+, sem erro factual |
| 6 | Vídeo curto em Hyperframes | vídeo | Opus 5.5, Sol | ritmo, áudio, sem bug de render |
| 7 | Pesquisa aberta com fontes (ex.: eventos de IA no mês) | pesquisa | Opus 5.5, Sol, Astra | fatos conferíveis, nada inventado |
| 8 | Planejar feature ambígua → executar | fluxo 2 etapas | Astra→Sol, Opus sozinho | plano executado sem improviso; custo total |

## O que decidir no fim
- A pilha do README se confirma nas nossas tarefas?
- Instalar `skills/escolher-modelo` ou atualizar o `/maestro-roteador`?
- Haiku/Sonnet saem mesmo da pilha Claude (casos 1 e 2)?
