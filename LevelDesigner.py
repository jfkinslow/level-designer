#!/usr/bin/python2.7

#imports and requirements
import pygtk;
pygtk.require('2.0');
import gtk;

#Create the main class
class Base:
	def destroy(self, widget, data=None):
		#Quit the script
		gtk.main_quit();

	def __init__(self):
		#Create the window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL);
		#Center the window on the screen
		self.window.set_position(gtk.WIN_POS_CENTER);
		#Set window size so that it doesn't go below the taskbar
		self.window.set_size_request(1024, 704);
		#Create a button
		self.button1 = gtk.Button("EXIT");
		self.button1.connect("clicked", self.destroy);
		fixed = gtk.Fixed();
		fixed.put(self.button1, 20, 30);
		self.window.add(fixed);
		#Show the window on the screen
		self.window.show_all();
		#Connect the destroy function to when the window closes
		self.window.connect("destroy", self.destroy);

	def main(self):
		#Run the main loop
		gtk.main()

if __name__ == "__main__":
	#Create the base object
	base = Base();
	#Run the main function
	base.main()


