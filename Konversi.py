import cv2

def video_to_frames(video_path, output_path):
    # Buka video
    cap = cv2.VideoCapture(video_path)

    # Periksa apakah video berhasil dibuka
    if not cap.isOpened():
        print("Error: Gagal membuka video.")
        return

    # Perulangan untuk membaca setiap frame dari video
    frame_count = 0
    while True:
        # Baca frame
        ret, frame = cap.read()

        # Periksa apakah berhasil membaca frame
        if not ret:
            break

        # Simpan frame ke file gambar
        frame_name = f"{output_path}/frame_{frame_count}.jpg"
        cv2.imwrite(frame_name, frame)

        # Tampilkan nomor frame yang sedang diproses
        print(f"Frame {frame_count} berhasil disimpan.")

        # Tingkatkan nomor frame
        frame_count += 1

    # Tutup video
    cap.release()

if __name__ == "__main__":
    # Ganti path_video dengan path video yang ingin Anda konversi
    path_video = "D:\LAPORAN TA\Pemrograman/contoh.mp4"
    
    # Ganti path_output dengan direktori tempat Anda ingin menyimpan frame-frame hasil konversi
    path_output = "D:\LAPORAN TA\Pemrograman/coba"
    frame_width = 255
    frame_height = 255

    # Panggil fungsi video_to_frames
    video_to_frames(path_video, path_output, frame_width, frame_height)

    # Tampilkan pesan
    print("Konversi video berhasil.")
