# cargo = input("Digite o seu cargo").strip().lower()
# salario_base_caixa=1500
# salario_base_vendedor = 2400
# salario_base_gerente = 4000

# inss_desc_caixa = (salario_base_caixa*12)/100
# inss_desc_vendedor = (salario_base_vendedor*12)/100
# inss_desc_gerente = (salario_base_gerente*12)/100

# desc_irrf_caixa = (salario_base_caixa*8)/100
# desc_irrf_vendedor = (salario_base_vendedor*14)/100
# desc_irrf_gerente = (salario_base_gerente*14)/100

# if (cargo == 'caixa'):
#     sal_final = salario_base_caixa-inss_desc_caixa-desc_irrf_caixa
#     print(f'O valor bruto de {salario_base_caixa} Inss descontara {inss_desc_caixa} e o IRRF descontara {desc_irrf_caixa} e o seu salario final sera {sal_final}')
# elif (cargo == 'vendedor'):
#     sal_final = salario_base_vendedor-inss_desc_vendedor-desc_irrf_vendedor
#     print(f'O valor bruto de {salario_base_vendedor} Inss descontara {inss_desc_vendedor} e o IRRF descontara {desc_irrf_vendedor} e o seu salario final sera {sal_final}')
# elif (cargo =='gerente'):
#     sal_final = salario_base_gerente-inss_desc_gerente-desc_irrf_gerente
#     print(f'O valor bruto do seu cargo é {salario_base_gerente}, o inss descontara {inss_desc_gerente} e o IRRF descontara {desc_irrf_gerente}. O seu salario final sera {sal_final}')
# else:
#     print("Cargo inexistente, tente outra vez.")




cargo=input("Digite um cargo").strip().lower()
if(cargo=="caixa"):
   sal=1500
elif (cargo=="vendedor"):
   sal=2400
elif (cargo=="gerente"):
   sal= 4000
else:
   sal=0
   print("Cargo inexistente")
inss = sal*0.12
if (sal >2000):
   irrf=sal*0.14
else:
   irrf=sal*0.08
salfinal = sal -inss - irrf
print(f"Seu salario final sera de {salfinal}.")