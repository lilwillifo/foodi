Feature: Diary

  Scenario: A user can save a food to their diary

    Given I empty the "User" table

    And I create the following users:
      | id | email             | username | password  |
      | 1  | annie@example.com | Annie    | pAssw0rd! |

    And I log in with username "Annie" and password "pAssw0rd!"

    And I search for "banana"

    When I click "Add To My Diary"

    Then it has been added to my diary
