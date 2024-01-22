from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img=AsyncImage(source='https://assets.stickpng.com/images/585968bf4f6ae202fedf2879.png',
                       size_hint=(1,.5),
                       pos_hint = {'center_x':.5,'center_y':.5})
        return img


if __name__ =='__main__':
    app = MainApp()
    app.run()
