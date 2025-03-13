import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Khởi tạo dữ liệu
x_data = np.array([])
y_data = np.array([])
t = 0
z = 0 
T = 1 / 850  # Chu kỳ của sóng sin 850Hz
last_t_z = 0  # Lưu thời điểm `z` được tăng lần cuối

# Tạo figure và axes
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Thiết lập trục X và Y
ax.set_ylim(-1.2, 1.2)
ax.set_xlim(0, 0.01)  # Ban đầu hiển thị 10ms
ax.set_xlabel("Thời gian (s)")
ax.set_ylabel("Biên độ")
ax.set_title("Sóng Sin động")
ax.grid()

# Hàm cập nhật đồ thị mỗi 10ms
def update(frame):
    global x_data, y_data, t, z, last_t_z

    # Tạo 100 điểm mới mỗi lần cập nhật
    new_x = np.linspace(t, t + 0.001, 100)

    if z % 32 > 4:
        new_y = np.sin(2 * np.pi * 850 * new_x)  # Sóng sin 850Hz
    else:
        new_y = np.zeros_like(new_x)

    # Kiểm tra nếu `t` vượt qua một chu kỳ mới
    if t - last_t_z >= T:
        z += 1  
        last_t_z += T  # Cập nhật bằng cách cộng thêm T, tránh mất chu kỳ


    # Thêm dữ liệu mới vào mảng
    x_data = np.append(x_data, new_x)
    y_data = np.append(y_data, new_y)
    t += 0.001  # Tăng biến thời gian

    # Cập nhật đường vẽ
    line.set_data(x_data, y_data)

    # Mở rộng trục X khi dữ liệu tăng (hiển thị 10ms gần nhất)
    ax.set_xlim(t - 0.01, t)

    return line,

# Tạo animation (cập nhật mỗi 10ms)
ani = animation.FuncAnimation(fig, update, interval=10)

# Hiển thị đồ thị
plt.show()
