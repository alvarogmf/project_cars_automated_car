# Project Cars Driving AI

![project_cars](https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/480/public/media/image/2015/05/475268-analisis-project-cars-ps4-one-pc.jpg?itok=QVd4SYm_ "Logo Title Text 1")

This is a Work in Progress project.

The aim of it is to build a self driving car through image processing and a Neural Network, able to race a full track in Project Cars 1 (to be tested its capacities in other racing games in the future).
This project has been based in the GTA V self driving car guide made by Sentdex (link [here](https://pythonprogramming.net/game-frames-open-cv-python-plays-gta-v/)). 

Using this programs, anyone can have a trained model (or make their own) to have a self driving car.

The main files are the following:
- *create_training_data.py:* this tool uses manual input from the game to gather data for the training model. In case you don't want to train a new model, you don't need to use this program. If you do, here is some important information to do it correctly:
    1. The game should be on window mode, with a resolution of 800 (WIDTH) x 600 (HEIGHT), and place it on the top-left of the screen. The program records that part of the screen.
    2. The input that, for now, it takes is going Straigt (W), Left (A) or right (D), when you are playing, bear in mind that these are the only buttons the program records.
    3. A four (4) second countdown will show in the terminal before it starts recording, so you can have time to change to the game and start playing with the car.
    4. The program saves a Numpy file in the data folder. Every 1000 new rows in the file, it will automatically save the file. Everytime you start again, it will take it from there.
    5. Recomendation, take as much data as possible. At least 100.000 rows (after balancing).

- *balance_data.py:* this program filters all the data gathered in the Numpy file, and equalizes the number of rows for each input (i.e: randomly discards rows from the two inputs with more rows until all three have the same).

- *train_model.py:* Using Alexnet, this will create a model based on the data provided.

- *test_model.py:* This program uses the model created previously and controls the vehicle in the game. Also, shows some information in the Terminal.



