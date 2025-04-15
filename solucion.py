dia=int(input("Ingrese min día: "))
noche=int(input("Ingrese min noche: "))
# minutos llamadas día
if dia >100:
    pago_dia=100*10
    dia=dia-100
    pago_dia+= dia*15 # pago_dia=pago_dia+dia*15 
    print(f"DIA: excede en {dia} minutos")
else:
    pago_dia=dia*10

# minutos llamadas noche
if noche >80:
    pago_noche=80*7
    noche=noche-80
    pago_noche=pago_noche+noche*13
    print(f"NOCHE: excede en {noche} minutos")
else:
    pago_noche=noche*7
print(f"Cliente paga {pago_dia+pago_noche}")
    