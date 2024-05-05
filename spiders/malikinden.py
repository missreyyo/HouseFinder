import scrapy
import csv

class IlanSpider(scrapy.Spider):
    name = 'ilan'
    start_urls = ['https://malikinden.com/satilik']
    page_number = 1
    seen_urls = set()

    def parse(self, response):
        ilan_urls = response.css('tr.searchResultsItem a::attr(href)').extract()

        for ilan_url in ilan_urls:
            if ilan_url not in self.seen_urls:
                self.seen_urls.add(ilan_url)
                yield scrapy.Request(url=response.urljoin(ilan_url), callback=self.parse_ilan)
        
        if self.page_number > 30:
            return

        self.page_number += 1
        next_page_url = f"https://malikinden.com/index.php?page={self.page_number}&ipp=24&cat1=1&cat2=2&cat3=31&cat4=&cat5=&do=rem_list&seo_cat=satilik"
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_ilan(self, response):
        ilan_informations = {}
        #ilan no
        ilan_no = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(1) > div:nth-child(2) > font::text').get()
        if ilan_no:
            ilan_no = ilan_no.strip()
        ilan_informations['ilan no'] = ilan_no
      
        # price 
        price = response.css('#fiyat::text').get()
        if price:
            price = price.strip()
        ilan_informations['Price'] = price
     
        # city
        city = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > h2 > a:nth-child(3)::text').get()
        if city:
            city = city.strip()
        ilan_informations['City'] = city
        
        # town 
        town = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > h2 > a:nth-child(5)::text').get()
        if town:
            town = town.strip()
        ilan_informations['Town'] = town
        
        # date
        date = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(2) > div:nth-child(2)::text').get()
        if date:
            date = date.strip()
        ilan_informations['Date'] = date
        # neighbourhood
        neighbourhood = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > h2 > a:nth-child(7)::text').get()
        if neighbourhood:
            neighbourhood = neighbourhood.strip()
        ilan_informations['Neighbourhood'] = neighbourhood

        # tapu status
        tapu_status = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(4) > div.value::text').get()
        if tapu_status:
            tapu_status = tapu_status.strip()
        ilan_informations['Tapu Status'] = tapu_status
        
        # structure status
        structure_status = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(5) > div.value::text').get()
        if structure_status:
            structure_status = structure_status.strip()
        ilan_informations['Structure Status'] = structure_status

        # Total square of meter
        total_meter = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(6) > div.value::text').get()
        if total_meter:
            total_meter = total_meter.strip()
        ilan_informations['Total Square of Meter'] = total_meter 
        
        # Number of room
        number_of_room = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(7) > div.value::text').get()
        if number_of_room:
            number_of_room = number_of_room.strip()
        ilan_informations['Number of room'] = number_of_room

        # Number of bathroom
        number_of_bathroom = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(8) > div.value::text').get()
        if number_of_bathroom:
            number_of_bathroom = number_of_bathroom.strip()
        ilan_informations['Number of bathroom'] = number_of_bathroom
        
        # Age of Structure
        age_of_structure = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(9) > div.value::text').get()
        if age_of_structure:
            age_of_structure = age_of_structure.strip()
        ilan_informations['Age of Structure'] = age_of_structure

        # Floor of house
        floor_of_house = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(11) > div.value::text').get()
        if floor_of_house:
            floor_of_house = floor_of_house.strip()
        # Number of floors
        number_of_floors = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(3) > div.value::text').get()
        if number_of_floors:
            number_of_floors = number_of_floors.strip()
        ilan_informations['Number of floors'] = number_of_floors

        # Heating
        heating = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(12) > div.value::text').get()
        if heating:
            heating = heating.strip()
        ilan_informations['Heating'] = heating
        
        # Credi Accepting
        credi_accepting = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(13) > div.value::text').get()
        if credi_accepting:
            credi_accepting = credi_accepting.strip()
        ilan_informations['Credi Accepting'] = credi_accepting
    
        # Seller 
        seller = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(14) > div.value::text').get()
        if seller:
            seller = seller.strip()
        ilan_informations['Seller'] = seller

        # Swap
        swap = response.css('body > div:nth-child(10) > div:nth-child(2) > div > div > div.details.col-md-6 > div > div:nth-child(1) > div > ul > li:nth-child(15) > div.value::text').get()
        if swap:
            swap = swap.strip()
        ilan_informations['Swap'] = swap

        
        yield ilan_informations

class CSVWriterPipeline:
    def open_spider(self, spider):
        self.csv_file = open('ilanlar.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=['Fiyat', 'Binadaki Kat Sayisi'])
        self.csv_writer.writeheader()

    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        self.csv_writer.writerow(item)
        return item