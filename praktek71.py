import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#client.open("koneksi").add_worksheet(title="worksheet baru",rows=1000,cols=20)
worksheets = client.open("koneksi").worksheet("data_orang")
#client.open("koneksi").del_worksheet(worksheets)

list_data = worksheets.get_all_records()

dataframe = pd.DataFrame(list_data)

#data_baru = pd.DataFrame.from_records({'no_wa':['628565756437'], 'nama':['lala'], 'pesan':['hello'], 'status':['3']})
#dataframe = pd.concat([dataframe,data_baru])

#dataframe.loc[dataframe['no_wa'] == 628565756437, ['status']] = 4
#dataframe.loc[dataframe['no_wa'] == 628565756437, ['nama']] = 'lala poo'
#set_with_dataframe(worksheets,dataframe)
#print(dataframe) 

filterData = 1+dataframe[(dataframe['no_wa'] == 6281271459870) & (dataframe['status'] == 1) ].index.item()
worksheets.delete_row(filterData)
 
print(filterData)