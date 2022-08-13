import unittest
from classes import *

class test(unittest.TestCase):
    def setup_method(self):
        self.Television = Television()

    def test_volume_down(self):
        self.Television.volume_down()
        assert self.Television.__str__() == 'Is on = False, Channel = 0, Volume = 0'
        self.Television.power()
        self.Television.volume_down()
        assert self.Television.__str__ == 'Is on = True, Channel = 0, Volume = 0'
        self.Television.volume_up()
        self.Television.volume_up()
        self.Television.volume_down()
        self.assertEqual(self.Television.__str__(), 'Is on = False, Channel = 0, Volume = 1')

    def test_volume_up(self):
        self.Television.volume_up()
        assert self.Television.__str__() == 'Is on = False, Channel = 0, Volume = 0'
        self.Television.power()
        assert self.Television.__str__ == 'Is on = True, Channel = 0, Volume = 0'
        self.Television.volume_up()
        self.Television.volume_up()
        self.assertEqual(self.Television.__str__(), 'Is on = False, Channel = 0, Volume = 2')

    def test_channel_up(self):
        self.Television.channel_up()
        assert self.Television.__str__() == 'Is on = False, Channel = 0, Volume = 0'
        self.Television.power()
        assert self.Television.__str__ == 'Is on = True, Channel = 0, Volume = 0'
        self.Television.channel_up()
        self.Television.channel_up()
        self.assertEqual(self.Television.__str__(), 'Is on = False, Channel = 2, Volume = 0')

    def test_channel_down(self):
        self.Television.channel_down()
        assert self.Television.__str__() == 'Is on = False, Channel = 0, Volume = 0'
        self.Television.power()
        assert self.Television.__str__ == 'Is on = True, Channel = 0, Volume = 0'
        self.Television.channel_down()
        self.Television.channel_down()
        self.assertEqual(self.Television.__str__(), 'Is on = False, Channel = 2, Volume = 0')


if __name__ == '__main__':
    unittest.main()