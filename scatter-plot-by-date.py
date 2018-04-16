#!/usr/bin/env python3

import sys

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

help_msg = f"""Usage:

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

    title   = sys.argv[1]
    csv_fnm = sys.argv[2]


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



#=================================
main()
