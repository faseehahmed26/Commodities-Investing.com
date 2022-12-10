# Commodities-Investing.com



# **Project overview**


In this project learned about time series analysis using deep learning =, also learned how to built a scraper which can scrape data based on respective timeline provided and can give output in **csv** or **excel** file. improved my visualization skills using seaborn 


## Analytic Insights 

From Last 5 Years

 ●   Crude Oil prices is **strongly correlated** with Brent Oil and Natural Gas

●   Crude Oil prices is positively correlated with Copper.

●    Brent Oil and Crude Oil are **strongly correlated**.

●   Brent Oil is positively correlated with Natural Gas and Copper.

●   Natural Gas is positively correlated with Brent Oil , Crude Oil and Copper.

●   Gold prices is **strongly correlated** with Silver

●   Gold prices is positively correlated with Silver and Copper.

●    Silver is positively correlated with Gold and Copper.

●   Copper is positively correlated with Brent Oil , Crude Oil , Gold and Copper.

●   Copper is positively correlated with all others.


## Tech Stack
●   Backend - Python,Pytorch,

●   Frontend - Streamlit

●   Database - SQLite3

●   Deep learning Inference- LSTM

●   Deep learning training - Tensorflow,Keras


## Application Features


Extracted data from Investing .com by building a web scraper which could extract data if Start and End Date are given as parameters.
You could find the scaper code here.
Copper ,Gold, Crude Oil , Brent Oil , Natural Gas, Silver Prices variation of each of the commodities from the last 10 Years .



![qwe dfd](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/commodities-trade-oil-gold-coins.jpeg?raw=true)



Context
LSTM stands for long short-term memory networks, used in the field of Deep Learning. It is a variety of recurrent neural networks (RNNs) that are capable of learning long-term dependencies, especially in sequence prediction problems. LSTM has feedback connections, i.e., it is capable of processing the entire sequence of data, apart from single data points such as images. This finds application in speech recognition, machine translation, etc. LSTM is a special kind of RNN, which shows outstanding performance on a large variety of problems.

## Copper
Copper prices are up 20% year to date, supported in part by a rebounding economy in the U.S. and other parts of the world as the pandemic comes under control. Improving economies are key to copper demand since it's an industrial metal that's a good conductor of electricity. Copper is found in a host of items from air conditioning units and televisions to cars. The base metal may also benefit from President Joe Biden's infrastructure plan and the growing appetite for electric vehicles. That's spurred investor interest in the red metal, but buyers need to do plenty of research. Commodities are unlike traditional stock and bond investing, as these markets have different fundamental drivers that affect pricing.
![asd](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/Screenshots/copper_res.png?raw=true)
## Gold
Gold has traditionally been regarded as a superior investment asset. It has become a safe haven for investors all around the world in recent years. Gold, in particular, possesses all of the characteristics that a traditional investor seeks in an asset class. Investing in gold has always shown to be a successful approach to combat inflation.
![asd](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/Screenshots/gold_res.png?raw=true)
## Crude Oil
Crude oil is at the heart of many global industries. It is the power that moves most vehicles, allows factories to operate and is used to generate electricity. Oil’s importance to mankind has made it a valuable commodity for many companies and countries. Along with its derivatives, crude oil is the most traded commodity in the world.
![asd](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/Screenshots/crude_res.png?raw=true)
## Brent Oil
Brent oil is a major benchmark price for purchases of oil worldwide. While Brent Crude oil is sourced from the North Sea the oil production coming from Europe, Africa and the Middle East flowing West tends to be priced relative to this oil. The Brent prices displayed in Trading Economics are based on over-the-counter (OTC) and contract for difference (CFD) financial instruments. Our market prices are intended to provide you with a reference only, rather than as a basis for making trading decisions. Trading Economics does not verify any data and disclaims any obligation to do so.
![asd](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/Screenshots/brent_res.png?raw=true)
## Natural Gas
The US Energy Information Administration says natural gas is the most widely used fuel for space heating in the US, and it has also started to beat out coal as the top fuel for power generation. Even so, demand for natural gas around the world can be volatile as it is very much dependent on the weather.
![asd](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/Screenshots/gas_res.png?raw=true)
## Silver
Silver may be used as an investment like other precious metals. It has been regarded as a form of money and store of value for more than 4,000 years, although it lost its role as legal tender in developed countries when the use of the silver standard came to a final end in 1935.
![asd](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/Screenshots/silver_res.png?raw=true)
Acknowledgements
For this dataset I depended upon Investing.com to scrape the data . It's the premier source for financial, economic, and alternative datasets, serving investment professionals. Investing’s platform is used by over 400,000 people, including analysts from the world’s top hedge funds, asset managers and investment banks.

Results
As we can see we build our model from the data we extracted from Investing.com from last 10 years and performed EDA on it and we could see how variuos commodities are related to each other then build LSTM models for each of the commodities and here are the MSE values for each of them

**Gold = 0.27**

**Silver = 0.40**

**Crude Oil = 0.34**

**Brent Oil = 0.27**

**Natural Gas = 0.35**

**Copper = 0.32**

If you would like to experiment with the [custom dataset](https://www.kaggle.com/datasets/faseeh001/commoditiesinvestingcom) yourself, you can download the scraping script from on [Kaggle](https://github.com/faseehahmed26/Commodities-Investing.com/blob/main/commoditiesScraper.py) and the code at [Github](https://github.com/faseehahmed26/Commodities-Investing.com)  .
