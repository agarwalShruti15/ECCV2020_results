import numpy as np
import seaborn as sns
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import pandas as pd
import os
import pickle

from matplotlib import rc
rc('text', usetex=False)


def load_obj(fldr, name ):
    if not os.path.exists(os.path.join(fldr, name + '.pkl')):
        return None
    with open(os.path.join(fldr, name + '.pkl'), 'rb') as f:
        return pickle.load(f)


def plot_one_curve(X, in_leg, ax, thres, bins):
    
    # plot the distrutions with bins
    X[X<bins[0]] = bins[0]

    # distplot
    sns.distplot(X, bins=bins, hist=False, kde=True, 
                 norm_hist=True, label=in_leg, ax=ax, kde_kws={'lw': 3})
    
    # write the name of the datset on top of the mode
    n, _ = np.histogram(X, bins=bins, density=True)    
    ax.plot([thres, thres], [0, np.max(n)], 'r--')
    

def plot_one_row(data_fldr, in_feat_nm, xlbl, thres):
    
    data = {}
    
    # params
    bins = np.linspace(0.3, 1, 50)
    fontdict={'family': 'serif', 'weight': 'normal', 'size': 20}
    
    _, ax = plt.subplots(figsize=(10, 4))
    data = load_obj(data_fldr, in_feat_nm)

    # plot
    for k in data.keys():
        plot_one_curve(data[k], k, ax, thres, bins)
    
    ax.grid(b=True)
    
    # xticks
    ax.set_xlim([bins[0], bins[-1]])
    xtcks = np.linspace(bins[0], bins[-1], 20)
    ax.set_xticks(xtcks)
    ax.set_xticklabels([f'{x:.2f}' for x in xtcks], rotation=90, fontdict=fontdict)
    ax.set_xlabel(xlbl, fontdict=fontdict)
    
    # yticks
    ax.set_yticklabels('', fontdict=fontdict)
    
    legend = ax.legend(loc='upper center', 
                       bbox_to_anchor=(0.5, 1.2), ncol=6, 
                       fancybox=True, shadow=False, fontsize=14)
    plt.tight_layout(pad=0.1, h_pad=None, w_pad=None, rect=None)
    plt.savefig(f'figures/{in_feat_nm}.eps')
    plt.show()

plot_one_row('data', 'vgg_face_id_sim', 'VGG similarity with Target', thres=0.86)
plot_one_row('data', 'vgg_behav_id_sim', 'VGG similarity with Source', thres=0.86)
plot_one_row('data', 'fab_face_id_sim', 'FAb-Net-metric similarity with Target', thres=0.76)
plot_one_row('data', 'fab_behav_id_sim', 'FAb-Net-metric similarity with Source', thres=0.76)


