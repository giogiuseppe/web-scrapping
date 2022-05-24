from bs4 import BeautifulSoup
import requests
from lxml import html

requisiçao = requests.get('https://www.deere.com.br/pt/tratores/médio-cabinado-4x4/')

tree = html.fromstring(requisiçao.content)

print()
print('Tratores Médios Série 6M - John Deere - Digite 1')
print('Caso queira cancelar digite qualquer coisa')
print()
opcao = str(input('Iniciar Pesquisa: '))

contador = 1
linha = 1

if opcao == '1':
    print()

    while linha < 9:

        modelo = tree.xpath('//*[@id="MainContentSection"]/div[20]/div/table/tbody/tr[%d]/th/div/p/a/text()' %contador)
        potencia_nonimal = tree.xpath('//*[@id="MainContentSection"]/div[20]/div/table/tbody/tr[%d]/td[1]/div/p/text()' %contador)
        reserva_de_torque = tree.xpath('//*[@id="MainContentSection"]/div[20]/div/table/tbody/tr[%d]/td[2]/div/p/text()' %contador)
        eixo_dianteiro = tree.xpath('//*[@id="MainContentSection"]/div[20]/div/table/tbody/tr[%d]/td[3]/div/p/text()' %contador)
        transmissao = tree.xpath('//*[@id="MainContentSection"]/div[20]/div/table/tbody/tr[%d]/td[4]/div/p/text()' %contador)
        vazao_hidraulica = tree.xpath('//*[@id="MainContentSection"]/div[20]/div/table/tbody/tr[%d]/td[5]/div/p/text()' %contador)
        lastro_maximo = tree.xpath('//*[@id="MainContentSection"]/div[20]/div/table/tbody/tr[%d]/td[6]/div/p/text()' %contador)

        print("MODELO               |     ",modelo[0])           
        print("POTÊNCIA NONIMAL     |     ",potencia_nonimal[0]) 
        print("RERSERVA DE TORQUE   |     ",reserva_de_torque[0])  
        print("EIXO DIANTEIRO       |     ",eixo_dianteiro[0])    
        print("TRANSMISSÃO          |     ",transmissao[0])    
        print("VAZÃO HIDRÁULICA     |     ",vazao_hidraulica[0])      
        print("LASTRO MÁXIMO        |     ",lastro_maximo[0])       
        print('---------------------------------------------')

        linha = linha + 1
        contador = contador +1

else:
    print()
    print('Pesquisa Cancelada!')