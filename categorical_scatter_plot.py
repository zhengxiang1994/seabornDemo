# -*- coding: utf-8 -*-
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)
tips = sns.load_dataset("tips")
# print(tips)

# a simple example
# sns.catplot(x="day", y="total_bill", data=tips)

# The jitter parameter controls the magnitude of jitter or disables it altogether
# sns.catplot(x="day", y="total_bill", jitter=False, data=tips)

# another scatter approach that prevents the points from overlapping named "swarmplot"
# sns.catplot(x="day", y="total_bill", kind="swarm", data=tips)

# similarly, it can add another dimension to a categorical plot by using a hue semantic
# sns.catplot(x="day", y="total_bill", hue="sex", kind="swarm", data=tips)

# the order of categories can be controlled by "order" parameter
# sns.catplot(x="smoker", y="tip", order=["Yes", "No"], kind="swarm", data=tips)

# change the categorical variable to the vertical axis
sns.catplot(x="total_bill", y="day", hue="time", kind="swarm", data=tips)

plt.show()


