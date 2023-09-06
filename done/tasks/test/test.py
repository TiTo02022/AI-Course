import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Student_Performance.csv")

sns.violinplot(data=df,x="Performance Index",y="Sample Question Papers Practiced")
plt.xlabel("Performance Index")
plt.ylabel("Sample Question Papers Practiced")
plt.show()