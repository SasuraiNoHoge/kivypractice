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
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)

        self.title = '国会図書館検索'
    pass

if __name__ == '__main__':
    #TestAppクラスを実行
    TestApp().run()
