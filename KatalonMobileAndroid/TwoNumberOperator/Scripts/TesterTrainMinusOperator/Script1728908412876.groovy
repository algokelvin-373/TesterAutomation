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
import org.junit.Assert as Assert
import org.openqa.selenium.Keys as Keys
import org.xbill.DNS.TXTRecord as Keys

'Start to open APK Two Number Operator'
Mobile.startApplication(GlobalVariable.pathAPK, false)

'Given Delay 5 Seconds'
Mobile.delay(5, FailureHandling.STOP_ON_FAILURE)

'Create Object for Data EditText_InputNumber1'
TestObject editTextNumber1 = findTestObject('EditText_InputNumber1')

'Set Value 500 for Data Number 1'
Mobile.setText(editTextNumber1, '500', 10)

'Create Object for Data EditText_InputNumber2'
TestObject editTextNumber2 = findTestObject('EditText_InputNumber2')

'Set Value 200 for Data Number 2'
Mobile.setText(editTextNumber2, '200', 10)

TestObject btnMinus = findTestObject('Button_MinusOperator')

Mobile.tap(btnMinus, 10)

'Given Delay 2 Seconds'
Mobile.delay(2, FailureHandling.STOP_ON_FAILURE)

'Create Object for Data TextView_Result'
String txtResult = Mobile.getText(findTestObject('TextView_ResultOperator'), 10)

assert txtResult == '300.0'

'Given Delay 2 Seconds'
Mobile.delay(2, FailureHandling.STOP_ON_FAILURE)

Mobile.closeApplication()

