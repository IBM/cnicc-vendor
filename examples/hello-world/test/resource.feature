Feature: ALM Lifecycle test  

Scenario: Test install
Given the ARM database is initialized
When I call the "Install" transition on resource "test-1" with type "resource::hello-world::1.0"
And that transition completes
Then the output contains "'requestState': 'COMPLETED'"

Scenario: Test install
Given the ARM database is initialized
When I call the "Install" transition on resource "test-1" with type "resource::hello-world::1.0"
And that transition completes
And I call the "Start" transition on resource "test-1" with type "resource::hello-world::1.0"
And that transition completes
Then the output contains "'requestState': 'COMPLETED'"
