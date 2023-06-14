def validar(entrada,tipo_dato,pedido,rango):
    if tipo_dato=="Texto":
        if entrada.isalpha()!=True:
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"Texto",None,None))
    if tipo_dato=="TextCon":
        if entrada.isalpha()!=True or (entrada.capitalize() not in pedido):
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"TextCon",pedido,None))
    if tipo_dato=="Rango":
        ent=[]
        for x in range(rango):
            ent.append(x)
        ent.pop(0)
        if entrada.isnumeric()==False:
            entrada=input("Entrada inválida, intente de nuevo")
            return(validar(entrada,"Rango",None,rango))
        if int(entrada) not in ent:
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"Rango",None,rango))
    if tipo_dato=="C.I":
        if entrada.isnumeric()!=True or "." in entrada or "," in entrada:
            entrada=input("Entrada inválida, intente de nuevo: ")
            return(validar(entrada,"C.I",None,None))
    