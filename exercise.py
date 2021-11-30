import numpy as np
import pandas as pd

# Logic


def check_uniqueness(lst):
    """
    Check if a list contains only unique values.
    Returns True only if all values in the list are unique, False otherwise
    """
    
    #use set to eliminate all the same elements,if length remains all values unique
    new_lst=set(lst)
    return len(new_lst)==len(lst)
    pass


def smallest_difference(array):    
    """
    Code a function that takes an array and returns the smallest
    absolute difference between two elements of this array
    Please note that the array can be large and that the more
    computationally efficient the 
    """
    #assume  array is an np.array
    #if only 1 element
    if len(array)<=1:
        print("There is only 1 element in the array")
        return 0
    #sort array
    array.sort()
    #define first min
    min_dif=array[1]-array[0]
    for i in range(1,len(array)-1):
        min_tmp=abs(array[i+1]-array[i])
        if min_tmp==0:
            return min_tmp
        elif min_tmp<min_dif:
            min_dif=min_tmp
    return min_dif
    
    
    pass


# Finance and DataFrame manipulation


def macd(prices, window_short=12, window_long=26):
    """
    Code a function that takes a DataFrame named prices and
    returns it's MACD (Moving Average Convergence Difference) as
    a DataFrame with same shape
    Assume simple moving average rather than exponential moving average
    The expected output is in the output.csv file
    """
    def get_SMA(price,N):
        sma=prices['SX5T Index'].rolling(window=N).mean()
        list_sma=[]
        for i in sma:
            list_sma.append(i)
        return list_sma

    def get_MACD(prices, short=12, long=26, M=9):    
        a=get_SMA(prices, window_short)
        b=get_SMA(prices, window_long)
        prices['macd_12_26']=pd.Series(a)-pd.Series(b)    
    pass


def sortino_ratio(prices):
    """
    Code a function that takes a DataFrame named prices and
    returns the Sortino ratio for each column
    Assume risk-free rate = 0
    On the given test set, it should yield 0.05457
    """
    prices["daily_return"]=prices["SX5T Index"].pct_change()
    return_dd=prices["daily_return"].mean()*len(prices)
    prices['dd']=prices[prices['daily_return'] <0] ['daily_return']
    dd_new=df.dd.std()*np.sqrt(len(price))
    sortino_ratio=return_dd/dd_new
    return sortion_ratio
    
    # i double check my function but i dont understand why i have the different 
    # answer from the reuslut ,i have 1.0161476208210756 the result
    pass


def expected_shortfall(prices, level=0.95):
    """
    Code a function that takes a DataFrame named prices and
    returns the expected shortfall at a given level
    On the given test set, it should yield -0.03468
    """
    
    prices["daily_return"]=prices["SX5T Index"].pct_change()
    def value_at_risk(returns, confidence_level=.05):
        return returns.quantile(confidence_level, interpolation='higher')
    def expected_shortfall(returns, confidence_level=.05):
        var = value_at_risk(returns, confidence_level)
        return returns[returns.lt(var)].mean()
    es=expected_shortfall(df['daily_return'])
    return es
    pass


# Plot


def visualize(prices, path):
    """
    Code a function that takes a DataFrame named prices and
    saves the plot to the given path
    """
    prices['date'] = pd.to_datetime(prices['date'])
    prices["daily_return"]=prices["SX5T Index"].pct_change()
    plt.figure(figsize=(10,10))
    plt.plot(prices['date'],prices['daily_return'].rolling(window=12).mean(),label="Sma_12")
    plt.plot(prices['date'],prices['daily_return'].rolling(window=26).mean(),'r',label="sma_26")
    plt.legend()
    plt.savefig(path,'macd.png', dpi=75)
    plt.show()
    
    pass
