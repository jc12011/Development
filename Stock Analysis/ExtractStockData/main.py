import os
import pandas as pd
from futu import *

pd.set_option('display.max_columns',None)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # 创建行情对象
#print(quote_ctx.get_market_snapshot('HK.00700'))  # 获取港股 HK.00700 的快照数据
df = pd.DataFrame(quote_ctx.get_market_snapshot('HK.00700')[1])
df.to_csv(r'./files/output.csv',index=False)
NeedColumns = ['volume','turnover']
print(df.columns)
print(df['code'])

quote_ctx.close() # 关闭对象，防止连接条数用尽


#trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)  # 创建交易对象
#print(trd_ctx.place_order(price=500.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE))  # 模拟交易，下单（如果是真实环境交易，在此之前需要先解锁交易密码）
#trd_ctx.close()  # 关闭对象，防止连接条数用尽
