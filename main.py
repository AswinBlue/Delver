from SlackBot import SlackBot
from WebScrapper import WebScrapper
if __name__ == '__main__':
    bot = SlackBot()
    ws = WebScrapper(site_list=[
                    {
                        "name":"퀘이사존", 
                        "url":'https://quasarzone.com/bbs/qe_sale?_method=post&page=1&kind=subject&keyword=%ED%8A%B9%EA%B0%80&sort=num%2C+reply&direction=DESC',
                        "target":{"type":'class', "value": 'event-img-list event-img-list-j', "child": 'li'},
                        "header":{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'},
                    },
                    {
                        "name":"쿨앤조이", 
                        "url":'https://coolenjoy.net/bbs/29',
                        "target":{"type":'class', "value": 'tbl_head01 tbl_wrap', "child": 'tr'},
                        "header":{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'},
                    },
                    {
                        "name":"쿠팡", 
                        "url":'https://www.coupang.com/np/search?&q=%ED%8A%B9%EA%B0%80&component=178155&listSize=48',
                        "target":{"type":'class', "value": 'search-product-list', "child": 'li'},
                        "header":{
                            "authority": 'www.coupang.com',
                            "method": 'GET',
                            "cache-control": 'max-age=0',
                            "accept-language": 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                            "accept-encoding": 'gzip, deflate, br',
                            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            "scheme": 'https',
                            "path": '/np/search?&q=%ED%8A%B9%EA%B0%80&component=178155&listSize=48',
                            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
                        },
                    },
                ],
                keywords=['노트북'])
    ws.find_keywords(bot.send_message)