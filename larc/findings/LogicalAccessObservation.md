# Access Review Findings

## Summary of Findings
The access review identified several discrepancies between the actual access levels and the authorized access matrix. Below is a detailed breakdown of the findings for each user.

---

## Detailed Findings

### USER001
- **system_a_access**: Access level matches the authorized matrix (maker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the authorized matrix (read-only).

### USER002
- **system_a_access**: Access level matches the authorized matrix (checker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `read-only`.
- **system_c_access**: Access level matches the authorized matrix (maker).

### USER003
- **system_a_access**: Discrepancy found. Actual access level is `maker`, but should be `read-only`.
- **system_b_access**: Access level matches the authorized matrix (maker).
- **system_c_access**: Access level matches the authorized matrix (checker).

### USER004
- **system_a_access**: Access level matches the authorized matrix (maker).
- **system_b_access**: Access level matches the authorized matrix (maker).
- **system_c_access**: Access level matches the authorized matrix (maker).

### USER005
- **system_a_access**: Access level matches the authorized matrix (checker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the authorized matrix (checker).

### USER006
- **system_a_access**: Access level matches the authorized matrix (read-only).
- **system_b_access**: Access level matches the authorized matrix (read-only).
- **system_c_access**: Discrepancy found. Actual access level is `maker`, but should be `read-only`.

### USER007
- **system_a_access**: Access level matches the authorized matrix (maker).
- **system_b_access**: Access level matches the authorized matrix (checker).
- **system_c_access**: Access level matches the authorized matrix (maker).

### USER008
- **system_a_access**: Access level matches the authorized matrix (checker).
- **system_b_access**: Access level matches the authorized matrix (maker).
- **system_c_access**: Discrepancy found. Actual access level is `read-only`, but should be `checker`.

### USER009
- **system_a_access**: Discrepancy found. Actual access level is `checker`, but should be `read-only`.
- **system_b_access**: Access level matches the authorized matrix (checker).
- **system_c_access**: Access level matches the authorized matrix (read-only).

### USER010
- **system_a_access**: Access level matches the authorized matrix (maker).
- **system_b_access**: Access level matches the authorized matrix (read-only).
- **system_c_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.

### USER021
- **system_a_access**: Unauthorized access. Actual access level is `maker`, but user is unauthorized.
- **system_b_access**: Unauthorized access. Actual access level is `read-only`, but user is unauthorized.
- **system_c_access**: Unauthorized access. Actual access level is `checker`, but user is unauthorized.

### USER012
- **system_a_access**: Access level matches the authorized matrix (read-only).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the authorized matrix (maker).

### USER013
- **system_a_access**: Access level matches the authorized matrix (maker).
- **system_b_access**: Access level matches the authorized matrix (maker).
- **system_c_access**: Access level matches the authorized matrix (checker).

### USER014
- **system_a_access**: Access level matches the authorized matrix (checker).
- **system_b_access**: Discrepancy found. Actual access level is `checker`, but should be `read-only`.
- **system_c_access**: Access level matches the authorized matrix (read-only).

### USER022
- **system_a_access**: Unauthorized access. Actual access level is `read-only`, but user is unauthorized.
- **system_b_access**: Unauthorized access. Actual access level is `maker`, but user is unauthorized.
- **system_c_access**: Unauthorized access. Actual access level is `maker`, but user is unauthorized.

### USER016
- **system_a_access**: Access level matches the authorized matrix (maker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the authorized matrix (checker).

### USER017
- **system_a_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_b_access**: Access level matches the authorized matrix (maker).
- **system_c_access**: Access level matches the authorized matrix (read-only).

### USER018
- **system_a_access**: Access level matches the authorized matrix (read-only).
- **system_b_access**: Access level matches the authorized matrix (read-only).
- **system_c_access**: Access level matches the authorized matrix (maker).

### USER023
- **system_a_access**: Unauthorized access. Actual access level is `maker`, but user is unauthorized.
- **system_b_access**: Unauthorized access. Actual access level is `checker`, but user is unauthorized.
- **system_c_access**: Unauthorized access. Actual access level is `read-only`, but user is unauthorized.

### USER024
- **system_a_access**: Unauthorized access. Actual access level is `checker`, but user is unauthorized.
- **system_b_access**: Unauthorized access. Actual access level is `maker`, but user is unauthorized.
- **system_c_access**: Unauthorized access. Actual access level is `maker`, but user is unauthorized.

---

## Conclusion
The access review identified multiple discrepancies and unauthorized access instances. Immediate action is recommended to align access levels with the authorized matrix and revoke unauthorized access.
```