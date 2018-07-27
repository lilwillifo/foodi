Feature: See all of a users foods on diary page
As a standard user
I want to see all my foods
So I can know what I have

Background: There are foods and users in the system
    Given there are a number of foods:
        |    food               |
        |    apple              |
        |    banana             |
        |    carrot             |

    And there are many users, each with different foods:
        |    username           |   foods                      |
        |    BillieJean    |   apple, banana              |
        |    RockyRaccoon  |   apple, carrot              |
        |    MajorTom      |   banana, carrot             |

Scenario: See my foods
    Given I am a logged in user
    When I go to my diary
    Then I see my foods
