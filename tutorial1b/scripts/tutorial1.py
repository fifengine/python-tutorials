#!/usr/bin/env python

# -*- coding: utf-8 -*-

# ####################################################################
#  Copyright (C) 2005-2011 by the FIFE team
#  http://www.fifengine.net
#  This file is part of FIFE.
#
#  FIFE is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library; if not, write to the
#  Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
# ####################################################################

import sys, os

from fife import fife

# Import the ApplicationBase.  This is where a lot of magic happens but
# you don't need to know the inner workings just yet.  Once you are more
# familiar with FIFE you'll understand ApplicationBase much more.
from fife.extensions.basicapplication import ApplicationBase

class Tutorial1Application(ApplicationBase):
	"""
	The main application.  It inherits fife.extensions.ApplicationBase
	and implements the _pump() function which gets called every frame.
	"""
	def __init__(self, settings):
		# Call our base class's __init__ function and pass it settings.
		# This is where the FIFE engine instance gets created and configured
		# (amoungst other things).  This includes reading the settings file,
		# applying the settings to the engine, initializing PyChan (our GUI
		# manager), creating the default application listener (more info on
		# this in our later tutorials), and setting up logging.  All of
		# these things you can do on your own but we provide ApplicationBase
		# to make your life easier.
		super(Tutorial1Application,self).__init__(settings)
		
		# Save a copy of our settings.  This could be useful in the future
		# as the Setting module allows you to store your own settins as
		# well as FIFE settings.
		self._settings = settings
		
		# Initialize an instance of fife.MapLoader which is a built in map
		# loader that we provide.  We must pass it some internal FIFE objects
		# that the loader requires to properly load a map.
		self._loader = fife.MapLoader(self.engine.getModel(), 
									self.engine.getVFS(), 
									self.engine.getImageManager(), 
									self.engine.getRenderBackend())
			
		# True if we have a map loaded.  False otherwise.
		self._mapLoaded = False

	def loadMap(self, filename):
		"""
		Simple function to load and display a map file. We could of course 
		have passed in the map filename but I'll leave that up to you.
		"""
	
		# This is the map filename.  Notice that it is relative to the tutorial
		# directory.
		self._mapfilename = filename
		
		# Check to make sure the map file is loadable (i.e. it's in the correct
		# format) and attempt to load the map.
		if self._loader.isLoadable(self._mapfilename):
			self._map = self._loader.load(self._mapfilename)
			self._mapLoaded = True
			
	def _pump(self):
		"""
		This function gets called every frame.  This is where you want to
		call your main game logic code.
		"""
		
		# On our first frame the map will be loaded
		if not self._mapLoaded:
			self.loadMap("../assets/maps/tutorial1map.xml")
