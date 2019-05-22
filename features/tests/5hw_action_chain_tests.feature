# Created by lleonteva at 2019-05-16
Feature: Tests using Actions

  Scenario: User can SignIn from Account&Lists nav link
    Given Open Amazon page
    When Hover over Account&Lists link
    And Click on Account&Lists SignIn btn
    Then Sign in page is opened
