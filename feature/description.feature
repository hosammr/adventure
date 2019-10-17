Feature: Description

Scenario Outline: asking description
  Given the user asks for description
  When the user asks for description
  Then the return should be <location>
  And the description <description>


  Examples:
      | location    |  description                                      |  item         |
      | woonkamer   |een gezellige ruimte                               | sleutel       |
      | hal         |een ruimte die andere ruimtes met elkaar verbind   |               |
      | keuken      |een ruimte om te koken                             | exit naar hal |
  
  