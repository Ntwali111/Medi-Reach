import unittest
from app import app

class MediReachRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Medi-Reach", resp.data)

    def test_medicines(self):
        resp = self.client.get("/medicines")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Medicines", resp.data)

    def test_order(self):
        resp = self.client.get("/order")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Order", resp.data)

    def test_track_no_id(self):
        resp = self.client.get("/track")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Track Your Order", resp.data)

    def test_track_with_id_found(self):
        resp = self.client.get("/track?order_id=123")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Out for delivery", resp.data)

    def test_track_with_id_not_found(self):
        resp = self.client.get("/track?order_id=999")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Order not found", resp.data)

if __name__ == "__main__":
    unittest.main()
