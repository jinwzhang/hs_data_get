from hs_udata import *
import time
set_token(token='_dtdm_HfS25UIPcknjTDbbvs1yyUYHDVIKyUsrTGcgmxVmDb_kAWlMLRSPr8wJCQ')

t0 = time.time()
stock_list = stock_list(listed_state="1")
cnt = 0
for i in stock_list[['hs_code']].iterrows():
    code = i[1][0]
    data = stock_quote_minutes(en_prod_code=code, begin_date="20211001", end_date="20211115")
    data['hs_code'] = code
    data.to_csv(r'D:\Users\zhangjinwei\Desktop\zlaw\stock\stock_quote_minutes.csv', mode='a')
    cnt += 1


t1 = time.time()
print(cnt, (t1-t0)//60)
