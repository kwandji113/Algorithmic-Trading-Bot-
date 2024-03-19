# Algorithmic-Trading-Bot
by Nathan, Kelyan, Aidan, Eamon, Robert, Alex and Angus

Rough Project Overview:
We are making an algorithmic trading bot. Using some complex math and a trained neural network to perform sentiment analysis, we are going to create an algorithm that should be able to predict the growth or decay of stocks with some reliability. Right now this will be a program that a user can download and be able to run on their computer. It should provide information on when to buy a stock and when to sell. We might be able to get the program to a point where we can handle the buying and selling of assets within the program. 



4-Month Timeline:
Checkpoint 1: Clear vision on what we want to do. Subject to change but a finished architecture diagram, research on algorithms, stock market, and neural networks done. Experimentation code on which technical indicators to use, api usage to get stock market data, and what data libraries we want to use. That also means code that can organize the data we pull into a processable format. Figure out the training for the first neural network. Look into parallel computing to train the neural networks faster. Build a framework to have set parameters for the time periods that is training data, validation data, and testing data. The chronological timing for these parameters is incredibly important. The time periods for training has to be before the validation and testing. 

Checkpoint 2: Should have some base-level neural network and algorithm working. Some sort of base-level UI done. Get the project to a state where data from a timeframe can be fed into the algorithms we have and we can return results whether the stock will trend up or down. Tested our algorithm with real-world data to educate decisions on how to adjust and improve.

Checkpoint 3: Neural network and algorithm should be very refined (95% done) where only fine tuning is needed. Interactable UI. Can feed longer timeframe into algorithms while still having positive results.

Checkpoint 4: Completely finished project, math and neural network completely done, functional, and working together to provide information on when to buy, sell, etc.
UI done and at minimum

Final litmus test on the effectiveness of our Algorithmic trader: 
Subject to change but we use tests to see on average if the amount of money made with the algorithmic trader is greater than the money made from random selections. 
Testing methodology: We take a 2 week period in which at the start we generate our 10 best performing stocks according to the model and buy a set $ value of each stock on the first day. For the random test we randomly choose 10 tickers in the s&p 500 and buy the same set $ value of each stock on the first day. In each subsequent day we randomly buy shares of 5 companies and sell 5 company shares in the "portfolio" we already have. This same process occurs for the algorithmic trader as well, the difference is the 5 stocks we buy is predicted by our model and the 5 we sell are the 5 worst performing as stated by our model in our "portfolio". 
At the end of each day, we find the total value of the assets from the algorithmic trading portfolio and the random portfolio. We then take the difference between these two values and this is the going to be the data point we have in our t-test sample. 