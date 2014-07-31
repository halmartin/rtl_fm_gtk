Description
===
rtl_fm_gui is a basic GTK GUI written in python to control rtl_fm.

Dependencies
===
aplay
mkfifo
python2
python-pygtk
rtl_fm (from rtl-sdr)

Installation
===
sudo make install

Alternatively if you don't want to install rtl_fm_gui to a system-wide bin directory, you may edit rtl_fm_gui.py and change DATADIR_PREFIX to the full path of the directory you install rtl_fm_gui.glade to.

License
===
Copyright (C) 2014 Hal Martin

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
