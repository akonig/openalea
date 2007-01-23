# -*- python -*-
#
#       OpenAlea.Core: OpenAlea Core 
#
#       Copyright or (C) or Copr. 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Christophe Pradal <christophe.prada@cirad.fr>
#                       Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#

__doc__="""
This module defines all the classes for the Observer design Pattern
"""

__license__= "Cecill-C"
__revision__=" $Id$ "

###############################################################################


class Observed(object):
    """ Observed Object """

    def __init__(self):

        self.listeners = set()

    def register_listener(self, listener):
        self.listeners.add(listener)

    def unregister_listener(self, listener):
        self.listeners.discard(listerner)

    def notify_listeners(self):
        for l in self.listeners :
            l.notify()


class AbstractListener(object):
    """ Listener base class """
    
    def initialise (self, observed):
        observed.register_listener(self)

    def notify (self):
        raise RuntimeError()

    
