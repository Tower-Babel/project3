import streamlit as st

st.title(" :blue[Project 3:] ")
st.title(" :blue[Walmart - Store Sales Forecasting] ")



st.write(
    """

**Introduce the problem and dataset.**
#
The dataset comes from Walmart. Walmart is an international retail store that attributes its revenue from selling a range of discounted products from food to auto supply. Walmart is known to have an economic impact due to its effects on retailers, jobs, and productivity. 
#
The Kaggle dataset contains data from 45 stores located in different regions. The data can be used to predict the revenue of a store. With these insights I can see which store and department would be affected and the extent of the sales impact. 
The challenge is to make predictions of limited historical data and consider the holiday markdown that affects sales.
#
**What is regression and how does it work?**
#
Regression is a method that uses targets and predictors to analyze relationships. There are different types of regression models such as logistic regression, ridge regression and polynomial regression. Based off the data, time series analysis could be best since the goal is to make future predictions with time dependent data. Regression models are not optimized for predicting the future the same way. But regression can be useful if I want to analyze the relationship between variables such as seeing if unemployment affects sales revenue when it is not time dependent. 
#
**Experiment 1: Data understanding**
#
The data includes values for:
#
    Store – numerical store number
    Dept – categorical section in store that deals with specific commodity. 
    Date – numerical value to represent day.
    Weekly_Sales – sales for the given department
    IsHoliday – whether the week is a special week including super bowl.
    Temperature- average temperature in the region
    Fuel_price – numerical cost of fuel.
    MarkDown(1-5)
    CPI – Consumer price index
    Unemployment – the unemployment rate
    The last column ‘revenue’ is our target column.
What is not included is the open date, city, type of store such as neighborhood Walmart or supermarket, Demographic data, real estate data, commercial data.
#
**Experiment 2: Pre-processing**
#
The last column ‘revenue’ is our target column. With the dates, I will drop the day and keep the year and month. It will also be helpful to categorize the holiday and data that is not related to numerical values. 
There are a few outliers and the only data that’s missing is markdown data. The missing data can be from the items that were not marked down.
#
**Experiment 1: Modeling**
#
**Experiment 2: Evaluation**
#
**Experiment 3: Feature Engineering**
#
**Impact**
#
**Conclusion**

    """
)

