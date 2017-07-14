import requests
# Python Script to get case details of
# Supreme Court for a given set of parameters.
# @uthor: Shivank Awasthi
# TimeStamp: 13th February, 2017 17:33
from bs4 import BeautifulSoup

# necessary package imports

selType = raw_input('Enter case type:')
caseNo = raw_input('Enter case number:')
selYear = raw_input('Enter year:')

# input from user about the case details

def get_case_status(selType, caseNo, selYear):
    res = requests.post('http://courtnic.nic.in/supremecourt/casestatus_new/querycheck_new.asp',data = {'seltype':selType,'txtnumber':caseNo,'selcyear':selYear})
# using post method of requests to submit form data.
    soupBody = BeautifulSoup(res.text,'html.parser')
    allText = soupBody.get_text()
# using BeautifulSoup to extract the text in web page.    
    if "DISPOSED" not in allText:
        is_disposed = False
    else:
        is_disposed = True
# Searching for disposed keyword in the text obtained.
    textTokens = allText.split("\n")
# Simply on observing the text for different queries I found the pattern of spaces
# between desirable strings. On this basis I searched for one keyword's index and
# then used it to obtain all strings. 
    firstPos = textTokens.index("Vs.")
# found index of Vs.
    petitioner = textTokens[firstPos-3]
    respondent = textTokens[firstPos+3]
# found petitioner and respondent on the basis of position of Vs.
    secondPos = firstPos + 23
    pet_advocate = textTokens[secondPos]
    res_advocate = textTokens[secondPos+4]
# found the advocates also using the same principle
    dicti = {'is_disposed':is_disposed,'petitioner':petitioner,'respondent':respondent,'pet_advocate':pet_advocate,'res_advocate':res_advocate}
    return dicti
# additional statements for testing of function

test = get_case_status(selType,caseNo,selYear)
print(test)




