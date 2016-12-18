#!/usr/bin/env python
#coding=utf-8
import wx, os, subprocess
 
class MainInterfaz(wx.Frame):
    """ Una clase personalizada de frame """
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title='Youtube-dl catch', size=(800,600))
         
        self.CreateStatusBar() 
         
        # Creamos el submenú Archivo
        menuArchivo = wx.Menu() 
        menuActualizar = menuArchivo.Append(103, "&Actualizar"," Abrir comando")
        menuArchivo.AppendSeparator()
        #menuGuardar = menuArchivo.Append(wx.ID_SAVE,"&Guardar","Abrir Guardar")
        menuAyuda = menuArchivo.Append(wx.ID_HELP,"&Ayuda","Abrir Ayuda")
        menuAcercaDe = menuArchivo.Append(wx.ID_ABOUT, "A&cerca de"," Informción del programa")
        menuSalir = menuArchivo.Append(wx.ID_EXIT,"&Salir"," Terminar el programa")
      
        labelUrl = '''Ingrese URL'''
        wx.StaticText(self, -1, labelUrl, (300,10))
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(self)
        labelUrl = '''Escoja el formato en que desea descargar el video'''
        wx.StaticText(self, -1, labelUrl, (300,70))
        button = wx.Button(self, label="Descargar")
        button2 = wx.Button(self,-1,"Cancelar", (150,100))
        self.cb1 = wx.CheckBox(self, -1, 'mp3', (250, 110))
        self.cb2 = wx.CheckBox(self, -1, 'mp4-[360x640]', (330, 110))
        self.cb3 = wx.CheckBox(self, -1, 'web-[720x1280]', (470, 110))
        self.cb4 = wx.CheckBox(self, -1, 'mp4-[720x1280]', (630, 110))
        self.cb1.SetValue(False)
        self.cb2.SetValue(False)
        self.cb3.SetValue(False)
        self.cb4.SetValue(False)
        
        button.Bind(wx.EVT_BUTTON, self.onDescargar)
        button2.Bind(wx.EVT_BUTTON, self.onCancelar)
        self.Bind(wx.EVT_CHECKBOX,self.onCheckBox)

        sizer.Add(self.text, 0, wx.ALL|wx.EXPAND, 30)
        sizer.Add(button, 0, wx.ALL, 5)

        self.SetSizer(sizer)
        # Creamos la barra del menú
        menuBar = wx.MenuBar()
        menuBar.Append(menuArchivo,"&Archivo")       
        self.SetMenuBar(menuBar) 
         
        # Creamos los eventos
        self.Bind(wx.EVT_MENU, self.OnUpdate, menuActualizar)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAcercaDe)
        self.Bind(wx.EVT_MENU, self.OnExit, menuSalir)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuAyuda)
        
        self.Show(True)
     
    # Definimos los métodos de los eventos
    def onCancelar(self, event):
		comando = ['youtube-dl','--skip-download']
		con = subprocess.check_output(comando)
		print con
		print 'cancelar'
		
    def onDescargar(self, event):
		con =  subprocess.check_output(comando)
		print con
		
		
    def OnAbout(self,event):
        # Creamos una ventana de diálogo con un botón de ok. wx.OK es una ID estàndard de wxWidgets.
        dlg = wx.MessageDialog( self, "Gestor de descargas multimedia desarrollado con python lenguaje"+
         "\nde scripting utlizando wxPython que es un kit de herramientas"+
         "\nmultiplataforma para la creación de Aplicaciones de escritorio GUI", "Acerca de el gestor de descargas", wx.OK)
        dlg.ShowModal() # La mostramos
        dlg.Destroy() # Finalmente la destruimos

    def OnExit(self,event):
        self.Close(True)  # Cerramos el frame
     
    def OnHelp(self,event):
		# Creamos una ventana de diálogo con un botón de ok. wx.OK es una ID estàndard de wxWidgets.
		dlg = wx.MessageDialog( self, "Para su correcto uso siga los siguientes pasos."+
		"\n1. Copie la URL del video que desea descargar"+
		"\n2. Ingrese la URL a caja de texto"+
		"\n3. Elija un formato en el que dese descargar el video"+
		"\n4. Precione el boton descargar"+
		"\nY listo su descarga a iniciado", 
		"Acerca de un Editor simple", wx.OK)
		dlg.ShowModal() # La mostramos
		dlg.Destroy() # Finalmente la destruimos
		
    def OnUpdate(self,event):
		
        comando = ['youtube-dl','-U']
        con = subprocess.check_output(comando)
        print con
        
    def onCheckBox(self, event):
		global comando
		if self.cb1.GetValue():
			s = self.text.GetValue()
			comando = ['youtube-dl','--extract-audio','--audio-format','mp3',s]
			print "mp3"
		else:
			print ""
			
		if self.cb2.GetValue():
			s = self.text.GetValue()
			comando = ['youtube-dl','--format','18',s]
			print "mp4-[360x640]"
		else:
			print ""
			
		if self.cb3.GetValue():
			s = self.text.GetValue()
			comando = ['youtube-dl','--format','45',s]
			print "webm-[720x1280]"
		else:
			print ""
			
		if self.cb4.GetValue():
			s = self.text.GetValue()
			comando = ['youtube-dl','--format','22',s]
			print "mp4-[720x1280]"
		else:
			print ""
	

				
app = wx.App(False)
frame = MainInterfaz()
app.MainLoop()
