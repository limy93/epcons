Feature: User Authentication on Login Page
  As a user
  I want to be able to log in
  So that I can access personalized features and my user profile

  @requires_login
  Scenario: Successful login with correct credentials
    Given I am on the login page
    When I enter valid credentials
    And I submit the login form
    Then I should be redirected to the dashboard

  @requires_login
  Scenario: Unsuccessful login with incorrect credentials
    Given I am on the login page
    When I enter invalid credentials
    And I submit the login form
    Then I should see an error message indicating login failure