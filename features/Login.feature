Feature: Login in http://practice.automationtesting.in/


  @SuccesfullLogin
  Scenario Outline: The user do a login
    Given launch chrome browser in <web>
    When user click on My Account Menu
    When enter <email> in email textbox
    When enter <password> textbox
    When click on login button
    Then User must successfully login to the web page
    And close browser

    Examples:
      | web                                   | email         | password            |
      | http://practice.automationtesting.in/ | zxc@gmail.com | laseguridadantetodo |


  @FailLogin
  Scenario Outline: The user fail doing a login
    Given launch chrome browser in <web>
    When user click on My Account Menu
    When enter <email> in email textbox
    When enter <password> textbox
    When click on login button
    Then Proper error must be displayed <error>
    And close browser

    Examples:
      | web                                   | email          | password                 | error                                              |
      | http://practice.automationtesting.in/ | zxca@gmail.com | laseguridadantetodo      | A user could not be found with this email address. |
      | http://practice.automationtesting.in/ | zxc@gmail.com  | estoesunaclaveincorrecta | The password you entered for the username          |



