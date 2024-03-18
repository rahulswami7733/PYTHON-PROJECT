# Q> develop pythone prog for pir chart
import matplotlib.pyplot as plt 
x=[45,12,35,56,78]
y=["JAVA","Python","c","PHP","JS"]
C=[0,0,0.1,0,0]
plt.pie(x,labels=y,radius=1.5,explode=C)
plt.legend(loc=9)
plt.show()  
 
