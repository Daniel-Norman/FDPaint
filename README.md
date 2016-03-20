# FDPaint
FPGA Paint Tool

## Introduction
FDPaint is a basic version of a classic desktop paint program, such as MS Paint, built in Verilog to run on the Nexys3 FPGA. This program was a collaboration with [Fay Wu](https://github.com/mfaywu) for our final project submission for UCLA's CS M152A course.

Sample Drawing:

![](https://raw.githubusercontent.com/Daniel-Norman/FDPaint/master/sample.jpg)

Here we see a drawing demonstrating the use of the pencil tool (large green lines for grass, thin blue lines for clouds) and the stamp tool (hearts, penguins, etc.). The current pencil color is shown on either side of the drawing region.

## Features
* VGA Driver
 * Uses standard 640x480 60Hz resolution
 * Displays the 240x240 drawing region in the center, stretched 2x to display as 480x480
 * Displays a cursor that changes style depending on the current tool
* Joystick Movement
 * Controls the cursor
 * Two speeds in each direction
* Tools
 * Pencil tool (3 sizes, 256 colors)
 * Eraser tool (3 sizes)
 * Stamp tool (7 available 30x30 stamps, transparency included)
 * Reset tool

## Technical Information
The drawing board is saved in a 240x240 byte dual-port RAM, while the stamps are stored in 30x30 byte ROMs. We were unable to use a 1-to-1 480x480 byte map for the drawing region due to space limitations on our board of around 65KB.

The user changes tools using the buttons on the board, with UP/DOWN for tool selection and LEFT/RIGHT for settings within a tool. Tools are used by pressing (and holding, if desired) the left button on the joystick.

Users are able to choose between 256 colors when using the pencil tool by moving the 8 switches provided on the board to pick an 8-bit color.

Nexys3 Board:

![](https://raw.githubusercontent.com/Daniel-Norman/FDPaint/master/board.jpg)

