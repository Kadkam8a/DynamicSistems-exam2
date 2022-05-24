# DynamicSistems-exam2
## Square fractal
Second exam of Dynamic Sistems at National University of Mexico (2022-2)

Karime Ochoa Jacinto karime8aj@gmail.com

GNU/GPL License 3.0
## Introduction
This code consists on a fractal made by squares. The main of them has edge= 1 and each iteration edge= edge/3
## Metodology
- First we create a function (named square) to draw the squares by given a starting point, create a list of the vertices and joining them with lines..
- Then the function fractal receives a square, the number of iterations, the edge size, a plotting space and a flag to draw the following squares (avoinding the plotting of squares to the inside of the fractal). This function provides new starting points that call the fractal function and this in turn, calls the square function. 
- Finally we create the plot.
## Execution requeriments
- [Python 3](https://www.python.org/).
## Example of output
![Fractal](https://github.com/Kadkam8a/DynamicSistems-exam2/blob/main/examen.png)
## References
- [Fractal made in class](https://github.com/giccunam/dynamicsystems2022/blob/main/itztli/fractales/fractal-recursive.py)
