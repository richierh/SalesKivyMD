from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout



class Table(MDDataTable):
    column_data =[("Column 1", dp(30)),("Column 2", dp(30)),("Column 3", dp(30)),("Column 4", dp(30)),("Column 5", dp(30)),("Column 6", dp(30)),]
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = 0.9,0.6
        # self.row_data=[("1", "2", "3", "4", "5", "6"),
        #         ("1", "2", "3", "4", "5", "6"),
        #     ]
        self.open()

    # def on_start(self):
    #     self.open()

class Box(BoxLayout):
    pass


kv = Builder.load_string("""
Box:
    Button:
        text:"hello"
    MDDataTable:
        size_hint : .9,.6
        column_data :[("Column 1", dp(30)),("Column 2", dp(30)),("Column 3", dp(30)),("Column 4", dp(30)),("Column 5", dp(30)),("Column 6", dp(30)),]

""")

class Example(MDApp):
    def build(self):
        # self.data_tables = MDDataTable(
        #     size_hint=(0.9, 0.6),
        #     column_data=[
        #         ("Column 1", dp(30)),
        #         ("Column 2", dp(30)),
        #         ("Column 3", dp(30)),
        #         ("Column 4", dp(30)),
        #         ("Column 5", dp(30)),
        #         ("Column 6", dp(30)),
        #     ],
        #     row_data=[
        #         # The number of elements must match the length
        #         # of the `column_data` list.
        #         ("1", "2", "3", "4", "5", "6"),
        #         ("1", "2", "3", "4", "5", "6"),
        #     ],
        # )
        # self.table = Table()
        # self.data_tables.open()
        kv
        return kv

    # def on_start(self):
    #     self.data_tables.open()


Example().run()