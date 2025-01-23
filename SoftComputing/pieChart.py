import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'Javascript']
sizes = [50,25,15,10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

plt.pie(sizes, labels = labels, colors=colors, autopct = '%1.1f%%', startangle=140)

plt.title('Programming Language Popularity')

plt.show()