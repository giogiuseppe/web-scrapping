from bs4 import BeautifulSoup
import requests
from lxml import html

requisiçao = requests.get('https://www.deere.com.br/pt/tratores/série-5e-pequenos/')

tree = html.fromstring(requisiçao.content)

contador = 1
linha = 1

print()
print('Tratores Pequenos   Série 5E - John Deere  -  Digite 1')
print('Caso queira cancelar digite qualquer coisa')
print()
opcao = str(input('Iniciar Pesquisa: '))
if opcao == '1':
    print()
    while linha < 8:
        
        modelo = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/th/div/p/a/text()' %contador)
        potencia_nonimal = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/td[1]/div/p/text()' %contador)
        nº_de_cilindros = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/td[2]/div/p/text()' %contador)
        emissao_mar_1 = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/td[3]/div/p/text()' %contador)
        torque_maximo = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/td[4]/div/p/text()' %contador)
        transmissao = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/td[5]/div/p/text()' %contador)
        nº_de_vcrs = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/td[6]/div/p/text()' %contador)
        reserva_de_torque = tree.xpath('//*[@id="MainContentSection"]/div[17]/div/table/tbody/tr[%d]/td[7]/div/p/text()' %contador)

        print("MODELO               |     ",modelo[0])           
        print("POTÊNCIA NONIMAL     |     ",potencia_nonimal[0]) 
        print("Nº DE CILINDROS      |     ",nº_de_cilindros[0])  
        print("EMISSÃO MAR-1        |     ",emissao_mar_1[0])    
        print("TORQUE MÁXIMO        |     ",torque_maximo[0])    
        print("TRANSMISSÃO          |     ",transmissao[0])      
        print("Nº DE VCRS           |     ",nº_de_vcrs[0])       
        print("RESERVA DE TORQUE    |     ",reserva_de_torque[0])
        print('---------------------------------------------')

        linha = linha + 1
        contador = contador +1

else:
    print()
    print('Pesquisa Cancelada!')