#!/usr/bin/env python

# -*- coding: utf-8 -*-

# ####################################################################
#  Copyright (C) 2005-2013 by the FIFE team
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
		
	def _pump(self):
		"""
		This function gets called every frame.  This is where you want to
		call your main game logic code.
		"""
		pass
