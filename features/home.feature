Feature: Home Page Accessibility
  As a visitor
  I want to visit the home page
  So that I can confirm the web application is accessible

  Scenario: The home page loads correctly
    Given I am on the home page
    Then I should see the page title "Home"

  Scenario: Navigation to the About page
    Given I am on the home page
    When I click on the "About" button
    Then I should be redirected to the About page

  Scenario: Navigation to the Explore Countries page
    Given I am on the home page
    When I click on the "Explore Countries" button
    Then I should be redirected to the Explore Countries page
