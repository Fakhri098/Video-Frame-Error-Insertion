#Konversi Video.mp4 ke frame dengan dimensi 255x255


import cv2

def convert_video_to_frames(video_path, output_dir, frame_width, frame_height):
  """Konversi video ke frame dengan dimensi yang ditentukan.

  Args:
    video_path: Path ke video yang akan dikonversi.
    output_dir: Path ke direktori tempat frame akan disimpan.
    frame_width: Lebar dimensi frame.
    frame_height: Tinggi dimensi frame.

  Returns:
    None.
  """

  # Buka video
  video = cv2.VideoCapture(video_path)

  # Cek apakah video dapat dibuka
  if not video.isOpened():
    raise FileNotFoundError("Video tidak dapat ditemukan.")

  # Dapatkan frame rate video
  frame_rate = video.get(cv2.CAP_PROP_FPS)

  # Looping untuk membaca setiap frame
  while True:
    # Baca frame
    ret, frame = video.read()

    # Jika frame tidak dapat dibaca, keluar dari looping
    if not ret:
      break

    # Ubah dimensi frame
    frame = cv2.resize(frame, (frame_width, frame_height))

    # Simpan frame
    filename = f"{output_dir}/frame_{int(video.get(cv2.CAP_PROP_POS_FRAMES))}.jpg"
    cv2.imwrite(filename, frame)

  # Tutup video
  video.release()

if __name__ == "__main__":
  # Input
  video_path = "D:\LAPORAN TA\Pemrograman/contoh.mp4"
  output_dir = "D:\LAPORAN TA\Pemrograman/hasil cobaan 256"
  frame_width = 256
  frame_height = 256

  # Konversi video
  convert_video_to_frames(video_path, output_dir, frame_width, frame_height)

  # Tampilkan pesan
  print("Konversi video berhasil.")
