#!/bin/bash

# Run cmatrix command for 3 seconds
cmatrix -s 3 &

# Wait for 3 seconds
sleep 3

# Stop cmatrix command
echo -e "q" | pkill cmatrix

# Clear terminal
clear

# Print welcome message
echo "----------------------------------------------Welcome to hackers code---------------------------------------------------"
echo "Exit game and navigate to instructions.txt to learn how to play"
sleep 5
echo "starting game."
sleep 0.2
clear
echo "----------------------------------------------Welcome to hackers code---------------------------------------------------"
echo "Exit game and navigate to instructions.txt to learn how to play"
echo "starting game.."
sleep 0.2
clear
echo "----------------------------------------------Welcome to hackers code---------------------------------------------------"
echo "Exit game and navigate to instructions.txt to learn how to play"
echo "starting game..."
sleep 0.2
clear
echo "----------------------------------------------Welcome to hackers code---------------------------------------------------"
echo "Exit game and navigate to instructions.txt to learn how to play"
echo "starting game...."
sleep 0.2
clear
echo "----------------------------------------------Welcome to hackers code---------------------------------------------------"
echo "Exit game and navigate to instructions.txt to learn how to play"
echo "starting game....."
clear
python3 code.py
