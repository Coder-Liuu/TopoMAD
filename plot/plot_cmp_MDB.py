import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['Microsoft YaHei']

#柱高信息
Y1 = [0.275,0.325]
Y2 = [0.2747,0.3253]
X = np.arange(len(Y1))

bar_width = 0.25
tick_label = ['LOF','OCSVM']

#显示每个柱的具体高度
for x,y in zip(X,Y1):
    plt.text(x+0.005,y+0.005,'%.3f' %y, ha='center',va='bottom')

for x,y1 in zip(X,Y2):
    plt.text(x+0.24,y1+0.005,'%.3f' %y1, ha='center',va='bottom')
 
#绘制柱状图    
plt.ylim(0,0.4)
plt.bar(X, Y1, bar_width, align="center", color="red", label="论文效果")
plt.bar(X+bar_width, Y2, bar_width, color="yellow", align="center",label="复现效果")

plt.title("MDB dataset")
plt.ylabel("AP Score")
plt.xlabel("Epoch")

plt.xticks(X+bar_width/2, tick_label)
plt.tight_layout()

plt.savefig("effect-cmp-MDB.png",dpi=150)
