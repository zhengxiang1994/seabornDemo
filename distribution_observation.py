# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt

# set the style and load the dataset
sns.set(style="ticks", color_codes=True)
tips = sns.load_dataset("tips")
diamonds = sns.load_dataset("diamonds")

# a simple example of boxplot
# sns.catplot(x="day", y="total_bill", kind="box", data=tips)

# add a hue semantic
# sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips)

# add additional column ("weekend") to provide more information
# tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
# sns.catplot(x="day", y="total_bill", hue="weekend", kind="box", dodge=False, data=tips)

# a related function boxenplot that can provide more information
# sns.catplot(x="color", y="price", kind="boxen", data=diamonds.sort_values("color"))

# a simple example of violinplot
sns.catplot(x="total_bill", y="day", kind="violin", data=tips)

plt.show()
