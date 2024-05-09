import kivy

from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        img= AsyncImage(source='https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1024px-Instagram_logo_2022.svg.png',
        size_hint=(1, .5),
        pos_hint={'center_x':.5, 'center_y':.5})
        return img


if __name__=='__main__':
    app= MainApp()
    app.run()      