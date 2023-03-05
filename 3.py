import json

#abrindo arquivo
file = open('dados.json')
data = json.load(file)

#variaveis para os valores
valor_total = 0
menor_valor = 0
menor_valor_dia = 0
maior_valor = 0
maior_valor_dia = 0
n_dias = 0

#processando os dados
for line in data:
    if line['valor'] > 0:
        n_dias += 1
        valor_atual = line['valor']
        dia_atual = line['dia']
        valor_total += valor_atual
        if dia_atual == 1:
            menor_valor = valor_atual
            menor_valor_dia = dia_atual
            maior_valor = valor_atual
            maior_valor_dia = dia_atual
        if valor_atual <= menor_valor:
            menor_valor = valor_atual
            menor_valor_dia = dia_atual
        if valor_atual >= maior_valor:
            maior_valor = valor_atual
            maior_valor_dia = dia_atual

#calculando a media
media_mensal = valor_total/n_dias
n_dias_superior = 0

#calculando o numero de dias acima da media
for line in data:
    valor_atual = line['valor']
    if valor_atual > media_mensal:
        n_dias_superior += 1

#exibindo os resultados
print('O dia com menor valor foi o dia', menor_valor_dia, 'com valor de {:.4f}'.format(menor_valor))
print('O dia com maior valor foi o dia', maior_valor_dia, 'com valor de {:.4f}'.format(maior_valor))
print('O numero de dias com faturamento acima da media foi de:', n_dias_superior)