# Orquestrador Opus 5.5 + workers baratos (Sol / Luna)

O Opus decide e revisa; workers baratos fazem as partes bem definidas.
Use quando a tarefa se quebra em **várias subtarefas independentes e verificáveis**.

## Prompt do orquestrador (Opus 5.5, esforço baixo)

```
Objetivo: <resultado final>

1. Quebre em subtarefas independentes. Para cada uma escreva uma instrução para um worker
   mais simples que NÃO vai tomar decisões:
   - pasta exclusiva onde ele pode escrever (nenhuma outra)
   - entrada, saída esperada, formato
   - como verificar que ficou pronto
2. Guarde para você as partes de julgamento (design, texto, escolhas) e a integração final.
3. Quando os workers devolverem, revise cada resultado contra a verificação e integre.
```

## Prompt de cada worker (Sol ou Luna)

```
Você só pode criar/editar arquivos dentro de: <pasta>
Tarefa: <instrução do orquestrador>
Pronto quando: <verificação>
Se algo não estiver claro, pare e diga o que falta — não invente.
Ao terminar: o que fez, o resultado da verificação, e o que ficou pendente.
```

## Quando NÃO usar
- Tarefa criativa única (site, reel, design): o Opus sozinho se saiu melhor no teste comparativo.
- Subtarefas que dependem umas das outras: a coordenação custa mais do que economiza.
