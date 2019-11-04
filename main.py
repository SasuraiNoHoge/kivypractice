from random import sample
from string import ascii_lowercase

#アプリケーションの生成に必要
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

#フォントの読み込みに必要
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

# デフォルトに使用するフォントを変更する
resource_add_path('./fonts')
#resource_add_path('/storage/emulated/0/kivy/calc/fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する

kv = """
<Row@BoxLayout>:
    #canvasへの色つけ
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            size: self.size
            pos: self.pos
    value: ''
    Label:
        text: root.value #それぞれのボタンを押して反映される値

#テストクラスで呼べるようにする
<Test>:
    canvas:
        Color:
            rgba: 0.3, 0.3, 0.3, 1
        Rectangle:
            size: self.size
            pos: self.pos
    rv: rv  #左辺のrvはPythonファイル上としてrvを呼び出すために使う，右辺のrvはkvファイルのRecycleViewのidとして使う
    orientation: 'vertical'
    GridLayout:
        cols: 3
        rows: 2
        size_hint_y: None
        height: dp(108)
        padding: dp(8)
        spacing: dp(16)
        Button:
            text: '人口リスト'
            on_press: root.populate()   #人口リストをクリックするとPythonファイルのpopulate関数が呼ばれる
        Button:
            text: '昇順に変更'
            on_press: root.sort()
        Button:
            text: 'リストの全消去'
            on_press: root.clear()
        BoxLayout:
            spacing: dp(8)
            Button:
                text: 'データの挿入'
                on_press: root.insert(new_item_input.text)  #new_item_inputはTextInputのidで宣言
            TextInput:
                id: new_item_input
                size_hint_x: 0.6
                hint_text: '文字を入力'  #薄文字で表示
                padding: dp(10), dp(10), 0, 0
        BoxLayout:
            spacing: dp(8)
            Button:
                text: 'データの更新'
                on_press: root.update(update_item_input.text) #update_item_inputはTextInputのidで宣言
            TextInput:
                id: update_item_input
                size_hint_x: 0.6
                hint_text: '先頭を変更'
                padding: dp(10), dp(10), 0, 0
        Button:
            text: '1データ削除'
            on_press: root.remove()

    RecycleView:
        id: rv  #Canvasを反映させるため
        scroll_type: ['bars', 'content']
        scroll_wheel_distance: dp(114)
        bar_width: dp(10)
        viewclass: 'Row'
        RecycleBoxLayout:
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing: dp(2)
"""

#kvファイルをPythonファイルに直書き
#Builder.load_string(kv)

#BoxLayoutクラスを継承
class Test(BoxLayout):

    #ランダムな文字列を50個生成
    def populate(self):
        # ディクショナリ型で，各要素の値valueに対してforループ処理
        #小文字で6文字のランダム文字列を生成
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]

    def sort(self):
        #self.rv.dataにリストの情報が含まれる
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        #先頭にデータを挿入
        self.rv.data.insert(0, {'value': value or 'default value'})

    def update(self, value):
        if self.rv.data:
            #データの更新
            self.rv.data[0]['value'] = value or 'default new value'
            #データの更新を反映
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            #先頭のデータをポップ
            self.rv.data.pop(0)

#Appクラスを継承
class TestApp(App):
    #最初に呼ばれる
    #def build(self):
        #self.title = '国会図書館検索'
        #Testクラスを実行
        #return Test()
        #現状だとtest.kvファイルは無視される
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)

        self.title = '国会図書館検索'
    pass

if __name__ == '__main__':
    #TestAppクラスを実行
    TestApp().run()
