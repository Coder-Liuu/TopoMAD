import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei']

y = np.array([ 0.1593, 0.1532, 0.1594, 0.1644, 0.1635, 0.1686, 0.1626, 0.1641, 0.1604, 0.1659, 0.1676, 0.1657, 0.1711, 0.1801, 0.1769, 0.2029, 0.2052, 0.2138, 0.2197, 0.2481, 0.2518, 0.2765, 0.2963, 0.2997, 0.3272, 0.3320, 0.3395, 0.3561, 0.3984, 0.3780, 0.3834, 0.3993, 0.3968, 0.4009, 0.3975, 0.4017, 0.4006, 0.4240, 0.4428, 0.4325, 0.4326, 0.4063, 0.3997, 0.3838, 0.4144, 0.4348, 0.4314, 0.4427, 0.4591, 0.4176 ])

x = range(1,len(y)+1)

plt.plot(x,y,label="个人实现")
plt.title("MDB dataset")
plt.ylabel("AP Score")
plt.xlabel("Epoch")
plt.axhline(0.415,linestyle='--',color='r',label="论文效果")
plt.legend()
plt.tight_layout()
plt.savefig("effect-MDB.png",dpi=150)
