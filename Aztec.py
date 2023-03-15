{\rtf1\ansi\ansicpg1251\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 select\
  date_trunc('day', "block_time") as day, -- get day from block time\
  round(sum(value / 1e18), 2) as ETH,  -- Total Deposit ETH Value\
  count(distinct "from") as users -- Total Unique Deposit Users\
from\
  ethereum."transactions"\
where\
  "to" = '\\xFF1F2B4ADb9dF6FC8eAFecDcbF96A2B351680455' -- zk.money Aztec V2\
  and substring(data,1,4) = '\\x7ff48afb' -- depositPendingFunds function\
  and value > 0 -- ONLY ETH deposit is counted, DAI/WBTC are excluded \
  and success\
group by\
  day}