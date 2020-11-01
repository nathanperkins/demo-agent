#!/usr/bin/env python3

import rospy
import pygame
import time

class Joystick(object):
    def __init__(self, dev="/dev/input/js0", index=0):
        pygame.init()
        pygame.joystick.init()

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        rospy.logwarn("Joystick initialized: {}".format(self.joystick.get_name()))

        self.axis_states = [0.0 for _ in range(self.joystick.get_numaxes())]
        self.button_states = [0 for _ in range(self.joystick.get_numbuttons())]

    def poll(self):
        pygame.event.get()

        # update joystick
        for i in range(self.joystick.get_numaxes()):
            state = self.joystick.get_axis(i)
            if self.axis_states[i] != state:
                rospy.logwarn("Change axis {}, now {}".format(self.axis_names[i], state))
                self.axis_states[i] = state

        # update buttons
        for i in range(self.joystick.get_numbuttons()):
            state = self.joystick.get_button(i)
            if self.button_states[i] != state:
                rospy.logwarn("Changed button {}, now {}".format(self.button_names[i], state))
                self.button_states[i] = state

        return self.axis_states, self.button_states

class PS4Joystick(Joystick):
    def __init__(self, *args, **kwargs):
        self.axis_names = [
            "left-x",
            "left-y",
            "left-trig",
            "right-x",
            "right-y",
            "right-trig",
        ]

        self.button_names = [
            "cross",
            "circle",
            "triangle",
            "square",
            "L1",
            "R1",
            "L2",
            "R2",
            "share",
            "options",
            "PS",
            "L3",
            "R3",
        ]

        super(PS4Joystick, self).__init__(*args, **kwargs)
                
if __name__ == '__main__':
    js = PS4Joystick()
    while True:
        js.poll()

