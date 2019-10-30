Feature: Movement

Scenario Outline: Start moving
    Given the user starts moving from location to another 
    When the user starts moving
    Then the name <location> where he is located
    And the target <target>


Examples:
    | location    |  target    |
    | woonkamer   |  hal       |
    | hal         |  keuken    |
    | keuken      |  woonkamer |