
__author__ = 'Macbookair'

from .base import FunctionalTest

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