*** Settings ***
Library    rf.AddressBook
Library    Collections
Suite Setup    Init Fixtures
Suite Teardown    Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=    Get Contact List
    ${contact}=    New Contact     First Name 1    Last Name 1    Address 1
    Create Contact    ${contact}
    ${new_list}=    Get Contact List
    APPEND TO LIST    ${old_list}    ${contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}

Modify contact
    ${old_list}=    Get Contact List
    ${len}=   Get Length    ${old_list}
    ${index}=    Evaluate    random.randrange(${len})    random
    ${contact_old}=    get from list     ${old_list}    ${index}
    ${contact_new}=    Modified Contact     First Name 2    Last Name 2    Address 2    ${contact_old}
    Modify Contact    ${contact_old}    ${contact_new}
    ${new_list}=    Get Contact List
    REMOVE VALUES FROM LIST    ${old_list}    ${contact_old}
    APPEND TO LIST    ${old_list}    ${contact_new}
    Log list    ${old_list}
    Log list    ${new_list}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}

Delete contact
    ${old_list}=    Get Contact List
    ${len}=   Get Length    ${old_list}
    ${index}=    Evaluate    random.randrange(${len})    random
    ${contact}=    get from list     ${old_list}    ${index}
    Delete Contact    ${contact}
    ${new_list}=    Get Contact List
    REMOVE VALUES FROM LIST    ${old_list}    ${contact}
    Contact Lists Should Be Equal    ${new_list}    ${old_list}
