# f1-tyre-pit-strategy
## Overview
(This project was made in early 2023)
This project provides a tool for optimizing tyre strategies in a racing simulation. It evaluates different tyre combinations and determines the best pit stop strategy to minimize total lap time over a given number of laps. The tool also plots the lap times for different strategies to visually compare their effectiveness.

## Features

- **Tyre Class**: Represents tyres with different compounds, ages, and base lap times.
- **Strategy Calculation**: Computes the optimal pit stop strategy for two tyre compounds.
- **Plotting**: Visualizes lap times for different tyre strategies.
- **Optimal Strategy Selection**: Identifies the best tyre combination based on total race time.

## Tyre Compounds

The project supports three types of tyres:
- **Hard ('H')**: (base + 2.5) × (1.001)^age
- **Medium ('M')**: (base + 1.6) × (1.003)^age
- **Soft ('S')**: base × (1.005)^age

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/SharmaKabir/f1-tyre-pit-strategy.git
   cd f1-tyre-pit-strategy
   ```


2. **Install Dependencies**
    ```bash
    pip install numpy matplotlib
    ```

3. **Run the Script**
    ```bash
    python3 f1.py
    ```

 When prompted, enter the number of laps you want to simulate. The script will then calculate and display the optimal tyre strategy and its total time.
 The script will print the best tyre combination, the total race time in minutes and seconds and a plot comparing the lap times for the selected tyre strategies.


## Screenshots
 ![alt text]( https://github.com/SharmaKabir/f1-tyre-pit-strategy/blob/main/screenshot-1.png?raw=true)
 ![alt text]( https://github.com/SharmaKabir/f1-tyre-pit-strategy/blob/main/screenshot-2.png?raw=true)


