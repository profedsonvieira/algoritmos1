<!-- Para criar vários arquivos de uma vez
No Windows (CMD):

type nul > part1.py
type nul > part2.py
type nul > part3.py
type nul > part4.py
type nul > part5.py
type nul > extra.py

No PowerShell:

New-Item part1.py
New-Item part2.py
New-Item part3.py
New-Item part4.py
New-Item part5.py
New-Item extra.py

ou de forma compacta:

1..5 | ForEach-Object { New-Item "part$_.py" }
New-Item extra.py

No Linux / Mac:

touch part1.py part2.py part3.py part4.py part5.py extra.py -->

# 📚 Estruturas de Dados e Algoritmos em Python

Projeto desenvolvido para estudos e práticas da disciplina de **Estruturas de Dados e Algoritmos**, utilizando a linguagem Python.

---

# 🚀 Conteúdo do Projeto

Este repositório contém exemplos e atividades práticas relacionadas a:

- Matrizes
- Listas
- Strings
- Tuplas
- Ordenação
- Busca Sequencial
- Busca Binária
- Cópias Rasas e Profundas
- Modularização em Python

---

# 📂 Estrutura do Projeto

```text
algoritmos/
│
├── src/
│   ├── atividades/
│   │   ├── part1.py
│   │   ├── part2.py
│   │   ├── part3.py
│   │   ├── part4.py
│   │   ├── part5.py
│   │   └── extra.py
│   │
│   ├── exercicios/
│   │   ├── ex1.py
│   │   ├── ex2.py
│   │   ├── ex3.py
│   │   ├── ex4.py
│   │   ├── ex5.py
│   │   ├── ex6.py
│   │   ├── ex7.py
│   │   ├── ex8.py
│   │   ├── ex9.py
│   │   └── ex10.py
│   │
│   ├── utils/
│   │   ├── listas_utils.py
│   │   ├── range_utils.py
│   │   ├── strings_utils.py
│   │   └── tuplas_utils.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── tests/
├── venv/
├── README.md
└── .gitignore