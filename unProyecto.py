def PotenciaDeUnNumero(base):
    i=0
    resultado=1
    potencia = int(input("Ingresar la potencia de la base -->2"))

    while(i!=potencia):
          resultado = resultado*base
          i+=1
    
    return resultado



print(PotenciaDeUnNumero(9))