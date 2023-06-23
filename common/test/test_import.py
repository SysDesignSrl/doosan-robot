#!/usr/bin/env python
import os
import sys
import unittest
# ROS
import rospkg
import rosunit

rospack = rospkg.RosPack()
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(os.path.join(rospack.get_path('common'), 'imp')))     # get import path : DSR_ROBOT.py


ROBOT_ID = 'dsr01'
ROBOT_MODEL = 'm1013'

class TestImport(unittest.TestCase):

    def test_import(self):
        pass


if __name__ == '__main__':

    # Doosan Robotics Library
    import DR_init
    DR_init.__dsr__id = ROBOT_ID
    DR_init.__dsr__model = ROBOT_MODEL
    from DSR_ROBOT import *

    PKG='common'
    rosunit.unitrun(PKG, 'test_import', TestImport, sys.argv)