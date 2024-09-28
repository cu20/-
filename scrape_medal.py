import requests
from bs4 import BeautifulSoup
import sys

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
    "tokyo-2020"
]
for a in olympics_data:
    s=f"https://olympics.com/zh/olympic-games/{a}/medals"
    response = requests.get(s,headers=headers)
    print(response.status_code)
    country_name=[]
    content = response.text
    soup=BeautifulSoup(content,"html.parser")
    names = soup.findAll("span",attrs={"data-cy":"country-name"})    
    #print(len(names))
    for name in names:
        country_name.append(name.string)
    country_dict = {c: [] for c in country_name}
    golds = soup.findAll("div",attrs={"title":"金牌"})
    silvers = soup.findAll("div",attrs={"title":"银牌"})
    bronzes = soup.findAll("div",attrs={"title":"铜牌"})
    a="sc-hKFymg ioYFft text--sm-body"
    b="sc-bCwene ebfbmP text--sm-body"
    # print(len(golds))
    # print(len(silvers))
    # print(len(bronzes))
    i=0
    for gold in golds:
        num=gold.find("span",attrs={"class":a})
        if num is None:
            num=gold.find("span",attrs={"class":b})
        #print(len(num))
        n=num.string
        if n == '-':
            n='0'
        country_dict[country_name[i]].append(n)
        i=i+1
    i=0
    for sil in silvers:
        num=sil.find("span",attrs={"class":a})
        if num is None:
            num=sil.find("span",attrs={"class":b})
        n=num.string
        if n == '-':
            n='0'
        country_dict[country_name[i]].append(n)
        i=i+1 
    i=0
    for br in bronzes:
        num=br.find("span",attrs={"class":a})
        if num is None:
            num=br.find("span",attrs={"class":b})
        n=num.string
        if n == '-':
            n='0'
        country_dict[country_name[i]].append(n)
        i=i+1
    hh1=soup.find("h1")
    h1=hh1.find("span").string
    output_file = h1+"获奖情况.txt"
    
    # 打开输出文件，并将标准输出重定向到文件
    with open(output_file, 'w') as f:
        sys.stdout = f
        print(h1+"获奖情况")
        i=0
        # print的内容将会输出到output.txt文件中
        for dic in country_dict:
            print(country_name[i])
            print("金牌数："+country_dict[country_name[i]][0],end="   ")
            print("银牌数："+country_dict[country_name[i]][1],end="   ")
            print("铜牌数："+country_dict[country_name[i]][2],end="   ")
            print("总牌数：",end='')
            print(int(country_dict[country_name[i]][0])+int(country_dict[country_name[i]][1])+int(country_dict[country_name[i]][2]))
            i=i+1
    
    # 恢复标准输出
    sys.stdout = sys.__stdout__
