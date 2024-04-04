import random
import datetime
import yfinance as yf
import os
import path
import pandas as pd
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter


tickers = ["MMM","AOS","ABT","ABBV","ACN","ADBE","AMD","AES","AFL","A","APD","ABNB","AKAM","ALB","ARE","ALGN","ALLE","LNT","ALL","GOOGL","GOOG","MO","AMZN","AMCR","AEE","AAL","AEP","AXP","AIG","AMT","AWK","AMP","AME","AMGN","APH","ADI","ANSS","AON","APA","AAPL","AMAT","APTV","ACGL","ADM","ANET","AJG","AIZ","T","ATO","ADSK","ADP","AZO","AVB","AVY","AXON","BKR","BALL","BAC","BK","BBWI","BAX","BDX","BBY","BIO","TECH","BIIB","BLK","BX","BA","BKNG","BWA","BXP","BSX","BMY","AVGO","BR","BRO","BLDR","BG","CDNS","CZR","CPT","CPB","COF","CAH","KMX","CCL","CARR","CTLT","CAT","CBOE","CBRE","CDW","CE","COR","CNC","CNP","CF","CHRW","CRL","SCHW","CHTR","CVX","CMG","CB","CHD","CI","CINF","CTAS","CSCO","C","CFG","CLX","CME","CMS","KO","CTSH","CL","CMCSA","CMA","CAG","COP","ED","STZ","CEG","COO","CPRT","GLW","CPAY","CTVA","CSGP","COST","CTRA","CCI","CSX","CMI","CVS","DHR","DRI","DVA","DAY","DECK","DE","DAL","XRAY","DVN","DXCM","FANG","DLR","DFS","DG","DLTR","D","DPZ","DOV","DOW","DHI","DTE","DUK","DD","EMN","ETN","EBAY","ECL","EIX","EW","EA","ELV","LLY","EMR","ENPH","ETR","EOG","EPAM","EQT","EFX","EQIX","EQR","ESS","EL","ETSY","EG","EVRG","ES","EXC","EXPE","EXPD","EXR","XOM","FFIV","FDS","FICO","FAST","FRT","FDX","FIS","FITB","FSLR","FE","FI","FMC","F","FTNT","FTV","FOXA","FOX","BEN","FCX","GRMN","IT","GEHC","GEN","GNRC","GD","GE","GIS","GM","GPC","GILD","GPN","GL","GS","HAL","HIG","HAS","HCA","DOC","HSIC","HSY","HES","HPE","HLT","HOLX","HD","HON","HRL","HST","HWM","HPQ","HUBB","HUM","HBAN","HII","IBM","IEX","IDXX","ITW","ILMN","INCY","IR","PODD","INTC","ICE","IFF","IP","IPG","INTU","ISRG","IVZ","INVH","IQV","IRM","JBHT","JBL","JKHY","J","JNJ","JCI","JPM","JNPR","K","KVUE","KDP","KEY","KEYS","KMB","KIM","KMI","KLAC","KHC","KR","LHX","LH","LRCX","LW","LVS","LDOS","LEN","LIN","LYV","LKQ","LMT","L","LOW","LULU","LYB","MTB","MRO","MPC","MKTX","MAR","MMC","MLM","MAS","MA","MTCH","MKC","MCD","MCK","MDT","MRK","META","MET","MTD","MGM","MCHP","MU","MSFT","MAA","MRNA","MHK","MOH","TAP","MDLZ","MPWR","MNST","MCO","MS","MOS","MSI","MSCI","NDAQ","NTAP","NFLX","NEM","NWSA","NWS","NEE","NKE","NI","NDSN","NSC","NTRS","NOC","NCLH","NRG","NUE","NVDA","NVR","NXPI","ORLY","OXY","ODFL","OMC","ON","OKE","ORCL","OTIS","PCAR","PKG","PANW","PARA","PH","PAYX","PAYC","PYPL","PNR","PEP","PFE","PCG","PM","PSX","PNW","PXD","PNC","POOL","PPG","PPL","PFG","PG","PGR","PLD","PRU","PEG","PTC","PSA","PHM","QRVO","PWR","QCOM","DGX","RL","RJF","RTX","O","REG","REGN","RF","RSG","RMD","RVTY","RHI","ROK","ROL","ROP","ROST","RCL","SPGI","CRM","SBAC","SLB","STX","SRE","NOW","SHW","SPG","SWKS","SJM","SNA","SO","LUV","SWK","SBUX","STT","STLD","STE","SYK","SMCI","SYF","SNPS","SYY","TMUS","TROW","TTWO","TPR","TRGP","TGT","TEL","TDY","TFX","TER","TSLA","TXN","TXT","TMO","TJX","TSCO","TT","TDG","TRV","TRMB","TFC","TYL","TSN","USB","UBER","UDR","ULTA","UNP","UAL","UPS","URI","UNH","UHS","VLO","VTR","VLTO","VRSN","VRSK","VZ","VRTX","VFC","VTRS","VICI","V","VMC","WRB","WAB","WBA","WMT","DIS","WBD","WM","WAT","WEC","WFC","WELL","WST","WDC","WRK","WY","WMB","WTW","GWW","WYNN","XEL","XYL","YUM","ZBRA","ZBH","ZTS","SOLV","VFC","XRAY","SMCI","WHR","DECK","ZION","UBER","SEE","JBL","ALK","BLDR","SEDG","HUBB","OGN","LULU","ATVI","DXC","VLTO","BX","LNC","ABNB","NWL","KVUE","AAP","PANW","DISH","AXON","FRC","FICO","LUMN","BG","SBNY","PODD","SIVB","VNO","GEHC","STLD","ABMD","FSLR","FBHS","MBC","MBC","ACGL","TWTR","TRGP","NLSN","PCG","CTXS","EQT","DRE","CSGP","PVH","INVH","PENN","UA","KDP","UAA","ON","IPGP","VICI","CERN","CPT","PBCT","MOH","INFO","NDSN","XLNX","GPS","CEG","SBNY","LEG","SEDG","HBI","FDS","WU","EPAM","KSU","MTCH","PRGO","CDAY","UNM","BRO","NOV","TECH","MXIM","MRNA","ALXN","HFC","OGN","CRL","FLIR","PTC","VAR","NXPI","FLS","PENN","SLG","GNRC","XRX","CZR","VNT","MPWR","FTI","TRMB","CXO","ENPH","TIF","TSLA","AIV","NBL","VNT","POOL","ETFC","ETSY","HRB","TER","COTY","CTLT","KSS","BIO","ADS","TDY","HOG","TYL","JWN","WST","HP","DPZ","CPRI","DXCM","AGN","M","RTN","OTIS","CARR","HWM","ARNC","IR","XEC","PAYC","WCG","LYV","AMG","ZBRA","TRIP","STE","MAC","ODFL","STI","WRB","VIAB","NOW","CELG","LVS","NKTR","NVR","JEF","CDW","TSS","LDOS","APC","IEX","FL","TMUS","RHT","MKTX","LLL","AMCR","BMS","BMS","MAT","DD","DWDP","CTVA","FLR","DOW","BHF","WAB","GT","ATO","NFX","TFX","PCG","FRC","SCG","CE","ESRX","LW","COL","MXIM","AET","FANG","SRCL","JKHY","EQT","KEYS","CA","FTNT","EVHC","ROL","ANDV","WCG","XL","ANET","GGP","CPRT","DPS","FLT","TWX","BR","RRC","HFC","AYI","TWTR","MON","EVRG","NAVI","ABMD","WYN","MSCI","CSRA","TTWO","SIG","SIVB","PDCO","NKTR","CHK","IPGP","SNI","HII","BCR","NCLH","LVLT","CDNS","SPLS","DWDP","DOW","SBAC","DD","Q","WFM","BHF","AN","DRE","RIG","AOS","BBBY","PKG","MUR","RMD","MNK","MGM","RAI","HLT","YHOO","ALGN","TDC","ANSS","R","RE","MJN","INFO","TGNA","IT","DNB","DXC","SWN","AMD","URBN","RJF","FTR","ARE","FSLR","SNPS","HAR","DISH","LLTC","REG","ENDP","CBOE","PBI","INCY","SE","IDXX","STJ","AGN","MAA","OI","EVHC","LM","ARNC","AA","COTY","DO","COO","HOT","CHTR","EMC","MTD","TYC","FTV","CPGX","LNT","GAS","ALB","TE","FBHS","CVC","TDG","BXLT","AJG","CCE","LKQ","ARG","DLR","TWC","ALK","SNDK","AYI","ADT","GPN","GME","ULTA","THC","UA","FL","CAM","HOLX","POM","CNC","ESV","UDR","GMCR","AWK","CNX","CXO","PCL","CFG","PCP","FRT","BRCM","EXR","ACE","WLTW","FOSL","CHD","ALTR","CMCSK","CSRA","CSC","ILMN","SIAL","SYF","GNW","HPE","HCBK","VRSK","JOY","CMCSK","FOX","NWS","UAL","HSP","ATVI","PLL","SIG","DTV","PYPL","NE","AAP","FDO","KHC","KRFT","CPGX","ATI","JBHT","TEG","BXLT","QEP","QRVO","LO","O","WIN","AAL","AGN","EQIX","DNR","SLG","NBR","HBI","AVP","HSIC","CFN","SWKS","PETM","HCA","SWY","ENDP","COV","RCL","BMS","LVLT","JBL","URI","BTU","UHS","GHC","MNK","RDC","DISCK","MLM","X","AMG","FRX","XEC","IGT","AVGO","LSI","UA","BEAM","NAVI","SLM","GOOGL","ESS","CLF","GMCR","WPX","TSCO","LIFE","ADS","ANF","MHK","JDSU","FB","TER","GGP","MOLX","ALLE","JCP","KORS","NYX","RIG","DELL","VRTX","AMD","AME","SAI","DAL","BMC","NLSN","S","NWSA","APOL","ZTS","FHN","GM","HNZ","KSU","DF","MAC","CVH","REGN","PCS","PVH","BIG","ABBV","FII","DLPH","TIE","GRMN","RRD","DG","CBE","PETM","SUN","KRFT","ANR","ADT","LXK","PNR","DV","LYB","SHLD","ESV","GR","STX","PGN","MNST","SLE","LRCX","NVLS","ALXN","MMI","KMI","EP","PSX","SVU","FOSL","MHS","CCI","CEG","WPX","CPWR","TRIP","TLAB","BWA","AKS","PRGO","MWW","DLTR","WFR","GAS","GAS","CBE","JNS","XYL","ITT","TEL","CEPH","MOS","NSM","ACN","MI","MPC","RSH","ANR","MEE","CMG","NOVL","BLK","GENZ","EW","Q","COV","MFE","JOYG","AYE","CVC","KG","FFIV","EK","NFLX","ODP","NFX","NYT","IR","PTV","TYC","SII","CB","MIL","QEP","STR","KMX","XTO","CERN","BJS","HP","RX","V","CIEN","MJN","DYN","CLF","KBH","SAI","CVG","ROST","MBI","PCLN","SGP","ARG","CBE","FMC","CTX","PCS","TEL","FTI","COV","HRL","ACAS","VTR","JNY"]

start_date_testing = datetime.date(2006, 2, 1)
end_date_testing = datetime.date(2018, 2, 1)

start_date_validation = datetime.date(2018, 2, 1)
end_date_validation = datetime.date(2022, 2, 1)




#The amount of trading dates may not be the same for each two week period because of weekends, holidays
def data_gen(start_date, end_date, data_points):
    random_dates = set()
    while len(random_dates) < data_points:
        time_delta = end_date - start_date
        random_days = random.randint(0, time_delta.days)
        random_date = start_date + datetime.timedelta(days=random_days)
        #This exists for making the file name, trying to use str() there for some reason causes a error....
        ticker_for_filename = tickers[random.randint(0,1084)]
        random_ticker = yf.Ticker(ticker_for_filename)
        if str(random_date) + str(random_ticker) in random_dates:
            continue
        stock_data_frame = random_ticker.history(start=random_date, end=random_date + datetime.timedelta(days=14))
        if stock_data_frame.empty:
            continue
        #TODO do not hardcode paths!!!!!
        stock_data_frame.to_csv("data_test\\test_" +ticker_for_filename+ str(len(random_dates))+ ".csv")
        random_dates.add(str(random_date) + str(random_ticker))
    
    
data_gen(start_date_testing, end_date_testing, 5000)