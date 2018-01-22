Feature: FunctionalTest
  This feature deals with Acuo functional test.

  Scenario:Full Functional test with Acuo
    Given Navigate to login prompt
    And I enter the username and password
    And I click login button
    And I should see the dashboard
    And Navigate to upload page
#    And I want to upload a portfolio
#    And I want to valued a portfolio
#    And I want to generate a MarginCalls
#    Then I want to send MarginCalls