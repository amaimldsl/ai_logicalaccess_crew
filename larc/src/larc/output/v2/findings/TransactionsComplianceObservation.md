# Transaction Policy Compliance Findings

## Summary of Transaction Policy Findings

Below is a detailed report of transactions analyzed against organizational policies. The analysis identifies compliant transactions and those that violate transaction policies.

---

### **Transaction ID: T001**
- **Date**: 09-07-24
- **Amount**: 14236.29 AED
- **Vendor**: Microsoft
- **Purchase Order ID**: PO1970
- **Type**: Purchase
- **Discount**: 16.84%
- **Discount Justification**: Special promotion applied
- **Tax Paid**: No
- **Submitted Date**: 17-07-24
- **Department Authorization**: Yes
- **Item Description**: Software Subscription
- **Prior Finance Approval**: Yes
- **Violations**:
  - The transaction exceeds the maximum purchase limit (AED 10,000) without prior approval. (Policy Condition 1 referenced.)
  - The transaction does not include tax payments as required by the policy. (Policy Condition 6 referenced.)

---

### **Transaction ID: T002**
- **Date**: 17-10-24
- **Amount**: 3091.7 AED
- **Vendor**: HP
- **Purchase Order ID**: PO1672
- **Type**: Purchase
- **Discount**: 22.53%
- **Discount Justification**: None
- **Tax Paid**: Yes
- **Submitted Date**: 17-10-24
- **Department Authorization**: Yes
- **Item Description**: Office Computers
- **Prior Finance Approval**: Yes
- **Violations**:
  - This transaction violates the Maximum Purchase Limit rule as the purchase amount (3091.7 AED) exceeds the single transaction limit of AED 10,000 without prior approval from the finance department.
  - The transaction also violates the Discounts rule since the discount percentage (22.53%) is above the allowed threshold of 15%. Since there is no justification provided for the discount in the given data, it further violates the Discount_Justification rule as well.

---

### **Transaction ID: T003**
- **Date**: 21-08-24
- **Amount**: 8655.29 AED
- **Vendor**: Oracle
- **Purchase Order ID**: PO1335
- **Type**: Invoice
- **Discount**: 22.07%
- **Discount Justification**: Special promotion applied
- **Tax Paid**: Yes
- **Submitted Date**: 26-09-24
- **Department Authorization**: Yes
- **Item Description**: Printer Supplies
- **Prior Finance Approval**: Yes
- **Violations**:
  - The transaction exceeds the maximum purchase limit without prior approval as it is AED 8655.29 and the policy states purchases cannot exceed AED 10,000 for a single transaction without approval (Policy Rule 1).
  - The discount applied (22.07%) exceeds the allowable limit of 15% without an appropriate justification from the vendor and internal approval (Policy Rule 5).

---

### **Transaction ID: T004**
- **Date**: 16-10-24
- **Amount**: 13029.37 AED
- **Vendor**: HP
- **Purchase Order ID**: PO1635
- **Type**: Purchase
- **Discount**: 22.61%
- **Discount Justification**: None
- **Tax Paid**: Yes
- **Submitted Date**: 01-11-24
- **Department Authorization**: No
- **Item Description**: Consulting Services
- **Prior Finance Approval**: No
- **Violations**:
  - The transaction violates Rule 1 (Maximum Purchase Limit) as the amount exceeds AED 10,000 without prior approval from the finance department.
  - It also violates Rule 7 (Purchase Authorization) because the Department_Authorization field indicates that there was no authorization from the department head for this transaction.

---

### **Transaction ID: T005**
- **Date**: 15-09-24
- **Amount**: 15451.42 AED
- **Vendor**: Apple
- **Purchase Order ID**: PO1210
- **Type**: Purchase
- **Discount**: 14.16%
- **Discount Justification**: None
- **Tax Paid**: Yes
- **Submitted Date**: 11-10-24
- **Department Authorization**: No
- **Item Description**: Laptops
- **Prior Finance Approval**: No
- **Violations**:
  - This transaction exceeds the maximum purchase limit as it is AED 15,451.42 which is above the limit of AED 10,000 for a single transaction without prior approval from the finance department (Policy Condition 1).
  - The transaction was not submitted within the invoice submission deadline as it was submitted more than 30 days after the purchase date (Policy Condition 2).
  - The vendor Apple is not listed as an approved vendor by the procurement department (Policy Condition 3).

---

## **Key Observations**
1. **Policy Violations**: Several transactions violate organizational policies, including exceeding purchase limits, missing tax payments, unauthorized discounts, and lack of department authorization.
2. **Compliant Transactions**: Some transactions are compliant with organizational policies, indicating proper adherence to SLAs.

---

## **Recommendations**
1. **Investigate Policy Violations**: Investigate and resolve the policy violations for the identified transactions.
2. **Reject Unauthorized Transactions**: Ensure transactions carried out without proper authorization are flagged and corrected.
3. **Training and Awareness**: Provide training to users on transaction policies and compliance requirements.
4. **Regular Audits**: Conduct periodic reviews of transactions to ensure ongoing compliance with organizational policies.

---

This report highlights critical transaction policy compliance issues that require immediate attention to ensure adherence to organizational policies and controls.
```