import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BbsSpider(CrawlSpider):
    name = "bbs"
    allowed_domains = ["bbs.hupu.com"]
    start_urls = ["https://bbs.hupu.com/"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def __init__(self,**kwargs):
        # self.cookies = 'smidV2=2024051010043201be3f8b47d34b0adba60bf68cf1a48b007dabd097aba3bf0; csrfToken=PHRpBKZMWeCijMiIKgbyMWn4; sajssdk_2015_cross_new_user=1; Hm_lvt_df703c1d2273cc30ba452b4c15b16a0d=1715306733; _HUPUSSOID=af90cb8d-243a-4a8c-8d9a-517a2da6326a; u=109632577|6JmO5omRSlIxMzY1NDAwNDM1|24fe|f913f61320a6b97114139c09dacabd42|d931e014fdedf4f2|aHVwdV8zZTEyYWE0ZTcwODk4ZGM4; ua=21991112; _CLT=00376064be821b71351c003dda774e37; us=14ada595f7f2c3570682b300cce5ab836ca1753f34c619c4e2aab5048454ca3e275f9ee0fcd62f6b23e99d3af4371592fcd7f4d52bfd034a301ee8169b2b2c36; tfstk=fVFjitsWjnxjPbUSjxQrN14uIMh_Go1FCFgT-Pd2WjhYWfaTScoqQcyW5yz93AImg5Z7Slmx_jPV1RG0a-RZ0ic_Wkl1YM5FTr4mZfIFYcso_FhKSdn9bmh-egJxJ_fFTr4YEkisN67gwf2nfchtHA3-e00BMfnvMai-52m9MlhOPzno7ELxBCHJequiWXWJ54Lj2rsNXhdGUZ-8u0O9OUmxHa4XQIdYNqMborm7lrNSlxiEUAF_bSEzWSPmE9vEszyQfRERNIZ_kJEt07Ip1cyn5P3I96YI2Sa_Nx2yDK3IGmMLMYLeazHTF7G4MGv3zzixdbyPEikZGownxxBlqlaS0lFjensrbJzzMYZd4QZiC-EjyXIztBoIfVp6PvAsPD75PdvZaW_oyou3PmDxr4XVPa9hSHA9_KNNPdptH40lDa_WKw1..; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f603f9b9e346-0eb0b4ebb3de02-4c657b58-784000-18f603f9b9f64c%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f603f9b9e346-0eb0b4ebb3de02-4c657b58-784000-18f603f9b9f64c%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfYW5vbnltb3VzX2lkIjoiMThmNjAzZjliOWUzNDYtMGViMGI0ZWJiM2RlMDItNGM2NTdiNTgtNzg0MDAwLTE4ZjYwM2Y5YjlmNjRjIiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4ZjYwNWRmMTg1MTBhOC0wOGIxNmQzNjZlNDQyMDgtNGM2NTdiNTgtNzg0MDAwLTE4ZjYwNWRmMTg2MTc4NiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; Hm_lpvt_df703c1d2273cc30ba452b4c15b16a0d=1715310356; .thumbcache_33f5730e7694fd15728921e201b4826a=vpLBO5zdSYP/3dxzBbdCQoUWQWzktJg2Tf8ct2eYciFNuYD/sVdlWRIbw8uVyOTAomEBoK/bWQ3VeRJoaf/02w%3D%3D'
        # self.headers = {'user-agent':''}
        pass

    def start_requests(self):
        
        url = 'https://bbs.hupu.com/'
        yield scrapy.Request(url)

    def parse_item(self, response):
        item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        filename = 'page.html'
        open(filename,'w').write(response.body)
        return item
