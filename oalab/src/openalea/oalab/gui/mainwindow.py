#---------------------------------------------
# Main Window class
# 
# OALab start here with the 'main' function
#---------------------------------------------

import sys
import os

import qt

from openalea.oalab.editor.text_editor import PythonCodeEditor as Editor
from openalea.oalab.editor.text_editor import LPyCodeEditor as LPyEditor
from openalea.oalab.editor.text_editor import SelectEditor
from openalea.oalab.shell.shell import ShellWidget
from openalea.oalab.shell.interpreter import Interpreter
from openalea.oalab.gui.project import ProjectManager

class MainWindow(qt.QMainWindow):
    def __init__(self, parent=None):
        super(qt.QMainWindow, self).__init__(parent)
        # -- show the splash screen --
        self.splash = show_splash_screen()
        # project
        self.projectManager = ProjectManager()
        self.projectManager.new_project()
        
        # list of central widgets
        self.widList = []
        
        # Central widgets
        # Virtual World
        self.set_virtual_world()
        # editor
        self.set_text_editor_container()
        # central widget
        self.set_central_widget(1,2)
        
        # Other widgets
        # control panel
        self.set_control_panel()
        # observation panel
        self.set_observation_panel()
        # shell
        self.set_shell()
        # help
        self.set_help()
        # Shell and Help
        # self.splitDockWidget(self.shellDockWidget, self.helpDockWidget, qt.Qt.Horizontal)
        # Ressources
        self.set_ressources_manager()
        # Packages
        self.set_package_manager()
        
        # Status Bar
        self.set_status_bar()
        # Actions bars and buttons
        self.set_editor_actions()
        self.set_permanent_editor_buttons()
        self.set_model_actions()
        self.set_model_buttons()
        self.set_view_actions()
        self.set_view_buttons()
        # window title and icon
        self.setWindowTitle("Open Alea Virtual Laboratory")
        self.setWindowIcon(qt.QIcon("./resources/openalea_icon2.png"))
        self.splash.finish(self)
    
    #----------------------------------------
    # Setup Central Widget
    #----------------------------------------
    def set_central_widget(self, row, column):
        layout = qt.QGridLayout()
        self.central = qt.QWidget()
        self.central.setMinimumSize(600, 500)
        
        l = len(self.widList)
        
        # Fill central Widget in a layout
        i=0
        for x in range(row):
            for y in range(column):
                if i < l:
                    wid = self.widList[i]
                # if they are more panels than widgets in widgList
                else:
                    wid = qt.QWidget()
                
                try:
                    wid.setMinimumSize(100,100) 
                except:
                    pass
  
                layout.addWidget(wid ,x ,y)
                i += 1
        
        # If they are too many widgets, they are add (in new lines)
        if l > i:
            for w in self.widList[i:]:
                layout.addWidget(w)

        
        self.central.setLayout(layout)

        self.setCentralWidget(self.central)         

        
    def set_central_widget11(self):    
        self.set_central_widget(1,1)
    def set_central_widget12(self):    
        self.set_central_widget(1,2)
    def set_central_widget13(self):    
        self.set_central_widget(1,3)
    def set_central_widget21(self):    
        self.set_central_widget(2,1)
    def set_central_widget22(self):    
        self.set_central_widget(2,2)
    def set_central_widget23(self):    
        self.set_central_widget(2,3)    
        
    #----------------------------------------
    # Setup Virtual World
    #----------------------------------------
    def set_virtual_world(self):
    
        imageLabel = qt.QLabel()
        image = qt.QImage("./resources/arbre.png")
        pix = qt.QPixmap()
        pix = pix.fromImage(image)
        imageLabel.setPixmap(pix)
        
        scrollArea = qt.QScrollArea()
        scrollArea.setBackgroundRole(qt.QPalette.Dark)
        scrollArea.setWidget(imageLabel)
        scrollArea.setAlignment(qt.Qt.AlignCenter)
        
        self.VW = scrollArea
        self.VW.setMinimumSize(300, 300)
        
        # self.VWDockWidget = qt.QDockWidget("Virtual World", self)
        # self.VWDockWidget.setObjectName("VW")
        # self.VWDockWidget.setAllowedAreas(qt.Qt.LeftDockWidgetArea | qt.Qt.RightDockWidgetArea | qt.Qt.TopDockWidgetArea)
        # self.VWDockWidget.setWidget(self.VW)
        # self.addDockWidget(qt.Qt.RightDockWidgetArea, self.VWDockWidget) 
        
        self.widList.append(self.VW)
        
    #----------------------------------------
    # Setup Ressources Manager Dock Widget
    #----------------------------------------
    def set_ressources_manager(self):
        # Ressources
        self.ressManaWid = qt.QWidget()
        self.ressManaWid.setMinimumSize(100, 100)
        self.ressManaWid.setMaximumSize(400, 400)

        self.ressManaDockWidget = qt.QDockWidget("Ressources Manager", self)
        self.ressManaDockWidget.setObjectName("RessMana")
        self.ressManaDockWidget.setAllowedAreas(qt.Qt.LeftDockWidgetArea | qt.Qt.RightDockWidgetArea | qt.Qt.TopDockWidgetArea)
        self.ressManaDockWidget.setWidget(self.ressManaWid)
        self.addDockWidget(qt.Qt.LeftDockWidgetArea, self.ressManaDockWidget) 
        
    #----------------------------------------
    # Setup Package Manager Dock Widget
    #----------------------------------------
    def set_package_manager(self):
        # Ressources
        self.packManaWid = qt.QWidget()
        self.packManaWid.setMinimumSize(100, 100)
        self.packManaWid.setMaximumSize(400, 400)

        self.packManaDockWidget = qt.QDockWidget("Package Manager", self)
        self.packManaDockWidget.setObjectName("RessMana")
        self.packManaDockWidget.setAllowedAreas(qt.Qt.LeftDockWidgetArea | qt.Qt.RightDockWidgetArea | qt.Qt.TopDockWidgetArea)
        self.packManaDockWidget.setWidget(self.packManaWid)
        self.addDockWidget(qt.Qt.LeftDockWidgetArea, self.packManaDockWidget)     
        
    
    #----------------------------------------
    # Setup Help Dock Widget
    #----------------------------------------
    def set_help(self):
    
        # Help
        self.helpWid = qt.QWidget()
        self.helpWid.setMinimumSize(150, 150)
        self.helpWid.setMaximumSize(400, 400)

        self.helpDockWidget = qt.QDockWidget("Help", self)
        self.helpDockWidget.setObjectName("Help")
        self.helpDockWidget.setAllowedAreas(qt.Qt.LeftDockWidgetArea | qt.Qt.RightDockWidgetArea | qt.Qt.TopDockWidgetArea)
        self.helpDockWidget.setWidget(self.helpWid)
        self.addDockWidget(qt.Qt.BottomDockWidgetArea, self.helpDockWidget)         
    
    
    
    #----------------------------------------
    # Setup Control Panel Dock Widget
    #----------------------------------------
    def set_control_panel(self):
    
        # Help
        self.controlWid = qt.QWidget()
        self.controlWid.setMinimumSize(150, 150)
        self.controlWid.setMaximumSize(400, 400)

        self.controlDockWidget = qt.QDockWidget("Control Panel", self)
        self.controlDockWidget.setObjectName("ControlPanel")
        self.controlDockWidget.setAllowedAreas(qt.Qt.LeftDockWidgetArea | qt.Qt.RightDockWidgetArea | qt.Qt.TopDockWidgetArea | qt.Qt.BottomDockWidgetArea)
        self.controlDockWidget.setWidget(self.controlWid)
        self.addDockWidget(qt.Qt.BottomDockWidgetArea, self.controlDockWidget)       
    
    
    #----------------------------------------
    # Setup Observation Panel Dock Widget
    #----------------------------------------
    def set_observation_panel(self):
    
        # Help
        self.obsWid = qt.QWidget()
        self.obsWid.setMinimumSize(150, 150)
        self.obsWid.setMaximumSize(400, 400)

        self.obsDockWidget = qt.QDockWidget("Observation Panel", self)
        self.obsDockWidget.setObjectName("ObservationPanel")
        self.obsDockWidget.setAllowedAreas(qt.Qt.LeftDockWidgetArea | qt.Qt.RightDockWidgetArea | qt.Qt.TopDockWidgetArea | qt.Qt.BottomDockWidgetArea)
        self.obsDockWidget.setWidget(self.obsWid)
        self.addDockWidget(qt.Qt.BottomDockWidgetArea, self.obsDockWidget) 

        
    #----------------------------------------
    # Setup Editor Container Dock Widget
    #----------------------------------------
    def set_text_editor_container(self):
    
        # Editor
        self.textEditorContainer = qt.QTabWidget()
        self.textEditorContainer.max_ID = 0
        self.textEditorContainer.current_file_name = [None]
        self.textEditorContainer.current_extension = [None]
        self.textEditorContainer.current_path_and_fname = [None]
        self.textEditorContainer.current_path = [None]
        self.textEditorContainer.setTabsClosable(True)
        self.new()
        self.textEditorContainer.setMinimumSize(250, 250)
        
        # editorsDockWidget = qt.QDockWidget("Editors", self)
        # editorsDockWidget.setObjectName("Editors")
        # editorsDockWidget.setAllowedAreas(qt.Qt.LeftDockWidgetArea | qt.Qt.RightDockWidgetArea | qt.Qt.TopDockWidgetArea)
        # editorsDockWidget.setWidget(self.textEditorContainer)
        # self.addDockWidget(qt.Qt.RightDockWidgetArea, editorsDockWidget)
        
        self.widList.append(self.textEditorContainer)
        
               
    def new_text_editor(self, name="NewFile", type="py"):
        # central widget => Editor
        if(self.textEditorContainer.tabText(self.textEditorContainer.currentIndex())=="Select your editor type"):
            self.textEditorContainer.removeTab(self.textEditorContainer.currentIndex())
        if type=='py':
            self.editorWidget = Editor(parent=self)
            self.textEditorContainer.addTab(self.editorWidget, name)
            self.textEditorContainer.setCurrentWidget(self.editorWidget)
            self.setup_new_tab()
        elif type=='lpy':
            self.editorWidget = LPyEditor()
            self.textEditorContainer.addTab(self.editorWidget, name)
            self.textEditorContainer.setCurrentWidget(self.editorWidget)
            self.setup_new_tab()

    
    def show_select_editor(self, name="Select your editor type"):
        self.selectEditor = SelectEditor(parent=self)
        self.textEditorContainer.addTab(self.selectEditor, name)
        self.textEditorContainer.setCurrentWidget(self.selectEditor)
    
    def setup_new_tab(self):
        self.textEditorContainer.max_ID += 1
        max_ID = self.textEditorContainer.max_ID
        self.textEditorContainer.current_file_name.append(None)
        self.textEditorContainer.current_extension.append(None)
        self.textEditorContainer.current_path_and_fname.append(None)
        self.textEditorContainer.current_path.append(None)
        self.textEditorContainer.currentWidget().ID = max_ID
        self.textEditorContainer.currentWidget().setup()
        
        self.set_local_actions()
        self.set_local_top_buttons()
        self.set_local_menu_bar()
    
    #----------------------------------------
    # Setup Windows, bars, buttons
    #----------------------------------------
    def set_model_actions(self):
        # Create actions
        self.actionAddPlant = qt.QAction(self)
        self.actionPlantGrowing = qt.QAction(self)
        
        self.actionSoil = qt.QAction(self)
        self.actionSky = qt.QAction(self)
        self.actionGreenhouse = qt.QAction(self)
        
        self.actionPlay= qt.QAction(self)
        
        self.actionGlobalWorkflow= qt.QAction(self)
                
        # Set title of buttons       
        self.actionAddPlant.setText(qt.QApplication.translate("MainWindow", "New Plant", None, qt.QApplication.UnicodeUTF8))
        self.actionPlantGrowing.setText(qt.QApplication.translate("MainWindow", "Plant Growth", None, qt.QApplication.UnicodeUTF8))
        
        self.actionSoil.setText(qt.QApplication.translate("MainWindow", "Soil", None, qt.QApplication.UnicodeUTF8))
        self.actionSky.setText(qt.QApplication.translate("MainWindow", "Weather", None, qt.QApplication.UnicodeUTF8))
        self.actionGreenhouse.setText(qt.QApplication.translate("MainWindow", "Greenhouse", None, qt.QApplication.UnicodeUTF8))
            
        self.actionPlay.setText(qt.QApplication.translate("MainWindow", "Run", None, qt.QApplication.UnicodeUTF8))
        
        self.actionGlobalWorkflow.setText(qt.QApplication.translate("MainWindow", "Global Workflow", None, qt.QApplication.UnicodeUTF8))

    def set_editor_actions(self):
        # Create actions
        self.actionNew = qt.QAction(self)
        self.actionOpen = qt.QAction(self)
        self.actionSave = qt.QAction(self)
        self.actionSaveAll = qt.QAction(self)
        self.actionSaveAs = qt.QAction(self)
        self.actionClose = qt.QAction(self)

        # Set title of buttons
        self.actionNew.setText(qt.QApplication.translate("MainWindow", "New", None, qt.QApplication.UnicodeUTF8))
        self.actionOpen.setText(qt.QApplication.translate("MainWindow", "Open", None, qt.QApplication.UnicodeUTF8))
        self.actionSave.setText(qt.QApplication.translate("MainWindow", "Save", None, qt.QApplication.UnicodeUTF8))
        self.actionSaveAll.setText(qt.QApplication.translate("MainWindow", "Save All", None, qt.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(qt.QApplication.translate("MainWindow", "Save As", None, qt.QApplication.UnicodeUTF8))
        self.actionClose.setText(qt.QApplication.translate("MainWindow", "Close", None, qt.QApplication.UnicodeUTF8))
    
    
    def set_view_actions(self):
        # Create actions
        self.action11 = qt.QAction(self)
        self.action12 = qt.QAction(self)
        self.action13 = qt.QAction(self)
        self.action21 = qt.QAction(self)
        self.action22 = qt.QAction(self)
        self.action23 = qt.QAction(self)
        
        # Set title of buttons
        self.action11.setText(qt.QApplication.translate("MainWindow", "1 block", None, qt.QApplication.UnicodeUTF8))
        self.action12.setText(qt.QApplication.translate("MainWindow", "grid 1x2", None, qt.QApplication.UnicodeUTF8))
        self.action13.setText(qt.QApplication.translate("MainWindow", "grid 1x3", None, qt.QApplication.UnicodeUTF8))
        self.action21.setText(qt.QApplication.translate("MainWindow", "grid 2x1", None, qt.QApplication.UnicodeUTF8))
        self.action22.setText(qt.QApplication.translate("MainWindow", "grid 2x2", None, qt.QApplication.UnicodeUTF8))
        self.action23.setText(qt.QApplication.translate("MainWindow", "grid 2x3", None, qt.QApplication.UnicodeUTF8))

    
    def set_view_buttons(self):
        self.ViewBar = qt.QToolBar(self)
        self.ViewBar.setToolButtonStyle(qt.Qt.ToolButtonIconOnly)
        size = qt.QSize(20, 20)
        self.ViewBar.setIconSize(size)
        self.addToolBar(qt.Qt.LeftToolBarArea, self.ViewBar)    
        
        icon2_2 = qt.QIcon()
        icon2_2.addPixmap(qt.QPixmap("./resources/new/square11.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.action11.setIcon(icon2_2)
        icon2_3 = qt.QIcon()
        icon2_3.addPixmap(qt.QPixmap("./resources/new/square12.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.action12.setIcon(icon2_3)
        icon5 = qt.QIcon()
        icon5.addPixmap(qt.QPixmap("./resources/new/square13.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.action13.setIcon(icon5)
        icon6 = qt.QIcon()
        icon6.addPixmap(qt.QPixmap("./resources/new/square21.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.action21.setIcon(icon6)
        icon7 = qt.QIcon()
        icon7.addPixmap(qt.QPixmap("./resources/new/square22.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.action22.setIcon(icon7)
        icon8 = qt.QIcon()
        icon8.addPixmap(qt.QPixmap("./resources/new/square23.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.action23.setIcon(icon8)

        # connect actions to buttons
        qt.QObject.connect(self.action11, qt.SIGNAL('triggered(bool)'),self.set_central_widget11)
        qt.QObject.connect(self.action12, qt.SIGNAL('triggered(bool)'),self.set_central_widget12)
        qt.QObject.connect(self.action13, qt.SIGNAL('triggered(bool)'),self.set_central_widget13) 
        qt.QObject.connect(self.action21, qt.SIGNAL('triggered(bool)'),self.set_central_widget21)
        qt.QObject.connect(self.action22, qt.SIGNAL('triggered(bool)'),self.set_central_widget22)         
        qt.QObject.connect(self.action23, qt.SIGNAL('triggered(bool)'),self.set_central_widget23)         
        
        self.ViewBar.addAction(self.action11)
        self.ViewBar.addSeparator()
        self.ViewBar.addAction(self.action12)
        self.ViewBar.addAction(self.action13)
        self.ViewBar.addSeparator()
        self.ViewBar.addAction(self.action21)
        self.ViewBar.addAction(self.action22)
        self.ViewBar.addAction(self.action23)
    
    
    def set_model_buttons(self):
        self.ModelBar = qt.QToolBar(self)
        self.ModelBar.setToolButtonStyle(qt.Qt.ToolButtonTextUnderIcon)
        size = qt.QSize(40, 40)
        self.ModelBar.setIconSize(size)
        self.addToolBar(qt.Qt.TopToolBarArea, self.ModelBar)    
        
        icon2_2 = qt.QIcon()
        icon2_2.addPixmap(qt.QPixmap("./resources/new/plant.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionAddPlant.setIcon(icon2_2)
        icon2_3 = qt.QIcon()
        icon2_3.addPixmap(qt.QPixmap("./resources/new/grow.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionPlantGrowing.setIcon(icon2_3)
        icon5 = qt.QIcon()
        icon5.addPixmap(qt.QPixmap("./resources/new/soil.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionSoil.setIcon(icon5)
        icon6 = qt.QIcon()
        icon6.addPixmap(qt.QPixmap("./resources/new/sky.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionSky.setIcon(icon6)
        icon7 = qt.QIcon()
        icon7.addPixmap(qt.QPixmap("./resources/new/greenhouse.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionGreenhouse.setIcon(icon7)       
        icon2_4 = qt.QIcon()
        icon2_4.addPixmap(qt.QPixmap("./resources/new/play.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionPlay.setIcon(icon2_4)
        icon1 = qt.QIcon()
        icon1.addPixmap(qt.QPixmap("./resources/new/workflow.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionGlobalWorkflow.setIcon(icon1)
        
        # connect actions to buttons
        # qt.QObject.connect(self.actionAddPlant, qt.SIGNAL('triggered(bool)'),self.set_text_editor_container)
        # qt.QObject.connect(self.actionPlantGrowing, qt.SIGNAL('triggered(bool)'),self.set_text_editor_container)
        # qt.QObject.connect(self.actionSoil, qt.SIGNAL('triggered(bool)'),self.set_text_editor_container) 
        # qt.QObject.connect(self.actionSky, qt.SIGNAL('triggered(bool)'),self.set_text_editor_container)
        # qt.QObject.connect(self.actionGreenhouse, qt.SIGNAL('triggered(bool)'),self.set_text_editor_container)         
        # qt.QObject.connect(self.actionPlay, qt.SIGNAL('triggered(bool)'),self.play) 
        # qt.QObject.connect(self.actionGlobalWorkflow, qt.SIGNAL('triggered(bool)'),self.globalWorkflow) 
        
        self.ModelBar.addAction(self.actionAddPlant)
        self.ModelBar.addAction(self.actionPlantGrowing)
        self.ModelBar.addSeparator()
        self.ModelBar.addAction(self.actionSoil)
        self.ModelBar.addAction(self.actionSky)
        self.ModelBar.addAction(self.actionGreenhouse)
        self.ModelBar.addSeparator()
        self.ModelBar.addAction(self.actionPlay)
        self.ModelBar.addSeparator()
        self.ModelBar.addAction(self.actionGlobalWorkflow)
        
    
    def set_permanent_editor_buttons(self):
        # set top buttons
        self.CodeBar = qt.QToolBar(self)
        self.CodeBar.setToolButtonStyle(qt.Qt.ToolButtonTextUnderIcon)
        size = qt.QSize(30, 30)
        self.CodeBar.setIconSize(size)
        self.addToolBar(qt.Qt.RightToolBarArea, self.CodeBar)

        # Shortcuts
        self.actionNew.setShortcut(qt.QApplication.translate("MainWindow", "Ctrl+N", None, qt.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(qt.QApplication.translate("MainWindow", "Ctrl+O", None, qt.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(qt.QApplication.translate("MainWindow", "Ctrl+S", None, qt.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(qt.QApplication.translate("MainWindow", "Ctrl+W", None, qt.QApplication.UnicodeUTF8))
        icon0 = qt.QIcon()
        icon0.addPixmap(qt.QPixmap("./resources/new/new.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionNew.setIcon(icon0)
        icon1 = qt.QIcon()
        icon1.addPixmap(qt.QPixmap("./resources/new/open.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        icon2 = qt.QIcon()
        icon2.addPixmap(qt.QPixmap("./resources/new/save.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSaveAs.setIcon(icon2)
        icon2_1 = qt.QIcon()
        icon2_1.addPixmap(qt.QPixmap("./resources/filesaveall.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionSaveAll.setIcon(icon2_1)
        icon4 = qt.QIcon()
        icon4.addPixmap(qt.QPixmap("./resources/fileclose.png"), qt.QIcon.Normal, qt.QIcon.Off)
        self.actionClose.setIcon(icon4)
        

        # connect actions to buttons
        qt.QObject.connect(self.actionNew, qt.SIGNAL('triggered(bool)'),self.new)
        qt.QObject.connect(self.actionOpen, qt.SIGNAL('triggered(bool)'),self.open)
        qt.QObject.connect(self.actionSave, qt.SIGNAL('triggered(bool)'),self.save) 
        qt.QObject.connect(self.actionSaveAll, qt.SIGNAL('triggered(bool)'),self.saveall)
        qt.QObject.connect(self.actionSaveAs, qt.SIGNAL('triggered(bool)'),self.saveas)         
        qt.QObject.connect(self.actionClose, qt.SIGNAL('triggered(bool)'),self.close) 
        qt.QObject.connect(self.textEditorContainer, qt.SIGNAL('tabCloseRequested(int)'),self.autoclose)# Auto-close (red cross)

        self.CodeBar.addAction(self.actionNew)
        self.CodeBar.addAction(self.actionOpen)
        self.CodeBar.addAction(self.actionSave)
        self.CodeBar.addAction(self.actionSaveAll)
        self.CodeBar.addAction(self.actionClose)  
            
    def set_permanent_menu_bar(self):
        self.menubar = qt.QMenuBar()
        self.menubar.setGeometry(qt.QRect(0, 0, 1024, 20))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = qt.QMenu(self.menubar)
        self.menuFile.setTitle(qt.QApplication.translate("MainWindow", "File", None, qt.QApplication.UnicodeUTF8))
        self.menuFile.setObjectName("menuFile")
        
        self.menuRecents = qt.QMenu(self.menuFile)
        self.menuRecents.setTitle(qt.QApplication.translate("MainWindow", "Recents", None, qt.QApplication.UnicodeUTF8))
        self.menuRecents.setObjectName("menuRecents")
        
        self.menuImport = qt.QMenu(self.menuFile)
        self.menuImport.setTitle(qt.QApplication.translate("MainWindow", "Import", None, qt.QApplication.UnicodeUTF8))
        self.menuImport.setObjectName("menuImport")
        
        self.menuEdit = qt.QMenu(self.menubar)
        self.menuEdit.setTitle(qt.QApplication.translate("MainWindow", "Edit", None, qt.QApplication.UnicodeUTF8))
        self.menuEdit.setObjectName("menuEdit")
        
        self.menuHelp = qt.QMenu(self.menubar)
        self.menuHelp.setTitle(qt.QApplication.translate("MainWindow", "Help", None, qt.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName("menuHelp")
        
        self.menuView = qt.QMenu(self.menubar)
        self.menuView.setTitle(qt.QApplication.translate("MainWindow", "View", None, qt.QApplication.UnicodeUTF8))
        self.menuView.setObjectName("menuView")
        
        self.setMenuBar(self.menubar)
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionSaveAll)
        self.menuFile.addAction(self.actionClose)
       
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
       
    def set_status_bar(self):   
        # status bar
        self.sizeLabel = qt.QLabel()     
        self.sizeLabel.setFrameStyle(qt.QFrame.StyledPanel|qt.QFrame.Sunken)
        status = self.statusBar()     
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)     
        self.edit_status_bar(message="OALab is ready!", time=10000)   

    def edit_status_bar(self, message, time=10000):   
        self.statusBar().showMessage(message, time)     
        
    def set_local_actions(self):
        try:
            self.local_actions = self.textEditorContainer.currentWidget().set_actions()
        except:
            pass

    def set_local_top_buttons(self):
        try:
            self.remove_local_top_buttons()
        except:
            pass
        try:
            btn_local = self.textEditorContainer.currentWidget().set_buttons(self.local_actions, self)
            self.CodeBar.insertAction(self.actionClose, btn_local)    
        except:
            pass
    
    def remove_local_top_buttons(self):
        actions = self.CodeBar.actions()
        if len(actions)>=5:
            if actions[4] != self.actionClose:
                self.CodeBar.removeAction(actions[4])
        
    def set_local_menu_bar(self):
        try:
            self.remove_local_menu_bar()
        except:
            pass
        try:    
            menu_local = self.textEditorContainer.currentWidget().set_menu(self.menubar, self.local_actions)
            self.menubar.insertAction(self.menuEdit.menuAction(), menu_local)
        except:
            pass    
        
    def remove_local_menu_bar(self):
        actions= self.menubar.actions()
        if actions[1] != self.menuEdit.menuAction():
            self.menubar.removeAction(actions[1])
    
    #----------------------------------------
    # Interpreter
    #----------------------------------------
    def set_shell(self):

        # dock widget => Shell IPython
        self.interpreter = Interpreter()# interpreter
        self.shellDockWidget = qt.QDockWidget("IPython Shell", self)
        self.shellDockWidget.setObjectName("Shell")
        self.shellDockWidget.setAllowedAreas(qt.Qt.BottomDockWidgetArea | qt.Qt.TopDockWidgetArea)
        self.addDockWidget(qt.Qt.BottomDockWidgetArea, self.shellDockWidget)
        
        self.shellwdgt = ShellWidget(self.interpreter)
        self.shellwdgt.setMinimumSize(150,150)
        self.shellDockWidget.setWidget(self.shellwdgt)

    def run(self):
        code = self.textEditorContainer.currentWidget().get_text()
        interp = self.get_interpreter()
        interp.runsource(code)
        self.edit_status_bar("Code runned.")
 
    def get_interpreter(self):
        return self.interpreter
        
    #----------------------------------------
    # Actions on files
    #----------------------------------------
    def new(self):
        self.show_select_editor()
    
    def open(self, fname=None):
        try:
            try:
                old_id = self.textEditorContainer.currentWidget().ID
                fname = qt.QFileDialog.getOpenFileName(self, 'Open file', self.textEditorContainer.current_path[old_id], "Python or L-Py File (*.py *.lpy);;Any file(*.*)")
            except:
                fname = qt.QFileDialog.getOpenFileName(self, 'Open file', "/home", "Python or L-Py File (*.py *.lpy);;Any file(*.*)")
            f = open(fname, 'r')
            data = f.read()
            # TODO
            fnamesplit = os.path.split(fname)
            fnamesplitext = os.path.splitext(fname)
            f.close()
            self.new_text_editor(name=fnamesplit[1], type=fnamesplitext[1][1:])
            id = self.textEditorContainer.currentWidget().ID
            self.textEditorContainer.current_file_name[id] = fnamesplit[1]
            self.textEditorContainer.current_path_and_fname[id] = fname
            self.textEditorContainer.current_path[id] = fnamesplit[0]
            self.textEditorContainer.current_extension[id] = fnamesplitext[1][1:]
            try:
                self.textEditorContainer.currentWidget().set_text(data.decode("utf8"))#.decode("utf8")#ISO-8859-1
            except:
                self.textEditorContainer.currentWidget().set_text(data)
            self.edit_status_bar(("File '%s' opened.") %self.textEditorContainer.current_file_name[id])
            
            self.textEditorContainer.currentWidget().set_language(self.textEditorContainer.current_extension[id])
        except:
            self.edit_status_bar("No file opened...")

    
    def saveall(self):
        try:
            for _i in range(self.textEditorContainer.count()):
                self.textEditorContainer.setCurrentIndex(_i)
                self.save()
            self.edit_status_bar("All files saved")
        except:
            self.edit_status_bar("All files not saved...")
    
    def save(self):
        if(self.textEditorContainer.tabText(self.textEditorContainer.currentIndex())=="NewFile"):
            self.edit_status_bar("Save as...")
            self.saveas()
        else:
            try:
                code = self.textEditorContainer.currentWidget().get_text() # type(code) = unicode
                id = self.textEditorContainer.currentWidget().ID
                fname = self.textEditorContainer.current_path_and_fname[id]
                # Encode in utf8
                # /!\ 
                # encode("iso-8859-1","ignore") don't know what to do with "\n" and so ignore it
                # encode("utf8","ignore") works well but the read function need decode("utf8")
                code_enc = code.encode("utf8","ignore") #utf8 or iso-8859-1, ignore or replace
                
                # Write text in the file
                f = open(fname, "w")
                f.writelines(code_enc)
                f.close()
                
                fname_without_ext = self.textEditorContainer.current_file_name[id]
                self.edit_status_bar(("File '%s' saved.") %fname_without_ext )
                self.textEditorContainer.setTabText(self.textEditorContainer.currentIndex(), fname_without_ext)
            except:
                self.edit_status_bar("File not saved...") 
    
    def saveas(self):
        try:
            id = self.textEditorContainer.currentWidget().ID
            fname = qt.QFileDialog.getSaveFileName(self, 'Save file', self.textEditorContainer.current_path[id], "Python File(*.py)")
            code = self.textEditorContainer.currentWidget().get_text()
            code_enc = code.encode("utf8","ignore") 
            
            f = open(fname, "w")
            f.writelines(code_enc)
            f.close()
            
            fnamesplit = os.path.split(fname)
            fnamesplitext = os.path.splitext(fname)
            self.textEditorContainer.current_file_name[id] = fnamesplit[1]
            self.textEditorContainer.current_path_and_fname[id] = fname
            self.textEditorContainer.current_path[id] = fnamesplit[0]
            self.textEditorContainer.current_extension[id] = fnamesplitext[1][1:]
            
            fname_without_ext = self.textEditorContainer.current_file_name[id]
            self.edit_status_bar(("File '%s' saved.") % fname_without_ext)
            self.textEditorContainer.setTabText(self.textEditorContainer.currentIndex(), fname_without_ext)
        except:
            self.edit_status_bar("File not saved...")  

    def close(self):       
        try:
            id = self.textEditorContainer.currentWidget().ID
            self.textEditorContainer.removeTab(self.textEditorContainer.currentIndex())
            self.edit_status_bar(("File '%s' closed.") % self.textEditorContainer.current_file_name[id])
        except:
            try:
                self.textEditorContainer.removeTab(self.textEditorContainer.currentIndex())
                self.edit_status_bar("Selector closed.")
            except:    
                self.edit_status_bar("No file closed...")
                
        self.set_local_actions()
        self.set_local_top_buttons()
        self.set_local_menu_bar()

    def autoclose(self, n_tab):
        self.textEditorContainer.setCurrentIndex(n_tab)
        self.close()    
    
def show_splash_screen():
    """Show a small splash screen to make people wait for OpenAleaLab to startup"""
    # import metainfo
    pix = qt.QPixmap("./resources/splash.png")
    splash = qt.QSplashScreen(pix, qt.Qt.WindowStaysOnTopHint)
    splash.show()
    # message = "" + metainfo.get_copyright() +\
              # "Version : %s\n"%(metainfo.get_version(),) +\
              # "Loading modules..."
    message = "Loading..."
    splash.showMessage(message, qt.Qt.AlignCenter|qt.Qt.AlignBottom)
    # -- make sure qt really display the message before importing the modules.--
    qt.QApplication.processEvents()
    return splash

    
def main():
    app = qt.QApplication(sys.argv)
    app.setStyle('windows')
    MainW = MainWindow()
    MainW.resize(1200, 900)
    MainW.show()
    app.exec_()

    
if( __name__ == "__main__"):
    main()