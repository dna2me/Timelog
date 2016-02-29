import ticking_counter
import time

core = ticking_counter.TickingCounter()
core.start()
time.sleep(1)
core.suspend()
time.sleep(2)
core.resume()
time.sleep(1)
core.finish()
print core.get_break_time()
