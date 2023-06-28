# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class P44Item(scrapy.Item):
    area = scrapy.Field()
    pobla = scrapy.Field()
    gdp_percapita = scrapy.Field()
    unemploymentrate = scrapy.Field()
    Taxes_a_other_v = scrapy.Field()
    debt_ext = scrapy.Field()
    exchange = scrapy.Field()
    internet_Total = scrapy.Field()
    internet_percent__popu = scrapy.Field()
    airports = scrapy.Field()
    roadways_total = scrapy.Field()
    mili_expenditures = scrapy.Field()
    urls_ = scrapy.Field()

        
#if __name__==__main__():
 #   main()
