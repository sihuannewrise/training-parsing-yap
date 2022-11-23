import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        all_authors = response.css('a[href^="/author/"]')
        for author_link in all_authors:
            yield response.follow(author_link, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        author = response.css('div.author-details')
        yield {
            'name': author.css('h3.author-title::text').get().strip(),
            'born_date': author.css('span.author-born-date::text').get(),
            'born_location': author.css('span.author-born-location::text').get(),
        }
