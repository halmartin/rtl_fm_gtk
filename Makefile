prefix?=/usr/local
bindir=$(prefix)/bin
datadir=$(prefix)/share

install:
	install -p -m 755 rtl_fm_gui.py $(bindir)/rtl_fm_gui
	sed -i "s#DATADIR_PREFIX#$(datadir)#g" $(bindir)/rtl_fm_gui
	install -p -m 644 rtl_fm_gui.glade $(datadir)/

uninstall:
	rm -f $(bindir)/rtl_fm_gui
	rm -f $(datadir)/rtl_fm_gui.glade
