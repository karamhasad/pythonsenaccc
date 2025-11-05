#codigo para verificar se participante sera alistado ou nao

ano_ns_cand= int(input("Qual o ano do seu nascimento?"))
genero_cand= input("Qual o seu genero?").strip().upper()
from datetime import date
ano_atual= date.today().year
idade_cand= ano_atual-ano_ns_cand
if (idade_cand >= 18 and genero_cand == "MASCULINO"):
    print("Voce sera alistado no exercito")
else:
    print("Voce nao atende o perfil do exercito")
