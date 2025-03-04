import json
import requests
from bs4 import BeautifulSoup
class WebScrapper:
    def __init__(self, site_list, keywords):
        # Set the URL to scrape and the keywords to search for
        self.site_list = site_list
        # 쿨앤조이, 퀘이사, 쿠팡, 11번가,  디씨, 다나와
        self.keywords = keywords

    def find_keywords(self, callback, separate=False):
        result = []

        for site in self.site_list:
            print("[SEARCHING]", site["name"])
            url = site["url"]
            base_url = site["base_url"]
            # Make the request to the URL and parse the HTML with BeautifulSoup. set headers like chrome
            try:
                response = requests.get(url=url, headers=site["header"],timeout=30)
            except Exception as e:
                print("[ERROR]\n", e)
                continue
            
            root = BeautifulSoup(response.content, 'html.parser')
            # Find all the text on the page and convert it to lowercase for case-insensitive search
            target = root.find(attrs={site["target"]["type"]: site["target"]["value"]})  # find root of item list

            if target is None:
                print(f'{site["name"]} returns {target}')
                continue  # if web scrapping returns nothing

            target = target.find_all(site["target"]["child"])  # find all 'li' (or 'tr' or ... )  tags

            # Find the first tag containing the keyword
            '''
            detected = target.find_all(string=lambda text: text.strip() and any ((keyword in text) for keyword in keywords) )  # string 파라미터에 조건문 부여 가능
            '''
            
            # for all 'li' tags, check keywords are inherited
            for item in target:
                full_text = item.get_text(strip=True)
                # check keywords
                for idx, keyword in enumerate(self.keywords):
                    if (keyword in full_text):
                        # if keyword is found in tag
                        link = item.find('a').get('href')  # get link
                        item_json = {
                            "siteName":site["name"],
                            "text":full_text,
                            "link":base_url + link,
                        }
                        msg = f'> {item_json["siteName"]}\n> {item_json["text"]}\n> {item_json["link"]}\n\n'
                        if separate:  # 분리해서 전송할 경우
                            print(msg)
                            response = callback(msg)
                        else:  # 합쳐서 전송할 경우
                            result.append(msg)
                            # keywords are mutually 'or' in relation. so if found a single keyword, break.
                        break


            if len(result) > 0:
                message = "[ Keyword detected ] keywords = \"{}\"".format('\", \"'.join(self.keywords))
                for idx, item in enumerate(result):
                    message += f'{idx}. {item}'
                response = callback(message)