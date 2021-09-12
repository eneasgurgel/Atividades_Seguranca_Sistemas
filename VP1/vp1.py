import hashlib

def  cifraDeCesar(texto, chave, cifra):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '$', '!']
    textofinal = ''
    for l in texto:
        if (l != ' ') and (l in letras):
            if cifra:
                posicao = (letras.index(l) + chave) % len(letras)
            else:
                posicao = (letras.index(l) - chave) % len(letras)
            textofinal = textofinal + letras[posicao]
        else:
            textofinal += l
    return textofinal  


def enviar(mensagem, segredo, chave):
    pacote = []
    pacote.append(mensagem)
    pacote.append(mensagem+segredo)
    h = hashlib.md5()
    h.update(pacote[1].encode('UTF-8'))
    hash = h.digest()
    pacote[1] = str(hash)
    mensagemCifrada = cifraDeCesar(pacote[0], chave, True)
    hashCifrado = cifraDeCesar(pacote[1], chave, True)
    return mensagemCifrada, hashCifrado


def receber(mensagemCifrada, segredo, chave):
    mensagem = cifraDeCesar(mensagemCifrada[0], chave, False)
    hashDecifrado = cifraDeCesar(mensagemCifrada[1], chave, False)
    h = hashlib.md5()
    h.update((mensagem + segredo).encode('UTF-8'))
    hash = h.digest()
    concatenacao = str(hash)
    if concatenacao == hashDecifrado:
        return mensagem
    else:
        return None


if __name__ == "__main__":
    #Teste 1
    print('Teste 1')
    pacote = enviar('ola mundo', 'segredo', 5)
    print(receber(pacote, 'segredo', 5))
    print()

    #Teste 2
    print('Teste 2')
    pacote = enviar('ola mundo', 'segredo', 5)
    print(receber(pacote, 'segred', 5))
    print()

    #Teste 3
    print('Teste 3')
    pacote = enviar('ola mundo', 'segredo', 5)
    print(receber(pacote, 'segredo', 7))
    print()

    #Teste 4
    print('Teste 4')
    pacote = enviar('ola mundo', 'segredo', 5)
    print(receber(pacote, 'segrido', 6))
    print()