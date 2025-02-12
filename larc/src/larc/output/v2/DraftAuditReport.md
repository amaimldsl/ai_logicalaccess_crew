# Comprehensive Audit Report

## Executive Summary
This audit report consolidates findings from four key areas: Access Review, Transaction Limit Compliance, Change Management, and Transaction Policy Compliance. The audit identified several critical issues, including unauthorized access, transaction limit violations, change management policy breaches, and transaction policy non-compliance. These findings highlight the need for immediate corrective actions to ensure compliance with organizational policies and controls.

### Aggregated Statistics
- **Access Review**: 12 users with non-compliant access, 4 users with unauthorized access.
- **Transaction Limit Compliance**: 4 transactions exceeding user approval limits, 1 transaction exceeding joint approval limits.
- **Change Management**: 11 audit trail records without associated change tickets, 3 changes carried out by unauthorized users.
- **Transaction Policy Compliance**: 5 transactions violating organizational policies, including exceeding purchase limits and unauthorized discounts.

---

## Detailed Findings

### 1. Access Review Findings
#### Observation
- **Non-Compliant Access**: Several users have access levels that do not match the authorized access matrix. For example:
  - USER001 has "Maker" access to System B instead of "Checker."
  - USER003 has "Maker" access to System A instead of "Read-Only."
- **Unauthorized Access**: Users USER021, USER022, USER023, and USER024 have access to systems they are not authorized to use.

#### Risk Rating
- **High**: Unauthorized access poses a significant security risk.
- **Medium**: Non-compliant access increases the risk of operational errors.

#### Risks
- Unauthorized access could lead to data breaches or misuse of sensitive information.
- Non-compliant access may result in operational inefficiencies or errors.

#### Management Actions
1. **Revoke Unauthorized Access**: Immediately revoke access for users with unauthorized access.
2. **Adjust Non-Compliant Access**: Update access levels for users with non-compliant access to match the authorized access matrix.
3. **Regular Audits**: Conduct regular access reviews to ensure ongoing compliance with the access matrix.
4. **User Training**: Provide training to users and administrators on access control policies.

---

### 2. Transaction Limit Compliance Findings
#### Observation
- **Limit Violations**: Several transactions exceed the authorized approval limits for specific users. For example:
  - Transaction 0 exceeds USER008's approval limit.
  - Transaction 3 exceeds USER009's approval limit.
  - Transaction 14 exceeds the joint approval limit for USER001, USER002, and USER003.

#### Risk Rating
- **High**: Transactions exceeding limits could lead to financial losses or fraud.
- **Medium**: Non-compliant transactions may result in operational inefficiencies.

#### Risks
- Financial losses due to unauthorized or excessive transactions.
- Increased risk of fraud or misuse of funds.

#### Management Actions
1. **Review and Adjust Limits**: Investigate and adjust the approval limits for users with repeated violations.
2. **Reject Non-Compliant Transactions**: Ensure transactions exceeding limits are flagged and rejected until proper approvals are obtained.
3. **Training and Awareness**: Provide training to users on approval limits and compliance requirements.
4. **Regular Audits**: Conduct periodic reviews of transaction approvals to ensure ongoing compliance with authorized limits.

---

### 3. Change Management Audit Findings
#### Observation
- **Change Management Violations**: Several audit trail records do not have associated change tickets, indicating potential violations of change management policies. For example:
  - Audit Record 0, 1, 6, 8, 9, 14, 15, 16, 17, 18, and 19 do not have associated change tickets.
  - Audit Records 10, 11, and 12 were carried out by unauthorized users.

#### Risk Rating
- **High**: Unauthorized changes could lead to system instability or security breaches.
- **Medium**: Missing change tickets increase the risk of non-compliance with change management policies.

#### Risks
- System instability or outages due to unauthorized changes.
- Increased risk of security breaches or data loss.

#### Management Actions
1. **Investigate Missing Change Tickets**: Investigate and resolve the missing change tickets for the identified audit trail records.
2. **Reject Unauthorized Changes**: Ensure changes carried out by unauthorized users are flagged and corrected.
3. **Training and Awareness**: Provide training to users on change management policies and compliance requirements.
4. **Regular Audits**: Conduct periodic reviews of audit trail records to ensure ongoing compliance with change management policies.

---

### 4. Transaction Policy Compliance Findings
#### Observation
- **Policy Violations**: Several transactions violate organizational policies, including exceeding purchase limits, missing tax payments, unauthorized discounts, and lack of department authorization. For example:
  - Transaction T001 exceeds the maximum purchase limit without prior approval.
  - Transaction T002 violates the Discounts rule with a 22.53% discount without justification.

#### Risk Rating
- **High**: Policy violations could lead to financial losses or legal issues.
- **Medium**: Non-compliant transactions may result in operational inefficiencies.

#### Risks
- Financial losses due to unauthorized or excessive transactions.
- Legal or regulatory penalties for non-compliance with tax or procurement policies.

#### Management Actions
1. **Investigate Policy Violations**: Investigate and resolve the policy violations for the identified transactions.
2. **Reject Unauthorized Transactions**: Ensure transactions carried out without proper authorization are flagged and corrected.
3. **Training and Awareness**: Provide training to users on transaction policies and compliance requirements.
4. **Regular Audits**: Conduct periodic reviews of transactions to ensure ongoing compliance with organizational policies.

---

## Recommendations
1. **Immediate Corrective Actions**: Address the identified issues promptly to mitigate risks.
2. **Policy Updates**: Review and update policies to address recurring issues.
3. **Training Programs**: Implement training programs for employees to ensure awareness and compliance with policies.
4. **Regular Audits**: Establish a schedule for regular audits to monitor compliance and identify issues early.

---

This report highlights critical compliance issues that require immediate attention to ensure adherence to organizational policies and controls.
```