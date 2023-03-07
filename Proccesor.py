########Librerías
import time
import sys
import os
import shutil
import glob
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

import raas

workday_base_url='https://wd2-impl-services1.workday.com/ccx/oauth2/bnb_dpt1/token'
workday_tenant_name='bnb_dpt1'
raas_client_id='ZDAxYWQzMmItMDA0ZS00NWZiLWI5ZjMtYTlkOTRmNmI4ODI4'
raas_client_secret='1372s6aimipzllr3cpgryqwlqydhed054fuajfnnidt95d1r7gi3wiyovc4hl9sdiazueururcfg6ss6yd0o9jy5ammeepqueidr'
raas_refresh_token='i3pn4wz8eaf9tvilqhbm0o4d4asa4q4ih67ugef9h8r5alqrumdgpb80bahe0uskonbr042av0mgjsmdocfz2q6un7mq1clnsyy'

# initialize the RaaS class with your credentials
r = raas.RaaS(workday_base_url,workday_tenant_name,raas_client_id,raas_client_secret,raas_refresh_token)

# exchange refresh token for bearer token
r.create_bearer_token()

# run a web-enabled report
data = r.get_report(url='https://wd2-impl-services1.workday.com/ccx/service/customreport2/bnb_dpt1/lmcneil/BNB_Classes_Info?format=xml')

df = pd.DataFrame(data)


'''
df = pd.read_excel('BNB_Classes_Info.xlsx', engine="openpyxl")
print(df)
'''