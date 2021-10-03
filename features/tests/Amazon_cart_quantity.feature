# Created by Chopp at 9/29/2021
# Create a test case with BDD for HW3 verifying cart is empty
Feature: Amazon test cases (cart)

  Scenario: Check if Amazon Cart is empty
    Given Open Amazon homepage
    When Click on cart icon
    Then Verify Amazon Cart is empty

    # Works