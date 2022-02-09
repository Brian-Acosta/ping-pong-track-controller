# Single Color RGB565 Blob Tracking Example
#
# This example shows off single color RGB565 tracking using the OpenMV Cam.

import sensor, image, time, math, pyb

# Controller Tuning:
k_p = 10
k_d = 0.4
k_i = 0


# CONSTANT
# Color Tracking Threshold  Tuned for the ping pong ball
orange_thresh = (60, 100, -20, 40, 40, 90) # (L_min, L_max, a_min, a_max, b_min, b_max)
flip_img = True
i2c_addr=0x42

class PID_controller():
    def __init__(self, kp=k_p, ki=0, kd=0, setpoint=0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.sp = setpoint
        self.err = 0
        self.err_sum = 0
        self.u = 0
        self.t = time.ticks_ms()

    def adjust_setpoint(self, sp):
        self.sp = sp

    def calc_control(self, x):
        # timing
        t_new = time.ticks_ms()
        dt = (t_new - self.t) / 1e3

        # calculate error
        err_new = self.sp - x
        d_err = (err_new - self.err)/dt
        self.err_sum += dt*err_new

        # calculate input
        u = self.kp * err_new + self.ki * self.err_sum + self.kd * d_err

        # update internal variables
        self.err = err_new
        self.t = t_new
        self.u = u

        return u

def find_blob(color_thresh):
    img = sensor.snapshot()
    blobs = img.find_blobs([color_thresh], pixels_threshold=100,
                        area_threshold=100, merge=True)
    if blobs:
        return img, blobs[0]
    else:
        return img, None


def draw_blob(img, blob):
    if blob is not None:
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())


def calc_x(blob):
    l = sensor.width()/2
    x = (l - blob.cx()) / l
    return x if not flip_img else -x

def setup_camera():
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.HQVGA)
    sensor.skip_frames(time = 2000)
    sensor.set_auto_gain(False) # must be turned off for color tracking
    sensor.set_auto_whitebal(False) # must be turned off for color tracking


def main():
    setup_camera()
    s = pyb.Servo(1)
    controller = PID_controller(kp=k_p, kd=k_d, ki=k_i, setpoint=0)
    print("x, u")
    while True:
        img, blob = find_blob(orange_thresh)
        if not blob:
            s.angle(0)
        else:
            draw_blob(img, blob)
            x = calc_x(blob)
            u = controller.calc_control(x)
            s.angle(u)
            print(f"{x}, {u}")

main()
