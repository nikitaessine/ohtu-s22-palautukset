*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  villev
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Registration Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  v
    Set Password  ville123
    Set Password Confirmation  ville123
    Submit Registration Credentials
    Register Should Fail With Message  Username is too short!

Register With Valid Username And Too Short Password
    Set Username  villev
    Set Password  vil
    Set Password Confirmation  vil
    Submit Registration Credentials
    Register Should Fail With Message  Password is too short!

Register With Nonmatching Password And Password Confirmation
    Set username  villev
    Set Password  ville123
    Set Password Confirmation  villeeeee
    Submit Registration Credentials
    Register Should Fail With Message  Psw and pswconf dont match

Login After Succesful Registration
    Set Username  villev
    Set Password  ville12345
    Set Password Confirmation  ville12345
    Submit Registration Credentials 
    Go To Login Page
    Set Username  villev
    Set Password  ville12345
    Submit Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  villev
    Set Password  ville12345
    Set Password Confirmation  ville12345
    Submit Registration Credentials 
    Go To Login Page
    Set Username  villev
    Set Password  ville1234
    Submit Login
    Login Should Fail With Message  Invalid username or password

    





*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}