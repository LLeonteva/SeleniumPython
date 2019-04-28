# Created by lleonteva at 2019-04-23
Feature: HW1: Amazon tests

  # User can search for solutions of Cancelling an order on Amazon
  Scenario: Search Help returns correct result
    Given Open Amazon page
    When Click on Help navigation link
    And Input Cancel order into search help field
    And Click Go button
    Then Result contains Cancel Items or Orders

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click on Orders navigation link
    Then Sign in page is opened

  Scenario: Hamburger menu can be opened and closed
    Given Open Amazon page
    When Click on Hamburger menu icon on the left
    Then Verify ‘Shop by category’ text is present
    When Click on closing X of the side menu
    When Click on ‘Try Prime’ from Amazon logo
    Then Amazon Prime page is opened