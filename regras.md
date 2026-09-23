# Regras de uso

## 1. Sem lealdade
Use o modelo que resolve melhor **aquela** tarefa. Time Codex, time Claude — tanto faz.
Vá para onde você é melhor atendido.

## 2. Benchmark não decide
Benchmark mostra potencial; o que importa é o resultado nas **suas** tarefas.
Ex.: Sol parece com Astra no benchmark, mas fica abaixo no uso real.

## 3. Lua de mel (espere 1 semana)
Todo modelo novo parece divino nos primeiros 2 dias. A qualidade costuma cair depois,
quando a capacidade extra de lançamento é desligada.

- Dia 0–2: use, anote, **não troque a pilha**.
- Dia 7: compare com as anotações do dia 0. Caiu? Mantenha a pilha anterior.
- Registre tudo em [log.md](log.md).

## 4. Esforço: o menor que resolve
- Opus 5.5 em **baixo** já serve como modelo principal (default da API é `medium`).
- Acima do nível "alto" não houve ganho real — não gaste o orçamento no topo.
- Suba o esforço só com **evidência** de resultado insuficiente.

## 5. Planejar ≠ executar
Modelo forte planeja, modelo barato executa. Padrões prontos em [prompts/](prompts/).

## 6. Custo por resultado, não por token
Pergunta certa: "com a mesma assinatura, qual modelo me entrega mais resultado bom antes de bater o limite?"
Um modelo que gasta 3× mais cota mas acerta de primeira pode sair mais barato que 4 tentativas no econômico.
Preços por token (nas fichas) servem só de referência de peso relativo — o uso aqui é por assinatura.

## 7. Um agente, uma pasta
Dois agentes no mesmo repositório se atropelam (anulou 2 de 10 casos num teste comparativo).
Rode cada agente em pasta/worktree própria e diga no prompt: "não edite arquivos fora de `<pasta>`".

## Protocolo de teste rápido (30 min)

1. Escolha **3 tarefas reais** suas (1 simples, 1 média, 1 difícil/ambígua).
2. Rode as 3 no modelo atual e no candidato, mesmo prompt.
3. Anote por tarefa: resultado OK? retrabalho? tempo? quanto da cota da assinatura consumiu?
4. Registre uma linha por modelo em [log.md](log.md).
5. Repita a tarefa difícil no dia 7 (checagem de lua de mel).

Se ficou sobrecarregado com tantos lançamentos: normal. Teste rápido > ler benchmark.
