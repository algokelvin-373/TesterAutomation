import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys
import groovy.json.JsonOutput as JsonOutput
import groovy.json.JsonSlurper as JsonSlurper

WS.comment('This is a step to CREATE Users')

'To request "CreateUser"'
response = WS.sendRequest(findTestObject('Profile/CreateUser'))

'To show result response from "CreateUser"'
String responseCode = response.getResponseText()

'Inizialize "jsonSlurper"'
def jsonSlurper = new JsonSlurper()

'Convert from textJson to object response'
def object = jsonSlurper.parseText(responseCode)



WS.comment('This is a step to GET Users by ID')

'To request "GetUserById"'
responseGetData = WS.sendRequest(findTestObject('Profile/GetUserById', [('id') : object.id]))

'To check result response code'
WS.verifyResponseStatusCode(responseGetData, 200)

'To verify result "name" response "responseGetData"'
WS.verifyElementPropertyValue(responseGetData, 'response_data.name', 'Reggy Prabowo')

'To verify result "address" response "responseGetData"'
WS.verifyElementPropertyValue(responseGetData, 'response_data.address', 'Tangerang')

'To verify result "description" response "responseGetData"'
WS.verifyElementPropertyValue(responseGetData, 'response_data.description', 'Android Developer')



WS.comment('This is a step to UPDATE Users by ID')

'To request "UpdateUserById"'
responseUpdateData = WS.sendRequest(findTestObject('Profile/UpdateUserById', [('id') : object.id]))

'To check result response code'
WS.verifyResponseStatusCode(responseUpdateData, 200)

'To verify result "name" response "responseGetData"'
WS.verifyElementPropertyValue(responseUpdateData, 'name', 'Miawaug')

'To verify result "address" response "responseGetData"'
WS.verifyElementPropertyValue(responseUpdateData, 'address', 'Jakarta Utara')

'To verify result "description" response "responseGetData"'
WS.verifyElementPropertyValue(responseUpdateData, 'description', 'Gamer Youtuber')



WS.comment('This is a step to DELETE Users by ID')

'To request "DeleteUserById"'
responseDelete = WS.sendRequest(findTestObject('Profile/DeleteUserById', [('id') : object.id]))

'To check result response code from \'DeleteUserById\''
WS.verifyResponseStatusCode(responseDelete, 200)



WS.comment('This is a step to Check Data User has been Deleted')

'To request "GetUserById"'
responseCheckingData = WS.sendRequest(findTestObject('Profile/GetUserById', [('id') : object.id]))

'To check result response code'
WS.verifyResponseStatusCode(responseCheckingData, 200)

'To verify result "status" response "responseCheckingData"'
WS.verifyElementPropertyValue(responseCheckingData, 'status', 'false')
