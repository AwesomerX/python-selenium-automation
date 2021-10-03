# Created by Chopp at 9/25/2021
Feature: Test cases for search functionality

  Scenario: User can search for coffee on Amazon
    Given Open Amazon homepage
    When Input coffee into amazon search
    When Click on amazon search icon
    Then Verify "coffee" text is shown