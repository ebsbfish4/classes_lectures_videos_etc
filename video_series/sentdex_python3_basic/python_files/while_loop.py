#! python3

import time

# Added sleep
condition = 1
while condition < 10:
    print(condition)
    condition += 1
    time.sleep(2)

# This will create infinite loop. Also use with __main__?
while True:
    print('doing stuff')
