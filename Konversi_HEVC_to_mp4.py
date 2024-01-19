import subprocess

def convert_mov_to_mp4(input_file, output_file):
    try:
        # Gunakan subprocess untuk memanggil ffmpeg
        subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-c:a', 'aac', '-strict', 'experimental', output_file], check=True)
        print(f"Konversi berhasil: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: Gagal melakukan konversi - {e}")

if __name__ == "__main__":
    # Ganti input_file dengan path video MOV yang ingin Anda konversi
    input_file = "D:\LAPORAN TA\Pemrograman/contoh2.MOV"

    # Ganti output_file dengan path dan nama file untuk video hasil konversi MP4
    output_file = "D:\LAPORAN TA\Pemrograman\Hasil Konversi ke mp4/hasil.mp4"

    # Panggil fungsi convert_mov_to_mp4
    convert_mov_to_mp4(input_file, output_file)
