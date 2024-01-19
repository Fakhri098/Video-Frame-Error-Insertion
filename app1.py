from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import cv2
import os

class VideoConverter(BoxLayout):
    def __init__(self, **kwargs):
        super(VideoConverter, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Convert Video to Image', font_size=24)
        self.add_widget(self.label)

        self.browse_button = Button(text='Browse', size_hint=(1, 0.5))
        self.browse_button.bind(on_press=self.browse_file)
        self.add_widget(self.browse_button)

        self.convert_button = Button(text='Convert', size_hint=(1, 0.5))
        self.convert_button.bind(on_press=self.convert_video)
        self.add_widget(self.convert_button)

    def browse_file(self, instance):
        self.file_path = filedialog.askopenfilename()

    def convert_video(self, instance):
        cap = cv2.VideoCapture(self.file_path)
        frame_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imwrite('frame%d.jpg' % frame_count, gray_frame)
                frame_count += 1
            else:
                break
        cap.release()
        cv2.destroyAllWindows()

class VideoConverterApp(App):
    def build(self):
        return VideoConverter()

if __name__ == '__main__':
    VideoConverterApp().run()