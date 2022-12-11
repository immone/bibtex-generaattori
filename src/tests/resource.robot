*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${SEND URL}  http://${SERVER}/type

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Main Page
    Go To  ${HOME URL}

Go To Send Page
    Go To  ${SEND URL}

Main Page Should Be Open
    Title Should Be  Bibtex generaattori

Send Page Should Be Open
    Title Should Be  Tallenna viite

Send Reference
    [Arguments]  ${AUTHOR}  ${TITLE}  ${YEAR}
    Input Text  name=author  ${AUTHOR}
    Input Text  name=title  ${TITLE}
    Input Text  name=year  ${YEAR}
    Click Button  submit

Delete Reference
    Click Button  delete
    Click Button  delete_check
