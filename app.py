
from flask import Flask, jsonify, request
from flask import Flask, flash, request, redirect, url_for, render_template, session
import json
from web3 import Web3
import re
app = Flask(__name__)
ganache_url = "HTTP://127.0.0.1:7545"

web3= Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
s=0
# abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"string","name":"rname","type":"string"}],"name":"addReportEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tid","type":"uint256"},{"indexed":false,"internalType":"string","name":"tName","type":"string"}],"name":"addTaskEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"avgRating","type":"uint256"}],"name":"reviewReportEvent","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ReportIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"TaskIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalRating","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalwSubmittedReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"string","name":"rname","type":"string"},{"internalType":"string","name":"_content","type":"string"}],"name":"addReport","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"rAddress","type":"address"},{"internalType":"string","name":"tName","type":"string"},{"internalType":"string","name":"tDescription","type":"string"},{"internalType":"uint256","name":"minAmtForTask","type":"uint256"}],"name":"addTask","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllReportIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllTaskIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getAllWorkersForReport","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReport","outputs":[{"components":[{"internalType":"string","name":"reportName","type":"string"},{"internalType":"string","name":"reportContent","type":"string"},{"internalType":"address","name":"ReportCreatorAddress","type":"address"},{"internalType":"uint256","name":"avgRating","type":"uint256"},{"internalType":"uint256","name":"totalReviews","type":"uint256"},{"internalType":"address[]","name":"workers","type":"address[]"}],"internalType":"struct CrowdSource.Report","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReportAvgRating","outputs":[{"internalType":"string","name":"rname","type":"string"},{"internalType":"uint256","name":"avgrating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReportsSubmittedByWorker","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tid","type":"uint256"}],"name":"getTask","outputs":[{"components":[{"internalType":"string","name":"taskTitle","type":"string"},{"internalType":"string","name":"taskDescription","type":"string"},{"internalType":"address","name":"taskCreatorAddress","type":"address"},{"internalType":"uint256","name":"minAmt","type":"uint256"}],"internalType":"struct CrowdSource.Task","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rIdSubmittedByWorkerAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"uint256","name":"reportId","type":"uint256"},{"internalType":"uint256","name":"wRating","type":"uint256"},{"internalType":"string","name":"wComments","type":"string"}],"name":"reviewReport","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"string","name":"rname","type":"string"}],"name":"addReportEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"tid","type":"uint256"},{"indexed":false,"internalType":"string","name":"tName","type":"string"}],"name":"addTaskEvent","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"rid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"avgRating","type":"uint256"}],"name":"reviewReportEvent","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ReportIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"TaskIds","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalRating","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalwSubmittedReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"string","name":"rname","type":"string"},{"internalType":"string","name":"_content","type":"string"}],"name":"addReport","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"rAddress","type":"address"},{"internalType":"string","name":"tName","type":"string"},{"internalType":"string","name":"tDescription","type":"string"},{"internalType":"uint256","name":"minAmtForTask","type":"uint256"}],"name":"addTask","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getAllReportIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getAllTaskIds","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getAllWorkersForReport","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getCurrentWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReport","outputs":[{"components":[{"internalType":"string","name":"reportName","type":"string"},{"internalType":"string","name":"reportContent","type":"string"},{"internalType":"address","name":"ReportCreatorAddress","type":"address"},{"internalType":"uint256","name":"avgRating","type":"uint256"},{"internalType":"uint256","name":"totalReviews","type":"uint256"},{"internalType":"address[]","name":"workers","type":"address[]"}],"internalType":"struct CrowdSource.Report","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"}],"name":"getReportAvgRating","outputs":[{"internalType":"string","name":"rname","type":"string"},{"internalType":"uint256","name":"avgrating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getReportsSubmittedByWorker","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tid","type":"uint256"}],"name":"getTask","outputs":[{"components":[{"internalType":"string","name":"taskTitle","type":"string"},{"internalType":"string","name":"taskDescription","type":"string"},{"internalType":"address","name":"taskCreatorAddress","type":"address"},{"internalType":"uint256","name":"minAmt","type":"uint256"}],"internalType":"struct CrowdSource.Task","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalReports","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getTotalTasks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerComments","outputs":[{"internalType":"string","name":"wComments","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"rid","type":"uint256"},{"internalType":"address","name":"worker","type":"address"}],"name":"getWorkerRating","outputs":[{"internalType":"uint256","name":"wRating","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"rIdSubmittedByWorkerAddress","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"wAddress","type":"address"},{"internalType":"uint256","name":"reportId","type":"uint256"},{"internalType":"uint256","name":"wRating","type":"uint256"},{"internalType":"string","name":"wComments","type":"string"}],"name":"reviewReport","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3.toChecksumAddress('0xd9145CCE52D386f254917e481eB44e9943F39138')
contract  = web3.eth.contract(address=address, abi=abi)
# web3.eth.defaultAccount = web3.eth.accounts[0] 
web3.eth.defaultAccount = "0x3cBc9C4A7911a29E07186a6Eec2c8eb835A371af"
userAddress = web3.eth.defaultAccount
# print(web3.eth.defaultAccount)
# print(type(web3.eth.defaultAccount)) #string
workerData={'workerAddress':{},
            'reportIdsOfWorker':None,
            }

reportData={'reportId':None,
            'reportName':None,
            'reportContent':None,
            'reportAvgRating':None,
            'reportTotalReviews':None,
            'workersOfThisReport':None,
            'reportReviewData':{}
}

def createTask(taskName,taskDescription,taskAmount):
    print(taskName,taskDescription,taskAmount)
    taskName = taskName
    taskDescription = taskDescription
    taskAmount = int(taskAmount)
    tx_hash = contract.functions.addTask(userAddress,taskName,taskDescription,taskAmount).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    s=1
    print('Task successfully created')
def getTask(tid):
    task= contract.functions.getTask(tid).call()
    print(task)
    return task

def getReportsCount(): #return integer
    numOfReports=contract.functions.getTotalReports().call()
    return numOfReports

def getAllReportIds(): #returns list
    report_ids= contract.functions.getAllReportIds().call()
    # print('reports IDs are',report_ids)
    return report_ids

def getReportAvgRating(report_id):
    reportRating = contract.functions.getReportAvgRating(report_id).call()
    # reviewData['reportRating'] = reportRating
    return reportRating 

def getCurrentWorkerComments(report_id):
    workerComments= contract.functions.getCurrentWorkerComments(report_id).call()
    # reviewData['reportComments'] = workerComments
    return workerComments

def getCurrentWorkerRating():
    report_id = input('Enter report_id: ')
    workerRatings = contract.functions.getCurrentWorkerRating(report_id).call()
    return workerRatings

def getAnyWorkerComments():
    worker_eth_address =  input('Enter eth address: ')
    report_id = input('Enter report_id: ')
    return contract.functions.getAnyWorkerComments(report_id, worker_eth_address).call()

def getAnyWorkerRating():
    worker_eth_address =  input('Enter eth address: ')
    report_id = input('Enter report_id: ')
    return contract.functions.getAnyWorkerRating(report_id, worker_eth_address).call()

def getAllWorkersForReport():
    report_id = input('Enter report_id: ')
    allWorkers = contract.functions.getAllWorkersForReport(report_id).call()
    return allWorkers

def getReportIdsByWorkerAddress():
    report_ids=contract.functions.getReportsSubmittedByWorker().call()
    return report_ids

def getWorkerCompleteData(wAddress):
    workerData['workerAddress']=wAddress
    rIdsOfWorker=getReportIdsByWorkerAddress()
    workerData['reportIdsOfWorker'] = rIdsOfWorker
    print(workerData)

def addReport(name,content):
    reportName=name
    reportContent = content
    tx_hash = contract.functions.addReport(userAddress,reportName,reportContent).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('Report successfully added')
    # print('New count of Reports: ', getReportsCount())

reviewData={'reportRating':None,
            'reportComments':None}
def getReport(rid):
    report=contract.functions.getReport(rid).call()
    rName,rContent,rWorkerAddress,rAvgRating,rTotalReviews,rSubmittedWorkers=report
    reviewData['reportRating'] = getReportAvgRating(rid)
    reviewData['reportComments'] = getCurrentWorkerComments(rid)
    reportData['reportId']=rid
    reportData['reportName']=rName
    reportData['reportContent']=rContent
    reportData['reportAvgRating']=rAvgRating
    reportData['reportTotalReviews']= rTotalReviews
    reportData['workersOfThisReport']= rSubmittedWorkers
    reportData['reportReviewData'] = reviewData
    print(reportData)
    return reportData
def reviewReport():
    report_id = int(input('Enter report_id: '))
    print('Please review the report and rate it on scale of 1-5 and share feedback')
    print(getReport(report_id))
    report_rating = int(input('Enter rating: '))
    report_feedback = input('Enter feedback: ')
    tx_hash = contract.functions.reviewReport(userAddress,report_id,report_rating,report_feedback).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)
    print('Successfully reviewed the report')
@app.route('/auth',methods=('GET', 'POST'))
def auth():
    if request.method == 'POST':
        rgmail= request.form['email']
        print(rgmail)
        rtype = request.form['type']
        obj = re.search(r'[\w.]+\@gitam.edu+', rgmail)
        if obj:
            return redirect("/requestordashboard")
        else:
            return redirect("/workerdashboard")
    return render_template('signpage.html')
@app.route('/workerdashboard',methods=('GET', 'POST'))
def workerdashboard():
  if request.method == 'POST':
    rname= request.form['reportname']
    rdes = request.form['reportdes']
    print(rname,rdes)
    addReport(rname,rdes)
  return render_template('wdashboard.html')
@app.route('/requestordashboard',methods=('GET', 'POST'))
def requestordashboard():
  if request.method == 'POST':
    tname= request.form['taskname']
    tdes = request.form['taskdes']
    tamount=request.form['taskamount']
    print(tname,tdes,tamount)  
    createTask(tname,tdes,tamount)
  return render_template('rdashboard.html',s=s)
@app.route('/')
def main():
  return render_template('signpage.html')
if __name__ == '__main__':
  app.run()
 