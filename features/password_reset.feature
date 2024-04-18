Feature: Password Reset Functionality
  As a user
  I want to be able to reset my password simply
  So that I can recover access to my account if I forget my password

  Scenario: Simple Password Reset Process
    Given I am on the "Password Reset" page
    When I submit a valid email address for password reset
    Then I should see a simplified confirmation message