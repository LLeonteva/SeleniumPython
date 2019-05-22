# Created by lleonteva at 2019-05-15
Feature: Class4. Dress color selection tests

  Scenario: User can select dress color
    Given Open Amazon /Lark-Ro-Sleeveless-Sweetheart-Pockets/dp/B07K16Z8LH/ page
    When Click on color Black
    Then Verify color is updated to Black

  Scenario Outline: User can select dress colors
    Examples:
      |color            |
      |Emerald          |
      |Navy             |
      |Winter White     |
    Given Open Amazon /Lark-Ro-Sleeveless-Sweetheart-Pockets/dp/B07K16Z8LH/ page
    When Click on color <color>
    Then Verify color is updated to <color>


  Scenario: User can loop through dress colors
    Given Open Amazon /Lark-Ro-Sleeveless-Sweetheart-Pockets/dp/B07K16Z8LH/ page
    Then Verify user can select dress colors