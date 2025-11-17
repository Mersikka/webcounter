
*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Counter should be set to the value specified, even when it is initially non-zero
   Go To  ${HOME_URL}
   Click Button  Nollaa
   Click Button  Paina
   Page Should Contain  nappia painettu 1 kertaa
   Input Text  num  10
   Click Button  Aseta
   Page Should Contain  nappia painettu 10 kertaa
