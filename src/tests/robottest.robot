*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Go To Main Page And Check Title
    Go To Main Page
    Main Page Should Be Open

Go To Send Page And Check Title
    Go To Send Page
    Send Page Should Be Open

Go To Send Page And Send Reference
    Go To Send Page
    Input Text  name=author  Mikael Agricola
    Input Text  name=title  Abckiria
    Input Text  name=year  1543
    Click Button  submit
    Main Page Should Be Open
    Go To References
    Page Should Contain  Mikael Agricola
    Page Should Contain  Abckiria
    Page Should Contain  1543