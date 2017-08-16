# reference : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib.request
import os
import numpy as np

def face(name):
    CDpath = "/Users/sinsanghun/Documents/pycharm/seleniumTest/chromedriver"

    driver = webdriver.Chrome(CDpath) # 크롬 드라이버의 위치를 지정해준다
    driver.get("https://www.google.com/imghp?hl=ko")  # 웹 주소를 받아온다

    # 해당 연예인 이미지 검색
    driver.find_element_by_name('q').send_keys(name)
    driver.find_element_by_xpath('//*[@id="_fZl"]').click()
    driver.implicitly_wait(3)

    # 첫번째 사진 클릭
    driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]').click()
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.findAll("img", class_="irc_mi")

    num = 1
    for i in tag:
        if num==2:
            url = i['src']
        num = num + 1

    image_set = [url]

    # 두번째 사진부터 url 검색
    for j in range(500):
        print(name, j)
        driver.find_element_by_xpath('// *[ @ id = "irc_ra"]').click()
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        tag2 = soup.findAll("img", class_="irc_mi")

        for k in tag2:
            if 'src' in str(k):
                url = k['src']
                image_set.append(url)


    # 사진 저장
    image_set = np.unique(image_set)

    for number in range(len(image_set)):
        try :
            print(number)
            full_name = name + str(number + 1) + ".jpg"
            urllib.request.urlretrieve(image_set[number], full_name)
        except :
            pass

    driver.close()

# 11
flist1 = ["정유미","오나미", "장도연", "고아라", "강예원", "구혜선", "강소라", "손예진", "박신혜", "공효진", "문근영", "한효주"]
# 12
flist2 = ["한지민", "조여정", "아이비", "서현", "태연", "강민경", "이효리", "옥주현", "최유정", "김세정", "소희", "아이유"]
# 11
flist3 = ["전지현", "김옥빈", "이나영", "김고은", "김희선", "김혜수", "엄지원", "라미란", "심은하", "김민희", "유진"]
# 12
flist4 = ["엄정화", "신민아", "하지원", "이보영", "박보영", "전혜빈", "서현진", "전도연", "송혜교", "김소현", "김유정", "김슬기"]
# 11
flist5 = ["이유리", "김태희", "조혜련", "박민영", "문채원", "김신영", "박나래", "김숙", "안영미", "이국주", "신봉선"]
# 12
flist6 = ["이영자", "예지원", "문소리", "김선아", "백지영", "장서희", "최지우", "홍진경", "홍진영", "오현경", "정선희", "김남주"]
# 8
flist7 = ["박진희", "정혜영", "이영애", "이하늬", "성유리", "이진", "산다라박", "박수진"]
# 24
flist8 = [ "민효린", "장나라", "송지효", "이민정", "이태임", "설리", "혜리", "선미", "태연", "윤아",
           "김지원", "청하", "헤이즈", "신세경","AOA 설현", "유빈", "서예지", "제시카", "정소민", "정채연",
           "크리스탈", "손나은", "정은지", "보미"]
# 9
flist9 = ["조보아", "조이", "아이린", "주결경", "김태리", "소유", "효린", "수지", "보라"]
# 36
flist10 =["AOA 초아", "티파니", "전효성", "현아", "써니", "하니", "솔지", "공민지", "나나", "레이나", "이연희", "마마무 화사", "마마무 휘인",
          "김소혜", "전소미", "진지희", "서신애", "쯔위", "트와이스 다현", "트와이스 나연", "러블리즈 케이", "러블리즈 류수정", "여자친구 예린",
          "여자친구 은하", "여자친구 엄지", "에이핑크 초롱", "AOA 지민", "AOA 민아", "우주소녀 성소", "오마이걸 승희", "오마이걸 아린",  "트와이스 사나",
          "트와이스 모모", "블랙핑크 지수", "블랙핑크 제니", "블랭핑크 로제"]
# 16
flist11 = ["주니엘", "황승언", "솔비", "박정현", "유리", "효연", "경리", "예은", "임지연", "정려원", "김하늘",  "유인나", "수애", "구구단 미나", "구구단 하나", "러블리즈 미주" ]
# 10
flist12 = ["경수진", "한보름", "이엘",  "고보결", "이소은", "김소은", "장희령", "차정원", "다비치 이해리","신보라", "홍윤화","걸스데이 유라"]
# 15
flist13 = ["걸스데이 소진", "걸스데이 민아", "레드벨벳 슬기", "레드벨벳 웬디", "레드벨벳 예리", "미쓰에이 민", "미쓰에이 페이"
            ,"러블리즈 지애", "러블리즈 예인", "우주소녀 성소", "우주소녀 루다", "우주소녀 보나", "트와이스 지효"]
# 13
flist14 = ["박한별", "김새론", "황정음", "제시카", "김아중", "배두나", "조윤희", "송하윤", "천우희", "윤하", "임수정", "오연서", "류혜영"]
# 13
flist15 = ["박진주", "남규리", "박소담", "하연수", "한예슬", "박하선", "김윤진", "최강희", "신소율", "심은경", "백진희", "고아성", "서우"]
# 13
flist16 = ["이영은", "한지혜", "추자현", "정은채", "한채아", "이요원", "한은정", "손은서", "김규리", "정가은", "차예련", "유인영", "서효림"]
# 12
flist17 = ["홍수아", "김희애", "황우슬혜", "황신혜", "한고은", "윤진서", "전소민", "모델 한혜진", "배우 한혜진", "서지혜", "강혜정", "티아라 은정"]
# 12
flist18 = ["티아라 효민", "티아라 보람", "티아라 지연", "윤승아", "송은이", "한가인", "허가윤", "김현주", "엄현경", "이열음", "송소희", "이시영"]
# 11
flist19 = ["이하나", "달샤벳 우희", "달샤벳 수빈", "달샤벳 세리", "소율", "여자친구 신비", "여자친구 유주", "가인", "나르샤", "서인영", "박정아"]
# 12
flist20 = ["트와이스 채영", "제아", "미료", "나라", "여자친구 소원", "유이", "나인뮤지스 혜미", "리지", "오하영", "정화", "빅토리아", "기희현"]
# 14
flist21 = ["강유미", "안소미", "채수빈", "트와이스 정연", "AOA 찬미", "마마무 문별", "마마무 솔라", "오마이걸 유아", "이수영", "박경림", "손담비", "간미연", "가수 박지윤", "박지선"]
# 12
flist22 = ["개그맨 김지민", "김사랑", "개그맨 김영희", "개그맨 이세영", "라붐 솔빈", "라붐 유정", "장재인", "박시연", "김성은", "보아", "엠버", "다나"]
# 13
flist23 = ["씨엘", "이하이", "악동뮤지션 이수현", "이성경", "강승현", "써니힐 주비", "써니힐 승아", "차오루", "정혜성", "문지애", "김원희", "김재경", "조현영"]
# 12
flist24 = ["이유비", "백예린", "고우리", "이선빈", "혜이니", "류화영", "최정원", "에일리", "제시", "시크릿 송지은", "시크릿 정하나", "러블리즈 베이비소울"]
# 13
flist25 = ["clc 승희", "백아연", "박지민", "원더걸스 혜림", "박보람", "조혜정", "쥬얼리 예원", "우주소녀 설아", "윤진이", "요조", "레이디 제인"]
# 13
flist26 = ["김소영", "연상은", "최희", "공서영", "정순주", "정인영", "장예원", "강지영 아나운서", "카라 강지영", "한승연", "구하라", "카라 규리", "조수"]


for name in flist1:
    pwd = os.getcwd()  # 현재 경로 저장
    os.mkdir(name)   # 이름으로 디렉토리 생성
    os.chdir(pwd+"/"+name) # 위치 이동
    face(name) # 이미지 크롤링
    os.chdir(pwd) # 다시 원래 위치로 이동



