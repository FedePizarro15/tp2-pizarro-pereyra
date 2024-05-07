letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '?', '!', '¿', '¡', '(', ')', ':', ';', '-', '“', '‘', 'á', 'é', 'í', 'ó', 'ú', 'ü', 'ñ']

secuencia = [(numero, letra) for numero, letra in enumerate(letras,1)]

msg = 'Hola, ¿cómo estás?'

msg_lower = msg.lower()

msg_list = list(msg_lower)

for i in range(len(msg) - 1):
    msg_list.insert(i * 2 + 1,-1)
    
for i,l in enumerate(msg_list):
    if l != -1:
        for n,k in secuencia:
            if l == k:
                msg_list[i] = n
                break

z = False

for i, l in enumerate(msg_list):
    if z:
        z = False
        continue
    
    if l != -1:
        if l >= 10:
            z = True
            msg_list.pop(i)
            for j, k in enumerate(str(l)):
                msg_list.insert(i+j, int(k) + 1)
        else:
            msg_list[i] = msg_list[i] + 1

msg_list.append(0)
    
print(msg_list)