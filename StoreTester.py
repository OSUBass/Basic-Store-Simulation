import unittest
from Store import Customer, Product, Store


class TestStore(unittest.TestCase):

    def test_1(self):
        """test to confirm quantity of products after decreasing quantity"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p1.decrease_quantity()
        number = p1.get_quantity_available()
        self.assertEqual(number, 7)

    def test_2 (self):
        """test to confirm myStore functions are adding to customer cart correctly"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("123", "Bitch fest", "when a rodent tries to date you", 42, 15)
        c1 = Customer("Yinsheng", "QWF", False)
        self.myStore = Store()
        self.myStore.add_product(p1)
        self.myStore.add_product(p2)
        self.myStore.add_member(c1)
        self.myStore.add_product_to_member_cart('889','QWF')
        self.myStore.add_product_to_member_cart('123', 'QWF')
        cart = c1.get_cart()
        self.assertIn('123', cart)

    def test_3(self):
        """tests price calculation at checkout with 2 items added to cart for a premium member"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("123", "Bitch fest", "when a rodent tries to date you", 42, 15)
        c1 = Customer("Yinsheng", "QWF", True)
        self.myStore = Store()
        self.myStore.add_product(p1)
        self.myStore.add_product(p2)
        self.myStore.add_member(c1)
        self.myStore.add_product_to_member_cart("889", "QWF")
        self.myStore.add_product_to_member_cart("123", "QWF")
        price = self.myStore.check_out_member("QWF")
        self.assertEqual(price, 75.45)

    def test_4(self):
        """tests price calculation at checkout with 2 items added to cart for a non-premium member"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("123", "Bitch fest", "when a rodent tries to date you", 42, 15)
        c1 = Customer("Yinsheng", "QWF", False)
        self.myStore = Store()
        self.myStore.add_product(p1)
        self.myStore.add_product(p2)
        self.myStore.add_member(c1)
        self.myStore.add_product_to_member_cart("889", "QWF")
        self.myStore.add_product_to_member_cart("123", "QWF")
        price = self.myStore.check_out_member("QWF")
        self.assertAlmostEqual(price, 80.7315)

    def test_5(self):
        """tests price calculation at checkout with 3 items in cart for a premium member when one of the items is sold
        out at checkout"""
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("123", "Bitch fest", "when a rodent tries to date you", 42, 1)
        c1 = Customer("Yinsheng", "QWF", True)
        self.myStore = Store()
        self.myStore.add_product(p1)
        self.myStore.add_product(p2)
        self.myStore.add_product(p2)
        self.myStore.add_member(c1)
        self.myStore.add_product_to_member_cart("889", "QWF")
        self.myStore.add_product_to_member_cart("123", "QWF")
        self.myStore.add_product_to_member_cart("123", "QWF")
        price = self.myStore.check_out_member("QWF")
        self.assertAlmostEqual(price, 75.45)


if __name__ == '__main__':
    unittest.main()
