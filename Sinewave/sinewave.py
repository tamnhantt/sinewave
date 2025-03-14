import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Khởi tạo dữ liệu
x_data = np.array([])
y_data = np.array([])
t = 0
z = 0 
T = 1 / 850  # Chu kỳ của sóng sin 850Hz

# Tạo figure và axes
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_ylim(-1.2, 1.2)
ax.set_xlim(0, 0.01)  
ax.set_xlabel("Thời gian (s)")
ax.set_ylabel("Biên độ")
ax.set_title("Sóng Sin động")
ax.grid()

def update(frame):
    global x_data, y_data, t, z

    new_x = np.linspace(t, t + 0.001, 100)
    
    if z % 32 < 4:
        new_y = np.sin(2 * np.pi * 850 * new_x)  # Sóng sin 850Hz
    else:
        new_y = np.zeros_like(new_x)

    # Kiểm tra nếu sóng đạt đỉnh (từ âm sang dương)
    if np.all(new_y==0):
        z += 1
        

    # Thêm dữ liệu mới
    x_data = np.append(x_data, new_x)
    y_data = np.append(y_data, new_y)
    t += 0.001  

    line.set_data(x_data, y_data)

    ax.set_xlim(t - 0.01, t)

    return line,

# Chạy animation
ani = animation.FuncAnimation(fig, update, interval=10)
plt.show()
