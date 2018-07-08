Feature: About
    Faq for freelancers about payments

Scenario: Navigating to freelancer about page
    Given I'm on how it works page
    When I press the get paid button
    Then Get paid on time header is visible

Scenario: Open client about page
    Given I'm on main page
    When I press how it works button
    Then Client faq page is opened