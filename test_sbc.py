
import unittest
from unittest.mock import patch
from side_bicep_curl import side_bicep_curl

class TestSideBicepCurl(unittest.TestCase):

    def test_sbc_initialization(self):
        sbc = side_bicep_curl()
        self.assertEqual(sbc.xShoulder, -1)
        self.assertEqual(sbc.yShoulder, -1)
        self.assertEqual(sbc.xElbow, -1)
        self.assertEqual(sbc.yElbow, -1)
        self.assertEqual(sbc.xWrist, -1)
        self.assertEqual(sbc.yWrist, -1)
        self.assertIsNone(sbc.startPoint)
        self.assertIsNone(sbc.startPoint2)
        self.assertIsNone(sbc.finalPoint)
        self.assertEqual(sbc.progress, 0)
        self.assertEqual(sbc.rep, 0)
        self.assertFalse(sbc.counted)



    @patch('time.time', side_effect=[1, 5, 9])
    def test_sbc_color_exception(self, mock_time):
        sbc = side_bicep_curl()
        sbc.display_colors = "#32ba19"
        with self.assertRaises(Exception):
            sbc.sbc(sbc.display_colors, 10, 20)
            sbc.sbc(sbc.display_colors, 10, 20)
            sbc.sbc(sbc.display_colors, 10, 20)



    def test_sbc_invalid_color(self):
        sbc = side_bicep_curl()
        with self.assertRaises(Exception):
            sbc.sbc("#ffffff", 10, 20)

    def test_sbc_wrist_below_start_point(self):
        sbc = side_bicep_curl()
        sbc.startPoint = 50
        sbc.yWrist = 40
        sbc.finalPoint = 97
        sbc.sbc("#000c7c", 10, 20)
        self.assertEqual(sbc.rep, 0)



if __name__ == '__main__':
    unittest.main()

