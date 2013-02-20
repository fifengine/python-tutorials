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

from fife.extensions import pychan

# Import the ApplicationBase.  This is where a lot of magic happens but
# you don't need to know the inner workings just yet.  Once you are more
# familiar with FIFE you'll understand ApplicationBase much more.
from fife.extensions.basicapplication import ApplicationBase

class Tutorial1MouseListener(fife.IMouseListener):
	"""
	Main game listener.  Listens for Mouse events.  You must include all
	possible event functions or you will get an exception.  These functions
	are called by the engine's event manager when the corresponding events 
	are triggered.
	"""
	def __init__(self, application):
		
		self._engine = application.engine
		self._application = application
		self._eventmanager = self._engine.getEventManager()
		
		# We must make sure to call our base class' constructor to make sure
		# the listener is setup correctly.
		fife.IMouseListener.__init__(self)
		
	def mousePressed(self, event):
		# Mouse press was consumed by a PyChan widget so lets ignore it.
		# Dont worry too much about this yet.  This will come into play once
		# we have a GUI in place.
		if event.isConsumedByWidgets():
			return

		clickpoint = fife.ScreenPoint(event.getX(), event.getY())

		# Tell the application to move the player instance to the screen 
		# coordinate where the user clicked.
		self._application.movePlayer(clickpoint)
				
	def mouseReleased(self, event):
		pass

	def mouseMoved(self, event):
		pass
		
	def mouseEntered(self, event):
		pass
		
	def mouseExited(self, event):
		pass
		
	def mouseClicked(self, event):
		pass
		
	def mouseWheelMovedUp(self, event):
		pass	
		
	def mouseWheelMovedDown(self, event):
		pass
		
	def mouseDragged(self, event):
		pass

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

		# Since we want to listen for mouse events lets save a reference to
		# the event manager and create our event listener and attach it to 
		# the manager.
		self._eventmanager = self.engine.getEventManager()
		self._mouselistener = Tutorial1MouseListener(self)
		
		# Listeners are executed in the order in which they are added.
		# Lets ensure this one gets executed first.
		self._eventmanager.addMouseListenerFront(self._mouselistener)

	def loadMap(self, filename):
		"""
		Simple function to load and display a map file. We could of course 
		have passed in the map filename but I'll leave that up to you.
		
		@param filename The filename.
		"""
	
		self._mapfilename = filename
		
		# Check to make sure the map file is loadable (i.e. it's in the correct
		# format) and attempt to load the map.
		if self._loader.isLoadable(self._mapfilename):
			self._map = self._loader.load(self._mapfilename)
			self._mapLoaded = True

	def getLocationAt(self, screenpoint):
		"""
		Query the main camera for the Map location (on the actor layer)
		that a screen point refers to.
		
		@param screenpoint A fife.ScreenPoint
		"""
		
		# We must transform the point from screen coords to map coords then
		# create a Location object based on a the actor layer
		target_mapcoord = self._camera.toMapCoordinates(screenpoint, False)
		target_mapcoord.z = 0
		location = fife.Location(self._actorlayer)
		location.setMapCoordinates(target_mapcoord)
		return location

	def movePlayer(self, screenpoint):
		"""
		Simple function that moves the player instance to the given screenpoint.
		
		@param screenpoint A fife.ScreenPoint
		"""
		
		# You must tell the move function which action should be used for moving.
		# In this case we have the "walk" action defined for the player so we 
		# use that.  The 4.0 is how fast we want the player instance to move.
		self._player.move('walk', self.getLocationAt(screenpoint), 4.0)
			
	def _pump(self):
		"""
		This function gets called every frame.  This is where you want to
		call your main game logic code.
		"""
		
		# On our first frame the map will be loaded and we will grab a reference
		# to our camera, map and player instance.
		if not self._mapLoaded:
			self.loadMap("../assets/maps/tutorial1map.xml")
			
			# Save a reference to the main camera.  "camera1" must exist on the
			# map.
			self._camera = self._map.getCamera("camera1")
			
			# Save a ref to the actor layer and player on the map.  There must 
			# be a layer with an id of "actor_layer" and an instance with an id 
			# of "player" for this to work.
			self._actorlayer = self._map.getLayer("actor_layer")
			self._player = self._actorlayer.getInstance("player")
