senha_correta= 'python123'
tentativas = 0
max_tentativas= 3

while tentativas < max_tentativas:
    tentativa=input(f"Digite a senha(tentativa {tentativas+1}/{max_tentativas}):")
    #print(tentativa)
    if tentativa == senha_correta:
        print("Acesso concedido! Bem vindo")
        break
    else:
        print("Senha incorreta")
        tentativas+=1
else:
    print("Voce excedeu o número de tentativas. Acesso bloqueado")
