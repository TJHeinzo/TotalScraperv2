import scrapy

# USER AGENT is defined in settings.py


class TotalScraper(scrapy.Spider):

    name = "total"
    start_urls = [
        "https://www.totalwine.com/wine/c/c0020?viewall=true&pageSize=120&aty=1,1,0,0&instock=1"
    ]
    pageNum = 1

    def parse(self, response):
        for product in response.css("article.productCard__2nWxIKmi"):
            yield {
                "name": product.xpath(".//h2/a/text()").get(),
                "size": product.xpath(".//h2/span/text()").get(),
                "price": product.xpath('.//*[@class="price__1JvDDp_x"]/text()').get(),
                # "isWD": 0 if product.xpath('.//div[@class="Popoverstyled__ToolTipHolder-shared-packages__sc-16w01om-0 aycRH"]').get() is None else 1,
                "url": "https://www.totalwine.com"
                + product.xpath(".//h2/a/@href").get(),
            }

        maxPage = int(
            response.css('a[data-at="product-search-pagination-link"]::text').getall()[
                -1
            ]
        )

        self.pageNum += 1
        if self.pageNum <= maxPage:
            yield response.follow(
                f"https://www.totalwine.com/wine/c/c0020?viewall=true&page={self.pageNum}&pageSize=120&aty=1,1,0,0&instock=1",
                callback=self.parse,
            )
