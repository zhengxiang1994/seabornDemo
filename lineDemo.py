# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# a simple example of line plot
# cussum(): return the cumulative sum of the elements along the given axis
# df = pd.DataFrame(dict(time=np.arange(500), value=np.random.randn(500).cumsum()))
# # print(df)
# g = sns.relplot(x="time", y="value", kind="line", data=df)
# g.fig.autofmt_xdate()
# plt.show()

# the above example is equal to the following example:
# # cussum(): return the cumulative sum of the elements along the given axis
# df = pd.DataFrame(dict(time=np.arange(500), value=np.random.randn(500).cumsum()))
# # print(df)
# sns.lineplot(x="time", y="value", data=df)
# plt.show()

# Because lineplot() assumes that you are most often trying to draw y as a function of x,
# the default behavior is to sort the data by the x values before plotting. However, this can be disabled
# df = pd.DataFrame(np.random.randn(500, 2).cumsum(0), columns=["x", "y"])
# print(df)
# sns.relplot(x="x", y="y", sort=False, kind="line", data=df)
# plt.show()

# If the more complex datasets have multiple measurements for the same value x variable, The default behavior in
# seaborn is to aggregate the multiple measurements at each x value by plotting the mean and the 95% confidence
# interval around the mean
# fmri = sns.load_dataset("fmri")
# sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)
# plt.show()

# disable the confidence interval, it is calculated by bootstrapping which is time-consuming
# fmri = sns.load_dataset("fmri")
# sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri)
# plt.show()

# using the standard deviation instead of a confidence interval
# fmri = sns.load_dataset("fmri")
# sns.relplot(x="timepoint", y="signal", ci="sd", kind="line", data=fmri)
# plt.show()

# To turn off aggregation altogether, set the estimator parameter to None.
# This might produce a strange effect when the data have multiple observations at each point.
# fmri = sns.load_dataset("fmri")
# sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri)
# plt.show()

# adding a hue semantic
# fmri = sns.load_dataset("fmri")
# sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri)
# plt.show()

# add a style semantic
# fmri = sns.load_dataset("fmri")
# sns.relplot(x="timepoint", y="signal", hue="region", style="event", kind="line", data=fmri)
# plt.show()

# using markers instead of dashes
# fmri = sns.load_dataset("fmri")
# sns.relplot(x="timepoint", y="signal", hue="region", style="event", dashes=False, markers=True, kind="line", data=fmri)
# plt.show()

# The default colormap and handling of the legend in lineplot() also depends on whether the hue semantic is
# categorical or numeric
dots = sns.load_dataset("dots").query("align == 'dots'")
# print(dots)
sns.relplot(x="time", y="firing_rate", hue="coherence", style="choice", kind="line", data=dots)
plt.show()


