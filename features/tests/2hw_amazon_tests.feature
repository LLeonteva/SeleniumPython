# Created by lleonteva at 2019-04-26
Feature: HW1: Amazon tests

"""
update 05/20: webpage was changed, so TC is not valid any more
  Scenario: Verify 4 benefits cards are displayed on Amazon Prime page
    Given Open Amazon page
    When Click on ‘Try Prime’ from Amazon logo
    Then Verify 4 benefits cards are displayed on Prime page
    """

  Scenario: Ad feedback form can be opened
    Given Open Amazon page
    When Click on ‘Ad feedback’ link
    Then Ad feedback form is opened

  Scenario: An item can be added to the cart
    Given Open page for product B07PPN4DZ2
    When Click Add to cart button
    Then Label 'Added to card' is present
    And Item has been added to the cart