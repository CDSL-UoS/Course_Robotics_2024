from spatialmath import SE3, SE2

import numpy as np
import math
import roboticstoolbox as rtb
import matplotlib.animation as animation
import matplotlib.pyplot as plt

from roboticstoolbox.backends.PyPlot import PyPlot

p560 = rtb.models.DH.Puma560()
qt = rtb.jtraj(p560.qz, p560.qr, 50)
p560.plot(qt.q, block = False)


