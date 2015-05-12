
__author__ = 'Macbookair'

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class NewVisitorTest(FunctionalTest): #unitest.TestCase를 상속해서 테스트를 클래스 형태로 만듬.

    def test_can_start_a_list_and_retrieve_it_later(self):

        '''
        에디스는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        해답 웹사이트를 확인하러 간다.'''
        self.browser.get(self.server_url) # http://localhost:8000

        #웹사이트 타이틀과 헤더가 'To-Do'를 표시하고있다.
        self.assertIn('To-Do', self.browser.title) #유용한 디버깅 정보와 함께 도움이 되는 에러메시지를 출력
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #이제 바로 작업을 추가하기로한다.

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )


        #공작깃털사기를 입력창에 추가한다.(에디스의 취미는 그물만들기이므로)
        inputbox.send_keys('공작깃털 사기')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+') #assertRegex는 지정한 정규표현과 문자열이 일치하는지 확인한다. (unittest)안에있음
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물만들기')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        #새로운 사용자 프란시스가 접속한다.
        ##새로운 브라우저 세션을 통해서 에디스의 정보가 쿠키를 통해 유입되는 것을 방지한다.

        self.browser.quit()
        self.browser = webdriver.Firefox()

        #프란시스가 접속하고 에디스의 리스트는 보이지않는다.

        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('공작깃털 사기', page_text)
        self.assertNotIn('공작깃털을 이용해서 그물만들기', page_text)

        #프란시스가 새로운 아이템을 입력한다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('우유사기')
        inputbox.send_keys(Keys.ENTER)

        #프란시스가 전용 URL을 취득한다.
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #에디스 입려흔적이 없는지 다시 확인한다.
        page_text= self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('공작깃털 사기', page_text)
        self.assertIn('우유사기', page_text)

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):

        #에디스는 메인 페이지를 방문한다. 입력창이 가운데 배치 되어있는 것도 확인한다.
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        inputbox = self.browser.find_element_by_tag_name("input")
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2,
            512,
            delta=10)
