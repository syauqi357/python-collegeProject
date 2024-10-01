import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk
from image_processing import process_image, export_image

# Fungsi untuk menampilkan gambar di dalam Tkinter
def show_image_in_tkinter(image, window):
    # Convert image dari format OpenCV (BGR) ke PIL (RGB)
    try:
        image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        print("Gambar berhasil dikonversi ke RGB")
        image_pil = Image.fromarray(image_rgb)
        print("Gambar berhasil dikonversi ke format PIL")
        image_tk = ImageTk.PhotoImage(image=image_pil)
        print("Gambar berhasil dikonversi ke format ImageTk")
    
        # Buat label di Tkinter untuk menampilkan gambar
        label = tk.Label(window, image=image_tk)
        label.image = image_tk  # Simpan referensi gambar agar tidak terhapus oleh garbage collector
        label.pack()
        print("Label berhasil ditambahkan ke jendela Tkinter")
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan gambar: {e}")

# Fungsi untuk mengekspor gambar
def export_button_pressed():
    if processed_image is not None:
        export_image(processed_image)
    else:
        print("Belum ada gambar yang diproses untuk diekspor.")

# Fungsi untuk memproses gambar dan menampilkan di Tkinter
def process_and_show_image():
    global processed_image
    processed_image = process_image('anyaForger.jpeg')
    
    if processed_image is not None:
        show_image_in_tkinter(processed_image, window)

# Setup Tkinter window
window = tk.Tk()
window.title("Image Display with Tkinter")
window.geometry("600x600")

# Tombol untuk memproses gambar
process_button = tk.Button(window, text="Proses Gambar", command=process_and_show_image)
process_button.pack(pady=10)

# Tombol untuk mengekspor gambar
export_button = tk.Button(window, text="Ekspor Gambar", command=export_button_pressed)
export_button.pack(pady=10)

# Inisialisasi variabel global untuk menyimpan gambar yang telah diolah
processed_image = None

# Jalankan Tkinter mainloop
window.mainloop()
