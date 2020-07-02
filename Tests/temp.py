def get_products(urls, num, wait_time):
    """
    Arguments:
    - urls: 리스트. 크롤링할 url들을 원소로 함.
    - num: url당 크롤링할 아이템 수
    - wait_time: 로딩을 몇 초까지 기다릴지

    Return:
    - total_posts: 리스트. 아이템 당 {"product_url": 상품url, "img_url": 이미지url} 정보를 크롤링한 것을 원소로 함.

    크롤링 완료 후 "key":고유번호(5자리수)를 추가해줄 것임 (key를 사후에 추가하는 이유는 중복 크롤링 처리를 쉽게 하기 위함임)
    """

    total_posts = []  # 전체 크롤링 결과를 저장할 리스트
    product_set = set()  # 중복 크롤링 거르기 위한 셋. product_url을 원소로 함
    unit_of_scroll = 3  # 반복할 스크롤 단위

    # 브라우저에 임의로 User-agent 옵션을 넣어 Python 코드로 접속함을 숨김
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"')
    # 크롬 브라우저 실행
    browser = webdriver.Chrome(executable_path='chromedriver_81', chrome_options=chrome_options)
    # 대기가능한 최대 시간
    wait = WebDriverWait(browser, wait_time)

    for url in urls:  # 인자로 주어진 url 하나씩 취함

        posts = []  # 당해 url 크롤링 결과를 저장할 리스트

        browser.get(url)
        body = browser.find_element_by_tag_name('body')

        count = 0  # 더 이상 로드되는 데이터가 없을 시 크롤링 종료하기 위해 필요한 count임
        prev_posts_count = 0

        # 초기에 목표값만큼 스크롤
        count_temp = 0
        for _ in range(num // 24 + 1):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            count_temp += 1

        while len(posts) < num:
            # Get scroll height
            last_height = browser.execute_script("return document.body.scrollHeight")

            # 현재까지 리스트 개수 카운트
            if count_temp >= unit_of_scroll:
                count_temp = 0
                ele_posts = browser.find_element_by_class_name('products_container').find_elements_by_class_name(
                    'ProductItem')
                cur_posts_count = len(ele_posts)

            # 목표 갯수에 도달하지 못헀을 경우 더 스크롤 (단위로)
            if cur_posts_count < num:
                for _ in range(unit_of_scroll):
                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(0.5)
                    count_temp += 1


                '''
                #스크롤이 더이상 안 되면서 수집한 목록이 목표 갯수 미만일 경우
                # Scroll down to bottom
                SCROLL_PAUSE_TIME = 1
                time.sleep(SCROLL_PAUSE_TIME)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIME)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
                time.sleep(SCROLL_PAUSE_TIME)
                # Calculate new scroll height and compare with last scroll height
                new_height = browser.execute_script("return document.body.scrollHeight")
                if new_height == last_height : 
                    break
                '''

    for ele in ele_posts:
        image_container = ele.find_element_by_class_name('image_container')
        info_container = ele.find_element_by_class_name('info_container')
        product_url = image_container.find_element_by_tag_name('a').get_attribute('href')
        if product_url not in product_set:
            dict_post = {"product_url": product_url}
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ImageLoader.ratio_1_1.loaded')))
            ele_img = image_container.find_element_by_class_name('ImageLoader.ratio_1_1.loaded')
            dict_post["img_url"] = ele_img.get_attribute("src")
            dict_post["channel"] = info_container.find_elements_by_class_name('text_container').find_element_by_tag_name(
                'a').text
            dict_post['product_name'] = info_container.find_elements_by_class_name('product_name').find_element_by_tag_name(
                'a').text
            dict_post['price_discount'] = info_container.find_elements_by_class_name('price').find_element_by_class_name(
                'discount_price').text
            dict_post['price_consumer'] = info_container.find_elements_by_class_name('price').find_element_by_class_name(
                'consumer_price').text
            product_set.add(product_url)
            posts.append(dict_post)

    prev_posts_count = cur_posts_count

    total_posts.extend(posts[:num])
    posts = []  # initialize posts

    return total_posts


def output(data, filepath):
    out = json.dumps(data, ensure_ascii=False)

    if filepath:
        with open(filepath, "w", encoding="utf8") as f:
            f.write(out)
        # for permission
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IWOTH)
    else:
        print(out)