# Access Review Findings

## Summary of Access Discrepancies

The following users have discrepancies between their actual access levels and the authorized access matrix:

### USER001
- **system_b_access**: Actual access level is `maker`, but should be `checker`.

### USER002
- **system_b_access**: Actual access level is `maker`, but should be `read-only`.

### USER003
- **system_a_access**: Actual access level is `maker`, but should be `read-only`.

### USER005
- **system_b_access**: Actual access level is `maker`, but should be `checker`.

### USER006
- **system_c_access**: Actual access level is `maker`, but should be `read-only`.

### USER008
- **system_c_access**: Actual access level is `read-only`, but should be `checker`.

### USER009
- **system_a_access**: Actual access level is `checker`, but should be `read-only`.

### USER010
- **system_c_access**: Actual access level is `maker`, but should be `checker`.

### USER012
- **system_b_access**: Actual access level is `maker`, but should be `checker`.

### USER014
- **system_b_access**: Actual access level is `checker`, but should be `read-only`.

### USER016
- **system_b_access**: Actual access level is `maker`, but should be `checker`.

### USER017
- **system_a_access**: Actual access level is `maker`, but should be `checker`.

### USER021
- **system_a_access**: Actual access level is `maker`, but user is unauthorized.
- **system_b_access**: Actual access level is `read-only`, but user is unauthorized.
- **system_c_access**: Actual access level is `checker`, but user is unauthorized.

### USER022
- **system_a_access**: Actual access level is `read-only`, but user is unauthorized.
- **system_b_access**: Actual access level is `maker`, but user is unauthorized.
- **system_c_access**: Actual access level is `maker`, but user is unauthorized.

### USER023
- **system_a_access**: Actual access level is `maker`, but user is unauthorized.
- **system_b_access**: Actual access level is `checker`, but user is unauthorized.
- **system_c_access**: Actual access level is `read-only`, but user is unauthorized.

### USER024
- **system_a_access**: Actual access level is `checker`, but user is unauthorized.
- **system_b_access**: Actual access level is `maker`, but user is unauthorized.
- **system_c_access**: Actual access level is `maker`, but user is unauthorized.

## Users with No Discrepancies
- USER004
- USER007
- USER013
- USER018

## Recommendations
1. **Immediate Revocation**: Unauthorized access for users USER021, USER022, USER023, and USER024 should be revoked immediately.
2. **Access Adjustment**: Adjust access levels for users with discrepancies to match the authorized access matrix.
3. **Periodic Reviews**: Conduct periodic access reviews to ensure compliance with the access matrix.

## Conclusion
This report highlights discrepancies and unauthorized access patterns. Immediate action is required to align access levels with the authorized access matrix to maintain compliance and security.
```