import scrapy


class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["bbs.hupu.com"]
    start_urls = ["https://bbs.hupu.com/"]

    def __init__(self):
        self.cnt = 0
        self.part = 'topic-daily' # 对应各个主题
        self.page_range = 3 # 最大20页
        self.keyword = '%E5%A5%B3%E6%80%A7' # 对应`女性`


    def parse(self, response):
        # filename ="page{}.html".format(self.cnt)
        # print('name is ',filename)
        # self.cnt = self.cnt + 1
        # with open(filename, 'wb') as f:
        # #     f.write(response.body)


        title_short_list = list() #精简后的标题
        url_list = list()
        content_list = list()
        post_time_list = list()

        div_head = response.xpath('//div[@class="bbs-search-web-content"]')
        print('title and url')
        for div in div_head:
            title_short_comp = div.xpath('./div[@class="content-outline"]/div/a[contains(@class, "content-wrap-span")]//text()').getall()
            title_short = "".join(title_short_comp)
            url = div.xpath('./div[@class="content-outline"]/div/a').xpath('@href').get()
            print(title_short,'    ',url)






        # t1 = response.xpath('//li[@class="bbs-sl-web-post-body"]')
        # np = 0
        # for item in t1:
        #     title = item.xpath('./div/div[@class="post-title"]/a/text()').get()
        #     title_list.append(title)
        #     url = 'https://bbs.hupu.com' + item.xpath('./div/div/a').xpath('@href').get()
        #     # print(url)
        #     post_time = item.xpath('./div/div[@class="post-time"]/text()').get()
        #     print(post_time)
            # 爬取每个字页面
            # yield scrapy.Request(url,callback=self.parse_post)
            # np = np + 1
            # if np == 3:
                # break
        
    # 解析帖子中具体的内容
    def parse_post(self, respones): 
        post_name = 'post1.html'
        with open(post_name, 'wb') as f:
            f.write(respones.body)

        post = respones.xpath('//')
        post_name = respones.xpath('//h1[@class="index_name__M5qqs"]/text()').get()



    def start_requests(self):
        # 获取 对应主题下的内容
        for page_num in range(self.page_range):
                yield scrapy.Request('https://bbs.hupu.com/search?q=%E5%A5%B3%E6%80%A7&topicId=1&sortby=general&page='+str(page_num+1))
        

        # 步行街热帖
        # yield scrapy.Request('https://bbs.hupu.com/all-gambia')
        
        
