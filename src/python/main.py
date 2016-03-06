# _*_ coding: utf-8 _*_

import ticking_counter

ticking = ticking_counter.TickingCounter()
console_input = ''
while console_input != 'exit' and console_input != 'exit()':
    console_input = raw_input("Enter something: ")
    print ("you entered " + console_input)

    if console_input == 's' or console_input == 'start':
        ticking.start()
        print('process start.')
    elif console_input == 'pause' or console_input == 'p':
        ticking.suspend()
        print('pause ticking.')
    elif console_input == 'resume' or console_input == 'r':
        ticking.resume()
    elif console_input == 'f' or console_input == 'stop' or console_input == 'finish':
        ticking.finish()
        hours, minutes, seconds = ticking_counter.show_elapsed_time_tuple(ticking.get_total_working_time())
        result = ticking_counter.show_elapsed_time(ticking.get_whole_period_time())
        print("Total working time: {:0>2}:{:0>2}:{:05.2f}".format(
            int(hours), int(minutes), seconds))
        print("Whole period time: {:0>2}:{:0>2}:{:05.2f}".format(
            int(result['hour']), int(result['minute']), result['second']))

    else:
        pass
