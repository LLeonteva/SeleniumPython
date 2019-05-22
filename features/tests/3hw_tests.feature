# Created by lleonteva at 2019-05-08
Feature: HW3. Amazon tests

  Scenario: User can open registration page in Amazon
    Given Open Amazon page
    When Click on Accounts and Lists navigation link
    Then Sign in page is opened
    When Click on 'Create your Amazon Account' button
    Then Sign up page is opened


  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on Cart icon
    Then Verify 'Your Shopping Cart is empty.' is presented