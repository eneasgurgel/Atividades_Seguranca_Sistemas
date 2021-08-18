
def  cifraDeCesar(texto, chave, cifra):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    textofinal = ''
    for l in texto:
        if l != ' ':
            if cifra:
                posicao = (letras.index(l) + chave) % len(letras)
            else:
                posicao = (letras.index(l) - chave) % len(letras)
            textofinal = textofinal + letras[posicao]
        else:
            textofinal += l
    return textofinal  

def algForcaBruta(texto):
     letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     textofinal = ''
     for i in range(0, len(letras)):
        for l in texto: 
            if l != ' ':
                posicao = (letras.index(l) - i) % len(letras)
                textofinal = textofinal + letras[posicao]
            else:
                textofinal += l
        print(f'Chave: {i} - Texto: {textofinal}')
        textofinal = ''
        

# Decodificando:
print('Mensagem codificada: ' + cifraDeCesar('quero uma pizza de calabresa', 13, True) + '\n')

# Codificando:
print('Mensagem decodificada: ' + cifraDeCesar('dhreb hzn cvmmn qr pnynoerfn', 13, False) + '\n')

# Força Bruta:
algForcaBruta('dhreb hzn cvmmn qr pnynoerfn')
