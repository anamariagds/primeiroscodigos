ht= int(input("Horas normal trabalhada: "))
hmin = int(input("min normal trabalhados: "))

mth = hmin/60

salario_normal = (ht*10)+(mth*10)
print("Normal sem hora extra: ", round(salario_normal,2), "reais")

hx = int(input("Horas extra: "))
minx = int(input("minutos extra: "))

mnt = minx/60

dnh_extra = (hx*15) + (mnt*15)
print("Dinheiro das horas extra: ", dnh_extra, "reais")

slr_bruto = salario_normal + dnh_extra 

print("Salario bruto: ",round( slr_bruto,2), "reais")

sal_liq = slr_bruto*0.90

print("Salario liquido: ", round(sal_liq,2), "reais")
