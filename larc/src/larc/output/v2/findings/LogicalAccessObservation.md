# Access Review Findings

## Summary of Access Discrepancies

Below is a detailed report of access discrepancies identified during the review of system access levels against the authorized access matrix.

---

### **USER001**
- **System A Access**: Compliant (Actual: Maker, Expected: Maker)
- **System B Access**: Non-Compliant (Actual: Maker, Expected: Checker)
- **System C Access**: Compliant (Actual: Read-Only, Expected: Read-Only)

---

### **USER002**
- **System A Access**: Compliant (Actual: Checker, Expected: Checker)
- **System B Access**: Non-Compliant (Actual: Maker, Expected: Read-Only)
- **System C Access**: Compliant (Actual: Maker, Expected: Maker)

---

### **USER003**
- **System A Access**: Non-Compliant (Actual: Maker, Expected: Read-Only)
- **System B Access**: Compliant (Actual: Maker, Expected: Maker)
- **System C Access**: Compliant (Actual: Checker, Expected: Checker)

---

### **USER004**
- **System A Access**: Compliant (Actual: Maker, Expected: Maker)
- **System B Access**: Compliant (Actual: Maker, Expected: Maker)
- **System C Access**: Compliant (Actual: Maker, Expected: Maker)

---

### **USER005**
- **System A Access**: Compliant (Actual: Checker, Expected: Checker)
- **System B Access**: Non-Compliant (Actual: Maker, Expected: Checker)
- **System C Access**: Compliant (Actual: Checker, Expected: Checker)

---

### **USER006**
- **System A Access**: Compliant (Actual: Read-Only, Expected: Read-Only)
- **System B Access**: Compliant (Actual: Read-Only, Expected: Read-Only)
- **System C Access**: Non-Compliant (Actual: Maker, Expected: Read-Only)

---

### **USER007**
- **System A Access**: Compliant (Actual: Maker, Expected: Maker)
- **System B Access**: Compliant (Actual: Checker, Expected: Checker)
- **System C Access**: Compliant (Actual: Maker, Expected: Maker)

---

### **USER008**
- **System A Access**: Compliant (Actual: Checker, Expected: Checker)
- **System B Access**: Compliant (Actual: Maker, Expected: Maker)
- **System C Access**: Non-Compliant (Actual: Read-Only, Expected: Checker)

---

### **USER009**
- **System A Access**: Non-Compliant (Actual: Checker, Expected: Read-Only)
- **System B Access**: Compliant (Actual: Checker, Expected: Checker)
- **System C Access**: Compliant (Actual: Read-Only, Expected: Read-Only)

---

### **USER010**
- **System A Access**: Compliant (Actual: Maker, Expected: Maker)
- **System B Access**: Compliant (Actual: Read-Only, Expected: Read-Only)
- **System C Access**: Non-Compliant (Actual: Maker, Expected: Checker)

---

### **USER021**
- **System A Access**: Unauthorized Access (Actual: Maker, Expected: No Access)
- **System B Access**: Unauthorized Access (Actual: Read-Only, Expected: No Access)
- **System C Access**: Unauthorized Access (Actual: Checker, Expected: No Access)

---

### **USER012**
- **System A Access**: Compliant (Actual: Read-Only, Expected: Read-Only)
- **System B Access**: Non-Compliant (Actual: Maker, Expected: Checker)
- **System C Access**: Compliant (Actual: Maker, Expected: Maker)

---

### **USER013**
- **System A Access**: Compliant (Actual: Maker, Expected: Maker)
- **System B Access**: Compliant (Actual: Maker, Expected: Maker)
- **System C Access**: Compliant (Actual: Checker, Expected: Checker)

---

### **USER014**
- **System A Access**: Compliant (Actual: Checker, Expected: Checker)
- **System B Access**: Non-Compliant (Actual: Checker, Expected: Read-Only)
- **System C Access**: Compliant (Actual: Read-Only, Expected: Read-Only)

---

### **USER022**
- **System A Access**: Unauthorized Access (Actual: Read-Only, Expected: No Access)
- **System B Access**: Unauthorized Access (Actual: Maker, Expected: No Access)
- **System C Access**: Unauthorized Access (Actual: Maker, Expected: No Access)

---

### **USER016**
- **System A Access**: Compliant (Actual: Maker, Expected: Maker)
- **System B Access**: Non-Compliant (Actual: Maker, Expected: Checker)
- **System C Access**: Compliant (Actual: Checker, Expected: Checker)

---

### **USER017**
- **System A Access**: Non-Compliant (Actual: Maker, Expected: Checker)
- **System B Access**: Compliant (Actual: Maker, Expected: Maker)
- **System C Access**: Compliant (Actual: Read-Only, Expected: Read-Only)

---

### **USER018**
- **System A Access**: Compliant (Actual: Read-Only, Expected: Read-Only)
- **System B Access**: Compliant (Actual: Read-Only, Expected: Read-Only)
- **System C Access**: Compliant (Actual: Maker, Expected: Maker)

---

### **USER023**
- **System A Access**: Unauthorized Access (Actual: Maker, Expected: No Access)
- **System B Access**: Unauthorized Access (Actual: Checker, Expected: No Access)
- **System C Access**: Unauthorized Access (Actual: Read-Only, Expected: No Access)

---

### **USER024**
- **System A Access**: Unauthorized Access (Actual: Checker, Expected: No Access)
- **System B Access**: Unauthorized Access (Actual: Maker, Expected: No Access)
- **System C Access**: Unauthorized Access (Actual: Maker, Expected: No Access)

---

## **Key Observations**
1. **Non-Compliant Access**: Several users have access levels that do not match the authorized access matrix. For example:
   - USER001 has "Maker" access to System B instead of "Checker."
   - USER003 has "Maker" access to System A instead of "Read-Only."

2. **Unauthorized Access**: Users USER021, USER022, USER023, and USER024 have access to systems they are not authorized to use.

3. **Compliant Access**: Many users have access levels that match the authorized access matrix, indicating proper access control for these cases.

---

## **Recommendations**
1. **Revoke Unauthorized Access**: Immediately revoke access for users with unauthorized access (USER021, USER022, USER023, USER024).
2. **Adjust Non-Compliant Access**: Update access levels for users with non-compliant access to match the authorized access matrix.
3. **Regular Audits**: Conduct regular access reviews to ensure ongoing compliance with the access matrix.
4. **User Training**: Provide training to users and administrators on access control policies to prevent future discrepancies.

---

This report highlights critical access control issues that require immediate attention to ensure compliance and security.
```