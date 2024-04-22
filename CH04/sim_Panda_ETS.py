from spatialmath import SE3, SE2

import numpy as np
import math
import roboticstoolbox as rtb
import matplotlib.animation as animation
import matplotlib.pyplot as plt

from roboticstoolbox.backends.PyPlot import PyPlot

panda_ETS = rtb.models.ETS.Panda()
qt = rtb.jtraj(panda_ETS.qz, panda_ETS.qr, 50) # 두 configuration을 시작과 끝으로 하는 trajectory를 생성합니다.
panda_ETS.plot(qt.q, block = False)