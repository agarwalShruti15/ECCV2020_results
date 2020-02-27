from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt

rc('text', usetex=True)


poi_names = ['Barack Obama', 'Bete O Rourke', 'Bernie Sanders', 
             'Cory Booker', 'Donald J. Trump', 'Elizabeth Warren', 
             'Hillary Clinton', 'Joe Biden', 'Kamala Haris', 'Pete Buttigieg', 
             'Obama Imperson.', 'Sanders Imperson.', 'Trump Imperson.', 
             'Warren Imperson.', 'Clinton Imperson.', 'Biden Imperson.']

durs = [750.1, 132.1, 248.0, 180.0, 364.5, 131.5, 140.3, 129.0, 104.6, 115.6, 
       9.5, 6.6, 11.3, 2.4, 10.4, 2.2]

log_dur = np.linspace(np.log10(np.min(durs)), np.log10(np.max(durs)), 10)

#poi_df = pd.DataFrame(data=poi_names, columns=['names'])
#poi_df['time(minutes)'] = durs.copy()

plt.rcdefaults()
fig, ax = plt.subplots(figsize=(5, 4))

y_pos = np.arange(len(poi_names))
ax.barh(y_pos, np.log10(durs), align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels([fr'{x}' for x in poi_names])
ax.set_xlabel(r'time in minutes (logscale)')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xticks(log_dur)
ax.set_xticklabels([fr'${np.power(10, x):.0f}$' for x in log_dur], rotation=90)
ax.grid(b=True, axis='x')
plt.tight_layout(pad=0, h_pad=None, w_pad=None, rect=None)
plt.savefig(f'figures/dataset.eps')
plt.show()
