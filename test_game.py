# -*- encoding=utf8 -*-
__author__ = "tranhau"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/7c1d765c?cap_method=MINICAP_STREAM&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)# -*- encoding=utf8 -*-
__author__ = "tranhau"

from airtest.core.api import *

auto_setup(__file__)

dev = device()

touch(Template(r"icon.png", record_pos=(0.356, 0.581), resolution=(1080, 2340)))

sleep(5)

# click start
if exists(Template(r"start_btn.png", record_pos=(-0.004, 0.755), resolution=(1080, 2340))):
    touch(Template(r"start_btn.png", record_pos=(-0.004, 0.755), resolution=(1080, 2340)))

# click run
dev.touch((518,1830), duration=0.01)

sleep(5.0)

number_play=2

for i in range(number_play):
    print(" count-" + str(i))
    while not exists(Template(r"game_over_btn.png", record_pos=(0.011, 0.742), resolution=(1080, 2340))):
        # swipe left
        dev.swipe_along([(543, 1577), (150, 1534)])

        sleep(1.0)
        
        # swipe up
        dev.swipe_along([(525, 1544), (522, 1344)])
        
        sleep(1.0)
        
        # swipe right
        dev.swipe_along([(543, 1577), (840, 1451)])

        sleep(1.0)
        # swipe up
        dev.swipe_along([(525, 1544), (522, 1344)])
        
    dev.touch((475,1970), duration=0.01)
    if i != number_play-1:
        touch(Template(r"run_btn.png", record_pos=(0.006, 0.606), resolution=(1080, 2340)))
        
    else: 
        touch(Template(r"main_menu_btn.png", record_pos=(-0.003, 0.305), resolution=(1080, 2340)))





        
        
        
        






