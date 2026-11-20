tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

for linha in tabuleiro:
  print(linha)
  print(" 10 ".join(linha))

def table(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print( "_" * 9)

#table(tabuleiro)