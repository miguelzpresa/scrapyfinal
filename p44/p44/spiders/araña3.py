import scrapy
import json
import time
import csv
from p44.items import P44Item
from urllib.parse import urljoin
import random 


class Spiderr(scrapy.Spider):
    name = 'araña3'
    start_urls = ['https://www.cia.gov/the-world-factbook/page-data/sq/d/4232547903.json']
    download_delay = 1.0 + random.random() * 3.0

    def __init__(self):
        super(Spiderr,self).__init__()
        self.lista_urls= list()
        self.names = list()
        self.csvfile = open("../data.csv","a",newline="")
        self.writer = csv.DictWriter(self.csvfile, fieldnames=[
        "area","pobla","gdp_percapita","unemploymentrate","Taxes_a_other_v","debt_ext","exchange","internet_Total","internet_percent__popu","airports","roadways_total","mili_expenditures",])
        if self.csvfile.tell() == 0:
            self.writer.writeheader()


    def closed(self, reason):
        self.csvfile.close()
    def parse(self,response):
        #names = list() 
        
        first_slice_url = "https://www.cia.gov/the-world-factbook/"
        uri_values =list()
        data = json.loads(response.body)
        for country in data['data']['allWordpressWpCountry']['nodes']:
            uri_values.append(country['uri'])
            new_url= urljoin(first_slice_url, country["uri"])
            self.lista_urls.append(new_url )
            print(new_url)
            self.names.append(country["title"])

        item = P44Item()
        item['urls_'] = self.lista_urls
        
        for country in self.lista_urls[:3]:
            yield scrapy.Request(country ,callback=self.segunda_fase)
            time.sleep(random.uniform(1, 5))
    

    def segunda_fase(self,response):
        area = response.xpath('''//*[@id="geography"]/div[4]/p/text()[1]''')  
        pobla =  response.xpath('''//*[@id="people-and-society"]/div[1]/p''')
        gdp_percapita = response.xpath('''/html/body/div/div[1]/div[2]/main/div[2]/section/div/div/div[2]/div[6]/div[4]/p/text()[1]''')
        unemploymentrate = response.xpath('''//html/body/div/div[1]/div[2]/main/div[2]/section/div/div/div[2]/div[6]/div[14]/p/text()[1]''')
        Taxes_a_other_v= response.xpath('''//*[@id="economy"]/div[22]/p''')
        debt_ext = response.xpath('''//*[@id="economy"]/div[32]/p''')
        exchange = response.xpath('''//*[@id="economy"]/div[33]/p/text()[2]''')
        internet_Total = response.xpath('''//*[@id="communications"]/div[6]/p/text()[1]''')
        internet_percent__popu= response.xpath('''//*[@id="communications"]/div[6]/p/text()[2]''')
        airports = response.xpath('''//*[@id="transportation"]/div[3]/p''')
        roadways_total = response.xpath('''//*[@id="transportation"]/div[8]/p/text()[1]''')
        mili_expenditures = response.xpath('''//*[@id="military-and-security"]/div[2]/p/text()[1]''')
        data = { "area":area,"pobla":pobla,"gdp_percapita":gdp_percapita,"unemploymentrate":unemploymentrate,"Taxes_a_other_v":Taxes_a_other_v,"debt_ext":debt_ext,"exchange":exchange,"internet_Total":internet_Total,"internet_percent__popu":internet_percent__popu,"airports":airports,"roadways_total":roadways_total,"mili_expenditures":mili_expenditures}

        self.writer.writerow(data)


        

