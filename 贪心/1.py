import matplotlib.pyplot as plt
from scipy.optimize import leastsq
x = [[6.2],[9.9],[14.4],[18.9],[23.4],[28.6],[32.7]]
y = [[0.043],[0.084],[0.121],[0.169],[0.21],[0.253],[0.295]]
plt.plot(x,y)
plt.show()
from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(x,y)
print(clf.coef_,clf.intercept_)