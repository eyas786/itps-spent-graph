# itps-spent-graph
# ITPS Spent Graph Generator

A lightweight Python script that simulates monthly expenditure data over a 12-month period and plots a line graph using **NumPy** and **Matplotlib**. The generated visualization is displayed on screen and automatically saved as a PNG image.

## Features
* **Random Data Simulation:** Uses `numpy` to generate 12 random spending values between `25,000` and `99,999`.
* **Custom Line Styling:** Plots monthly trends with circular markers (`o`), a red color theme, and a dashed line (`--`).
* **Auto-Export:** Saves the final chart directly to the project directory as `ITPS Spent Graph.png`.

## Prerequisites
Make sure you have Python installed along with the required libraries:

```bash
pip install numpy matplotlib
```

## Usage
1. Clone this repository or download the script.
2. Run the Python file from your terminal:

```bash
python your_script_name.py
```

3. View the interactive plot window and check your folder for the exported `ITPS Spent Graph.png` file.

## Code Overview
* **`year`**: A list containing the 12 months (`jan` to `dec`) mapped to the X-axis.
* **`t_spent`**: An array of 12 random integers representing monthly totals mapped to the Y-axis.
* **`plt.savefig()`**: Exports the rendered figure before displaying it with `plt.show()`.
