#!/usr/bin/python
# -*- python -*-
#
#       OpenAlea.SecondNature
#
#       Copyright 2006-2011 INRIA - CIRAD - INRA
#
#       File author(s): Daniel Barbeau <daniel.barbeau@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################

__license__ = "CeCILL v2"
__revision__ = " $Id$"

import os, sys



def level_one():
    envdict = os.environ
    os.execle(sys.executable, sys.executable, "-c",
              '"import sys; from openalea.secondnature import main;sys.argv+="'+str(sys.argv)+'";main.level_two(sys.argv)"',
              envdict)


def level_two(args):
    # Restore default signal handler for CTRL+C
    import signal


    from PyQt4 import QtGui
    from PyQt4 import QtCore

    from openalea.core import logger
    from openalea.core.session import Session
    from openalea.visualea.visualeagui import threadit
    from openalea.secondnature import mainwindow

    class SecondNature(QtGui.QApplication):
        """Materialisation of the Openalea application.
        Does the basic inits. The session is initialised
        in a thread. It is safe to use once the sessionStarted
        signal has been emitted."""


        def __init__(self, args):
            QtGui.QApplication.__init__(self, args)
            # -- reconfigure LoggerOffice to use Qt log handler and a file handler --
            logger.default_init(level=logger.DEBUG, handlers=["qt"]) #TODO get level from settings
            logger.connect_loggers_to_handlers(logger.get_logger_names(), logger.get_handler_names())

            if __debug__:
                logger.set_global_logger_level(logger.DEBUG)
            else:
                logger.set_global_logger_level(logger.WARNING)

            # -- status clearout timer --
            self.__statusTimeout = QtCore.QTimer(self)
            self.__statusTimeout.setSingleShot(True)
            self.__statusTimeout.timeout.connect(self.clear_status_message)

            # -- main window --
            self.win = mainwindow.MainWindow(None)
            self.win.statusBar().showMessage("Starting up! Please wait")
            self.win.setEnabled(False)
            self.win.show()

            # -- start session in a thread --
            self.sessionth = threadit(self.__start_session, self,
                                      self.__cb_session_thread_end)

        def post_status_message(self, msg, timeout=2000):
            if self.__statusTimeout.isActive():
                self.__statusTimeout.stop()
            self.win.statusBar().showMessage(msg)
            self.__statusTimeout.start(timeout)

        def clear_status_message(self):
            self.win.statusBar().clearMessage()

        def get_session(self):
            return self.__session

        def __start_session(self):
            self.__session = Session()

        def __cb_session_thread_end(self):
            self.win.init_extensions()
            self.win.statusBar().clearMessage()
            self.win.setEnabled(True)

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = SecondNature(args)
    return app.exec_()


if( __name__ == "__main__"):
    level_two()




