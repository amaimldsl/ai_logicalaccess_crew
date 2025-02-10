# Access Review Findings

## User Access Discrepancies

### USER001
- **system_b_access**: User has actual access level of `maker` but should have `checker`.

### USER002
- **system_b_access**: User has actual access level of `maker` but should have `read-only`.

### USER003
- **system_a_access**: User has actual access level of `maker` but should have `read-only`.

### USER005
- **system_b_access**: User has actual access level of `maker` but should have `checker`.

### USER006
- **system_c_access**: User has actual access level of `maker` but should have `read-only`.

### USER008
- **system_c_access**: User has actual access level of `read-only` but should have `checker`.

### USER009
- **system_a_access**: User has actual access level of `checker` but should have `read-only`.

### USER010
- **system_c_access**: User has actual access level of `maker` but should have `checker`.

### USER012
- **system_b_access**: User has actual access level of `maker` but should have `checker`.

### USER014
- **system_b_access**: User has actual access level of `checker` but should have `read-only`.

### USER016
- **system_b_access**: User has actual access level of `maker` but should have `checker`.

### USER017
- **system_a_access**: User has actual access level of `maker` but should have `checker`.

### USER021
- **system_a_access**: User has access level of `maker` but is unauthorized.
- **system_b_access**: User has access level of `read-only` but is unauthorized.
- **system_c_access**: User has access level of `checker` but is unauthorized.

### USER022
- **system_a_access**: User has access level of `read-only` but is unauthorized.
- **system_b_access**: User has access level of `maker` but is unauthorized.
- **system_c_access**: User has access level of `maker` but is unauthorized.

### USER023
- **system_a_access**: User has access level of `maker` but is unauthorized.
- **system_b_access**: User has access level of `checker` but is unauthorized.
- **system_c_access**: User has access level of `read-only` but is unauthorized.

### USER024
- **system_a_access**: User has access level of `checker` but is unauthorized.
- **system_b_access**: User has access level of `maker` but is unauthorized.
- **system_c_access**: User has access level of `maker` but is unauthorized.

## Summary
- **Total Users Reviewed**: 18
- **Users with Discrepancies**: 16
- **Unauthorized Access Detected**: 4 users (USER021, USER022, USER023, USER024)

## Recommendations
1. Revise access levels for users with discrepancies to align with the authorized access matrix.
2. Immediately revoke access for users identified as unauthorized (USER021, USER022, USER023, USER024).
3. Conduct a follow-up review after corrections to ensure compliance.
```