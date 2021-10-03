# Created by Chopp at 9/28/2021
Feature: Amazon Bestsellers functionality test

  Scenario: There are 5 bestsellers links
    Given Open Amazon Bestsellers
    Then Verify there are 5 links
