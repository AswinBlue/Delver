# from SlackBot import SlackBot
import DiscordMessage
from WebScrapper import WebScrapper
if __name__ == '__main__':
    # 수정방법
    # 1. keywords에 원하는 키워드를 입력한다.
    # 2. 검색하고 싶은 사이트의 링크를 url에 넣고, base_url 에는 해당 사이트의 root 주소를 넣는다. (메인 페이지의 주소)
    # 3. 브라우저에서 검색 결과를 표시하는 표의 가장 root component를 찾는다. component의 class가 'ROOT' 라면, type에 class, value에 ROOT 를 입력한다.
    #    class 외 다른 식별자가 있다면 사용할 수 있다. (ex:  id=result_table)
    #    그리고 표의 행에 해당하는 component의 타입을 'child' 로 설정한다(보통 tr 또는 li)
    # 4. 필요하다면 헤더를 수정한다. 매크로를 막기 위해 헤더값을 보고 결과를 회신하는 사이트도 있음을 인지한다.

    ws = WebScrapper(site_list=[
                    {
                        "name":"퀘이사존_이벤트",
                        "base_url": 'https://quasarzone.com',
                        "url":'https://quasarzone.com/bbs/qe_sale',
                        "target":{"type":'class', "value": 'event-img-list event-img-list-j', "child": 'li'},
                        "header":{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'},
                    },
                    {
                        "name":"퀘이사존_지름", 
                        "url":'https://quasarzone.com/bbs/qb_saleinfo',
                        "base_url": 'https://quasarzone.com',
                        "target":{"type":'class', "value": 'market-type-list market-info-type-list relative', "child": 'tr'},
                        "header":{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'},
                    },
                    {
                        "name":"쿨앤조이_이벤트", 
                        "url":'https://coolenjoy.net/bbs/29',
                        "base_url":'',
                        # "target":{"type":'class', "value": 'tbl_head01 tbl_wrap', "child": 'tr'},
                        "target":{"type":'id', "value": 'bo_webzine', "child": 'li'},
                        "header":{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'},
                    },
                    {
                        "name":"쿨앤조이_지름", 
                        "url":'https://coolenjoy.net/bbs/jirum',
                        "base_url":'',
                        "target":{"type":'name', "value": 'fboardlist', "child": 'li'},
                        "header":{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'},
                    },
                    # {
                    #     "name":"쿠팡", 
                    #     "url":'https://m.coupang.com/nm/search?q=%ED%8A%B9%EA%B0%80',
                    #     "base_url":'https://www.coupang.com',
                    #     "target":{"type":'class', "value": 'search-product-list', "child": 'li'},
                    #     "header":{
                    #         "authority": 'www.coupang.com',
                    #         "method": 'GET',
                    #         "cache-control": 'no-cache',
                    #         "accept-language": 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                    #         "accept-encoding": 'gzip, deflate, br',
                    #         "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    #         "scheme": 'https',
                    #         "path": '/np/search?&q=%ED%8A%B9%EA%B0%80&component=178155&listSize=48',
                    #         "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
                    #     },
                    # },
                ],
                keywords=['노트북', '마우스', '키보드'])
    # bot = SlackBot()
    ws.find_keywords(DiscordMessage.send_message, separate=True)