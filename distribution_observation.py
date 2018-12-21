# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt

# set the style and load the dataset
sns.set(style="ticks", color_codes=True)
tips = sns.load_dataset("tips")

# a simple example of boxplot
sns.catplot(x="day", y="total_bill", kind="box", data=tips)

plt.show()
