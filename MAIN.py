#MADE AND PROGRAMMED BY: SAMUEL MARTINO
#THANKS TO GEOFFREY SMITH
import gspread
import requests
import json
import urllib
import datetime
while True:

    r=requests.get("https://api.vexdb.io/v1/get_rankings?sku=RE-VRC-17-4148").json()
    match=requests.get("https://api.vexdb.io/v1/get_matches?sku=RE-VRC-17-2580").json()



    from oauth2client.service_account import ServiceAccountCredentials
    scope= ['https://spreadsheets.google.com/feeds']
    creds=ServiceAccountCredentials.from_json_keyfile_name('AutoVex.json',scope)
    client=gspread.authorize(creds)
    import pprint
    sheet=client.open('AutoVex').sheet1
    sheet2 = client.open("AutoVex").get_worksheet(1)
    sheet3= client.open("AutoVex").get_worksheet(2)
    pp = pprint.PrettyPrinter()


    AutoVex=sheet.get_all_records()
    for i in range(len(r['result'])):
        sheet.update_cell(1,2,'TEAM NUMBER')
        sheet.update_cell(1, 3, 'RANK')
        sheet.update_cell(1,4,'RESULTS MAY NOT BE CORRECT TIME LAST UPDATED:'+str(datetime.datetime.now()))
        sheet.update_cell(i+2, 2, r['result'][i]['team'])
        sheet.update_cell(i+2, 3, r['result'][i]['rank'])
        sheet.update_cell(1,5,'UPDATE FINISHED AT:'+str(datetime.datetime.now()))
    for i in range(len(match['result'])):
        sheet2.update_cell(1,10,'RESULTS MY NOT BE CORRECT TIME LAST UPDATED'+ str(datetime.datetime.now()))
        sheet2.update_cell(1, 2, 'RED1')
        sheet2.update_cell(1, 3, 'SCORE')
        sheet2.update_cell(1, 4, 'RED2')
        sheet2.update_cell(1, 5, 'SCORE')
        sheet2.update_cell(1, 6, 'BLUE1')
        sheet2.update_cell(1, 7, 'SCORE')
        sheet2.update_cell(1, 8, 'BLUE2')
        sheet2.update_cell(1, 9, 'SCORE')
        sheet2.update_cell(i + 2, 2, match['result'][i]['red1'])
        sheet2.update_cell(i + 2, 3, match['result'][i]['redscore'])
        sheet2.update_cell(i+2, 4,match['result'][i]['red2'])
        sheet2.update_cell(i+2, 5, match['result'][i]['redscore'])
        sheet2.update_cell(i + 2, 6, match['result'][i]['blue1'])
        sheet2.update_cell(i + 2, 7, match['result'][i]['bluescore'])
        sheet2.update_cell(i + 2, 8, match['result'][i]['blue2'])
        sheet2.update_cell(i + 2, 9, match['result'][i]['bluescore'])
        sheet2.update_cell(1,11,'FINISHED UPDATE AT:'+str(datetime.datetime.now()))
    for i in range(len(match['result'])):
        curMatch = datetime.datetime.strptime(match['result'][i]['scheduled'][:-6], "%Y-%m-%dT%H:%M:%S") - datetime.datetime.now()
        hours, remainder = divmod(curMatch.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        timeString = "{0} minutes, {1} seconds".format(minutes, seconds)
        sheet3.update_cell(1,1,'TEAMS:')
        sheet3.update_cell(1, 2, 'TIME:')
        sheet3.update_cell(1,3,'TIMES MAY NOT BE ACCURATE TIME LAST UPDATED:'+str(datetime.datetime.now()))
        sheet3.update_cell(i+2, 2, timeString)
        sheet3.update_cell(i+2, 1, match['result'][i]['red1']+"  "+match['result'][i]['red2']+"  "+match['result'][i]['blue1']+"  "+match['result'][i]['blue2'])
        sheet3.update_celll(1,4,'FINISHED UPDATE AT:'+str(datetime.datetime.now()))


