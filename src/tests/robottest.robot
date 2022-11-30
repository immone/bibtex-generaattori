*** Settings ***
Resource  resource_sample.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Go To Main Page And Check Title
    Go To Main Page
    Main Page Should Be Open

Go To Send Page And Check Title
    Go To Send Page
    Send Page Should Be Open
