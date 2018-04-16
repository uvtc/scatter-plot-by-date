#!/usr/bin/env python3

import sys, csv
import matplotlib.pyplot as plt
import matplotlib as mpl
import time, datetime

version = '1.0'

license_info = f"""scatter-plot-by-date v{version}: creates a scatter plot from a csv data file.
Copyright (C) 2018 John Gabriele

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

help_msg = """Usage:

    scatter-plot-by-date.py 'My Plot Title' input.csv
    scatter-plot-by-date.py --license
    scatter-plot-by-date.py --version

This program comes with ABSOLUTELY NO WARRANTY.  This is free
software, and you are welcome to redistribute it under certain
conditions; run it with the `--license` option for details.

Exiting.
"""


def main():
    handle_args()

    plot_title = sys.argv[1]
    csv_fnm = sys.argv[2]
    rows = read_csv(csv_fnm)
    x_axis_label = rows[0][0]
    y_axis_label = rows[0][1]
    rows = rows[1:]

    xs = [dt_date(row[0]) for row in rows]
    ys = [float(row[1]) for row in rows]

    # print("Dates:")
    # for d in xs:
    #     print(d)
    # print("Vals:", ys)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, color='tab:blue', marker="o")
    ax.set(xlabel=x_axis_label, ylabel=y_axis_label, title=plot_title)
    ax.grid()
    fig.autofmt_xdate()

    plt.show()


# `d` is a string like '2018-04-16'. Returns a datetime.date.
def dt_date(d):
    tt = time.strptime(d, '%Y-%m-%d')
    et = time.mktime(tt)
    return datetime.date.fromtimestamp(et)


def handle_args():
    if len(sys.argv) == 1:
        print(help_msg)
        sys.exit()
    elif len(sys.argv) == 2:
        if sys.argv[1] == '--license':
            print(license_info)
            sys.exit()
        elif sys.argv[1] == '--version':
            print(f"scatter-plot-by-date, v{version}")
            sys.exit()
        else:
            print(help_msg)
            sys.exit()
    elif len(sys.argv) != 3:
        print(help_msg)
        sys.exit()


def read_csv(fnm):
    rows = []
    with open(fnm, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows


#=================================
main()
