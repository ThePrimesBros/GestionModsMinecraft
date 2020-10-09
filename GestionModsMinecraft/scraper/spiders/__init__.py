# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scraper.items import TheodoTeamItem

class TheodoSpider(scrapy.Spider):
      name = "theodo"
      start_urls = ["https://www.theodo.co.uk/team"]

      # this is what start_urls does
      # def start_requests(self):
      #     urls = ['https://www.theodo.co.uk/team',]
      #     for url in urls:
      #       yield scrapy.Request(url=url, callback=self.parse)

      def parse(self, response):
          data = response.css("div.st-about-employee-pop-up")

          for line in data:
              item = TheodoTeamItem()
              item["name"] = line.css("div.h3 h3::text").extract_first()
              item["image"] = line.css("img.img-team-popup::attr(src)").extract_first()
              item["fun_fact"] = line.css("div.p-small p::text").extract().pop()
              yield item