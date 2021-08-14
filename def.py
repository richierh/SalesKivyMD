
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivymd.icon_definitions import md_icons
from kivymd.toast import toast


keyword = None

Builder.load_string('''
#:import MDDropdownMenu kivymd.uix.menu.MDDropdownMenu
<MyMDTextFieldRound@MDTextFieldRound>
    size_hint_x: None
    normal_color: [0.3, .3, .3, 1]
    active_color: [0.5,0.5,0.5,1]
    pos_hint: {"center_x": .5}
    
<IconBtn>:
	icon_: ''
	MDIconButton:
		icon: root.icon_
		on_release: root.ToastIconName(root.icon_)
		
<IconHub>
	orientation: "vertical"
	
	MDToolbar:
		title: app.title
		pos_hint: {"top": 1}
		md_bg_color: app.theme_cls.primary_color
		background_palette: "Primary"
		elevation: 10
		right_action_items:
			[["dots-vertical", lambda x: MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)]]
            
		
	RecycleView:
		id: iconbtn
		size_hint: 1, .9
		pos_hint: {'center_x':0.5,'center_y':0.45}
		bar_color: app.theme_cls.primary_color
		viewclass: 'IconBtn'
		RecycleGridLayout:
			cols: 5
			default_size: None, None
			default_size_hint: 1, None
			size_hint_y: None
			height: self.minimum_height
			
	MDFloatingActionButton:
		id: floatbtn
		pos_hint: {'center_x':0.85,'center_y':0.1}
		icon: "eye"
		opposite_colors: True
		elevation_normal: 8
		md_bg_color: app.theme_cls.primary_color
		on_release: root.Show()
<PopSearch>:
	title: 'Search'
	title_color: app.theme_cls.primary_color
	title_align: 'center'
	pos_hint: {'center_y': .7}
	title_size: 30
	auto_dismiss: False
	size_hint: 0.8,0.4
	background: 'white.png'
	separator_color: 0,0,0,1
	BoxLayout:
		orientation: 'vertical'
		Label:
		MyMDTextFieldRound:
			id: request
			icon_type: "without"
			hint_text: "Search"
		Label:
		MDRaisedButton:
			text: 'Search'
			pos_hint: {'center_x': .5, 'center_y': .15}
			elevation_normal: 4
			opposite_colors: True
			on_release:  root.Search()
<AboutMe@Popup>
	title: 'About'
	title_color: 0,0,0,1
	title_align: 'center'
	title_size: dp(20)
	auto_dismiss: False
	size_hint: 1,1
	background: 'white.png'
	separator_color: 1,1,1,1
	FloatLayout:
		BoxLayout:
			orientation: 'vertical'
			size_hint: .8, .8
			pos_hint: {'center_x': .5, 'center_y': .58}
			canvas.before:
				Color:
					rgba: app.theme_cls.primary_color
				RoundedRectangle:
					size: self.size
					pos: self.pos
					radius: dp(10), dp(10), dp(10), dp(10)
			Label:
				text: 'Made by'
				font_size: dp(20)
			Label:
				text: '[b]Oluwafemi David'
				font_size: dp(25)
				markup: True
		MDRaisedButton:
			text: 'Done'
			pos_hint: {'center_x': .5, 'center_y': .1}
			elevation_normal: 2
			opposite_colors: True
			on_release:  root.dismiss()
''')

class IconBtn(BoxLayout):
	
	def ToastIconName(self, icon_):
		toast(icon_)
		
class IconHub(FloatLayout):
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.search_bool = 0
		Clock.schedule_interval(self.search, 1/10)
		
	def clear(self):
		self.ids.iconbtn.data = []
		
	def Show(self):
		if self.search_bool:
			Factory.PopSearch().open()
		else:
			self.ids.iconbtn.data = [{'icon_':icon_} for icon_ in md_icons.keys()]
			self.ids.floatbtn.icon = 'magnify'
			self.search_bool = 1
			
	def search(self, _):
		global keyword
		if keyword:
			data = []
			for icon_ in md_icons.keys():
				if keyword in icon_:
					data.append({'icon_':icon_})
			self.ids.iconbtn.data = data
			keyword = None
			
class PopSearch(Popup):
	
	def Search(self):
		global keyword
		keyword = self.ids.request.text
		self.dismiss()
		
class IconHubApp(MDApp):
    
    def __init__(self, **kwargs):
        self.title = "IconHub"
        # self.theme_cls.primary_palette = "Green"
        super().__init__(**kwargs)

    def build(self):
    	self.menu_items = [{"viewclass": "MDMenuItem",
    	"text": "About",
    	"callback": self.callback_for_menu_items,}]
    	self.root = Factory.IconHub()
    	
    def callback_for_menu_items(self, *args):
    	Factory.AboutMe().open()

if __name__ == "__main__":
    IconHubApp().run()
