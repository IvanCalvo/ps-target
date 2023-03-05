#Dados
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

#Valor total
total = sp+rj+mg+es+outros

#calculando as porcentagens
sp_por = (sp/total)*100
rj_por = (rj/total)*100
mg_por = (mg/total)*100
es_por = (es/total)*100
outros_por = (outros/total)*100

#imprimindo os valores de porcentagem
print('Porcentagem de SP: {:.2f}'.format(sp_por),'%')
print('Porcentagem de RJ: {:.2f}'.format(rj_por),'%')
print('Porcentagem de MG: {:.2f}'.format(mg_por),'%')
print('Porcentagem de ES: {:.2f}'.format(es_por),'%')
print('Porcentagem de Outros: {:.2f}'.format(outros_por),'%')