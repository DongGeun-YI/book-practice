from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError

# Create your tests here.

class ListAndItemModelsList(TestCase):

    def test_saving_and_retrieving_item(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.list = list_
        second_item.save()
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, '두 번째 아이템')
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_save_empty_list(self):
        list_ = List.objects.create()
        item = Item(list=list_, text = '')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean() #SQLite의 부족함으로 인해서, 유효성검증을 수동으로 해주어야함.


    def test_get_absoloute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absoloute_url(), '/lists/%d/' % (list_.id))

#with 구문을 try: item.save() \n self.fail('save 기능이 예외를 발생기켜야한다') \except ValidationError: \n pass;



