
# Introduction 

This is a mobile testing framework that automates E2E user workflows using python, pytest, appium client and android emulator. 
The workflow involves comprehensive list of UI interactions. This is built to be robust and scalable. 
By wrapping dependencies and utilizing page objects, we can add functionality, simplify test flows, and 
protect against change. If a new tool becomes available, all tests will remain relevant with minor changes.

![](images/automation.gif)

# Setup Choice 

`pytest` - This is a really mature test runner for Python Programming Language

`appium` - Technology leader in mobile automation for both android and iOS

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

Step 2 - Make sure you have `python3` install in the system

Step 3 - Git clone this project, setup a virtual environment and install all the dependencies 

    git clone <project_url>

    cd stock-simulator-automation
    
    pip3 install virtualenv
    
    virtualenv venv 
    
    source venv/bin/activate
    
    pip install -r requirements.txt

Step 4 - Download Android Studio and make sure `Pixel 2 API 30` virtual device is setup 

![](images/device-configuration.png)
![](images/pixel-2-device.png)


Step 5 - Make sure `ANDROID_HOME` and `JAVA_HOME` are setup in your environment 

    export ANDROID_HOME=/Users/<user_name>/Library/Android/sdk/
    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-18.0.1.jdk/Contents/Home/


# Running the tests 

| Scenario |           command                                      |
|------|:------------------------------------------------------:|
| Buy a stock | py.test -s tests/test_buy_and_verify_stock_purchase.py |
| Access news feed about a company |   py.test -s tests/test_verify_news_feed_company.py  |
| Add a company to watchlist     |    py.test -s tests/test_add_and_verify_watchlist.py   |
