Feature: Login

  Scenario: A user can log into the app

    Given I empty the "User" table

    And I go to the signup page

    And enter a username and password

    Then I have created an account
