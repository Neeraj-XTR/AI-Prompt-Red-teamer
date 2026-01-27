AI-Prompt-Red-teamer  
This repo majorly focuses on the generation of Adversial prompt injection / jailbreak prompts.  
It is a Python-based system design + reference implementation that can automatically generate diverse, category-specific jailbreak / prompt-injection prompts for red-teaming, detector training, and eval corpora expansion  
```
REPO Structure
adversarial_prompt_generator/
│
├── main.py 
├── generator/
│   ├── __init__.py
│   ├── categories.py
│   ├── strategies.py
│   ├── templates.py
│   ├── prompt_generator.py
│   ├── diversity_filter.py
│
├── outputs/
│   └── .gitkeep
│
├── requirements.txt
└── README.md

Script Ideology
┌────────────────────────┐
│  Attack Category Spec  │  ← structured taxonomy
└──────────┬─────────────┘
           ↓
┌────────────────────────┐
│  Attack Strategy Bank  │  ← tactics, primitives, patterns
└──────────┬─────────────┘
           ↓
┌────────────────────────┐
│  Prompt Template Engine│  ← parametric adversarial templates
└──────────┬─────────────┘
           ↓
┌────────────────────────┐
│  Variation & Mutation  │  ← paraphrase, obfuscation, role-play
└──────────┬─────────────┘
           ↓
┌────────────────────────┐
│  Diversity Scoring     │  ← semantic + lexical diversity
└──────────┬─────────────┘
           ↓
┌────────────────────────┐
│  Output Generator      │  ← JSON / CSV / corpus
└────────────────────────┘
