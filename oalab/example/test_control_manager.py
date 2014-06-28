

from openalea.vpltk.qt import QtGui
from openalea.oalab.control.manager import ControlManager, ControlContainer
from openalea.oalab.gui.control.manager import ControlManagerWidget
from openalea.oalab.gui.control.panel import ControlPanel
from openalea.oalab.service import control, interface, qt_control

if __name__ == '__main__':
    instance = QtGui.QApplication.instance()
    if instance is None :
        app = QtGui.QApplication([])
    else :
        app = instance

    cm = ControlManager()
#     cc1 = ControlContainer()
#     cc2 = ControlContainer()

    cmw = ControlManagerWidget()
#     cmw.model.set_manager(cc2)
    cp = ControlPanel()

    # Fill al
    for iname in interface.names():
        for i, editor in enumerate(qt_control.qt_widget_plugins(iname)):
            if iname == 'IColorList':
                continue
            name = editor.name.replace('Plugin', 'P.').replace('Widget', 'W.')
            name = '%s_%s' % (iname, name)
            c = control.new(name, iname)
#             cc1.add_control(c)

    percent = interface.get('IInt', min=0, max=100)
    c = control.new('i', percent)
#     cc2.add_control(c)

    c = control.new('f', 'IFloat')
    cm.add_control(c)


#     from openalea.oalab.editor.text_editor import TextEditor
#     from openalea.oalab.editor.highlight import Highlighter
#     text = TextEditor()
#     Highlighter(text)
#     text.show()
#     text.raise_()


    from openalea.vpltk.shell.shell import get_shell_class, get_interpreter_class

    # Set interpreter
    interpreter = get_interpreter_class()()
    interpreter.locals['interp'] = interpreter
    interpreter.locals.update(locals())
    # Set Shell Widget

    widget = QtGui.QWidget()
    layout = QtGui.QHBoxLayout(widget)

    shellwdgt = get_shell_class()(interpreter)

    layout.addWidget(cmw)
    layout.addWidget(cp)
    layout.addWidget(shellwdgt)

    layout.setSpacing(0)
    layout.setContentsMargins(0, 0, 0, 0)
    widget.show()
    widget.raise_()

    if instance is None :
        app.exec_()


    import sys
    for k, v in cm.namespace().items():
        print >> sys.__stdout__, k, v

"""
from openalea.oalab.control.manager import ControlManager
from openalea.oalab.control.control import Control
a = Control('length', 'IInt', value=4)
b = Control('curve', 'ICurve2D')
c = Control('colors', 'IColorList')
cm  = ControlManager()
for control in (a, b, c):
    cm.add_control(control)
"""