import numpy as np
arr = np.array([2,3,4,6,7,8,9,12,13,16,17,23,25,27,34,37,201])

#print(arr)
q1 = np.percentile(arr, 25) # 25th percentile
q3 = np.percentile(arr, 50) # 50th percentile (median)
IQR = q3 - q1
print(f'IQR IS : {IQR}')


uf = q3 + 1.5 * IQR
lf = q1 - 1.5 * IQR
print(f'Upper Fence : {uf}')
print(f'Lower Fence : {lf}')


l=[]
for i in arr:
    if i >= lf and i <= uf:
        l.append(i)

arr2 = np.array(l)
print(f'Outliers are : {arr2}')
print(arr)

#figure 1
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(arr2)
plt.savefig('boxplot.png', dpi=300, bbox_inches='tight')
plt.show()










