import requests
from bs4 import BeautifulSoup
import json  

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
olympics_data = [  
    "athens-1896",    
    "london-1908",  
    "stockholm-1912",  
    "antwerp-1920",  
    "paris-1924",  
    "amsterdam-1928",  
    "los-angeles-1932",  
    "berlin-1936",  
    "london-1948",  
    "helsinki-1952",  
    "melbourne-1956",  
    "rome-1960",  
    "tokyo-1964",  
    "mexico-city-1968",  
    "munich-1972",  
    "montreal-1976",  
    "moscow-1980",  
    "los-angeles-1984",  
    "seoul-1988",  
    "barcelona-1992",  
    "atlanta-1996",  
    "sydney-2000",  
    "athens-2004",  
    "beijing-2008",  
    "london-2012",  
    "rio-2016",  
     
]
for a in olympics_data:
    s=f"https://olympics.com/en/olympic-games/{a}/results"
    s_title=f"https://olympics.com/zh/olympic-games/{a}/results"
    r = requests.get(s_title,headers = headers)
    tex = r.text
    soup_title = BeautifulSoup(tex,"html.parser")
    title = soup_title.find('title')
    r_title = title.string
    output_file = r_title+"获奖情况.txt"
    with open(output_file, 'w',encoding='utf-8') as file:
        response=requests.get(s,headers=headers)
        # print(response.status_code)
        # if response.status_code == 404:
        #     print(a)
        match_list = []
        content = response.text
        soup = BeautifulSoup(content,"html.parser")
        m = soup.find("script",attrs={"id":"__NEXT_DATA__"})
        s=m.string
        # 假设script_content是一个JSON格式的字符串  
        data = json.loads(s)  
        # 现在你可以根据需要访问data中的特定内容了  
        props = data['props'] 
        pg = props['pageProps']
        oly = pg['olympicGame']
        match = oly['disciplines']
        for ma in match:
            match_list.append(ma['slug'].lower())
        for mb in match_list:
            url = f"https://olympics.com/zh/olympic-games/{a}/results/{mb}"
            response2 = requests.get(url,headers = headers)
            content2 = response2.text
            soup2 = BeautifulSoup(content2,"html.parser")
            ziye = soup2.find('script',id="__NEXT_DATA__")
            s2 = ziye.string
            data2 = json.loads(s2)
            props2 = data2['props']
            pg2 = props2['pageProps']
            key = pg2['gameDiscipline']
            h1 = soup2.find('title')
            h11 = h1.string
            output_file = h11+key['title']+"获奖情况.txt"
            if '/' in output_file:
                output_file = output_file.replace('/', '_')
            with open(output_file, 'w',encoding='utf-8') as file:    
                print(h11+key['title']+"获奖情况",file=file)
                events = key['events']
                for event in events:
                    print(event['title']+"-"+event['gender'],file=file)
                    awards = event['awards']
                    for order in awards:
                        if order['participant']['__typename'] == "GameTeam":
                            print("第"+f"{order['rank']['order']}"+"名:"+order['participant']['country']['name'],file=file)
                        if order['participant']['__typename'] ==  "Athlete":                  
                            print("第"+f"{order['rank']['order']}"+"名:"+order['participant']['displayName']+' '+'来自 '+order['participant']['countryObject']['name'],file=file)                   
            sys.stdout = sys.__stdout__                    
