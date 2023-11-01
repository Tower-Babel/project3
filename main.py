import streamlit as st
from PIL import Image

st.title(" :blue[Project 3:] ")
st.title(" :blue[Walmart - Store Sales Forecasting] ")

image1 = Image.open("img1.png")
image2 = Image.open("img2.png")
image3 = Image.open("img3.png")
image4 = Image.open("img4.png")
image5 = Image.open("img5.png")
image6 = Image.open("img6.png")
image7 = Image.open("img7.png")
image8 = Image.open("img8.png")
image9 = Image.open("img9.png")
image10 = Image.open("img10.png")
image11 = Image.open("pic1.png")
image12 = Image.open("img11.png")
image13 = Image.open("img12.png")
image14 = Image.open("img13.png")
image20 = Image.open("Picture14.png")
image21 = Image.open("Picture15.png")
image22 = Image.open("Picture16.png")

st.header("Introduce the Problem and Dataset")
st.write("""
        The dataset comes from Walmart stores during the years 2010-2013. Walmart is an international retail store that attributes its revenue from selling a range of discounted products from food to auto supplies. Walmart is known to have an economic impact due to its effects on retailers, jobs, and productivity so it’s important for the stores to always stay stocked. 
        
         link: https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting
         #
        The Kaggle dataset contains data from 45 stores located in different regions. The data can be used to predict the revenue of a store. With these insights we can see which store and department would be affected and the extent of the sales impact. 
        The dataset contains 3 csv files
            #
         
            Train.csv: which has 42,000 rows and 5 columns. The columns are for a store, department, date, weekly sales, and holiday Boolean.
            
            Features.csv: which is very useful and contains 8190 rows and 12 columns. It contains outside temperature, fuel price, date, consumer price index and more features. 
            
            Store.csv: this has 45 rows and 3 columns. The columns are stores and size.
        #
        The challenge is to make predictions of limited historical data and consider the holiday markdown that affects sales. These predictions can help stock stores before they sell out. Also these predictions can help create targeted marketing strategies.

        """
)


st.header("What is Regression and How Does it Work?")
st.write(
            """
            Regression is a method that uses targets and predictors to analyze relationships. 
            #
            There are different types of regression models such as logistic regression, ridge regression and polynomial regression. Based off the data, time series analysis could be best since the goal is to make future predictions with time dependent data. Regression models are not optimized for predicting the future the same way. But regression can be useful if I want to analyze the relationship between variables such as seeing if unemployment affects sales revenue when it is not time dependent. 
            It would be beneficial to analyze each correlated feature to see the relationship between it and the weekly sales.
            To perform regression analysis, I will:
            #

                    •	Import the necessary libraries
                    •	Load the dataset
                    •	Assign the target features to x
                    •	Assign the target features to y
                    •	Initialize the algorithm with each feature
                    •	Train the model
                    •	Predict from the test dataset
                    •	Find the accuracy of the model
            """


)
st.header("Experiment 1: Data Understanding")
st.write(

    """
    The data features include values for:
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
    The last column ‘revenue’ or weekly_sales is our target column.
    What is not included is the open date, city, type of store such as neighborhood Walmart or supermarket, 
    Demographic data, real estate data, commercial data, or department names. It would be great to 
    have this data to compare the model accurately to. Since we do not have this data, I will split the 
    data into training and testing data.
    """
)
st.image(image1, caption=None)
st.write("The three csv files will be joined below")
st.image(image2, caption=None)
st.image(image3, caption=None)

st.header("Experiment 1: Pre-processing")
st.write(
    """
    The last column weekly_sales is our target column. With the dates, I will drop the day and keep the year and month. It will also be helpful to separate the data into categorize and numerical groups. 
    There are a few outliers and the only data that’s missing is markdown data. The missing data can be from the items that were not marked down during that period. I will join all the csv into one and merge all the missing data and not use it since it is the Markdown 1 to Markdown 5. There are over 250,000 missing data points in markdown. If the Model evaluation is low, it may be good to add this data point back to see if it improves the model and use the mean correlation to fill in the missing points.
    """
)
st.image(image4, caption=None)
st.write(
    """
    Let’s see the correlation between the features and drop the uncorrelated 
    features for our regression model. I will drop non-numerical values in the first model as well. 
    And I will also set the categorical values by 
    converting Object values to numerical values, like store type will be converted to 1, 2 or 3.
    """
)
st.image(image5, caption=None)
st.write(
    """
    Looking at the relationship between the different features and how they correlate with the weekly sales.
    #
    The unemployment rate, CPI and fuel price do not relate to the sales so I will drop it for the second experiment. The size has a large correlation to the sales. But I need to visualize the features’ relationship to the weekly sales. It will be great to analyze the top store features as well. First let’s look at the size in relation to sales and compare the 3 store types.
    """
)
st.image(image6, caption=None)
st.write(
    """
    In the plot we see there is a relationship between the store size and sales. The sales increase with size. There also seem to be outliers shown in the plot. This can relate to the time of year or top stores. Let’s analyze further. 
    #
    First lets now see how the sales relates to the months of the year.
    """

)
st.image(image7, caption=None)
st.write(
    """
    This shows there is a relationship between the time. Each year in December the sales increase. 
    This is interesting and not reflected in the correlation map. The correlation map s does show a relationship between Departments and sales so let’s visualize it next. 
    Since there were outliers in the store size lets see if there’s any in the top stores as well.
    """
)
st.image(image8, caption=None)
st.image(image20, caption=None)
st.write(
    """
    Each department showed 
    different average sales. Each sale is represented by 10,000 to 1. There is not much correlation here.
    """
)


st.header("Experiment 1: Modeling")
st.write(
   """ 
    Based off the analysis, I will train the first model on all the features except markdown and I will use a numeric preprocessor, standard scaling, categorical preprocessor. And hot encoder to convert categorical values into binary 0 or 1. This seemed to be the best practice to ensure numerical values are only available for the regression model.
    The preprocessor combines both the features into a format for regression. It uses numerical values and not the categorical first.
    """
)

st.image(image9, caption=None)
st.write("Let’s visualize the predictions for accuracy before we use MAE to evaluate.")
st.image(image10, caption=None)
st.write(
    """
    At first glance we see the performance is weak. There is one prediction that is right on target. I will use MAE to evaluate as well as MSE, RSME and R squared. This will give us the mean error of all the predictions. 
    #
    MAE is the mean absolute error. This is the difference between the predicted values and actual. Where MSE is the squared difference between the predict values and actual value. These will be used to assess the performance of the model. The lower the score the better.
    """
)




st.header("Experiment 2: Evaluation")
st.write(
    """
    The model is not great. It tells us the predicted sales price is off by $14,000.  Linear Regression is the most basic so let’s try to drop some other features before using a different regression algorithm.
    Some other options we can do are engineer a new feature such as a ratio between the fuel price and temperature. Or Store size and weekly sales.
    """
)
st.image(image11, caption=None)
st.image(image21, caption=None)


st.header("Experiment 3: Feature Engineering")
st.image(image5, caption=None)
st.write(
    """ 
    Since the correlation map showed no relationship to our target between temperature, fuel price, type, CPI and unemployment, 
    I will drop these and see if the MAE is stronger. I will create a new data frame without these features.
    """
)
st.image(image12, caption=None)
st.write(
    """
    The scores did not change much. Surprisingly the score got worse. I would not use these features for predicting future sales. I will a few different regressions such as Elastic Net and Ridge Regression to see if I can predict the future sales better. I will add back all the numerical features that performed best in the first model.
    Ridge Regression adds weights to get better performance. We will set the alpha to 1 and ratio to .5. The goal is to find the coefficient that is smaller to prevent overfitting.
    Elastic Net also adds weight.
    """

)
st.write("Ridge:")
st.image(image13, caption=None)
st.write("Elastic Net:")
st.image(image14, caption=None)
st.write()

st.header("Impact")
st.write(
    """
    Based on the analysis and the correlation map, there are other features needed to make a accurate prediction of future sales. Our model shows the regression is not the correct model for predicting because regression performs poorly in relation to historical data. The trained models can show which features affect sales and what departments will be affected. Looking back at the visual with the strongest relationship – Months compared to Sales, 
    I see that sales increase at Christmas or at end of year. The sales increase in each feature. 
    """
)

st.header("Conclusion")
st.write(
    """
    The regression models were weak. This seems to be a time-series related analysis and not a regression analysis. Regression is not worth much here. I assumed feature engineering would continue to make the model worse. We aren’t given enough data to fit the regression very well. The more data the stronger the model performance. A better approach would be to look at the historical trends and the seasons.
    """
)
st.image(image22, caption=None)
st.write(
    """    
    With predictions like these, Retail stores can solve supply chain challenges. Retail would be able to plan supply chain accordingly without overstocking or understocking.
    """
)

st.header("References")
st.write(
    """
    https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting?rvi=1
    #
    https://www.kaggle.com/code/cdeotte/linear-regression-baseline-lb-1-092#Write-Submission-CSV
    #
    https://www.kaggle.com/code/cdeotte/recommend-items-purchased-together-0-021
    #
    https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting

    """

)

st.header("Code")
st.write("https://www.kaggle.com/code/august33rd/project3")
