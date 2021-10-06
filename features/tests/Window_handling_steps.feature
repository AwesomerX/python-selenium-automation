# Created by Chopp at 10/5/2021
Feature: Amazon window handling test case

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original window
    And Click on Amazon Privacy Notice link
    And Switch to new window
    Then Verify Amazon Privacy Notice page is open
    And User can close new window and return to original window