from scrapy import Request,Spider
from lxml import etree
from comment.items import CommentItem


class CommentSpider(Spider):
    '''
    这个是三生三世十里桃花
    '''
    name = 'comment'

    def start_requests(self):
        templateurl = 'https://movie.douban.com/subject/25823277/comments?start={}&limit=20&sort=new_score&status=P'
        for i in range(3201):
            url = templateurl.format(str(i * 20))
            yield Request(url=url, callback=self.parse, meta={'dont_merge_cookies': True})

    def parse(self, response):
        selector = etree.HTML(response.text)
        item = SanshengItem()
        item['comments'] = selector.xpath('//div[@class="comment"]/p/text()')
        yield item


# class CommentSpider(Spider):
#     '''
#     这个是二十二
#     '''
#     name = 'comment'
#
#     def start_requests(self):
#         templateurl = 'https://movie.douban.com/subject/26430107/comments?start={}&limit=20&sort=new_score&status=P'
#         for i in range(1601):
#             url = templateurl.format(str(i * 20))
#             yield Request(url=url, callback=self.parse, meta={'dont_merge_cookies': True})
#
#     def parse(self, response):
#         selector = etree.HTML(response.text)
#         item = SanshengItem()
#         item['comments'] = selector.xpath('//div[@class="comment"]/p/text()')
#         yield item
#
# class CommentSpider(Spider):
#     '''
#     这个是战狼
#     '''
#     name = 'comment'
#
#     def start_requests(self):
#         templateurl = 'https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P'
#         for i in range(9001):
#             url = templateurl.format(str(i * 20))
#             yield Request(url=url, callback=self.parse, meta={'dont_merge_cookies': True})
#
#     def parse(self, response):
#         selector = etree.HTML(response.text)
#         item = SanshengItem()
#         item['comments'] = selector.xpath('//div[@class="comment"]/p/text()')
#         yield item