# -*- coding: utf-8 -*-
# the examples of scatter
import seaborn as sns
import matplotlib.pyplot as plt

# there are 5 styles, i.e., darkgrid, whitegrid, dark, white, ticks
sns.set(style="darkgrid")
# load datasets
tips = sns.load_dataset("tips")
print(tips)

# a simplest example of scatter
# sns.relplot(x="total_bill", y="tip", data=tips)

# the above example is equal to the following example:
# sns.scatterplot(x="total_bill", y="tip", data=tips)

# While the points are plotted in two dimensions, another dimension can be added to the plot by coloring the points
# according to a third variable. In seaborn, this is referred to as using a “hue semantic”, because the color of the
# point gains meaning
# sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips)

# To emphasize the difference between the classes, and to improve accessibility, you can use a different marker style
# for each class
# sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips)

# It’s also possible to represent four variables by changing the hue and style of each point independently.
# But this should be done carefully, because the eye is much less sensitive to shape than to color
# here, using color to represent hue and using shape to represent style
# sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips)

# In the examples above, the hue semantic was categorical, so the default qualitative palette was applied.
# If the hue semantic is numeric (specifically, if it can be cast to float), the default coloring switches
# to a sequential palette
# sns.relplot(x="total_bill", y="tip", hue="size", data=tips)

# you can also customize the color palette
# sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips)

# you can also customize the size of each point
# sns.relplot(x="total_bill", y="tip", size="size", data=tips)

# Unlike with matplotlib.pyplot.scatter(), the literal value of the variable is not used to pick the area of the point.
# Instead, the range of values in data units is normalized into a range in area units. This range can be customized
sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips)

plt.show()

