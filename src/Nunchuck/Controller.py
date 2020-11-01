from Nunchuck import Nunchuck

class Controller:
    def __init__(self):
        self.Nunchuck = Nunchuck.Nunchuck()
        self.Nunchuck.setdelay(0.005)

    @property
    def x(self):
        x_val = self.Nunchuck.joystick_x() * 5 - 260
        return x_val

    @property
    def y(self):
        y_val = self.Nunchuck.joystick_y()
        
        if y_val < 130:
            y_val = 130 + (y_val - 130) * (-1)
        else:
            y_val = 130 - (y_val - 130)
            
        return y_val * 4 - 260

    @property
    def z(self):
        z_button_val = self.Nunchuck.button_z()
        return z_button_val
