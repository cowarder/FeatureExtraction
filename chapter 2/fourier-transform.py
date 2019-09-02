import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../pics/street.jpg", 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
row, col = img.shape

# amplitude image
f_amp = np.log(np.abs(f))
# centralization
fshift_amp = np.log(np.abs(fshift))

plt.subplot(3, 3, 1)
plt.title("original")
plt.imshow(img)
plt.subplot(3, 3, 2)
plt.title("amplitude")
plt.imshow(f_amp)
plt.subplot(3, 3, 3)
plt.title("amplitude cdentralized")
plt.imshow(fshift_amp)

# phase position
f_pha = np.angle(f)
fshift_pha = np.angle(fshift)

plt.subplot(3, 3, 4)
plt.title("phase pos")
plt.imshow(f_pha)

plt.subplot(3, 3, 5)
plt.title("phase pos centralized")
plt.imshow(fshift_pha)
plt.imshow(f_pha)

s1 = np.abs(fshift)                         # amplitude
s1_angle = np.angle(fshift)                 # phase position
s1_real = s1 * np.cos(s1_angle)
s1_imag = s1 * np.sin(s1_angle)
s2 = np.zeros(img.shape, dtype=complex)
s2.real = np.array(s1_real)
s2.imag = np.array(s1_imag)

f2shift = np.fft.ifftshift(s2)
f2 = np.fft.ifft2(f2shift)
f2 = np.abs(f2)
plt.subplot(3, 3, 6)
plt.title("back")
plt.imshow(f2)


# high-pass filter
mask = np.ones(img.shape, dtype=np.uint8)
mask[row // 2 - 30:row // 2 + 30, col // 2-30:col // 2 + 30] = 0
fshift_high = fshift * mask
fshift_high = np.fft.ifftshift(fshift_high)
fshift_high = np.fft.ifft2(fshift_high)
fshift_high = np.abs(fshift_high)
plt.subplot(3, 3, 7)
plt.title("hith-pass filter")
plt.imshow(fshift_high)

# low-pass filter
mask = np.zeros(img.shape, dtype=np.uint8)
mask[row // 2 - 30:row // 2 + 30, col // 2-30:col // 2 + 30] = 1
fshift_low = fshift * mask
fshift_low = np.fft.ifftshift(fshift_low)
fshift_low = np.fft.ifft2(fshift_low)
fshift_low = np.abs(fshift_low)
plt.subplot(3, 3, 8)
plt.title("hith-pass filter")
plt.imshow(fshift_low)

plt.show()
