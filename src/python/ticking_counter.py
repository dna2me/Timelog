# encoding: utf-8

import time

__author__ = 'dna2me'
__project__ = 'Timelog'


class TickingCounter:
    def __init__(self):
        self.break_record = []
        self.time_record = []

    def start(self):
        self.time_record.append(time.time())
        return

    def finish(self):
        if len(self.time_record) == 0:
            raise Exception('Have to run start before finish.')
        self.time_record.append(time.time())
        return

    def suspend(self):
        if len(self.time_record) == 0:
            raise Exception('Have to run start before suspend.')
        if len(self.break_record) % 2 != 0:
            return
        self.break_record.append(time.time())

    def resume(self):
        if len(self.break_record) % 2 == 0:
            return
        self.break_record.append(time.time())

    def get_break_time(self):
        break_record_length = len(self.break_record)
        result = 0
        if break_record_length % 2 == 0:
            result = self.count_break_time_last_break_record_is_resume(break_record_length)
        else:
            result = self.count_break_time_last_break_record_is_suspend(break_record_length)
        return result

    def count_break_time_last_break_record_is_resume(self, break_record_length):
        sum_break_time = 0
        for i in xrange(1, break_record_length, 2):
            sum_break_time += self.break_record[i] - self.break_record[i - 1]
        return sum_break_time

    def count_break_time_last_break_record_is_suspend(self, break_record_length):
        sum_break_time = self.count_break_time_last_break_record_is_resume(break_record_length - 1)
        if len(self.time_record) < 2:
            return sum_break_time

        var = self.time_record[1] - self.break_record[break_record_length - 1]
        sum_break_time += var
        return sum_break_time
