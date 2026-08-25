# Use-Case Flow Specification

## Use Case: Customize Monthly Subscription Box

### Primary Actor
Subscriber

### Preconditions

1. The subscriber has an active subscription.
2. The subscriber is logged into the subscription box portal.
3. The upcoming billing cycle is still open for customization.
4. The subscriber has an upcoming subscription box scheduled.

### Postconditions

1. The subscriber's updated product selections are saved successfully.
2. The upcoming subscription box reflects the updated selections.
3. The fulfillment information is updated with the latest product selections.

### Main Success Scenario

1. The subscriber logs into the subscription box portal.
2. The subscriber opens their upcoming monthly subscription box.
3. The system displays the products currently selected for the upcoming box.
4. The subscriber modifies one or more product selections.
5. The system validates that the customization deadline has not passed.
6. The system validates that the selected products are eligible for the subscription box.
7. The subscriber confirms the updated selections.
8. The system saves the updated product selections.
9. The system updates the fulfillment information with the new selections.
10. The system displays a confirmation that the subscription box has been successfully customized.

### Alternate Flow

**A1. Customization Deadline Has Passed**

1. The subscriber attempts to modify the upcoming subscription box.
2. The system checks the customization deadline.
3. The system determines that the customization deadline has passed.
4. The system prevents the subscriber from making changes to the current billing cycle.
5. The system informs the subscriber that customization is no longer available for the current cycle.
6. The subscriber may continue without making changes or customize a future eligible billing cycle.
