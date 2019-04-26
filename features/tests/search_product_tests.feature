# Created by Liudmila at 04/22/19
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input dress into search field
    And Click on search icon
    Then Product results for dress are shown
    And First result contains dress

  Scenario: User can search for a product on Amazon
    Given Open Amazon page
    When Input phone into Amazon search field
    And Click on Amazon search icon
    Then Amazon product results for phone are shown
    And Amazon first result contains phone

  Scenario: User can see more then 5 items upon search
    Given Open Amazon page
    When Input hat into Amazon search field
    And Click on Amazon search icon
    Then Verify more then 5 items are displayed
