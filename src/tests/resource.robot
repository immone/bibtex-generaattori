*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${SEND URL}  http://${SERVER}/send

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
