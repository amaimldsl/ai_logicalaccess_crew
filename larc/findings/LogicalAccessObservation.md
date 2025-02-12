# Access Review Findings

## Summary
This document outlines the findings from the access review conducted to compare system access levels against the authorized access matrix. The review identified discrepancies and unauthorized access patterns for several users across different systems.

---

## Detailed Findings

### USER001
- **system_a_access**: Access level matches the access matrix (maker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the access matrix (read-only).

### USER002
- **system_a_access**: Access level matches the access matrix (checker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `read-only`.
- **system_c_access**: Access level matches the access matrix (maker).

### USER003
- **system_a_access**: Discrepancy found. Actual access level is `maker`, but should be `read-only`.
- **system_b_access**: Access level matches the access matrix (maker).
- **system_c_access**: Access level matches the access matrix (checker).

### USER004
- **system_a_access**: Access level matches the access matrix (maker).
- **system_b_access**: Access level matches the access matrix (maker).
- **system_c_access**: Access level matches the access matrix (maker).

### USER005
- **system_a_access**: Access level matches the access matrix (checker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the access matrix (checker).

### USER006
- **system_a_access**: Access level matches the access matrix (read-only).
- **system_b_access**: Access level matches the access matrix (read-only).
- **system_c_access**: Discrepancy found. Actual access level is `maker`, but should be `read-only`.

### USER007
- **system_a_access**: Access level matches the access matrix (maker).
- **system_b_access**: Access level matches the access matrix (checker).
- **system_c_access**: Access level matches the access matrix (maker).

### USER008
- **system_a_access**: Access level matches the access matrix (checker).
- **system_b_access**: Access level matches the access matrix (maker).
- **system_c_access**: Discrepancy found. Actual access level is `read-only`, but should be `checker`.

### USER009
- **system_a_access**: Discrepancy found. Actual access level is `checker`, but should be `read-only`.
- **system_b_access**: Access level matches the access matrix (checker).
- **system_c_access**: Access level matches the access matrix (read-only).

### USER010
- **system_a_access**: Access level matches the access matrix (maker).
- **system_b_access**: Access level matches the access matrix (read-only).
- **system_c_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.

### USER021
- **system_a_access**: Unauthorized access. User has `maker` access but should have no access.
- **system_b_access**: Unauthorized access. User has `read-only` access but should have no access.
- **system_c_access**: Unauthorized access. User has `checker` access but should have no access.

### USER012
- **system_a_access**: Access level matches the access matrix (read-only).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the access matrix (maker).

### USER013
- **system_a_access**: Access level matches the access matrix (maker).
- **system_b_access**: Access level matches the access matrix (maker).
- **system_c_access**: Access level matches the access matrix (checker).

### USER014
- **system_a_access**: Access level matches the access matrix (checker).
- **system_b_access**: Discrepancy found. Actual access level is `checker`, but should be `read-only`.
- **system_c_access**: Access level matches the access matrix (read-only).

### USER022
- **system_a_access**: Unauthorized access. User has `read-only` access but should have no access.
- **system_b_access**: Unauthorized access. User has `maker` access but should have no access.
- **system_c_access**: Unauthorized access. User has `maker` access but should have no access.

### USER016
- **system_a_access**: Access level matches the access matrix (maker).
- **system_b_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_c_access**: Access level matches the access matrix (checker).

### USER017
- **system_a_access**: Discrepancy found. Actual access level is `maker`, but should be `checker`.
- **system_b_access**: Access level matches the access matrix (maker).
- **system_c_access**: Access level matches the access matrix (read-only).

### USER018
- **system_a_access**: Access level matches the access matrix (read-only).
- **system_b_access**: Access level matches the access matrix (read-only).
- **system_c_access**: Access level matches the access matrix (maker).

### USER023
- **system_a_access**: Unauthorized access. User has `maker` access but should have no access.
- **system_b_access**: Unauthorized access. User has `checker` access but should have no access.
- **system_c_access**: Unauthorized access. User has `read-only` access but should have no access.

### USER024
- **system_a_access**: Unauthorized access. User has `checker` access but should have no access.
- **system_b_access**: Unauthorized access. User has `maker` access but should have no access.
- **system_c_access**: Unauthorized access. User has `maker` access but should have no access.

---

## Recommendations
1. **Immediate Remediation**: Revoke unauthorized access for users flagged with discrepancies or unauthorized access.
2. **Access Matrix Update**: Ensure the access matrix is updated to reflect any changes in roles or responsibilities.
3. **Regular Audits**: Conduct periodic access reviews to maintain compliance and prevent unauthorized access.
4. **User Training**: Educate users on access policies and the importance of adhering to the access matrix.

--- 

**Prepared by**: Access Review Specialist  
**Date**: [Insert Date]  
**Version**: 1.0
```