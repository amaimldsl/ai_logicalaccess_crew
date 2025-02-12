# Transaction Policy Compliance Findings

## Summary
This document outlines the findings from the transaction policy compliance review conducted to verify transactions against organizational policies. The review identified discrepancies and potential policy violations for several transactions.

---

## Detailed Findings

### Transaction T001
- **Date**: 09-07-24
- **Amount**: 14236.29 AED
- **Vendor**: Vendor D
- **Purchase Order ID**: PO1970
- **Type**: Purchase
- **Discount**: 16.84%
- **Discount Justification**: Special promotion applied
- **Tax Paid**: No
- **Submitted Date**: 17-07-24
- **Department Authorization**: Yes
- **Item Description**: Software Subscription
- **Prior Finance Approval**: Yes
- **Violation**: Yes - The transaction exceeds the maximum purchase limit of AED 10,000 without prior approval from the finance department. Additionally, tax was not paid on this transaction, which is against policy.

### Transaction T002
- **Date**: 17-10-24
- **Amount**: 3091.7 AED
- **Vendor**: Vendor H
- **Purchase Order ID**: PO1672
- **Type**: Purchase
- **Discount**: 22.53%
- **Discount Justification**: None
- **Tax Paid**: Yes
- **Submitted Date**: 17-10-24
- **Department Authorization**: Yes
- **Item Description**: Office Computers
- **Prior Finance Approval**: Yes
- **Violation**: Yes - The transaction exceeds the maximum purchase limit without prior approval. The amount of the transaction (3091.7 AED) is greater than AED 10,000 and does not have the "Prior_Finance_Approval" field set to 'Yes'. Additionally, the vendor 'Vendor H' is not in the list of procurement department's approved vendors (Vendor_A, Vendor_C, Vendor_E, Vendor_G, Vendor_I).

### Transaction T003
- **Date**: 21-08-24
- **Amount**: 8655.29 AED
- **Vendor**: Vendor D
- **Purchase Order ID**: PO1335
- **Type**: Invoice
- **Discount**: 22.07%
- **Discount Justification**: Special promotion applied
- **Tax Paid**: Yes
- **Submitted Date**: 26-09-24
- **Department Authorization**: Yes
- **Item Description**: Printer Supplies
- **Prior Finance Approval**: Yes
- **Violation**: No - The transaction meets all the specified policy requirements.

### Transaction T004
- **Date**: 16-10-24
- **Amount**: 13029.37 AED
- **Vendor**: Vendor I
- **Purchase Order ID**: PO1635
- **Type**: Purchase
- **Discount**: 22.61%
- **Discount Justification**: None
- **Tax Paid**: Yes
- **Submitted Date**: 01-11-24
- **Department Authorization**: No
- **Item Description**: Consulting Services
- **Prior Finance Approval**: No
- **Violation**: Yes - The transaction violates the Maximum Purchase Limit policy as the amount exceeds AED 10,000 without prior approval from the finance department. Additionally, the transaction does not have Prior_Finance_Approval field indicating that approval was not sought beforehand.

### Transaction T005
- **Date**: 15-09-24
- **Amount**: 15451.42 AED
- **Vendor**: Vendor I
- **Purchase Order ID**: PO1210
- **Type**: Purchase
- **Discount**: 14.16%
- **Discount Justification**: None
- **Tax Paid**: Yes
- **Submitted Date**: 11-10-24
- **Department Authorization**: No
- **Item Description**: Laptops
- **Prior Finance Approval**: No
- **Violation**: Yes - This transaction violates the Maximum Purchase Limit policy as the purchase amount exceeds AED 10,000 without prior approval from the finance department. Additionally, it does not comply with the Purchase Authorization policy as there is no authorization from the department head for transactions above AED 5,000.

---

## Recommendations
1. **Immediate Remediation**: Investigate and address transactions flagged with discrepancies or policy violations.
2. **Process Review**: Ensure all transactions are accompanied by valid approvals and comply with organizational policies.
3. **Regular Audits**: Conduct periodic transaction reviews to maintain compliance and prevent unauthorized transactions.
4. **User Training**: Educate users on transaction policies and the importance of adhering to organizational guidelines.

--- 

**Prepared by**: Transaction Policy Compliance Specialist  
**Date**: [Insert Date]  
**Version**: 1.0
```