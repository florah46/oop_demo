import unittest
import order_verify

class TestOrder(unittest.TestCase):
    def test_order_status(self):
        order_id = 2
        self.assertEqual(order_verify.check_order_status(order_id), True)
        

    def test_order_status_pending(self):
        order_id = 3
        self.assertEqual(order_verify.check_order_status_pending(order_id), False)
    

    def test_order_status_pending1(self):
        order_id = 3
        self.assertFalse(order_verify.check_order_status_pending(order_id))
    
    def test_order_status_absent(self):
        order_id = 3
        self.assertTrue(order_verify.check_order_status_absent(order_id), True)
    
    def test_order_add(self):
        order_id = 45
        self.assertEqual(order_verify.check_order_add(order_id), False)

    def test_add_new_order(self):
        order_id = 79
        self.assertEqual(order_verify.add_new_order(order_id), False)

    def test_order_delivered(self):
        order_id = 7
        self.assertEqual(order_verify.order_delivered(order_id), True)