import os
import shutil
import scrapy
import pandas as pd
from scrapy.crawler import CrawlerProcess

# Define the spider class
os.chdir('Web_Crawler')
class ArticleSpider(scrapy.Spider):
    name = 'article_extract'

    def start_requests(self):
        for index, row in self.urls.iterrows():
            url = row["URL"]
            url_id = str(row["URL_ID"])
            yield scrapy.Request(url=url, callback=self.parse, meta={'url_id': url_id})

    def parse(self, response):
        title = response.xpath('//h1[@class="entry-title"]/text()').get() or response.xpath('//h1[@class="tdb-title-text"]/text()').get()
        article_text = response.xpath('//div[@class="td-post-content tagdiv-type"]//*[self::p or self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::h7 or self::span]/text()').getall()  or response.xpath('//div[@class="tdb-block-inner td-fix-index"]//*[self::p or self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::h7 or self::span]/text()').getall()
        content = f"{title}\n\n{' '.join(article_text)}"
        ids = response.meta['url_id']
        file_path = os.path.join(self.directory, ids + ".txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

# Define the main function
def main():
    # Read the URLs from an Excel file
    urls = pd.read_excel("..\Data Preprocessing\Input Data\Input.xlsx")

    # Create the output directory
    directory = os.path.join("..", "Data Preprocessing", "Output Data", "Extracted articles")
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.mkdir(directory)

    # Set up the Scrapy process
    process = CrawlerProcess()
    process.crawl(ArticleSpider, urls=urls, directory=directory)
    process.start()

main()