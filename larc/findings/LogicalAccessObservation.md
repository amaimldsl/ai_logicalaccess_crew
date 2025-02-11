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

The following users have access levels that match the authorized access matrix:

- USER004
- USER007
- USER013
- USER018

## Recommendations

1. **Revoke Unauthorized Access**: Users USER021, USER022, USER023, and USER024 should have their access revoked immediately as they are unauthorized to access any systems.
2. **Adjust Access Levels**: For users with discrepancies, adjust their access levels to match the authorized access matrix.
3. **Regular Audits**: Implement regular access reviews to ensure compliance and prevent unauthorized access.

---

This concludes the access review findings. Immediate action is recommended to address the identified discrepancies.
```