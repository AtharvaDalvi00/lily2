# Firestore Security Specification - Quick Calc Leads

This document outlines the security invariants, validation rules, and the "Dirty Dozen" hostile payloads designed to test our Firestore rules against exploitation attempts.

## 1. Data Invariants
- **Lead Creation**: Anyone (including unauthenticated visitors) can create a lead document because this is a public contact form used to request download links.
- **Lead Access Control**: No client-side users (whether signed-in or not) are allowed to read, update, list, or delete other users' lead submissions. It is a strictly write-only collection from the perspective of client-side queries.
- **Name Validation**: The `name` must be a non-empty string between 1 and 100 characters.
- **Email Validation**: The `email` must be a valid email format string and at most 100 characters.
- **Phone Validation**: The `phone` must be a string containing 10 to 15 characters.
- **Source Identification**: The `source` must be a string identifying the lead origin, limited to 50 characters.
- **Timestamps**: The `submittedAt` field must be present.
- **Payload Strictness**: All specified fields (`name`, `email`, `phone`, `submittedAt`, `source`, `calculations`) must exist and adhere to their types/lengths. No extra ghost fields are permitted.

---

## 2. The "Dirty Dozen" hostile Payloads
The following payloads should be rejected by our Firestore security rules.

### Payload 1: The Ghost Field (Shadow Update)
Attempting to inject an unapproved field to grant administrative or other status.
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": {},
  "isAdmin": true
}
```

### Payload 2: Massive Name Field (Denial of Wallet)
Attempting to overload storage via a massive name payload.
```json
{
  "name": "Jane Doe Jane Doe Jane Doe ... [10,000 characters]",
  "email": "jane@example.com",
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": {}
}
```

### Payload 3: Non-String Email (Type Safety violation)
```json
{
  "name": "Jane Doe",
  "email": 12345,
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": {}
}
```

### Payload 4: Invalid/Short Phone Number
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "123",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": {}
}
```

### Payload 5: Missing Required Field (Name)
```json
{
  "email": "jane@example.com",
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": {}
}
```

### Payload 6: Invalid Format / Missing calculations
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator"
}
```

### Payload 7: Huge Phone Number
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "12345678901234567",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": {}
}
```

### Payload 8: Null values for properties
```json
{
  "name": null,
  "email": "jane@example.com",
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": {}
}
```

### Payload 9: Invalid/Excessive Source length
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "source_source_source_source_source_source_source_source_source_source_source_source_",
  "calculations": {}
}
```

### Payload 10: Calculations parameter is not a Map
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "9876543210",
  "submittedAt": "2026-07-15T12:00:00.000Z",
  "source": "quick_calculations_calculator",
  "calculations": "not_a_map_or_object"
}
```

### Payload 11: Attempting to update an existing Lead Document (Immutable Guard)
An attacker tries to edit/override an existing lead record.
- **Action**: Update
- **Target**: Rejection on any updates to `/quick_calc_leads/{leadId}`

### Payload 12: Attempting to read another user's Lead Document (PII Leak Guard)
An attacker tries to retrieve lead documents.
- **Action**: Read/Get/List
- **Target**: Rejection on all reads/lists to `/quick_calc_leads/{leadId}`

---

## 3. Test Runner Concept
Test verification logic is defined to execute these security assertions and confirm `PERMISSION_DENIED` on all hostile payloads.
