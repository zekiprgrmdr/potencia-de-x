def PotenciaDeUnNumero(base,potencia):
    i=0
    resultado=1

    while(i!=potencia):
          resultado = resultado*base
          i+=1
    
    return resultado



print(PotenciaDeUnNumero(9,5))