def procedimentomenu():
    print("------------------------------------------")
    print("SEJA BEM VINDO A SUA CALCULADORA DE NOTAS")
    print("------------------------------------------")



def calcularmedia(lista1, lista2):
    medias = []
    for i in range(len(lista1)):
        media = (lista1[i] + lista2[i]) / 2
        medias.append(media)
    return medias
