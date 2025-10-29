#!/usr/bin/env python3
#console\animations.py
import time
import sys
import signal
import os
from colorama import init,Fore



class Animation:
    def __init__(self, frames = None, interval=0.08, duration=100):
        if frames is None:
            frames = [
            "⠋", "⠙", "⠹", "⠸", "⠼",
            "⠴", "⠦", "⠧", "⠇", "⠏"
            ]
        self.frames = frames
        self.interval = interval
        self.duration = duration
    def draw_andCallback(self, exit = lambda:sys.exit(1), interval = None, duration = None, callback = None, text=None ,colour=None, animate=False):
        init(autoreset=True)
        interval = interval or self.interval
        duration = duration or self.duration
        time_ = 0
        i = 0
        while  time_ < duration:
            try:
                signal.signal(signal.SIGINT, exit)
                signal.signal(signal.SIGTERM, exit)
                frame = self.frames[i % len(self.frames)]
                sys.stdout.write('\033[?25l')
                sys.stdout.write(f'\r{colour}{frame}')
                sys.stdout.flush()
                time_ += 0.72
                i += 1
                time.sleep(interval)
            except SystemExit:
                print("SystemExit Exception")
                exit()
        sys.stdout.write('\r \r\033[?25h')
        sys.stdout.flush()
        if callback:
            callback(text=text,colour=colour,animate=animate)