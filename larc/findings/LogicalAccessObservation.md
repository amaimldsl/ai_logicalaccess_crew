# Access Review Findings

## Summary of Discrepancies

The following users have access discrepancies when compared to the authorized access matrix:

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

## Unauthorized Access Findings

The following users have unauthorized access to systems:

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

## Conclusion

The access review identified several discrepancies and unauthorized access instances. Immediate action is required to revoke unauthorized access and align user access levels with the authorized access matrix to ensure compliance and security.
```