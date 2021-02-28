import scrapy
from ..items import TorentNeighborhoodItem
class Toronto(scrapy.Spider):
    name='neighbors'
    start_urls=[
        'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M',
    ]
    def _parse(self, response):
        data=TorentNeighborhoodItem()
        table=response.xpath("//table[@class='wikitable sortable']").css('tr')
        for row in table:
            neighborhood=row.css('td~ td+ td ::text').extract()
            borough=row.css('td:nth-child(2) ::text').extract()
            postal_code=row.css('td:nth-child(1) ::text').extract()
            data['postal_code']=postal_code
            data['borough']=borough
            data['neighborhood']=neighborhood
            yield data