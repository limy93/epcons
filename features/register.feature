Feature: User Registration on Registration Page
  As a potential user
  I want to be able to register an account
  So that I can access personalized features and my user profile

  Scenario: Successful registration with valid information
    Given I am on the registration page
    When I enter valid registration information
    And I submit the registration form
    Then I should be registered and redirected to the dashboard

  Scenario: Unsuccessful registration with invalid information
    Given I am on the registration page
    When I enter invalid registration information
    And I submit the registration form
Then I should see an error message indicating registration failure