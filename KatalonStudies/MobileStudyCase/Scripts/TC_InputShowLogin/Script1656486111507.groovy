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

'Start run app'
Mobile.startApplication('/Users/kelvin-tsm/Kelvin/MyProject/play-tester-automation/KatalonStudies/android-input-output-debug.apk', 
    false)

'Input Name Login'
Mobile.sendKeys(findTestObject('page_input_login/edt_name_login'), GlobalVariable.SAMPLE_NAME, FailureHandling.STOP_ON_FAILURE)

'Click Login to Show Data Login'
Mobile.tap(findTestObject('page_input_login/btn_login'), 5)

'Get Data Login from Input Data Name'
def login_name = Mobile.getText(findTestObject('page_show_login/txt_login_name'), 5)

'Verify Name Login'
Mobile.verifyEqual(login_name, GlobalVariable.SAMPLE_NAME)

'Close app'
Mobile.closeApplication()

