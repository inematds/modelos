# Transformar este catálogo em skill

As fichas em `modelos/` têm frontmatter padronizado (`status`, `melhor_para`, `evitar_para`,
`esforco_recomendado`), então uma skill pode ser derivada direto delas.

## Rascunho pronto
`escolher-modelo/SKILL.md` — responde "qual modelo uso pra isso?" com base na pilha atual.
**Não instalado.** Para instalar:

```bash
cp -r skills/escolher-modelo ~/.claude/skills/
```

## Antes de instalar, decidir
- **Sobreposição com `/maestro-roteador`:** o maestro decide modelo × esforço só na pilha Claude
  (e ainda cita Sonnet/Haiku/Fable). Opções: (a) instalar esta como skill multi-provedor separada;
  (b) atualizar o maestro com a pilha nova; (c) fazer o maestro apontar para este repo.
- **Esperar o teste de 1 semana** (`regras.md`) antes de cravar a pilha numa skill.

## Ao mudar a pilha
Atualize as fichas → README (tabela) → `escolher-modelo/SKILL.md`. Registre em `log.md`.
