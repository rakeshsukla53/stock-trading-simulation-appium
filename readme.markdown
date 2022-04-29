
# Introduction 

This is a mobile testing framework that automates E2E user workflows using python, pytest, appium client and android emulator. 
The workflow involves comprehensive list of UI interactions. This is built to be robust and scalable. 
By wrapping dependencies and utilizing page objects, we can add functionality, simplify test flows, and 
protect against change. If a new tool becomes available, all tests will remain relevant with minor changes.

![](images/automation.gif)

# Setup Choice 

`pytest` - This is a really mature test runner for Python Programming Language

`appium` - This technology is a leader in mobile automation because of different language bindings and community support 

`python` - This is also a widely used programming language and easy to learn. The ecosystem is really specifically 
when it comes to test automation  


# Project Structure 


| file_name  |                      description                       |            path |
|------------|:------------------------------------------------------:|----------------:|
| app.py     |          This is a wrapper for appium client           |    /core/app.py |
| common.py  |  This contains all the common functions used by tests  | /core/common.py |
| prop.py    |    This is a placeholder to store global constants     |   /core/prop.py |
| android.py | File contains all the page objects for the application |   /core/prop.py |
| tests/     |            Folder containing all the tests             |   /core/prop.py |

we are running all the tests in Android Emulator and our device is Pixel 2. This is the desired capabilities used in 
the tests. The android APK file is already present in the  `apk` folder.  

android_app = [

    {
        "app": get_current_working_directory(),
        "deviceName": "pixel_2",
        "platformName": "Android",
        "automationName": "uiautomator2",
        "platformVersion": "11.0",
        "new-command-timeout": 120,
        "command-timeout": 120
    }

]

# Setup Instructions 

Step 1 - Install appium `npm install -g appium `

Step 2 - 
