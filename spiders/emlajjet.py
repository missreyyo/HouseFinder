import scrapy


class IlanSpider(scrapy.Spider):
    name = 'ilan'
    city_name = 'istanbul'
    start_urls = ['https://www.emlakjet.com/satilik-daire/{city_name}/']
    page_number = 1
    seen_urls = set()

    def parse(self, response):
        ilan_urls = []
    

        for i in range(1,40):
            ilan_urls.extend(response.css(f'#listing-search-wrapper > div:nth-child({i}) > a::attr(href)').extract())
        
        for ilan_url in ilan_urls:
            if ilan_url not in self.seen_urls:
                self.seen_urls.add(ilan_url)
                yield scrapy.Request(url=response.urljoin(ilan_url), callback=self.parse_ilan)
        
        if self.page_number > 70:
            return

        self.page_number += 1
        next_page_url = f"https://www.emlakjet.com/satilik-daire/{self.city_name}/{self.page_number}/"
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_ilan(self, response):
        ilan_informations = {}
        #ilan no
        ilan_no = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)::text').get()
        if ilan_no:
            ilan_no = ilan_no.strip()
        ilan_informations['ilan no'] = ilan_no
        #price
        price = response.css('div._2TxNQv::text').get()
        if price:
            price = price.strip()
            ilan_informations['Price'] = price

        # city
        city = response.css('#__next > div._3TdBJx > div._3lQUdB > div.ej63.ej87 > div.ej64.ej100.ej156 > div._2lYhtg > div > ul > li:nth-child(3) > a::text').get()
        if city:
            city = city.strip()
        ilan_informations['City'] = city
        
        # town 
        town = response.css('#__next > div._3TdBJx > div._3lQUdB > div.ej63.ej87 > div.ej64.ej100.ej156 > div._2lYhtg > div > ul > li:nth-child(4) > a::text').get()
        if town:
            town = town.strip()
        ilan_informations['Town'] = town
        
      
        # neighbourhood
        neighbourhood = response.css('#__next > div._3TdBJx > div._3lQUdB > div.ej63.ej87 > div.ej64.ej100.ej156 > div._2lYhtg > div > ul > li:nth-child(5) > a::text').get()
        if neighbourhood:
            neighbourhood = neighbourhood.strip()
        ilan_informations['Neighbourhood'] = neighbourhood

       
        


        # Total square of meter
        total_meter = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw > div:nth-child(2) > div:nth-child(4) > div:nth-child(2)::text').get()
        if total_meter:
            total_meter = total_meter.strip()
        ilan_informations['Total Square of Meter'] = total_meter 
        
        # Number of room
        number_of_room = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw > div:nth-child(1) > div:nth-child(5) > div:nth-child(2)::text').get()
        if number_of_room:
            number_of_room = number_of_room.strip()
        ilan_informations['Number of room'] = number_of_room

      
        
        # Age of Structure
        age_of_structure = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw > div:nth-child(2) > div:nth-child(5) > div:nth-child(2)::text').get()
        if age_of_structure:
            age_of_structure = age_of_structure.strip()
        ilan_informations['Age of Structure'] = age_of_structure

        # Floor of house
        floor_of_house = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw > div:nth-child(2) > div:nth-child(6) > div:nth-child(2)::text').get()
        if floor_of_house:
            floor_of_house = floor_of_house.strip()
        ilan_informations['Floor of house'] = floor_of_house
        # Number of floors
        number_of_floors = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw > div:nth-child(1) > div:nth-child(6) > div:nth-child(2)::text').get()
        if number_of_floors:
            number_of_floors = number_of_floors.strip()
        ilan_informations['Number of floors'] = number_of_floors



        # Heating
        heating = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw > div:nth-child(1) > div:nth-child(7) > div:nth-child(2)::text').get()
        if heating:
            heating = heating.strip()
        ilan_informations['Heating'] = heating
        
        # Credi Accepting
        credi_accepting = response.css('#bilgiler > div > div._2VNNor._2eyo_P > div > div._3tH_Nw> div:nth-child(1) > div:nth-child(8) > div:nth-child(2)::text').get()
        if credi_accepting:
            credi_accepting = credi_accepting.strip()
        ilan_informations['Credi Accepting'] = credi_accepting
        yield ilan_informations


