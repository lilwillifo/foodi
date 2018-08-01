Feature: See data on my analytics page
As a standard user
I want to see my top 5 foods
So I can know my eating habits

Background: There are foods in the system
    Given there are a number of foods:
        |    food               |
        |    apple              |
        |    banana             |
        |    carrot             |
        |    orange             |
        |    grape              |
        |    tomato             |

    And there is a profile with top 5 five foods:
        |    username      |  foods                               |
        |    Margaret      |  banana, carrot, apple, orange, grape|

Scenario: See my top 5 foods
    Given I am a logged in user
    When I go to my analytics
    Then I see my top 5 foods
