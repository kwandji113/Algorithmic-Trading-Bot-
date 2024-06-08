For project 4, I worked on a neural network designed to predict the stock market.

# Overview of My Work
Our first plan was to make a mobile trading app where users could trade stocks with the help of the neural network. We would have people working on UI, machine learning, and data scraping/processing.

I first worked on data scraping/processing. In that role, I tried to create as much high-quality data as I could.

The final source of data was daily data from yfinance and 2m intervals for 60 days.

After I finished writing a script to scrape data from yahoo, we made the realization that the model was going to be a lot harder than we thought. As a result, we scrapped the plans for creating a front end - it took time we didn't have and wasn't as important as the backend. 

We decided that each group member would work on their own model to increase the speed we could try ideas. I agree with this; the faster we fail, the faster we can learn and find something that works.

For the neural network, we tried many different types of models until we settled on a LSTM. Robert made a hyper parameter tuner to find the best weights/vectors, which I then used. For my data processing, my first strategy was to train the model on random stock tickers, which didn't work so well. The strategy that gave me the best results was to group the stocks by sectors. At the end of the project, we were able to predict the direction of the stock better than random in the short run.

# Key Insights
The first major problem I faced was when trying to find data, I found 2 things:
1. Lots of data was behind a paywall.
2. Free data was often of low quality. In some cases, more than 2/3 of some data sets were found to be not valid.

For the first problem, there wasn't much I could do about it. Much of the data was thousands per year!
The second problem was more solvable as the data could be manually cleaned up. In this regard, I built a script to validate data. With this script, I was able to use expand my dataset beyond what yfinance offered.

In terms of creating the model, the most hands-on part wasn't creating the network itself - it was preprocessing the data. While creating the model was theory intensive, adding a new layer to the network was a single line thanks to the heavy lifting done by 3rd party libraries. On the other hand, preprocessing the data required lots of statical and array operations through pandas and numpy.

It was here that a breakthrough was found - grouping the data in certain ways had a sizeable impact on the quality of the model. While we struggled to get good results from data with random stocks, training only on stocks in the same sector or with similar prices improved predictions significantly. I had the best results by only training the model on "tech" stocks and then asking the model to give a prediction on another "tech" stock.

Since the data is timestamped, care was taken to ensure that all testing data came after the training data – what’s the point of predicting something that already happened?

# Lessons Learned
1. Machine Learning projects require lots of resources, both in terms of computing and development. It was common to have to leave my computer on overnight to train models.
2. You might find machine learning projects quite hard if you rely on visualizations. Oftentimes, the datasets are so large that looking at it is not viable. For the model itself, the training process is abstracted away through hundreds of functions in a 3rd party library.
3. The "fail fast" strategy was the correct thing to do. It gave us more freedom to try almost anything we wanted, which was important for learning purposes.
4. Having large amounts of high-quality data is a must for neural networks. It was very difficult to progress for several weeks due to a lack of data.
5. The neural network is very sensitive to changes in the environment. Code that worked in my Google Colab space didn't work when I tried to run the same code from a python file. I eventually gave up pushing to git and used google drive a VCS.
6. This model isn't 100% representative of the stock market. Trading fees, latency, etc, weren’t included in our testing simulation. It is almost certain that the performance of our model would decrease when making trades on the live market.

Overall, I enjoyed this project and the progress we made on something that was supposedly impossible. More importantly, I felt this project was effective at teaching machine learning concepts. I plan to use these concepts in future projects that are hopefully more possible.

Angus

