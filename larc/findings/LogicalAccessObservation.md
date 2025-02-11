# Access Review Findings

## Summary of Discrepancies

The following discrepancies were identified during the access review:

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

## Users with No Discrepancies
- USER004
- USER007
- USER013
- USER018

## Recommendations
1. **Immediate Remediation**: Revoke unauthorized access for users USER021, USER022, USER023, and USER024.
2. **Access Level Adjustments**: Adjust access levels for users with discrepancies to match the authorized access matrix.
3. **Periodic Reviews**: Implement periodic access reviews to ensure ongoing compliance with the access matrix.

## Conclusion
The access review has identified several discrepancies and unauthorized access instances. Immediate action is required to remediate these issues and ensure compliance with the authorized access matrix.
```