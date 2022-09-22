
from fetch.fetcher_interface import FetcherInterface
import requests

# 爬取网页：用requests访问网页。
# 解析网页：解析网页中的数据
# 结果入队：结果存入队列
# 如果我用java，首先启动多个线程，分布式爬取多个网站
# 所有的结果都存入队列，包括（源名称，节点列表）
# 消费者端将执行验证，并存入本地数据库中
class FetcherIpfsGithubIo(FetcherInterface):

    def url(self):
        return 'https://ipfs.github.io/public-gateway-checker/'

    def fetch(self):
        url_str = self.url()
        resp = requests.get(url_str, headers={
            'User-Agent': super().user_agent.random
        })
        if resp.status_code == 200:
            pass




