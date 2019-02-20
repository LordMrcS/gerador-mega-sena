import wx
import wx.xrc
import random


###########################################################################
## Interface WX
###########################################################################

class janela ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Gerador MEGA-SENA", pos = wx.DefaultPosition, size = wx.Size( 386,244 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.aposta_tamanho = wx.StaticText( self, wx.ID_ANY, u"Tamanho da aposta", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.aposta_tamanho.Wrap( -1 )

		bSizer2.Add( self.aposta_tamanho, 0, wx.ALL|wx.EXPAND, 5 )

		tamanhoChoices = [ u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
		self.tamanho = wx.ComboBox( self, wx.ID_ANY, u"-1", wx.DefaultPosition, wx.DefaultSize, tamanhoChoices, 0 )
		self.tamanho.SetSelection( 0 )
		self.tamanho.SetMinSize( wx.Size( 130,-1 ) )

		bSizer2.Add( self.tamanho, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableRow( 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.gerar = wx.Button( self, wx.ID_ANY, u"Gerar", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.gerar.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.gerar.SetToolTip( u"Clique para gerar os números." )

		fgSizer1.Add( self.gerar, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )

		self.limpa = wx.Button( self, wx.ID_ANY, u"Limpar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.limpa, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )


		gSizer1.Add( fgSizer1, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )


		bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )

		geradosChoices = [ u"Clique em Gerar" ]
		self.gerados = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, geradosChoices, 0 )
		self.gerados.SetMinSize( wx.Size( -1,100 ) )

		bSizer1.Add( self.gerados, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.menu = wx.MenuBar( 0 )
		self.arquivo = wx.Menu()
		self.ola = wx.MenuItem( self.arquivo, wx.ID_ANY, u"Olá", wx.EmptyString, wx.ITEM_NORMAL )
		self.arquivo.Append( self.ola )

		self.arquivo.AppendSeparator()

		self.sair = wx.MenuItem( self.arquivo, wx.ID_ANY, u"Sair", u"Sai do app.", wx.ITEM_NORMAL )
		self.arquivo.Append( self.sair )

		self.menu.Append( self.arquivo, u"Arquivo" )

		self.ajuda = wx.Menu()
		self.sobre = wx.MenuItem( self.ajuda, wx.ID_ANY, u"Sobre", u"Informações sobre o app.", wx.ITEM_NORMAL )
		self.ajuda.Append( self.sobre )

		self.menu.Append( self.ajuda, u"Ajuda" )

		self.SetMenuBar( self.menu )


		self.Centre( wx.BOTH )

		# Connect Events
		self.gerar.Bind( wx.EVT_BUTTON, self.Tgerar )
		self.limpa.Bind( wx.EVT_BUTTON, self.Tlimpa )
		self.Bind( wx.EVT_MENU, self.Tola, id = self.ola.GetId() )
		self.Bind( wx.EVT_MENU, self.Tclose, id = self.sair.GetId() )
		self.Bind( wx.EVT_MENU, self.Tsobre, id = self.sobre.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Tgerar( self, event ):
		event.Skip()

	def Tlimpa( self, event ):
		event.Skip()

	def Tola( self, event ):
		event.Skip()

	def Tclose( self, event ):
		event.Skip()

	def Tsobre( self, event ):
		event.Skip()

###########################################################################
## Subclasse e Código base
###########################################################################
		
class Teste():
    def testeplus(tam):
        tam=int(tam)
        vetor = []
        x=0
        while(x<tam):
            num = random.randint(1,99)
            if (not vetor.count(num)):
                vetor.append(num)
                x=x+1
        return vetor

class janelaup(janela):
    def Tgerar( self, event ):
        numero = []
        numero.append(str(Teste.testeplus(self.tamanho.GetValue())))
        self.gerados.InsertItems(numero,0)
        self.Refresh()

    def Tlimpa( self, event ):
        ##pegar contagem, fazer o for e selecionar tudo pra em seguida deletar
        ni=self.gerados.GetCount()-1
        while(ni>-1):
            self.gerados.SetSelection(ni)
            self.gerados.Delete(self.gerados.GetSelection())
            ni=ni-1

    def Tola( self, event ):
        wx.MessageBox("??? olá ???","Msg",wx.ICON_ERROR)

    def Tsobre( self, event ):
        wx.MessageBox("Desenvolvido por Marcos Aurélio","Sobre",wx.ICON_INFORMATION)

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App("file.log")
    frm = janelaup(None)
    frm.Show()

    ##frm.ErroMsg(frm, "teste erro")
    app.MainLoop()
