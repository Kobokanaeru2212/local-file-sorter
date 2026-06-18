import os
import shutil
import sys

def file_sorter_automation(target_directory):
    # Validasi jika path yang dimasukkan bukan sebuah folder resmi
    if not os.path.isdir(target_directory):
        print(f"Error: Path '{target_directory}' bukan folder yang valid.")
        return

    print(f"Memulai pemindaian otomatis pada folder: {target_directory}\n")

    # Pemetaan ekstensi file ke dalam kategori folder yang spesifik
    KATEGORI = {
        'Dokumen': ['pdf', 'docx', 'doc', 'xlsx', 'xls', 'txt', 'csv'],
        'Gambar': ['png', 'jpg', 'jpeg', 'bmp', 'gif', 'svg'],
        'Aplikasi_Instalasi': ['exe', 'msi'],
	'Lagu': ['mp3', 'wav'],
	'Vidio': ['mp4', 'mkv'],
        'Compressed_Zip': ['zip', 'rar', '7z']
    }

    try:
        semua_item = os.listdir(target_directory)
    except Exception as e:
        print(f"Error saat membaca folder: {e}")
        return

    jumlah_terpindah = 0
    nama_script_ini = os.path.basename(__file__)

    for item in semua_item:
        path_item = os.path.join(target_directory, item)
        
        # Memastikan objek adalah file dan bukan merupakan script utama
        if os.path.isfile(path_item) and item != nama_script_ini:
            nama_file, ekstensi = os.path.splitext(item)
            ekstensi = ekstensi.lower().replace('.', '')
            
            if not ekstensi:
                continue
                
            folder_nama = "Lainnya_files"
            for nama_kategori, daftar_ekstensi in KATEGORI.items():
                if ekstensi in daftar_ekstensi:
                    folder_nama = nama_kategori
                    break
            
            folder_tujuan = os.path.join(target_directory, folder_nama)
            
            if not os.path.exists(folder_tujuan):
                print(f"Membuat folder kategori: {folder_nama}/")
                os.makedirs(folder_tujuan)
            
            path_tujuan_file = os.path.join(folder_tujuan, item)
            
            try:
                shutil.move(path_item, path_tujuan_file)
                print(f"Sukses memindahkan: {item} -> {folder_nama}/")
                jumlah_terpindah += 1
            except Exception as e:
                print(f"Gagal memindahkan {item}: {e}")

    print(f"\nProses selesai. Total {jumlah_terpindah} file berhasil dikelompokkan.")

if __name__ == "__main__":
    # Logika CLI: Jika user memasukkan path folder saat menjalankan script
    # Contoh: python main.py "D:\Folder_Berantakan"
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Jika tidak ada argumen, otomatis merapikan folder tempat script aktif berada
        target = os.getcwd()
    
    file_sorter_automation(target)