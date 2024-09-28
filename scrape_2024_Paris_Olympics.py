import requests
from bs4 import BeautifulSoup
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
matches_name=["七人制橄榄球","三人篮球","举重","乒乓球","公路自行车","冲浪","击剑","场地自行车",
              "射击","射箭","小轮车竞速","山地自行车","帆船","手球","拳击","排球","摔跤","曲棍球",
              "柔道","水球","沙滩排球","游泳","滑板","现代五项","田径","皮划艇激流回旋","竞技体操",
              "篮球","网球","羽毛球","自由式小轮车","艺术体操","花样游泳","赛艇","足球","跆拳道",
              "跳水","蹦床","运动攀岩","铁人三项","霹雳舞","马拉松游泳","马术","高尔夫","体操",
              "皮划艇静水"
    ]
#转化为字典
matches_dict = {match: [[],[],[]] for match in matches_name} 
#七月份数据爬取
for day in range(24,32):
    response=requests.get(f"https://olympics.com/zh/paris-2024/schedule/{day}-july",headers=headers)
    #print(response.status_code)#获取状态码
    #获取html
    content=response.text
    #美化
    soup=BeautifulSoup(content,"html.parser")
    #当天的大比赛项目
    day_big_matches=soup.findAll("div",attrs={"class":"EventList-styles__Wrapper-sc-32051fc0-0 bUGvbg"})
    for match in day_big_matches:
        matchName=match.find("span",attrs={"class":"sc-bdnyFh dEmljd text--xs-title"})
        name=matchName.string
        #加上当天日期
        matches_dict[name][0].append(f"7月{day}日")
        match_time=match.findAll("span",attrs={"class":"sc-bdnyFh bUNYrV EventListItem-styles__Time-sc-8a193e56-2 NokMe text--sm-body"})
        #加上小比赛时间
        for time in match_time:
            matches_dict[name][0].append(time.string)
        #加上小比赛名称
        little_box=match.findAll("div","EventListItem-styles__Wrapper-sc-8a193e56-0 klNbrV")
        for little in little_box:
            little_name=little.find("span",attrs={"class","sc-bdnyFh bUNYrV text--sm-text"})
            matches_dict[name][1].append(little_name.string)
            #加上国家
            country_name=little.findAll("span",attrs={"class","sc-bdnyFh bUNYrV EventListItem-styles__CountryText-sc-8a193e56-13 gTSlYy text--sm-text"})
            #print(len(country_name))
            temp=[]
            if len(country_name) != 0:
                for c in country_name:
                    temp.append(c.string)
                matches_dict[name][2].append(temp[0]+"-"+temp[1])
#八月份数据爬取
for day in range(1,12):
    response=requests.get(f"https://olympics.com/zh/paris-2024/schedule/{day}-august",headers=headers)
    #print(response.status_code)#获取状态码
    #获取html
    content=response.text
    #美化
    soup=BeautifulSoup(content,"html.parser")
    #当天的大比赛项目
    day_big_matches=soup.findAll("div",attrs={"class":"EventList-styles__Wrapper-sc-32051fc0-0 bUGvbg"})
    for match in day_big_matches:
        matchName=match.find("span",attrs={"class":"sc-bdnyFh dEmljd text--xs-title"})
        name=matchName.string
        #加上当天日期
        matches_dict[name][0].append(f"8月{day}日")
        match_time=match.findAll("span",attrs={"class":"sc-bdnyFh bUNYrV EventListItem-styles__Time-sc-8a193e56-2 NokMe text--sm-body"})
        #加上小比赛时间
        for time in match_time:
            matches_dict[name][0].append(time.string)
        #加上小比赛名称
        little_box=match.findAll("div","EventListItem-styles__Wrapper-sc-8a193e56-0 klNbrV")
        for little in little_box:
            little_name=little.find("span",attrs={"class","sc-bdnyFh bUNYrV text--sm-text"})
            matches_dict[name][1].append(little_name.string)
            #加上国家
            country_name=little.findAll("span",attrs={"class","sc-bdnyFh bUNYrV EventListItem-styles__CountryText-sc-8a193e56-13 gTSlYy text--sm-text"})
            #print(len(country_name))
            temp=[]
            if len(country_name) != 0:
                for c in country_name:
                    temp.append(c.string)
                matches_dict[name][2].append(temp[0]+"-"+temp[1])
            
for name in matches_name[1:]:
    print()
    print()
    print(name+"  ")
    l=len(matches_dict[name][0])
    j=0
    k=0
    for i in range(0,l):
        print(matches_dict[name][0][i],end='  ')
        if "月" in matches_dict[name][0][i]:
            print()
            continue
        print(matches_dict[name][1][j],end=' ')
        j=j+1
        if len(matches_dict[name][2]) !=0 and k<len(matches_dict[name][2]):
            print(matches_dict[name][2][k],end=' ')
            k=k+1
# name="七人制橄榄球"
# print()
# print()
# print(matches_name[0]+" ")
# l=len(matches_dict[name][0])
# j=0
# k=0
# jiange=0
# for i in range(0,l):
#     print(matches_dict[name][0][i],end='  ')
#     if "月" in matches_dict[name][0][i]:
#         print()
#         continue
#     print(matches_dict[name][1][j],end=' ')
#     j=j+1
#     if len(matches_dict[name][2]) !=0 :
#         if k>=18 and jiange<16:
#             k=18
#             jiange=jiange+1
#         else :
#             if k>=51:
#                 k=k+1
                
#             else:
#                 print(matches_dict[name][2][k],end=' ')
#                 k=k+1

            