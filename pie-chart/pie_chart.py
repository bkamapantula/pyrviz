"""
plots production quality Fig 2 - NSR submission
"""
import pandas as pd
import matplotlib.gridspec as gridspec
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import sys
import os

pd.options.display.mpl_style = 'default'


def draw_pie_chart():

    pie_data = [270, 151, 149, 68, 
                56, 46, 7, 4, 
                37, 19, 4, 2]

    pie_labels = [
        "Human (270)", "Mouse (151)", "Zebrafish (149)", "Maize (68)", 
        "Rat (56)", "Arabidopsis (46)", "Drosophila (7)", "Dog (4)", 
        "Rice (37)", "Chlamydomonas (19)", "Caenorhabditis (4)", "Solanum (2)"
    ]

    data = {
        'labels': pd.Series(pie_labels, index=pie_labels),
        'pie_data': pd.Series(pie_data, index=pie_labels)
    }
    df = pd.DataFrame(data)

    fig = plt.figure(figsize=[8, 8])
    ax = fig.add_subplot(111)

    cmap = plt.cm.Blues_r
    colors = cmap(np.linspace(0., 1., len(pie_data)))

    # http://nxn.se/post/46440196846/making-nicer-looking-pie-charts-with-matplotlib
    large = pie_data[:len(pie_data) / 2]
    small = pie_data[len(pie_data) / 2:]

    reordered = large[::2] + small[::2] + large[1::2] + small[1::2]

    pie_wedges = ax.pie(reordered, labels=pie_labels, colors=colors, autopct='%.2f', labeldistance=1.05, pctdistance=0.8)

    # moves figure little to the right
    plot_pos = ax.get_position()
    ax.set_position([plot_pos.x0-0.03, plot_pos.y0, plot_pos.width, plot_pos.height])

    for wedge in pie_wedges[0]:
        wedge.set_edgecolor('white')

    # wedge labels - %s
    for wedge_id, wedge_label in enumerate(pie_wedges[2]):
        wedge_label.set_size('14')
        label_data = wedge_label.get_text()
        if float(label_data) > 33.00:
            wedge_label.set_color('white')
        elif float(label_data) < 1.0:
            if pie_data[wedge_id] == 68:
                wedge_label.set_position((-1.0, -0.5))
            elif pie_data[wedge_id] == 46:
                wedge_label.set_position((-0.85, -0.9))
            elif pie_data[wedge_id] == 2:
                wedge_label.set_position((1.53, -0.0061))
            elif pie_data[wedge_id] == 19:
                wedge_label.set_position((1.3, -0.25))
        wedge_label.set_text(label_data+"%")

    plt.title('Species distribution')
    plt.savefig('pie_chart_python.pdf', format='pdf', dpi=300)

draw_pie_chart()

