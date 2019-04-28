# Created by lleonteva at 2019-04-26
Feature: HW1: Amazon tests

  Scenario: Verify 4 benefits cards are displayed on Amazon Prime page
    Given Open Amazon page
    When Click on ‘Try Prime’ from Amazon logo
    Then Verify 4 benefits cards are displayed on Prime page

  Scenario: Ad feedback form can be opened
    Given Open Amazon page
    When Click on ‘Ad feedback’ link
    Then Ad feedback form is opened
