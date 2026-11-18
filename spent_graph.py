import numpy as np
import matplotlib.pyplot as plt
year=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
t_spent=np.random.randint(25000,99999,12)
plt.plot(year,t_spent,marker="o",color="red",linestyle="--")
plt.title("ITPS Spent Graph")
plt.xlabel("Year")
plt.ylabel("Total Spent")
plt.savefig("ITPS Spent Graph.png")
plt.show()
