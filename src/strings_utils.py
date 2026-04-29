def analisar_string(texto: str):
    return {
    "tamanho": len(texto),
    "primeiro": texto[0],
    "ultimo": texto[-1],
    "maiusculo": texto.upper()
    }