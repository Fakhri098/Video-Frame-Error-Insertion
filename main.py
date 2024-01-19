import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooser
from kivy.core.image import Image
from kivy.uix.popup import Popup


class VideoToImageApp(App):

    def build(self):
        root = BoxLayout(orientation="vertical")

        # Label untuk menampilkan judul aplikasi
        label = Label(text="Konverter Video ke Gambar")
        root.add_widget(label)

        # Tombol untuk memilih file video
        file_chooser = FileChooser(filters=["*.mp4"])
        button_pilih = Button(text="Pilih File", on_release=file_chooser.open)
        root.add_widget(button_pilih)

        # Tombol untuk memulai konversi
        button_konversi = Button(text="Konversi", disabled=True)
        button_konversi.bind(on_release=self.konversi)
        root.add_widget(button_konversi)

        # Tombol untuk menambahkan blok hitam
        button_black = Button(text="Tambah Blok Hitam", disabled=True)
        button_black.bind(on_release=self.tambah_blok_hitam)
        root.add_widget(button_black)

        return root

    def konversi(self, instance):
        # Mengambil file video yang dipilih
        file_video = file_chooser.selection[0]

        # Membaca video
        video = Image.open(file_video)

        # Mengubah ukuran video
        video = video.resize((256, 256))

        # Menyimpan gambar
        file_gambar = file_video.replace(".mp4", ".jpg")
        video.save(file_gambar)

        # Menampilkan pesan keberhasilan
        popup = Popup(title="Berhasil", content=Label(text="Gambar telah berhasil disimpan ke file {}.".format(file_gambar)))
        popup.open()

        # Mengaktifkan kembali tombol konversi
        button_konversi.disabled = False
        button_black.disabled = False

    def tambah_blok_hitam(self, instance):
        # Mengambil gambar yang dipilih
        file_gambar = file_chooser.selection[0]

        # Membaca gambar
        gambar = Image.open(file_gambar)

        # Menambah blok hitam
        for i in range(0, gambar.width, 100):
            gambar.paste((0, 0, 0, 0), (i, 0, i + 100, gambar.height))

        # Menyimpan gambar
        file_gambar_baru = file_gambar.replace(".jpg", "_black.jpg")
        gambar.save(file_gambar_baru)

        # Menampilkan pesan keberhasilan
        popup = Popup(title="Berhasil", content=Label(text="Gambar telah berhasil disimpan ke file {}.".format(file_gambar_baru)))
        popup.open()


if __name__ == "__main__":
    VideoToImageApp().run()
