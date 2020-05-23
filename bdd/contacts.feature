Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <last_name>, <first_name>, <address>
  When I add a new contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | last_name | first_name | address |
  | last_name1 | first_name1 | address1 |
  | last_name2 | first_name2 | address2 |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <last_name>, <first_name>, <address>
  When I modify the contact from the list
  Then the new contact list is equal to the old list without the modified contact

  Examples:
  | last_name | first_name | address |
  | last_name_new | first_name_new | address_new |