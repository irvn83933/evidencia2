#programa para calcular el salario neto
salario_bruto = float(input("Ingrese el salario bruto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (en %): "))
deduccion = salario_bruto * (porcentaje_descuento / 100)
salario_neto = salario_bruto - deduccion
print("El salario neto es:", salario_neto)