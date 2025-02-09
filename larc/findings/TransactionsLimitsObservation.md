# Transaction Limit Compliance Analysis

## Summary of Findings

The following transactions were analyzed against authorized limits. The results are categorized into compliant and non-compliant transactions.

---

### **Compliant Transactions**

1. **Transaction ID: transaction_1**
   - **Amount**: 150,000
   - **Date**: 2024-01-16
   - **Approved by**: USER004
   - **Result**: Transaction is approved within the single approval limit of USER004.

2. **Transaction ID: transaction_2**
   - **Amount**: 2,500,000
   - **Date**: 2024-01-17
   - **Approved by**: USER001, USER002
   - **Result**: Transaction is approved within the joint approval limit of users ['USER001', 'USER002'].

3. **Transaction ID: transaction_4**
   - **Amount**: 3,500,000
   - **Date**: 2024-01-19
   - **Approved by**: USER003, USER004
   - **Result**: Transaction is approved within the joint approval limit of users ['USER003', 'USER004'].

4. **Transaction ID: transaction_5**
   - **Amount**: 450,000
   - **Date**: 2024-01-20
   - **Approved by**: USER007
   - **Result**: Transaction is approved within the single approval limit of USER007.

5. **Transaction ID: transaction_6**
   - **Amount**: 1,500,000
   - **Date**: 2024-01-21
   - **Approved by**: USER002, USER003
   - **Result**: Transaction is approved within the joint approval limit of users ['USER002', 'USER003'].

6. **Transaction ID: transaction_8**
   - **Amount**: 4,000,000
   - **Date**: 2024-01-23
   - **Approved by**: USER001, USER002, USER003
   - **Result**: Transaction is approved within the joint approval limit of users ['USER001', 'USER002', 'USER003'].

7. **Transaction ID: transaction_10**
   - **Amount**: 2,800,000
   - **Date**: 2024-01-25
   - **Approved by**: USER001, USER004
   - **Result**: Transaction is approved within the joint approval limit of users ['USER001', 'USER004'].

8. **Transaction ID: transaction_11**
   - **Amount**: 95,000
   - **Date**: 2024-01-26
   - **Approved by**: USER008
   - **Result**: Transaction is approved within the single approval limit of USER008.

9. **Transaction ID: transaction_12**
   - **Amount**: 3,200,000
   - **Date**: 2024-01-27
   - **Approved by**: USER002, USER003
   - **Result**: Transaction is approved within the joint approval limit of users ['USER002', 'USER003'].

10. **Transaction ID: transaction_13**
    - **Amount**: 175,000
    - **Date**: 2024-01-28
    - **Approved by**: USER006
    - **Result**: Transaction is approved within the single approval limit of USER006.

---

### **Non-Compliant Transactions**

1. **Transaction ID: transaction_0**
   - **Amount**: 175,000
   - **Date**: 2024-01-15
   - **Approved by**: USER008
   - **Result**: Transaction Amount Exceeds user Approval Level for USER008.

2. **Transaction ID: transaction_3**
   - **Amount**: 120,000
   - **Date**: 2024-01-18
   - **Approved by**: USER009
   - **Result**: Transaction Amount Exceeds user Approval Level for USER009.

3. **Transaction ID: transaction_7**
   - **Amount**: 800,000
   - **Date**: 2024-01-22
   - **Approved by**: USER010
   - **Result**: Transaction Amount Exceeds user Approval Level for USER010.

4. **Transaction ID: transaction_9**
   - **Amount**: 600,000
   - **Date**: 2024-01-24
   - **Approved by**: USER005
   - **Result**: Transaction Amount Exceeds user Approval Level for USER005.

5. **Transaction ID: transaction_14**
   - **Amount**: 5,500,000
   - **Date**: 2024-01-29
   - **Approved by**: USER001, USER002, USER003
   - **Result**: Transaction Amount Exceeds the joint Approval Level of users ['USER001', 'USER002', 'USER003'].

---

## Notes

- **Non-Compliant Transactions**: These transactions exceed the authorized approval limits for the respective users. Immediate action is required to rectify these discrepancies.
- **Compliant Transactions**: These transactions are within the authorized limits and do not require further action.
```