peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = (peso)/(altura**2)


if imc <17: 
    print( "Muito abaixo do peso, ", round (imc,2) )
elif imc >= 17 and imc <18.5:
    print("Abaixo do peso normal, " , round (imc,2))
elif imc >= 18.5 and imc < 25.0:
    print("Peso dentro do normal, ", round (imc,2))
elif imc >= 25 and imc < 30:
    print("Acima do peso normal, ", round (imc,2))
else:
    print("Muito acima do peso, ", round (imc,2))