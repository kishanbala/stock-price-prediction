import time

from requirements import web, pd

start_time = time.time()

data1 = web.DataReader('TATASTEEL.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data2 = web.DataReader('WIPRO.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data3 = web.DataReader('TCS.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data4 = web.DataReader('INFY.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data5 = web.DataReader('HDFCBANK.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data6 = web.DataReader('SBIN.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data7 = web.DataReader('RELIANCE.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data8 = web.DataReader('LT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data9 = web.DataReader('DRREDDY.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data10 = web.DataReader('SUNPHARMA.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data11 = web.DataReader('AXISBANK.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data12 = web.DataReader('INDUSINDBK.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data13 = web.DataReader('ASIANPAINT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data14 = web.DataReader('HINDUNILVR.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data15 = web.DataReader('LUPIN.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data16 = web.DataReader('BRITANNIA.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data17 = web.DataReader('NESTLEIND.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data18 = web.DataReader('PIDILITIND.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data19 = web.DataReader('BERGEPAINT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data20 = web.DataReader('HAVELLS.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data21 = web.DataReader('ADANIENT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data22 = web.DataReader('BAJAJ-AUTO.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data23 = web.DataReader('BHARTIARTL.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data24 = web.DataReader('ADANIPOWER.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data25 = web.DataReader('BPCL.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data26 = web.DataReader('CIPLA.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data27 = web.DataReader('BAJAJFINSV.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data28 = web.DataReader('COALINDIA.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data29 = web.DataReader('DIVISLAB.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data30 = web.DataReader('EICHERMOT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data31 = web.DataReader('GRASIM.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data32 = web.DataReader('HCLTECH.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data33 = web.DataReader('HDFC.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data34 = web.DataReader('HDFCLIFE.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data35 = web.DataReader('HEROMOTOCO.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
# data36 = web.DataReader('HINDALCO.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data37 = web.DataReader('ICICIBANK.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data38 = web.DataReader('IOC.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data39 = web.DataReader('JSWSTEEL.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data40 = web.DataReader('KOTAKBANK.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data41 = web.DataReader('M&M.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data42 = web.DataReader('MARUTI.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data43 = web.DataReader('NTPC.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data44 = web.DataReader('ONGC.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data45 = web.DataReader('POWERGRID.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data46 = web.DataReader('SBILIFE.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data47 = web.DataReader('SHREECEM.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data48 = web.DataReader('TATAMOTORS.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data49 = web.DataReader('TATACONSUM.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data50 = web.DataReader('TECHM.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data51 = web.DataReader('TITAN.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data52 = web.DataReader('ULTRACEMCO.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data53 = web.DataReader('UPL.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data54 = web.DataReader('DABUR.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data55 = web.DataReader('QUICKHEAL.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data56 = web.DataReader('SONATSOFTW.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data57 = web.DataReader('BSOFT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data58 = web.DataReader('CYIENT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data59 = web.DataReader('PERSISTENT.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')
data60 = web.DataReader('MPHASIS.NS', data_source='yahoo', start='1995-01-01', end='2021-05-30')

data = pd.concat(
    [data1.reset_index(), data2.reset_index(), data3.reset_index(), data4.reset_index(), data5.reset_index(),
     data6.reset_index(),
     data7.reset_index(), data8.reset_index(), data9.reset_index(), data10.reset_index(), data11.reset_index(),
     data12.reset_index(),
     data13.reset_index(), data14.reset_index(), data15.reset_index(), data16.reset_index(), data17.reset_index(),
     data18.reset_index(),
     data19.reset_index(), data20.reset_index(), data21.reset_index(), data22.reset_index(), data23.reset_index(),
     data24.reset_index(),
     data25.reset_index(), data26.reset_index(), data27.reset_index(), data28.reset_index(), data29.reset_index(),
     data30.reset_index(),
     data31.reset_index(), data32.reset_index(), data33.reset_index(), data34.reset_index(), data35.reset_index(),
     data37.reset_index(), data38.reset_index(), data39.reset_index(), data40.reset_index(), data41.reset_index(),
     data42.reset_index(),
     data43.reset_index(), data44.reset_index(), data45.reset_index(), data46.reset_index(), data47.reset_index(),
     data48.reset_index(),
     data49.reset_index(), data50.reset_index(), data51.reset_index(), data52.reset_index(), data53.reset_index(),
     data54.reset_index(),
     data55.reset_index(), data56.reset_index(), data57.reset_index(), data58.reset_index(), data59.reset_index(),
     data60.reset_index()], axis=0, ignore_index=True)

end_time = time.time()

print("Imported data!")
print(f"Time taken to import data is {int(end_time - start_time)} seconds")
print("Data preparation done")
