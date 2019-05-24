# Created by lleonteva at 2019-05-23
Feature: Password Assistance tests

  Scenario: Invalid Forgot Password request
    Given Open Amazon page
    When Hover over Account&Lists link
    And Click on Account&Lists SignIn btn
    And Click on Forgot Password link
    And Enter invalid email abcd
    And Click on Continue button
    Then Verify error message There was a problem is presented


