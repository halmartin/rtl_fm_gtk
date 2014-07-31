#!/usr/bin/env python2
# Copyright (C) 2014 Hal Martin
# License: GPLv2

from gi.repository import Gtk
from gi.repository import GObject
import subprocess
import time

class MainWindow(object):

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('DATADIR_PREFIX/rtl_fm_gui.glade')

        self.window = self.builder.get_object('MainWindow')

        self.builder.connect_signals(self)

        self.spinbutton1 = self.builder.get_object('spinbutton1')

        mkfifo_command = ['mkfifo', '/tmp/radio']
        p = subprocess.Popen(mkfifo_command)

    def on_window_destroy(self, *args):
        try:
           self.p2.terminate()
           self.p3.terminate()
        except AttributeError:
           pass
        Gtk.main_quit(*args)

    def on_tune(self, signal):
        try:
            self.p2
            self.p3
            if(self.p2.poll() == None) & (self.p3.poll() == None):
                self.p2.terminate()
                self.p3.terminate()            
                time.sleep(1)
        except AttributeError:
            pass

        rtl_fm_command = ['rtl_fm', '-f', str(float(round(self.spinbutton1.get_value(),1))) + 'e6', '-M', 'wbfm', '-E', 'dc', '/tmp/radio', '2>&1', '>', '/dev/null']
        aplay_command = ['aplay', '-t', 'raw', '-c', '2', '-r', '16k', '-f', 'S16_LE', '/tmp/radio']

        self.p2 = subprocess.Popen(rtl_fm_command)
        self.p3 = subprocess.Popen(aplay_command)


    def show_help_window(self, signal):
        self.help_window = self.builder.get_object('AboutDialog1')
        self.help_window.show_all()

if __name__ == "__main__":
    hwg = MainWindow()
    Gtk.main()
