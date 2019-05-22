# Created by lleonteva at 2019-05-16
Feature: Tests using Actions in Home page

  Scenario: User can SignIn from Account&Lists nav link
    Given Open Amazon page
    When Hover over Account&Lists link
    And Click on Account&Lists SignIn btn
    Then Sign in page is opened

  Scenario: User can click ‘Learn more’ from language selection
    Given Open Amazon page
    When Hover over navig Lang link
    And Click on 'Learn more' link
    Then Language page is opened
    And Verify 'About the Spanish Language Experience on Amazon.com' is presented in Lang page

  Scenario: User can click on ‘Try Prime’ button in popup from ‘Try Prime’ navig link
    Given Open Amazon page
    When Hover over navig 'Try Prime' link
    And Click on 'Try Prime' btn
    Then Amazon Prime page is opened

