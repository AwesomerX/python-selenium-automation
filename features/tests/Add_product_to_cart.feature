#
Feature: Amazon functionality test cases

  Scenario: User can add product to the cart
    Given Open Amazon homepage
    When Input coffee mug into amazon search
#    When Click on Amazon search icon
    When Click on first product
    When Store product name
    When Click on Add to cart button
    When Open cart page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product

