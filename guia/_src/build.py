#!/usr/bin/env python3
"""Gera as páginas do guia (PT/EN/ES): guia/<lang>/index.html e guia/<lang>/modelos/index.html.

Uso:  python3 guia/_src/build.py
Conteúdo: MODELOS e T abaixo. Estilo: guia/_src/head.html (CSS do padrão INEMA) + foot.html.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # .../guia
HEAD = (ROOT / "_src/head.html").read_text()
FOOT = (ROOT / "_src/foot.html").read_text()
REPO = "https://github.com/inematds/modelos"
BASE = "https://inematds.github.io/modelos/guia/"
LANGS = ["pt", "en", "es"]
HTML_LANG = {"pt": "pt-BR", "en": "en", "es": "es"}
BRAND = {"pt": "Qual Modelo de IA Usar", "en": "Which AI Model to Use", "es": "Qué Modelo de IA Usar"}
BANNER = {"pt": "banner.jpg", "en": "banner-en.jpg", "es": "banner-es.jpg"}

# ---------------------------------------------------------------- modelos
# role_out=True → fora da pilha
MODELOS = [
  {"id": "opus", "emoji": "🟠", "nome": "Claude Opus 5.5", "out": False, "eff": "low",
   "role": {"pt": "Uso geral — o principal", "en": "General use — the main one", "es": "Uso general — el principal"},
   "one": {"pt": "O melhor para o dia a dia: rápido, direto, econômico em tokens e excelente em projetos complexos.",
           "en": "The best for everyday work: fast, direct, token-efficient and excellent on complex projects.",
           "es": "El mejor para el día a día: rápido, directo, económico en tokens y excelente en proyectos complejos."},
   "like": {"pt": "Pense nele como o profissional sênior que resolve quase tudo com pouca explicação.",
            "en": "Think of it as the senior professional who handles almost anything with little explanation.",
            "es": "Piensa en él como el profesional sénior que resuelve casi todo con poca explicación."},
   "use": {"pt": ["Trabalho geral e projetos grandes", "Sites, vídeo, design e tarefas criativas", "Pesquisa e uso do navegador", "Segunda opinião em casos ambíguos"],
           "en": ["General work and large projects", "Websites, video, design and creative tasks", "Research and browser use", "Second opinion on ambiguous cases"],
           "es": ["Trabajo general y proyectos grandes", "Sitios web, video, diseño y tareas creativas", "Investigación y uso del navegador", "Segunda opinión en casos ambiguos"]},
   "avoid": {"pt": ["Consertos de código repetitivos com critério claro — o Sol faz por menos"],
             "en": ["Repetitive code fixes with a clear criterion — Sol does it for less"],
             "es": ["Arreglos de código repetitivos con criterio claro — Sol lo hace por menos"]},
   "effort": {"pt": "esforço baixo (precisa de poucas instruções)", "en": "low effort (needs few instructions)", "es": "esfuerzo bajo (necesita pocas instrucciones)"}},
  {"id": "astra", "emoji": "🔷", "nome": "GPT-6 Astra", "out": False, "eff": "medium-high",
   "role": {"pt": "Planejamento e problemas difíceis", "en": "Planning and hard problems", "es": "Planificación y problemas difíciles"},
   "one": {"pt": "O modelo para pensar antes de fazer: planejar, decidir arquitetura e atacar o que é realmente difícil.",
           "en": "The model for thinking before doing: planning, deciding architecture and tackling what is truly hard.",
           "es": "El modelo para pensar antes de hacer: planificar, decidir arquitectura y atacar lo realmente difícil."},
   "like": {"pt": "Pense nele como o arquiteto: desenha o plano que outro vai executar.",
            "en": "Think of it as the architect: it draws the plan someone else will execute.",
            "es": "Piensa en él como el arquitecto: dibuja el plan que otro va a ejecutar."},
   "use": {"pt": ["Planejar projetos e simular cenários", "Decisões difíceis e de arquitetura", "Primeira proposta em caso ambíguo (com Opus revisando)"],
           "en": ["Planning projects and simulating scenarios", "Hard and architectural decisions", "First proposal on an ambiguous case (with Opus reviewing)"],
           "es": ["Planificar proyectos y simular escenarios", "Decisiones difíciles y de arquitectura", "Primera propuesta en un caso ambiguo (con Opus revisando)"]},
   "avoid": {"pt": ["Trabalho braçal e repetitivo — desperdício"],
             "en": ["Repetitive grunt work — a waste"],
             "es": ["Trabajo repetitivo y pesado — un desperdicio"]},
   "effort": {"pt": "esforço médio a alto (acima disso não houve ganho)", "en": "medium to high effort (no gain above that)", "es": "esfuerzo medio a alto (por encima no hubo ganancia)"}},
  {"id": "sol", "emoji": "☀️", "nome": "GPT-6 Sol", "out": False, "eff": "medium-high",
   "role": {"pt": "Execução com bom custo", "en": "Cost-effective execution", "es": "Ejecución con buen costo"},
   "one": {"pt": "Bom e econômico em tokens, mas abaixo do Astra no que é exigente. Brilha quando a tarefa já está bem definida.",
           "en": "Good and token-efficient, but below Astra on demanding work. It shines when the task is already well defined.",
           "es": "Bueno y económico en tokens, pero por debajo de Astra en lo exigente. Brilla cuando la tarea ya está bien definida."},
   "like": {"pt": "Pense nele como o executor eficiente: segue o plano à risca.",
            "en": "Think of it as the efficient executor: it follows the plan to the letter.",
            "es": "Piensa en él como el ejecutor eficiente: sigue el plan al pie de la letra."},
   "use": {"pt": ["Executar um plano pronto (planejar com Astra → executar com Sol)", "Revisar, rodar e consertar código com testes", "Worker de um orquestrador Opus 5.5"],
           "en": ["Executing a ready plan (plan with Astra → execute with Sol)", "Reviewing, running and fixing code with tests", "Worker under an Opus 5.5 orchestrator"],
           "es": ["Ejecutar un plan listo (planificar con Astra → ejecutar con Sol)", "Revisar, correr y arreglar código con pruebas", "Worker de un orquestador Opus 5.5"]},
   "avoid": {"pt": ["Tarefas criativas, design, vídeo e navegador", "Problemas difíceis sem um plano"],
             "en": ["Creative tasks, design, video and browser", "Hard problems without a plan"],
             "es": ["Tareas creativas, diseño, video y navegador", "Problemas difíciles sin un plan"]},
   "effort": {"pt": "esforço médio a alto", "en": "medium to high effort", "es": "esfuerzo medio a alto"}},
  {"id": "luna", "emoji": "🌙", "nome": "GPT-6 Luna", "out": False, "eff": "low | high",
   "role": {"pt": "Trabalho braçal", "en": "Grunt work", "es": "Trabajo pesado"},
   "one": {"pt": "O executor para tarefas repetitivas, claras e sem ambiguidade. Tem dois ritmos: leve e pesado.",
           "en": "The executor for repetitive, clear and unambiguous tasks. It has two gears: light and heavy.",
           "es": "El ejecutor para tareas repetitivas, claras y sin ambigüedad. Tiene dos ritmos: ligero y pesado."},
   "like": {"pt": "Pense nele como o assistente que faz o volume, desde que a instrução seja exata.",
            "en": "Think of it as the assistant who handles the volume, as long as the instruction is exact.",
            "es": "Piensa en él como el asistente que hace el volumen, siempre que la instrucción sea exacta."},
   "use": {"pt": ["Luna Low: tarefas simples e rápidas (renomear, extrair, formatar)", "Luna High / X-High: trabalho operacional pesado, lotes grandes"],
           "en": ["Luna Low: simple, fast tasks (rename, extract, format)", "Luna High / X-High: heavy operational work, large batches"],
           "es": ["Luna Low: tareas simples y rápidas (renombrar, extraer, formatear)", "Luna High / X-High: trabajo operativo pesado, lotes grandes"]},
   "avoid": {"pt": ["Qualquer coisa que precise interpretar o que você quis dizer"],
             "en": ["Anything that requires interpreting what you meant"],
             "es": ["Cualquier cosa que requiera interpretar lo que quisiste decir"]},
   "effort": {"pt": "Low para o simples; High / X-High para o pesado", "en": "Low for simple; High / X-High for heavy", "es": "Low para lo simple; High / X-High para lo pesado"}},
  {"id": "fable", "emoji": "💎", "nome": "Claude Fable 5.1", "out": True, "eff": "—",
   "role": {"pt": "Perdeu espaço", "en": "Lost its place", "es": "Perdió espacio"},
   "one": {"pt": "Muito capaz, mas consome muitos tokens — e o Opus 5.5 passou a entregar o mesmo ou mais por bem menos.",
           "en": "Very capable, but token-hungry — and Opus 5.5 now delivers the same or more for much less.",
           "es": "Muy capaz, pero consume muchos tokens — y Opus 5.5 ahora entrega lo mismo o más por mucho menos."},
   "like": {"pt": "Pense nele como o consultor caro que você só chama se nada mais resolver.",
            "en": "Think of it as the expensive consultant you only call when nothing else works.",
            "es": "Piensa en él como el consultor caro al que solo llamas si nada más funciona."},
   "use": {"pt": ["Para caso ambíguo, prefira Astra + Opus 5.5 como segunda opinião"],
           "en": ["For an ambiguous case, prefer Astra + Opus 5.5 as a second opinion"],
           "es": ["Para un caso ambiguo, prefiere Astra + Opus 5.5 como segunda opinión"]},
   "avoid": {"pt": ["Uso geral — pesa demais na cota da assinatura"],
             "en": ["General use — too heavy on the subscription quota"],
             "es": ["Uso general — pesa demasiado en la cuota de la suscripción"]},
   "effort": {"pt": "fora da pilha", "en": "out of the stack", "es": "fuera del stack"}},
  {"id": "grok", "emoji": "✖️", "nome": "Grok 4.7", "out": True, "eff": "—",
   "role": {"pt": "Rebaixamento", "en": "A step back", "es": "Un paso atrás"},
   "one": {"pt": "Experiência ruim nos testes de uso e inferior à versão anterior (4.6).",
           "en": "Poor experience in hands-on use and worse than the previous version (4.6).",
           "es": "Mala experiencia en el uso y peor que la versión anterior (4.6)."},
   "like": {"pt": "Se precisar de Grok, o 4.6 era melhor.",
            "en": "If you need Grok, 4.6 was better.",
            "es": "Si necesitas Grok, el 4.6 era mejor."},
   "use": {"pt": [], "en": [], "es": []},
   "avoid": {"pt": ["Tudo, por enquanto"], "en": ["Everything, for now"], "es": ["Todo, por ahora"]},
   "effort": {"pt": "fora da pilha", "en": "out of the stack", "es": "fuera del stack"}},
  {"id": "sonnet", "emoji": "➖", "nome": "Claude Sonnet 5 · Haiku 4.5", "out": True, "eff": "—",
   "role": {"pt": "Pular na pilha Claude", "en": "Skip in the Claude stack", "es": "Saltar en el stack de Claude"},
   "one": {"pt": "O Sonnet 5 gasta demais por tarefa; o Haiku atual é fraco. Dentro do Claude, use o Opus 5.5 em esforço baixo.",
           "en": "Sonnet 5 costs too much per task; the current Haiku is weak. Inside Claude, use Opus 5.5 at low effort.",
           "es": "Sonnet 5 gasta demasiado por tarea; el Haiku actual es débil. Dentro de Claude, usa Opus 5.5 con esfuerzo bajo."},
   "like": {"pt": "O papel deles passou para outros: Luna faz o braçal, Opus em baixo faz o geral.",
            "en": "Their role moved to others: Luna does grunt work, Opus at low effort does the general work.",
            "es": "Su papel pasó a otros: Luna hace el trabajo pesado, Opus en bajo hace lo general."},
   "use": {"pt": ["Haiku: só como subagente baratíssimo em fluxo 100% Claude — teste antes"],
           "en": ["Haiku: only as a very cheap subagent in a 100% Claude flow — test first"],
           "es": ["Haiku: solo como subagente muy barato en un flujo 100% Claude — prueba antes"]},
   "avoid": {"pt": ["Pilha principal"], "en": ["Main stack"], "es": ["Stack principal"]},
   "effort": {"pt": "fora da pilha", "en": "out of the stack", "es": "fuera del stack"}},
]

# ---------------------------------------------------------------- textos
T = {
 "pt": {
  "title": "Qual Modelo de IA Usar — o modelo certo para cada tarefa",
  "desc": "Guia direto para escolher entre Claude Opus 5.5, GPT-6 Astra, Sol e Luna: modelos explicados de forma simples, pilha por tarefa, regras, prompts e bateria de teste.",
  "mtitle": "Os modelos de IA novos, explicados de forma simples",
  "mdesc": "Opus 5.5, GPT-6 Astra, Sol, Luna, Fable 5.1, Grok 4.7, Sonnet 5 e Haiku: para que serve cada um, quando usar e quando evitar.",
  "nav": ["Modelos", "Pilha", "Guia de uso", "Padrões", "Esforço"],
  "eff_cta": ("Esforço na prática", "Dados do Opus 5.5 e do GPT-6 Astra em todos os níveis de esforço, com gráficos. Na opinião do Nei: medium por padrão, high quando precisar de mais raciocínio, xhigh só em caso extremo."), "toggle": "Alternar tema",
  "chip": "Claude · GPT-6 · Grok — setembro de 2026",
  "h1": 'O modelo <span class="amb">certo</span> para cada tarefa',
  "lead": "Muitos modelos chegaram ao mesmo tempo. A resposta prática é simples: use o melhor modelo para cada tarefa, sem lealdade a nenhuma plataforma.",
  "cta1": "Ver os modelos", "cta2": "Guia de uso", "alt": "Banner: qual modelo de IA usar para cada tarefa",
  "q_chip": "Visão rápida", "q_h": "Cada modelo em uma linha",
  "q_sub": "Clique em um modelo para a explicação completa, em linguagem simples.",
  "rule_h": "Regra principal: não confie só em benchmarks",
  "rule_p": ["<strong>Teste os modelos nas suas próprias tarefas.</strong>",
             "Cuidado com o efeito <strong>lua de mel</strong>: modelos novos parecem incríveis nos primeiros dias. Espere uma semana, observe estabilidade, qualidade e custo antes de mudar toda a sua pilha."],
  "stack_chip": "A pilha hoje", "stack_h": "Quem faz o quê",
  "stack_sub": "Uso via assinaturas (plano Claude + plano Codex). “Custo” aqui é quanto da cota cada modelo consome.",
  "short_stack": [("Planejamento e problemas difíceis", "GPT-6 Astra"), ("Uso geral e projetos complexos", "Opus 5.5"), ("Execução econômica", "GPT-6 Sol"), ("Tarefas repetitivas", "GPT-6 Luna")],
  "stack": [("1", "Planejar e problemas difíceis", "<strong>GPT-6 Astra</strong> · esforço médio–alto. Arquitetura, simular cenários, casos exigentes."),
            ("2", "Uso geral e projetos complexos", "<strong>Claude Opus 5.5</strong> · esforço baixo. Rápido, direto, econômico, pede pouca instrução."),
            ("3", "Criativo, design, vídeo, navegador", "<strong>Claude Opus 5.5</strong> · baixo–médio. Acerta de primeira onde o gosto importa."),
            ("4", "Executar um plano pronto", "<strong>GPT-6 Sol</strong> · médio–alto. Bom custo quando a tarefa já está bem definida."),
            ("5", "Revisar e consertar código", "<strong>GPT-6 Sol</strong> · médio–alto. Forte quando há critério claro (testes que passam ou falham)."),
            ("6", "Trabalho braçal", "<strong>GPT-6 Luna</strong> · Low para o simples e rápido; High / X-High para o pesado. Só tarefa sem ambiguidade."),
            ("7", "Muitas subtarefas em paralelo", "<strong>Opus 5.5 orquestra</strong>, Sol ou Luna executam. Julgamento uma vez, execução barata várias vezes."),
            ("8", "Caso ambíguo", "<strong>Astra propõe, Opus 5.5 revisa.</strong> Duas visões baratas valem mais que uma cara."),
            ("✕", "Fora da pilha", "Grok 4.7 (pior que o 4.6) · Fable 5.1 (caro, superado pelo Opus 5.5) · Sonnet 5 e Haiku 4.5 (custo-benefício fraco).")],
  "dec_chip": "Como decidir", "dec_h": "Do pedido ao modelo em quatro perguntas", "dec_sub": "Olhe para o passo mais difícil da tarefa, não para a tarefa inteira.",
  "flow": ["Qual o passo mais difícil?", "Menor modelo que resolve", "Menor esforço que cobre o risco", "Confere o resultado", "Anota no log"],
  "rules": [("🚫 Sem lealdade", "Vá para onde você é melhor atendido — time Claude ou time Codex, tanto faz."),
            ("📈 Não pague pelo topo", "Acima do nível “alto” de esforço não houve ganho real. Suba só com evidência."),
            ("🍯 Lua de mel", "Todo modelo novo parece ótimo nos primeiros dias. Espere uma semana antes de trocar a pilha."),
            ("🎯 Cota por resultado", "O modelo que gasta mais cota mas acerta de primeira pode sair mais barato que quatro tentativas no econômico."),
            ("📁 Um agente, uma pasta", "Dois agentes no mesmo repositório se atropelam. Isole cada um e diga no prompt onde ele pode escrever."),
            ("🧪 Teste você mesmo", "Três tarefas reais, dois modelos, mesmo prompt. Trinta minutos valem mais que qualquer benchmark.")],
  "pre_chip": "Pré-requisitos", "pre_h": "O que você precisa", "pre_sub": "Nada para instalar além das ferramentas que você já usa.",
  "pre": [("Assinatura Claude", "Claude Code ou Claude Desktop, para o Opus 5.5.", '<span class="c"># ver consumo da cota</span>\n<span class="k">/usage</span>'),
          ("Assinatura Codex", "Codex CLI ou Codex Desktop, para GPT-6 Astra, Sol e Luna.", '<span class="k">codex</span>  <span class="c"># abre a sessão</span>'),
          ("O repositório", "Fichas, regras e prompts em Markdown.", '<span class="k">git clone</span> <span class="s">https://github.com/inematds/modelos</span>')],
  "g_chip": "Guia de uso · passo a passo", "g_h": "Como usar no dia a dia", "g_sub": "Da consulta rápida até transformar o catálogo numa skill.",
  "steps": [("Consulte a pilha", "A tabela do README é a orientação rápida. Na dúvida, abra a ficha do modelo.",
             '<span class="k">cat</span> README.md               <span class="c"># pilha por tarefa + regras</span>\n<span class="k">cat</span> modelos/opus-5-5.md     <span class="c"># ficha: melhor para, evitar para, esforço</span>'),
            ("Use um padrão pronto", "Para fluxos com mais de um modelo, copie o prompt correspondente.",
             'prompts/planejar-executar.md     <span class="c"># Astra planeja → Sol executa</span>\nprompts/segunda-opiniao.md       <span class="c"># Astra propõe → Opus 5.5 revisa</span>\nprompts/orquestrador-workers.md  <span class="c"># Opus 5.5 distribui → Sol/Luna fazem</span>\nprompts/tarefa-bracal.md         <span class="c"># Luna em lote, sem ambiguidade</span>'),
            ("Registre o que observar", "Uma linha por observação, mais recente no topo. É isso que torna a regra da lua de mel prática.",
             '<span class="c"># log.md</span>\n| data | modelo | tarefa | resultado | fonte |'),
            ("Faça o teste rápido", "Três tarefas reais (simples, média, difícil), mesmo prompt no modelo atual e no candidato. Repita a difícil depois de uma semana.",
             'regras.md             <span class="c"># protocolo de 30 minutos</span>\navaliacao/bateria.md  <span class="c"># 8 casos reais, nota 0–3, cota gasta</span>'),
            ("Vire skill quando a pilha estabilizar", "Há um rascunho pronto que responde “qual modelo uso pra isso?”.",
             '<span class="k">cp -r</span> skills/escolher-modelo ~/.claude/skills/')],
  "p_chip": "Padrões de uso", "p_h": "Três combinações que funcionam", "p_sub": "A parte cara (julgamento) acontece uma vez; a parte longa (execução) sai barata.",
  "pats": [("🗺️ Planejar → executar", "Astra escreve um plano com passos verificáveis; Sol executa sem mudar o plano e para se algo sair do roteiro."),
           ("⚖️ Segunda opinião", "Astra propõe; Opus 5.5 revisa como cético. Se concordam, siga. Se discordam, a divergência é o que você decide."),
           ("🎛️ Orquestrador + workers", "Opus 5.5 quebra o trabalho e revisa; Sol ou Luna fazem cada parte na sua própria pasta.")],
  "r_chip": "Próximos passos", "r_h": "O que vem depois", "r_sub": "A pilha é um ponto de partida e será revista com uso real.",
  "road": [("Agora", "Catálogo publicado", "Modelos explicados, pilha, fichas, regras, prompts e bateria de casos."),
           ("30/09", "Revisão pós-lua de mel", "Confirmar ou ajustar a pilha depois de uma semana de uso."),
           ("Depois", "Skill de escolha de modelo", "Instalar a skill escolher-modelo ou integrar a pilha ao roteador de modelos existente.")],
  "foot": "guia prático de modelos de IA",
  # página modelos
  "m_chip": "Os modelos, em linguagem simples", "m_h1": 'Para que serve <span class="amb">cada modelo</span>',
  "m_lead": "Muitos modelos chegaram de uma vez e é fácil se sentir sobrecarregado. Aqui está, sem jargão, o que cada um faz bem, quando usar e quando evitar.",
  "m_back": "Voltar ao guia", "m_in": "Na pilha", "m_outlbl": "Fora da pilha",
  "m_one": "Em uma frase", "m_use": "Use para", "m_avoid": "Evite para", "m_eff": "Esforço",
  "m_stack_h": "Minha pilha hoje", "m_stack_sub": "Quatro papéis, quatro modelos.",
  "m_over_h": "Se estiver sobrecarregado", "m_over_p": "Você não está sozinho. Em vez de se perder no ruído dos benchmarks, faça um teste rápido: três tarefas reais suas, dois modelos, o mesmo pedido. Em meia hora você sabe mais do que em um dia lendo comparativos.",
  "m_cta": "Como usar isso no dia a dia →",
 },
 "en": {
  "title": "Which AI Model to Use — the right model for each task",
  "desc": "A direct guide to choosing among Claude Opus 5.5, GPT-6 Astra, Sol and Luna: models explained simply, stack per task, rules, prompts and a test battery.",
  "mtitle": "The new AI models, explained simply",
  "mdesc": "Opus 5.5, GPT-6 Astra, Sol, Luna, Fable 5.1, Grok 4.7, Sonnet 5 and Haiku: what each one is for, when to use it and when to avoid it.",
  "nav": ["Models", "Stack", "How to use", "Patterns", "Effort"],
  "eff_cta": ("Effort in practice", "Opus 5.5 and GPT-6 Astra data across every effort level, with charts. Nei's take: medium by default, high when you need more reasoning, xhigh only in extreme cases."), "toggle": "Toggle theme",
  "chip": "Claude · GPT-6 · Grok — September 2026",
  "h1": 'The <span class="amb">right</span> model for each task',
  "lead": "Many models shipped at the same time. The practical answer is simple: use the best model for each task, with no loyalty to any platform.",
  "cta1": "See the models", "cta2": "How to use", "alt": "Banner: which AI model to use for each task",
  "q_chip": "Quick view", "q_h": "Each model in one line",
  "q_sub": "Click a model for the full, plain-language explanation.",
  "rule_h": "Main rule: don't trust benchmarks alone",
  "rule_p": ["<strong>Test the models on your own tasks.</strong>",
             "Beware of the <strong>honeymoon</strong> effect: new models look amazing in their first days. Wait a week and watch stability, quality and cost before changing your whole stack."],
  "stack_chip": "The stack today", "stack_h": "Who does what",
  "stack_sub": "Used through subscriptions (Claude plan + Codex plan). “Cost” here means how much of the quota each model uses up.",
  "short_stack": [("Planning and hard problems", "GPT-6 Astra"), ("General use and complex projects", "Opus 5.5"), ("Cost-effective execution", "GPT-6 Sol"), ("Repetitive tasks", "GPT-6 Luna")],
  "stack": [("1", "Planning and hard problems", "<strong>GPT-6 Astra</strong> · medium–high effort. Architecture, scenario planning, demanding cases."),
            ("2", "General use and complex projects", "<strong>Claude Opus 5.5</strong> · low effort. Fast, direct, economical, needs few instructions."),
            ("3", "Creative, design, video, browser", "<strong>Claude Opus 5.5</strong> · low–medium. Gets it right the first time where taste matters."),
            ("4", "Executing a ready plan", "<strong>GPT-6 Sol</strong> · medium–high. Good value when the task is already well defined."),
            ("5", "Reviewing and fixing code", "<strong>GPT-6 Sol</strong> · medium–high. Strong when there is a clear criterion (tests that pass or fail)."),
            ("6", "Grunt work", "<strong>GPT-6 Luna</strong> · Low for simple and fast; High / X-High for heavy work. Unambiguous tasks only."),
            ("7", "Many parallel subtasks", "<strong>Opus 5.5 orchestrates</strong>, Sol or Luna execute. Judgment once, cheap execution many times."),
            ("8", "Ambiguous case", "<strong>Astra proposes, Opus 5.5 reviews.</strong> Two cheap views beat one expensive one."),
            ("✕", "Out of the stack", "Grok 4.7 (worse than 4.6) · Fable 5.1 (expensive, surpassed by Opus 5.5) · Sonnet 5 and Haiku 4.5 (weak value).")],
  "dec_chip": "How to decide", "dec_h": "From request to model in four questions", "dec_sub": "Look at the hardest step of the task, not the task as a whole.",
  "flow": ["What is the hardest step?", "Smallest model that handles it", "Lowest effort that covers the risk", "Check the result", "Log it"],
  "rules": [("🚫 No loyalty", "Go wherever you are best served — team Claude or team Codex, it doesn't matter."),
            ("📈 Don't pay for the top", "Above “high” effort there was no real gain. Raise it only with evidence."),
            ("🍯 Honeymoon", "Every new model looks great in its first days. Wait a week before changing your stack."),
            ("🎯 Quota per result", "A model that uses more quota but nails it the first time can beat four attempts on the cheaper one."),
            ("📁 One agent, one folder", "Two agents in the same repository trip over each other. Isolate each one and tell it where it may write."),
            ("🧪 Test it yourself", "Three real tasks, two models, same prompt. Thirty minutes beat any benchmark.")],
  "pre_chip": "Requirements", "pre_h": "What you need", "pre_sub": "Nothing to install beyond the tools you already use.",
  "pre": [("Claude subscription", "Claude Code or Claude Desktop, for Opus 5.5.", '<span class="c"># check quota usage</span>\n<span class="k">/usage</span>'),
          ("Codex subscription", "Codex CLI or Codex Desktop, for GPT-6 Astra, Sol and Luna.", '<span class="k">codex</span>  <span class="c"># opens a session</span>'),
          ("The repository", "Model cards, rules and prompts in Markdown (written in Portuguese).", '<span class="k">git clone</span> <span class="s">https://github.com/inematds/modelos</span>')],
  "g_chip": "How to use · step by step", "g_h": "Day-to-day use", "g_sub": "From a quick lookup to turning the catalog into a skill.",
  "steps": [("Check the stack", "The README table is the quick reference. When in doubt, open the model's card.",
             '<span class="k">cat</span> README.md               <span class="c"># stack per task + rules</span>\n<span class="k">cat</span> modelos/opus-5-5.md     <span class="c"># card: best for, avoid for, effort</span>'),
            ("Use a ready-made pattern", "For flows with more than one model, copy the matching prompt.",
             'prompts/planejar-executar.md     <span class="c"># Astra plans → Sol executes</span>\nprompts/segunda-opiniao.md       <span class="c"># Astra proposes → Opus 5.5 reviews</span>\nprompts/orquestrador-workers.md  <span class="c"># Opus 5.5 splits work → Sol/Luna do it</span>\nprompts/tarefa-bracal.md         <span class="c"># Luna in batch, no ambiguity</span>'),
            ("Log what you observe", "One line per observation, newest on top. This is what makes the honeymoon rule practical.",
             '<span class="c"># log.md</span>\n| date | model | task | result | source |'),
            ("Run the quick test", "Three real tasks (easy, medium, hard), same prompt on the current model and the candidate. Repeat the hard one after a week.",
             'regras.md             <span class="c"># 30-minute protocol</span>\navaliacao/bateria.md  <span class="c"># 8 real cases, 0–3 score, quota used</span>'),
            ("Turn it into a skill once the stack settles", "There is a ready draft that answers “which model should I use for this?”.",
             '<span class="k">cp -r</span> skills/escolher-modelo ~/.claude/skills/')],
  "p_chip": "Usage patterns", "p_h": "Three combinations that work", "p_sub": "The expensive part (judgment) happens once; the long part (execution) runs cheap.",
  "pats": [("🗺️ Plan → execute", "Astra writes a plan with verifiable steps; Sol executes without changing it and stops if anything goes off-script."),
           ("⚖️ Second opinion", "Astra proposes; Opus 5.5 reviews as a skeptic. If they agree, go ahead. If not, the disagreement is what you decide."),
           ("🎛️ Orchestrator + workers", "Opus 5.5 splits the work and reviews it; Sol or Luna handle each part in its own folder.")],
  "r_chip": "Next steps", "r_h": "What comes next", "r_sub": "The stack is a starting point and will be revisited with real use.",
  "road": [("Now", "Catalog published", "Models explained, stack, model cards, rules, prompts and test battery."),
           ("Sep 30", "Post-honeymoon review", "Confirm or adjust the stack after a week of use."),
           ("Later", "Model-picking skill", "Install the escolher-modelo skill or fold the stack into the existing model router.")],
  "foot": "practical guide to AI models",
  "m_chip": "The models, in plain language", "m_h1": 'What <span class="amb">each model</span> is for',
  "m_lead": "Many models arrived at once and it's easy to feel overwhelmed. Here, without jargon, is what each one does well, when to use it and when to avoid it.",
  "m_back": "Back to the guide", "m_in": "In the stack", "m_outlbl": "Out of the stack",
  "m_one": "In one sentence", "m_use": "Use it for", "m_avoid": "Avoid it for", "m_eff": "Effort",
  "m_stack_h": "My stack today", "m_stack_sub": "Four roles, four models.",
  "m_over_h": "If you feel overwhelmed", "m_over_p": "You're not alone. Instead of getting lost in benchmark noise, run a quick test: three of your real tasks, two models, the same request. In half an hour you'll know more than after a day of reading comparisons.",
  "m_cta": "How to use this day to day →",
 },
 "es": {
  "title": "Qué Modelo de IA Usar — el modelo correcto para cada tarea",
  "desc": "Guía directa para elegir entre Claude Opus 5.5, GPT-6 Astra, Sol y Luna: modelos explicados de forma simple, stack por tarea, reglas, prompts y batería de pruebas.",
  "mtitle": "Los nuevos modelos de IA, explicados de forma simple",
  "mdesc": "Opus 5.5, GPT-6 Astra, Sol, Luna, Fable 5.1, Grok 4.7, Sonnet 5 y Haiku: para qué sirve cada uno, cuándo usarlo y cuándo evitarlo.",
  "nav": ["Modelos", "Stack", "Guía de uso", "Patrones", "Esfuerzo"],
  "eff_cta": ("Esfuerzo en la práctica", "Datos de Opus 5.5 y GPT-6 Astra en todos los niveles de esfuerzo, con gráficos. Opinión de Nei: medium por defecto, high cuando haga falta más razonamiento, xhigh solo en casos extremos."), "toggle": "Cambiar tema",
  "chip": "Claude · GPT-6 · Grok — septiembre de 2026",
  "h1": 'El modelo <span class="amb">correcto</span> para cada tarea',
  "lead": "Muchos modelos llegaron al mismo tiempo. La respuesta práctica es simple: usa el mejor modelo para cada tarea, sin lealtad a ninguna plataforma.",
  "cta1": "Ver los modelos", "cta2": "Guía de uso", "alt": "Banner: qué modelo de IA usar para cada tarea",
  "q_chip": "Vista rápida", "q_h": "Cada modelo en una línea",
  "q_sub": "Haz clic en un modelo para ver la explicación completa, en lenguaje simple.",
  "rule_h": "Regla principal: no confíes solo en los benchmarks",
  "rule_p": ["<strong>Prueba los modelos en tus propias tareas.</strong>",
             "Cuidado con el efecto <strong>luna de miel</strong>: los modelos nuevos parecen increíbles los primeros días. Espera una semana y observa estabilidad, calidad y costo antes de cambiar todo tu stack."],
  "stack_chip": "El stack hoy", "stack_h": "Quién hace qué",
  "stack_sub": "Uso mediante suscripciones (plan Claude + plan Codex). “Costo” aquí es cuánto de la cuota consume cada modelo.",
  "short_stack": [("Planificación y problemas difíciles", "GPT-6 Astra"), ("Uso general y proyectos complejos", "Opus 5.5"), ("Ejecución económica", "GPT-6 Sol"), ("Tareas repetitivas", "GPT-6 Luna")],
  "stack": [("1", "Planificar y problemas difíciles", "<strong>GPT-6 Astra</strong> · esfuerzo medio–alto. Arquitectura, simular escenarios, casos exigentes."),
            ("2", "Uso general y proyectos complejos", "<strong>Claude Opus 5.5</strong> · esfuerzo bajo. Rápido, directo, económico, pide pocas instrucciones."),
            ("3", "Creativo, diseño, video, navegador", "<strong>Claude Opus 5.5</strong> · bajo–medio. Acierta a la primera donde el gusto importa."),
            ("4", "Ejecutar un plan listo", "<strong>GPT-6 Sol</strong> · medio–alto. Buen costo cuando la tarea ya está bien definida."),
            ("5", "Revisar y arreglar código", "<strong>GPT-6 Sol</strong> · medio–alto. Fuerte cuando hay un criterio claro (pruebas que pasan o fallan)."),
            ("6", "Trabajo pesado", "<strong>GPT-6 Luna</strong> · Low para lo simple y rápido; High / X-High para lo pesado. Solo tareas sin ambigüedad."),
            ("7", "Muchas subtareas en paralelo", "<strong>Opus 5.5 orquesta</strong>, Sol o Luna ejecutan. Juicio una vez, ejecución barata muchas veces."),
            ("8", "Caso ambiguo", "<strong>Astra propone, Opus 5.5 revisa.</strong> Dos visiones baratas valen más que una cara."),
            ("✕", "Fuera del stack", "Grok 4.7 (peor que el 4.6) · Fable 5.1 (caro, superado por Opus 5.5) · Sonnet 5 y Haiku 4.5 (costo-beneficio débil).")],
  "dec_chip": "Cómo decidir", "dec_h": "Del pedido al modelo en cuatro preguntas", "dec_sub": "Mira el paso más difícil de la tarea, no la tarea entera.",
  "flow": ["¿Cuál es el paso más difícil?", "El modelo más pequeño que lo resuelve", "El menor esfuerzo que cubre el riesgo", "Revisa el resultado", "Anótalo en el log"],
  "rules": [("🚫 Sin lealtad", "Ve a donde mejor te atiendan — equipo Claude o equipo Codex, da igual."),
            ("📈 No pagues por el tope", "Por encima del nivel “alto” de esfuerzo no hubo ganancia real. Súbelo solo con evidencia."),
            ("🍯 Luna de miel", "Todo modelo nuevo parece genial los primeros días. Espera una semana antes de cambiar el stack."),
            ("🎯 Cuota por resultado", "El modelo que gasta más cuota pero acierta a la primera puede salir más barato que cuatro intentos con el económico."),
            ("📁 Un agente, una carpeta", "Dos agentes en el mismo repositorio se pisan. Aísla a cada uno y dile en el prompt dónde puede escribir."),
            ("🧪 Pruébalo tú mismo", "Tres tareas reales, dos modelos, el mismo prompt. Treinta minutos valen más que cualquier benchmark.")],
  "pre_chip": "Requisitos", "pre_h": "Lo que necesitas", "pre_sub": "Nada que instalar además de las herramientas que ya usas.",
  "pre": [("Suscripción Claude", "Claude Code o Claude Desktop, para Opus 5.5.", '<span class="c"># ver consumo de la cuota</span>\n<span class="k">/usage</span>'),
          ("Suscripción Codex", "Codex CLI o Codex Desktop, para GPT-6 Astra, Sol y Luna.", '<span class="k">codex</span>  <span class="c"># abre la sesión</span>'),
          ("El repositorio", "Fichas, reglas y prompts en Markdown (escritos en portugués).", '<span class="k">git clone</span> <span class="s">https://github.com/inematds/modelos</span>')],
  "g_chip": "Guía de uso · paso a paso", "g_h": "Cómo usarlo en el día a día", "g_sub": "De la consulta rápida a convertir el catálogo en una skill.",
  "steps": [("Consulta el stack", "La tabla del README es la orientación rápida. Ante la duda, abre la ficha del modelo.",
             '<span class="k">cat</span> README.md               <span class="c"># stack por tarea + reglas</span>\n<span class="k">cat</span> modelos/opus-5-5.md     <span class="c"># ficha: mejor para, evitar para, esfuerzo</span>'),
            ("Usa un patrón listo", "Para flujos con más de un modelo, copia el prompt correspondiente.",
             'prompts/planejar-executar.md     <span class="c"># Astra planifica → Sol ejecuta</span>\nprompts/segunda-opiniao.md       <span class="c"># Astra propone → Opus 5.5 revisa</span>\nprompts/orquestrador-workers.md  <span class="c"># Opus 5.5 reparte → Sol/Luna ejecutan</span>\nprompts/tarefa-bracal.md         <span class="c"># Luna en lote, sin ambigüedad</span>'),
            ("Registra lo que observes", "Una línea por observación, la más reciente arriba. Eso hace práctica la regla de la luna de miel.",
             '<span class="c"># log.md</span>\n| fecha | modelo | tarea | resultado | fuente |'),
            ("Haz la prueba rápida", "Tres tareas reales (fácil, media, difícil), el mismo prompt en el modelo actual y en el candidato. Repite la difícil después de una semana.",
             'regras.md             <span class="c"># protocolo de 30 minutos</span>\navaliacao/bateria.md  <span class="c"># 8 casos reales, nota 0–3, cuota gastada</span>'),
            ("Conviértelo en skill cuando el stack se estabilice", "Hay un borrador listo que responde “¿qué modelo uso para esto?”.",
             '<span class="k">cp -r</span> skills/escolher-modelo ~/.claude/skills/')],
  "p_chip": "Patrones de uso", "p_h": "Tres combinaciones que funcionan", "p_sub": "La parte cara (el juicio) ocurre una vez; la parte larga (la ejecución) sale barata.",
  "pats": [("🗺️ Planificar → ejecutar", "Astra escribe un plan con pasos verificables; Sol lo ejecuta sin cambiarlo y se detiene si algo se sale del guion."),
           ("⚖️ Segunda opinión", "Astra propone; Opus 5.5 revisa como escéptico. Si coinciden, adelante. Si no, la diferencia es lo que decides tú."),
           ("🎛️ Orquestador + workers", "Opus 5.5 divide el trabajo y lo revisa; Sol o Luna hacen cada parte en su propia carpeta.")],
  "r_chip": "Próximos pasos", "r_h": "Lo que viene", "r_sub": "El stack es un punto de partida y se revisará con uso real.",
  "road": [("Ahora", "Catálogo publicado", "Modelos explicados, stack, fichas, reglas, prompts y batería de casos."),
           ("30/09", "Revisión post luna de miel", "Confirmar o ajustar el stack después de una semana de uso."),
           ("Después", "Skill para elegir modelo", "Instalar la skill escolher-modelo o integrar el stack al enrutador de modelos existente.")],
  "foot": "guía práctica de modelos de IA",
  "m_chip": "Los modelos, en lenguaje simple", "m_h1": 'Para qué sirve <span class="amb">cada modelo</span>',
  "m_lead": "Llegaron muchos modelos a la vez y es fácil sentirse abrumado. Aquí está, sin jerga, lo que cada uno hace bien, cuándo usarlo y cuándo evitarlo.",
  "m_back": "Volver a la guía", "m_in": "En el stack", "m_outlbl": "Fuera del stack",
  "m_one": "En una frase", "m_use": "Úsalo para", "m_avoid": "Evítalo para", "m_eff": "Esfuerzo",
  "m_stack_h": "Mi stack hoy", "m_stack_sub": "Cuatro papeles, cuatro modelos.",
  "m_over_h": "Si te sientes abrumado", "m_over_p": "No estás solo. En lugar de perderte en el ruido de los benchmarks, haz una prueba rápida: tres de tus tareas reales, dos modelos, el mismo pedido. En media hora sabrás más que tras un día leyendo comparativas.",
  "m_cta": "Cómo usar esto en el día a día →",
 },
}

# ---------------------------------------------------------------- render
def lang_prefix(lang):
    return "" if lang == "pt" else lang + "/"

def rel(depth):                       # caminho relativo até guia/
    return "../" * depth

def page_url(lang, kind):
    return lang_prefix(lang) + ("modelos/" if kind == "modelos" else "")

def head(lang, kind, depth):
    t = T[lang]
    title, desc = (t["mtitle"], t["mdesc"]) if kind == "modelos" else (t["title"], t["desc"])
    alt = "\n".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{BASE}{page_url(l, kind)}">' for l in LANGS)
    h = HEAD.replace("{{LANG}}", HTML_LANG[lang]).replace("{{TITLE}}", title).replace("{{DESC}}", desc)
    return h.replace("</head>", alt + "\n</head>")

def nav(lang, kind, depth):
    t = T[lang]; r = rel(depth); here = r + lang_prefix(lang)
    main = here if kind == "modelos" else ""
    links = [(here + "modelos/", t["nav"][0]), (main + "#pilha", t["nav"][1]), (main + "#guia", t["nav"][2]), (main + "#padroes", t["nav"][3]), (here + "esforco/", t["nav"][4])]
    sec = "\n".join(f'    <a class="sec" href="{h}">{n}</a>' for h, n in links)
    langs = " ".join(
        f'<a class="{"on" if l == lang else ""}" href="{r}{page_url(l, kind)}" hreflang="{HTML_LANG[l]}" lang="{HTML_LANG[l]}">{l.upper()}</a>'
        for l in LANGS)
    return f'''<body>

<nav><div class="wrap">
  <a class="brand" href="{here}"><span class="emoji">🧭</span> {BRAND[lang]}</a>
  <span class="sep">|</span>
  <span class="clubpro">
    <a class="inema" href="https://inema.club" target="_blank" rel="noopener">INEMA.CLUB</a>
    <span class="sep">-</span>
    <a class="pro" href="https://inema.pro" target="_blank" rel="noopener">PRO</a>
  </span>
  <div class="links">
{sec}
    <span class="langs">{langs}</span>
    <button class="tgl" id="themeToggle" aria-label="{t["toggle"]}" title="{t["toggle"]}">🌙</button>
    <a class="btn" href="{REPO}" target="_blank" rel="noopener">GitHub</a>
  </div>
</div></nav>
'''

def footer(lang, depth):
    t = T[lang]; r = rel(depth)
    langs = " · ".join(f'<a href="{r}{lang_prefix(l)}">{ {"pt":"Português","en":"English","es":"Español"}[l] }</a>' for l in LANGS if l != lang)
    return f'''
<footer>
  <div class="wrap">
    <div class="pill">Markdown</div><div class="pill">YAML</div><div class="pill">Claude Code</div><div class="pill">Codex</div>
    <p style="margin-top:18px">{BRAND[lang]} · {t["foot"]} ·
      <a href="{REPO}">inematds/modelos</a> · {langs} ·
      <a href="https://inema.club">INEMA.CLUB</a></p>
  </div>
</footer>

'''

def rule_box(t):
    ps = "".join(f"<p>{p}</p>" for p in t["rule_p"])
    return f'<div class="rule"><h3>⚖️ {t["rule_h"]}</h3>{ps}</div>'

def short_stack(t):
    rows = "".join(f'<div>{a}</div><div class="m">{b}</div>' for a, b in t["short_stack"])
    return f'<div class="stack">{rows}</div>'

def main_page(lang):
    t = T[lang]; depth = 0 if lang == "pt" else 1; r = rel(depth)
    q = "".join(
        f'<a class="qcard" href="modelos/#{m["id"]}"><span class="n">{m["emoji"]} {m["nome"]}</span>'
        f'<span class="r{" out" if m["out"] else ""}">{m["role"][lang]}</span><p>{m["one"][lang]}</p></a>'
        for m in MODELOS)
    stack = "".join(f'<div class="card"><div class="num">{n}</div><h3>{h}</h3><p>{p}</p></div>' for n, h, p in t["stack"])
    flow = '<span class="arr">→</span>'.join(f"<span>{s}</span>" for s in t["flow"])
    rules = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["rules"])
    pre = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p><pre>{c}</pre></div>' for h, p, c in t["pre"])
    steps = "".join(f'<div class="step"><div class="b">{i}</div><div><h3>{h}</h3><p>{p}</p><pre>{c}</pre></div></div>\n'
                    for i, (h, p, c) in enumerate(t["steps"], 1))
    pats = "".join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t["pats"])
    road = "".join(f'<div class="phase"><div class="tag">{a}</div><div class="d"><strong>{b}</strong><span>{c}</span></div></div>' for a, b, c in t["road"])
    body = f'''
<header class="hero" id="top">
  <div class="glow"></div>
  <div class="wrap">
    <div>
      <span class="chip">{t["chip"]}</span>
      <h1>{t["h1"]}</h1>
      <p class="lead">{t["lead"]}</p>
      <div class="cta">
        <a class="btn" href="modelos/">{t["cta1"]}</a>
        <a class="btn ghost" href="#guia">{t["cta2"]}</a>
      </div>
    </div>
    <figure><img src="{r}assets/{BANNER[lang]}" alt="{t["alt"]}"></figure>
  </div>
</header>

<section id="visao"><div class="wrap">
  <span class="chip">{t["q_chip"]}</span>
  <h2>{t["q_h"]}</h2>
  <p class="sub">{t["q_sub"]}</p>
  <div class="grid g3">{q}</div>
  {rule_box(t)}
</div></section>

<section id="pilha"><div class="wrap">
  <span class="chip">{t["stack_chip"]}</span>
  <h2>{t["stack_h"]}</h2>
  <p class="sub">{t["stack_sub"]}</p>
  {short_stack(t)}
  <div class="grid g3" style="margin-top:22px">{stack}</div>
</div></section>

<section id="fluxo"><div class="wrap">
  <span class="chip">{t["dec_chip"]}</span>
  <h2>{t["dec_h"]}</h2>
  <p class="sub">{t["dec_sub"]}</p>
  <div class="flow">{flow}</div>
  <div class="grid g3" style="margin-top:26px">{rules}</div>
</div></section>

<section id="pre"><div class="wrap">
  <span class="chip">{t["pre_chip"]}</span>
  <h2>{t["pre_h"]}</h2>
  <p class="sub">{t["pre_sub"]}</p>
  <div class="grid g3">{pre}</div>
</div></section>

<section id="guia"><div class="wrap">
  <span class="chip">{t["g_chip"]}</span>
  <h2>{t["g_h"]}</h2>
  <p class="sub">{t["g_sub"]}</p>
{steps}</div></section>

<section id="padroes"><div class="wrap">
  <span class="chip">{t["p_chip"]}</span>
  <h2>{t["p_h"]}</h2>
  <p class="sub">{t["p_sub"]}</p>
  <div class="grid g3">{pats}</div>
  <a class="qcard" href="esforco/" style="margin-top:22px;border-color:var(--amb)"><span class="n">📊 {t["eff_cta"][0]} →</span><p style="margin-top:.4em">{t["eff_cta"][1]}</p></a>
</div></section>

<section id="roadmap"><div class="wrap">
  <span class="chip">{t["r_chip"]}</span>
  <h2>{t["r_h"]}</h2>
  <p class="sub">{t["r_sub"]}</p>
  {road}
</div></section>
'''
    return head(lang, "main", depth) + nav(lang, "main", depth) + body + footer(lang, depth) + FOOT

def models_page(lang):
    t = T[lang]; depth = 1 if lang == "pt" else 2; r = rel(depth)
    def lst(items):
        return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>" if items else ""
    cards = ""
    for m in MODELOS:
        use = f'<div class="lbl">{t["m_use"]}</div>{lst(m["use"][lang])}' if m["use"][lang] else ""
        cards += f'''
  <div class="mcard" id="{m["id"]}">
    <h3>{m["emoji"]} {m["nome"]} <span class="role{" out" if m["out"] else ""}">{t["m_outlbl"] if m["out"] else t["m_in"]} · {m["role"][lang]}</span></h3>
    <p class="one">{m["one"][lang]}</p>
    <p class="like">{m["like"][lang]}</p>
    {use}
    <div class="lbl">{t["m_avoid"]}</div>{lst(m["avoid"][lang])}
    <div class="lbl">{t["m_eff"]}: <span class="eff">{m["effort"][lang]}</span></div>
  </div>'''
    body = f'''
<header class="hero" id="top">
  <div class="glow"></div>
  <div class="wrap">
    <div>
      <span class="chip">{t["m_chip"]}</span>
      <h1>{t["m_h1"]}</h1>
      <p class="lead">{t["m_lead"]}</p>
      <div class="cta">
        <a class="btn" href="#opus">Opus 5.5</a>
        <a class="btn ghost" href="../">{t["m_back"]}</a>
      </div>
    </div>
    <figure><img src="{r}assets/{BANNER[lang]}" alt="{t["alt"]}"></figure>
  </div>
</header>

<section id="modelos"><div class="wrap">
  <div class="grid g2">{cards}
  </div>
</div></section>

<section id="pilha"><div class="wrap">
  <span class="chip">{t["stack_chip"]}</span>
  <h2>{t["m_stack_h"]}</h2>
  <p class="sub">{t["m_stack_sub"]}</p>
  {short_stack(t)}
  {rule_box(t)}
  <div class="card" style="margin-top:22px"><h3>🌊 {t["m_over_h"]}</h3><p>{t["m_over_p"]}</p></div>
  <p style="margin-top:26px"><a class="btn" href="../#guia">{t["m_cta"]}</a></p>
</div></section>
'''
    return head(lang, "modelos", depth) + nav(lang, "modelos", depth) + body + footer(lang, depth) + FOOT

if __name__ == "__main__":
    for lang in LANGS:
        base = ROOT / lang_prefix(lang)
        (base / "modelos").mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(main_page(lang))
        (base / "modelos/index.html").write_text(models_page(lang))
        print("ok", lang)
