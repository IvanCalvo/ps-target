string = list(input(''))
size = len(string)

#criando uma lista vazia
string_reversed = list()

for i in range(size, 0, -1):
    #adicionando os valores na posicao invertida
    string_reversed.append(string[i-1])

#transformando a lista em string
string_reversed = ''.join(string_reversed)
print(string_reversed)
