# Created by Chopp at 9/26/2021
Feature: # Test cases for functionality
  # Amazon Cancel order feature

  Scenario: User can search for Help on Amazon
    Given Open Amazon Help page
    When Input Cancel order into Amazon Help Search
    Then Verify Cancel Items or Orders text is displayed
