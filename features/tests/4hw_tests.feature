# Created by lleonteva at 2019-05-16
Feature: HW4. Amazon tests

  Scenario: User can select single color of backpack
    Given Open page for product B07PPN4DZ2
    When Click on color Black
    Then Verify color is updated to Black


  Scenario Outline: User can select backpack colors
    Examples:
    |color    |
    |Black    |
    |Blue     |
    |Wine Red |
    Given Open page for product B07PPN4DZ2
    When Click on color <color>
    Then Verify color is updated to <color>


  Scenario: User can loop through backpack colors
    Given Open page for product B07PPN4DZ2
    Then Verify user can select backpack colors


