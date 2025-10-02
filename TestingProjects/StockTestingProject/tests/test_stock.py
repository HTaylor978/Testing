from unittest import TestCase
from unittest.mock import Mock

from TestingProjects.StockTestingProject.fin.exchange import Exchange
from TestingProjects.StockTestingProject.fin.stock import Stock

class TestStock(TestCase):

    def test_new_stock_has_0_trades(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        self.assertEqual(0, s.total_number_of_trades(), "New Stock should have no trades")

    def test_stock_had_1_buy(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.buy(100)
        self.assertEqual(1, s.total_number_of_trades(), "Stock with 1 buy should have 1 trade")

    def test_stock_had_1_sell(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.sell(100)
        self.assertEqual(1, s.total_number_of_trades(), "Stock with 1 sell should have 1 trade")

    def test_stock_has_100_shares_with_one_buy(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.buy(100)
        self.assertEqual(100, s.get_total_quantity_bought(), "Stock with 100 shares should have one trade")

    def test_stock_has_100_shares_with_two_buys(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.buy(50)
        s.buy(50)
        self.assertEqual(100, s.get_total_quantity_bought(), "Stock with 100 shares should have two trades")

    def test_stock_has_100_buys_with_one_buy_and_one_sell(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.buy(100)
        s.sell(100)
        self.assertEqual(100, s.get_total_quantity_bought(), "Stock with 100 shares should have one buy and one sell")

    def test_stock_has_100_shares_with_one_sell(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.sell(100)
        self.assertEqual(100, s.get_total_quantity_sold(), "Stock with 100 shares should have one trade")

    def test_stock_has_100_shares_with_two_sell(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.sell(50)
        s.sell(50)
        self.assertEqual(100, s.get_total_quantity_sold(), "Stock with 100 shares should have two trades")

    def test_stock_has_100_sells_with_one_buy_and_one_sell(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.buy(100)
        s.sell(100)
        self.assertEqual(100, s.get_total_quantity_sold(), "Stock with 100 shares should have one buy and one sell")

    def test_stock_with_1000_buys_has_greatest_of_1000(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.buy(1000)
        self.assertEqual(1000, s.get_biggest_quantity_buy(), "Stock with 1000 shares in one should have greatest trade of 1000")

    def test_stock_with_buys_of_50_100_1000_has_greatest_of_1000(self):
        dummy_exchange = Exchange()
        s = Stock('GGL', dummy_exchange)
        s.buy(50)
        s.buy(100)
        s.buy(1000)
        self.assertEqual(1000, s.get_biggest_quantity_buy(), "Stock with 1000 shares in one should have greatest trade of 1000")

    def test_total_value_is_105_with_10_buys_of_10_point_5(self):
        exchange_mock = Mock()
        exchange_mock.get_price.return_value = 10.5

        s = Stock('GGL', exchange_mock)
        s.buy(10)
        self.assertAlmostEqual(105, s.get_total_value_bought(), 5,"Stock with 10 shares at 10.5 should have total of 105")

    def test_total_value_is_477_point_3_with_10_buys_of_10_point_5_and_51_buys_of_7_point_3(self):
        exchange_mock = Mock()
        exchange_mock.get_price.return_value = 10.5

        s = Stock('GGL', exchange_mock)
        s.buy(10)

        exchange_mock.get_price.return_value = 7.3
        s.buy(51)

        self.assertAlmostEqual(477.3, s.get_total_value_bought(), 5,"Stock with 10 shares at 10.5 and 51 shares at 7.3 should have total of 477.3")

    def test_total_value_sold_is_105_with_10_sells_of_10_point_5(self):
        exchange_mock = Mock()
        exchange_mock.get_price.return_value = 10.5

        s = Stock('GGL', exchange_mock)
        s.sell(10)

        self.assertAlmostEqual(105, s.get_total_value_sold(), 5, "Stock with 10 sell shares at 10.5 should have total of 105")


    def test_total_value_sold_is_477_point_3_with_10_sells_of_10_point_5_and_51_sells_of_7_point_3(self):
        exchange_mock = Mock()
        exchange_mock.get_price.return_value = 10.5

        s = Stock('GGL', exchange_mock)
        s.sell(10)

        exchange_mock.get_price.return_value = 7.3
        s.sell(51)

        self.assertAlmostEqual(477.3, s.get_total_value_sold(), 5, "Stock with 10 sell shares at 10.5 and 51 sell shares at 7.3 should have total of 477.3")

    def test_biggest_value_is_572_point_8_with_32_buys_at_17_point_9(self):
        exchange_mock = Mock()
        exchange_mock.get_price.return_value = 17.9

        s = Stock('GGL', exchange_mock)
        s.buy(32)

        self.assertAlmostEqual(572.8, s.get_biggest_value(), 5, "Stock with 32 buy at 17.9 should have biggest value of 572.8")

    def test_biggest_value_is_1108_point_36_with_45_buys_at_12_point_3_and_11_buys_at_100_point_76(self):
        exchange_mock = Mock()
        exchange_mock.get_price.return_value = 12.3

        s = Stock('GGL', exchange_mock)
        s.buy(45)

        exchange_mock.get_price.return_value = 100.76
        s.buy(11)

        self.assertAlmostEqual(1108.36, s.get_biggest_value(), 5, "Stock with 45 buys at 12.3 (value = 553.5) and 11 buys at 100.76 (value = 1108.36) should have biggest value of 1108.36")