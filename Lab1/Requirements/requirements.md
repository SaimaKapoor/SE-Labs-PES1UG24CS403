# Requirements Table

## Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall allow subscribers to view and customize the products included in their upcoming monthly subscription box. | High | **Pass:** Subscriber's selected products are saved and displayed in their upcoming box. **Fail:** Changes are not saved or incorrect products are displayed. | Allows subscribers to personalize their monthly boxes according to their preferences. |
| FR-002 | Functional | The system shall allow subscribers to swap an item in their monthly box with another eligible product before the customization deadline. | High | **Pass:** The selected item is replaced and the updated selection is reflected in the fulfillment record. **Fail:** The original item remains or the swap is accepted after the deadline. | Provides flexibility while ensuring fulfillment has accurate product information. |
| FR-003 | Functional | The system shall allow subscribers to pause or skip an upcoming billing cycle before the applicable deadline. | High | **Pass:** The billing cycle is marked as paused or skipped and no box is scheduled for that cycle. **Fail:** The subscriber is charged or a box is scheduled despite the request. | Gives subscribers control over their subscription and prevents unwanted deliveries. |
| FR-004 | Functional | The system shall allow the Fulfillment Lead to view the fulfillment manifest containing the products and delivery details for upcoming subscription boxes. | High | **Pass:** The Fulfillment Lead can view an accurate manifest of boxes scheduled for fulfillment. **Fail:** Boxes or product selections are missing or incorrect. | Enables the fulfillment team to prepare accurate monthly shipments. |
| FR-005 | Functional | The system shall update the fulfillment manifest whenever a subscriber's eligible box customization is successfully changed. | Medium | **Pass:** The manifest reflects the subscriber's latest product selection. **Fail:** The manifest continues to show outdated selections. | Keeps fulfillment information synchronized with subscriber changes. |

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Performance | The fulfillment manifest generator shall generate the manifest for up to 10,000 monthly subscription boxes in under 1 minute under peak-load conditions. | High | **Pass:** Manifest generation completes within 60 seconds during a 10,000-box test. **Fail:** Generation takes longer than 60 seconds. | Ensures the system can support large-scale monthly fulfillment operations. |
| NFR-002 | Security | The system shall ensure that subscribers can access and modify only their own subscription and billing-cycle information. | High | **Pass:** Unauthorized attempts to access another subscriber's information are denied. **Fail:** A subscriber can view or modify another subscriber's data. | Protects subscriber information and prevents unauthorized subscription changes. |
