import scrapy
import csv

class IlanSpider(scrapy.Spider):
    name = 'ilan'
    start_urls = ['https://marketofrealty.com/satilik/konut/7/?d=&l=&g=&p=1']
    page_number = 1
    seen_urls = set()

    def parse(self, response):
        ilan_urls = []
        for i in range(4, 17): 
            ilan_urls.extend(response.css(f'body > div.container.ptop20 > div.row > div.col-md-9.padding > div > div:nth-child(6) > div:nth-child({i}) > div > div > div.col-md-5 > div.ilanBaslik > a::attr(href)').extract())
        
        for ilan_url in ilan_urls:
            ilan_url = response.urljoin(ilan_url)
            ilan_url = ilan_url + f"/?dil=tr"
            if ilan_url not in self.seen_urls:
                self.seen_urls.add(ilan_url)
                yield scrapy.Request(url=ilan_url, callback=self.parse_ilan)

        if self.page_number > 40:
            return

        
        self.page_number += 1
        next_page_url = f"https://marketofrealty.com/satilik/konut/7/?d=&l=&g=&p={self.page_number}"
        yield scrapy.Request(url=next_page_url, callback=self.parse)


    def parse_ilan(self, response):
        ilan_informations = {}
        #ilan no
        ilan_no = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(1) > span.tanim::text').get()
        if ilan_no:
            ilan_no = ilan_no.strip()
        ilan_informations['ilan no'] = ilan_no
      
        # price 
        price = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(4) > span.tanim::text').get()
        if price:
            price = price.strip()
        price_type = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(4) > span.tanim > i::attr(class)').get()
        if price_type:
            price_type = price_type.strip()
            if price_type == "fa fa-dollar":
                price = int(price.replace('.', '')) * 32.5
            elif price_type == "fa fa-euro":
                price = int(price.replace('.', '')) * 35
            elif price_type == "fa fa-gbp":
                price = int(price.replace('.', '')) * 40.6
            else:
                price = int(price.replace('.', ''))
        ilan_informations['Price'] = price
     
        # city
        city = response.css('body > div.container.genelcontainer > div > div.col-md-8 > header > ol > li:nth-child(5) > a > span::text').get()
        if city:
            city = city.strip()
        ilan_informations['City'] = city
        
        # town 
        town = response.css('body > div.container.genelcontainer > div > div.col-md-8 > header > ol > li:nth-child(6) > a > span::text').get()
        if town:
            town = town.strip()
        ilan_informations['Town'] = town
        
        # neighbourhood
        neighbourhood = response.css('body > div.container.genelcontainer > div > div.col-md-8 > header > ol > li:nth-child(7) > a > span::text').get()
        if neighbourhood:
            neighbourhood = neighbourhood.strip()
        ilan_informations['Neighbourhood'] = neighbourhood


        # Total square of meter
        total_meter = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(7) > span.tanim::text').get()
        if total_meter:
            total_meter = total_meter.strip()
        ilan_informations['Total Square of Meter'] = total_meter 
        
        # Number of room
        number_of_room = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(5) > span.tanim::text').get()
        if number_of_room:
            number_of_room = number_of_room.strip()
        ilan_informations['Number of room'] = number_of_room

        # Number of bathroom
        number_of_bathroom = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(18) > span.tanim::text').get()
        if number_of_bathroom:
            number_of_bathroom = number_of_bathroom.strip()
        ilan_informations['Number of bathroom'] = number_of_bathroom
        
        # Age of Structure
        age_of_structure = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(19) > span.tanim::text').get()
        if age_of_structure:
            age_of_structure = age_of_structure.strip()
        ilan_informations['Age of Structure'] = age_of_structure

        # Floor of house
        floor_of_house = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(14) > span.tanim::text').get()
        if floor_of_house:
            floor_of_house = floor_of_house.strip()
        # Number of floors
        number_of_floors = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(8) > span.tanim::text').get()
        if number_of_floors:
            number_of_floors = number_of_floors.strip()
        ilan_informations['Number of floors'] = number_of_floors

        # Heating
        heating = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(15) > span.tanim::text').get()
        if heating:
            heating = heating.strip()
        ilan_informations['Heating'] = heating
        
        # Credi Accepting
        credi_accepting = response.css('body > div.container.genelcontainer > div > div.col-sm-8.padding > div.row > div.col-md-5.padding > div.boxGenel > ul > li:nth-child(12) > span.tanim::text').get()
        if credi_accepting:
            credi_accepting = credi_accepting.strip()
        ilan_informations['Credi Accepting'] = credi_accepting
    
        # Remove the URL field from the item
        ilan_informations.pop('url', None)

        yield ilan_informations