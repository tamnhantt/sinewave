import tkinter as tk
import RPi.GPIO as GPIO
from Sinwave.sinwave import sinwave  # Corrected import statement

# Cấu hình GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# Khởi tạo PWM trên chân GPIO 17 với tần số 1000Hz
pwm = GPIO.PWM(17, 1000)  # 1000Hz
pwm.start(0)  # Bắt đầu với duty cycle = 0% (TẮT)

# Biến trạng thái GPIO
gpio_state = False  # False = Tắt, True = 50% Duty Cycle

# Hàm xử lý khi nhấn nút
def toggle_gpio():
    global gpio_state
    gpio_state = not gpio_state  # Đảo trạng thái
    
    # Lấy dữ liệu từ hàm sinwave
    new_y = sinwave()  # Giả sử sinwave trả về giá trị từ 0 đến 1
    
    pwm.ChangeDutyCycle((100 * new_y) if gpio_state else 0)  # Thay đổi duty cycle dựa trên giá trị sinwave
    
    # Cập nhật text và màu sắc của nút
    btn.config(text="TẮT" if gpio_state else "BẬT", bg="red" if gpio_state else "green")

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Điều khiển PWM GPIO 17")
root.geometry("200x100")

btn = tk.Button(root, text="BẬT", bg="green", fg="white", font=("Arial", 14), command=toggle_gpio)
btn.pack(expand=True, fill="both", padx=10, pady=10)

# Chạy giao diện
root.mainloop()

# Dừng PWM và dọn dẹp GPIO khi đóng chương trình
pwm.stop()
GPIO.cleanup()
