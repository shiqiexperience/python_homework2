from homework2_2_MyTimer import MyTimer
import time

with MyTimer(units="m") as t:
    print("Hello world")

print(t.elapsed_time())
