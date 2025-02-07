# Access Review Findings

## User Access Discrepancies

### USER001
- **System B Access**: User has actual access level of `maker` but should have `checker`.

### USER002
- **System B Access**: User has actual access level of `maker` but should have `read-only`.

### USER003
- **System A Access**: User has actual access level of `maker` but should have `read-only`.

### USER005
- **System B Access**: User has actual access level of `maker` but should have `checker`.

### USER006
- **System C Access**: User has actual access level of `maker` but should have `read-only`.

### USER008
- **System C Access**: User has actual access level of `read-only` but should have `checker`.

### USER009
- **System A Access**: User has actual access level of `checker` but should have `read-only`.

### USER010
- **System C Access**: User has actual access level of `maker` but should have `checker`.

### USER012
- **System B Access**: User has actual access level of `maker` but should have `checker`.

### USER014
- **System B Access**: User has actual access level of `checker` but should have `read-only`.

### USER016
- **System B Access**: User has actual access level of `maker` but should have `checker`.

### USER017
- **System A Access**: User has actual access level of `maker` but should have `checker`.

### USER021
- **System A Access**: User has access level of `maker` but is unauthorized.
- **System B Access**: User has access level of `read-only` but is unauthorized.
- **System C Access**: User has access level of `checker` but is unauthorized.

### USER022
- **System A Access**: User has access level of `read-only` but is unauthorized.
- **System B Access**: User has access level of `maker` but is unauthorized.
- **System C Access**: User has access level of `maker` but is unauthorized.

### USER023
- **System A Access**: User has access level of `maker` but is unauthorized.
- **System B Access**: User has access level of `checker` but is unauthorized.
- **System C Access**: User has access level of `read-only` but is unauthorized.

### USER024
- **System A Access**: User has access level of `checker` but is unauthorized.
- **System B Access**: User has access level of `maker` but is unauthorized.
- **System C Access**: User has access level of `maker` but is unauthorized.

## Summary
- **Total Users with Discrepancies**: 16
- **Unauthorized Access Detected**: 5 users (USER021, USER022, USER023, USER024)
- **Access Level Mismatches**: 11 users

## Recommendations
1. **Immediate Revocation**: Unauthorized access for users USER021, USER022, USER023, and USER024 should be revoked immediately.
2. **Access Level Adjustments**: Adjust access levels for users with discrepancies to match the authorized access matrix.
3. **Regular Audits**: Implement regular access reviews to ensure compliance with the access matrix.
```