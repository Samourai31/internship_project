
Feature: Test for REELLY filter functionality
  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open Reelly sign in page
    When Click on sign in link
    And Enter an email
    And Enter a password
    And Click on continue button
    And Click on Secondary tab
    And Click on Filter
    And Filter the products by “want to sell”
    And Close the filter panel
    Then Verify all cards have a “for sale” tag