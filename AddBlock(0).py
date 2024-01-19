import cv2

def add_black_blocks(frame, x1, y1, w1, h1, x2, y2, w2, h2):
  """
  Menambahkan 2 blok hitam pada frame.

  Args:
    frame: Frame yang akan ditambahkan blok hitam.
    x1: Posisi x blok hitam pertama.
    y1: Posisi y blok hitam pertama.
    w1: Lebar blok hitam pertama.
    h1: Tinggi blok hitam pertama.
    x2: Posisi x blok hitam kedua.
    y2: Posisi y blok hitam kedua.
    w2: Lebar blok hitam kedua.
    h2: Tinggi blok hitam kedua.

  Returns:
    Frame dengan 2 blok hitam.
  """

  black = (0, 0, 0)
  frame[y1:y1+h1, x1:x1+w1] = black
  frame[y2:y2+h2, x2:x2+w2] = black
  return frame


def main():
  # Membaca gambar
  img = cv2.imread("D:\LAPORAN TA\Pemrograman/sz_256x256.jpg")

  # Menambahkan blok hitam kesatu
  x1 = 125
  y1 = 100
  w1 = 10
  h1 = 10
  #Menambahkan blok hitam kedua
  x2 = 125
  y2 = 150
  w2 = 10
  h2 = 10
  img = add_black_blocks(img, x1, y1, w1, h1, x2, y2, w2, h2)

  # Menyimpan gambar
  cv2.imwrite("D:/LAPORAN TA/Pemrograman/256x256/hasil add/hasil_add.jpg", img)
  #cv2.imshow("Gambar", img)
  #cv2.waitKey(0)
  #cv2.destroyAllWindows() 

if __name__ == "__main__":
  main()
