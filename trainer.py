# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    trainerv1.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mfiguera <mfiguera@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/10/31 18:18:11 by mfiguera          #+#    #+#              #
#    Updated: 2018/10/31 21:33:57 by mfiguera         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import json
import numpy as np
import pandas
import matplotlib.pyplot as plt


def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

data = pandas.read_csv("data1.csv")
X = data.values[:,:1]
m = len(X)
y = data.values[:,1:2]
alpha = 0.1
theta = np.array([[7000], [0.0]])
A = theta
nice = np.transpose(data.values)
plt.plot(nice[0], nice[1], "rx")
mu = np.mean(X)
std = np.std(X)

X = (X - mu) / std
print(mu)
print(std)
print(X)
X = np.hstack((np.ones((m, 1)),X))
#theta = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.transpose(X)), y)
for i in range(200):
    theta -= (alpha / m) * np.dot(np.transpose(X), (np.dot(X, theta) - y))
print(theta)

#plt.plot(A)
abline(theta[1][0], theta[0][0])
#plt.axis([ -1000, 250000, -1000, 10000])
plt.show()
out = [theta.tolist(), mu, std]
with open('theta.json', 'w') as f:
    json.dump(out, f)