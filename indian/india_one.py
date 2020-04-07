import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('state_wise.csv', index_col=None)
print(df.columns)

df1 = df.nlargest(15,'Confirmed')
ax = df1.plot(x='State', y=['Recovered','Confirmed','Deaths'], kind="bar")
ax.set_xlabel('States')
ax.title('Comparing Recovered, Confirmed and Death cases of different states of India')
ax.legend()
plt.show()

ax = df1.plot(x='State', y=['Confirmed'], kind="bar")
ax.set_xlabel('States')
ax.title('Confirmed cases of India')
ax.set_ylabel('Confirmed Cases')
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
plt.show()
