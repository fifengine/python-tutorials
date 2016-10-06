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

# Import the main FIFE module
from fife import fife

# Import the FIFE Setting extension
from fife.extensions.fife_settings import Setting

# Import our Tutorial1Application class
from scripts.tutorial1 import Tutorial1Application

# This is required in order to use the ApplicationBase framework provided
# in the fife.extensions module.  app_name is the name of your application,
# settings_file is what to call your settings file.  If you don't provide
# a settings-dist.xml file a blank settings file will be created for you by
# the Setting extension.
settings = Setting(app_name="tutorial1",
              settings_file="./settings.xml")

def main():
	# This creates an instance of Tutorial1Application and passes it the
	# Setting instance you created above.  The ApplicationBase will 
	# automatically create and configure an instance of the FIFE engine.
	app = Tutorial1Application(settings)
	
	# Start the application
	app.run()

if __name__ == '__main__':
	main()
