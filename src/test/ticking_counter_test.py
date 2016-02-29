# _*_ coding: utf-8 _*_

from unittest import TestCase
from src.python import ticking_counter
import time


class TickingCounterTest(TestCase):
    def setUp(self):
        self.tickingCounter = ticking_counter.TickingCounter()

    def test_finish(self):
        try:
            self.tickingCounter.finish()
            self.fail('exception not thrown.')
        except Exception:
            pass

    def test_start_finish_quickly(self):
        self.tickingCounter.start()
        self.tickingCounter.finish()
        self.assertAlmostEqual(self.tickingCounter.time_record[0],
                               self.tickingCounter.time_record[1],
                               0)

    def test_start_finish_1_sec(self):
        self.tickingCounter.start()
        time.sleep(1)
        self.tickingCounter.finish()
        time_substraction = self.tickingCounter.time_record[1] - self.tickingCounter.time_record[0]
        self.assertAlmostEqual(1, time_substraction, 1)

    def test_suspend(self):
        try:
            self.tickingCounter.suspend()
            self.fail('exception not thrown.')
        except Exception:
            pass

        self.tickingCounter.start()
        time.sleep(0.1)
        self.tickingCounter.suspend()
        self.assertEqual(1, len(self.tickingCounter.break_record))
        self.tickingCounter.suspend()
        self.assertEqual(1, len(self.tickingCounter.break_record))

    def test_resume(self):
        self.assertEqual(0, len(self.tickingCounter.break_record))
        self.tickingCounter.resume()
        self.assertEqual(0, len(self.tickingCounter.break_record))

        self.tickingCounter.start()
        self.tickingCounter.suspend()
        self.tickingCounter.resume()
        self.assertEqual(2, len(self.tickingCounter.break_record))
        self.tickingCounter.resume()
        self.assertEqual(2, len(self.tickingCounter.break_record))

    def test_get_break_time(self):
        self.tickingCounter.start()
        time.sleep(1)
        self.tickingCounter.suspend()
        time.sleep(1)
        actual = self.tickingCounter.get_break_time()
        self.assertEqual(0, actual)
        self.tickingCounter.resume()
        actual1 = self.tickingCounter.get_break_time()
        self.assertAlmostEqual(1, actual1, 1)
        self.tickingCounter.suspend()
        actual2 = self.tickingCounter.get_break_time()
        self.assertAlmostEqual(1, actual2, 1)
        self.assertNotEqual(1, actual2)
        self.assertEqual(actual1, actual2)


    def test_count_breaktime_last_breakrecord_is_resume(self):
        self.tickingCounter.start()
        self.tickingCounter.suspend()
        self.tickingCounter.resume()
        actual = self.tickingCounter.count_break_time_last_break_record_is_resume(2)
        self.assertAlmostEqual(0, actual, 1)
        self.assertNotEqual(0, actual)

        self.tickingCounter.suspend()
        self.tickingCounter.resume()
        time.sleep(1)
        self.tickingCounter.suspend()
        self.tickingCounter.resume()
        self.assertAlmostEqual(0, actual, 1)
        self.assertNotEqual(0, actual)

    def test_count_breaktime_last_breakrecord_is_suspend(self):
        self.tickingCounter.start()
        self.tickingCounter.suspend()
        actual = self.tickingCounter.count_break_time_last_break_record_is_suspend(1)
        self.assertEqual(0, actual)

        self.tickingCounter.resume()
        self.tickingCounter.suspend()
        actual1 = self.tickingCounter.count_break_time_last_break_record_is_suspend(3)
        self.assertAlmostEqual(0, actual1, 1)
        self.assertNotEqual(0, actual1)

        self.tickingCounter.resume()
        time.sleep(1)
        self.tickingCounter.suspend()
        actual2 = self.tickingCounter.count_break_time_last_break_record_is_suspend(5)
        self.assertAlmostEqual(0, actual2, 1)
        self.assertNotEqual(0, actual2)

        self.tickingCounter.finish()
        actual3 = self.tickingCounter.count_break_time_last_break_record_is_suspend(5)
        self.assertAlmostEqual(0, actual3, 1)
        self.assertNotEqual(0, actual3)

