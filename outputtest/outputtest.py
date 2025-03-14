import tkinter as tk
import RPi.GPIO as GPIO

# Cấu hình GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

# Biến trạng thái GPIO
gpio_state = False  # False = Tắt, True = Bật

# Hàm xử lý khi nhấn nút
def toggle_gpio():
    global gpio_state
    gpio_state = not gpio_state  # Đảo trạng thái
    GPIO.output(17, GPIO.HIGH if gpio_state else GPIO.LOW)
    
    # Cập nhật text của nút
    btn.config(text="TẮT" if gpio_state else "BẬT", bg="red" if gpio_state else "green")

# Tạo giao diện
root = tk.Tk()
root.title("Điều khiển GPIO 17")
root.geometry("200x100")

btn = tk.Button(root, text="BẬT", bg="green", fg="white", font=("Arial", 14), command=toggle_gpio)
btn.pack(expand=True, fill="both", padx=10, pady=10)

# Chạy giao diện
root.mainloop()

# Dọn dẹp GPIO khi đóng chương trình
GPIO.cleanup()
