# Created by lleonteva at 2019-05-16
Feature: hw4. WholeFoods Deals

  Scenario: Every product on the page has a text ‘Regular $’ and a product name
    Given Open Amazon /wholefoodsdeals page
    Then Verify every product on the page has 'Regular' text
    Then Verify every product on the page has name