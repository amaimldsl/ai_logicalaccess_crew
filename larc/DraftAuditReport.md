# Comprehensive Audit Report

## Executive Summary
This audit report consolidates findings from three key areas: User Access Review, Transaction Limit Compliance, and Change Management Audit. The review identified significant discrepancies in user access levels, transaction approval violations, and change management policy non-compliance. Key findings include:
- **Access Review**: 16 out of 18 users had access discrepancies, with 4 users having unauthorized access.
- **Transaction Compliance**: 6 out of 15 transactions exceeded authorized approval limits.
- **Change Management**: 14 out of 20 audit records had potential violations, including unauthorized changes and missing change tickets.

## Detailed Findings

### 1. Access Review Findings (Critical Risk)
#### User Access Discrepancies
- **USER001**: System B access level mismatch (`maker` instead of `checker`).
- **USER002**: System B access level mismatch (`maker` instead of `read-only`).
- **USER003**: System A access level mismatch (`maker` instead of `read-only`).
- **USER005**: System B access level mismatch (`maker` instead of `checker`).
- **USER006**: System C access level mismatch (`maker` instead of `read-only`).
- **USER008**: System C access level mismatch (`read-only` instead of `checker`).
- **USER009**: System A access level mismatch (`checker` instead of `read-only`).
- **USER010**: System C access level mismatch (`maker` instead of `checker`).
- **USER012**: System B access level mismatch (`maker` instead of `checker`).
- **USER014**: System B access level mismatch (`checker` instead of `read-only`).
- **USER016**: System B access level mismatch (`maker` instead of `checker`).
- **USER017**: System A access level mismatch (`maker` instead of `checker`).

#### Unauthorized Access
- **USER021**: Unauthorized access to System A (`maker`), System B (`read-only`), and System C (`checker`).
- **USER022**: Unauthorized access to System A (`read-only`), System B (`maker`), and System C (`maker`).
- **USER023**: Unauthorized access to System A (`maker`), System B (`checker`), and System C (`read-only`).
- **USER024**: Unauthorized access to System A (`checker`), System B (`maker`), and System C (`maker`).

#### Root Cause Analysis
- Lack of periodic access reviews.
- Inadequate segregation of duties.
- Weak access control policies.

#### Recommendations
1. Revise access levels for users with discrepancies.
2. Immediately revoke access for unauthorized users (USER021, USER022, USER023, USER024).
3. Conduct follow-up reviews to ensure compliance.

---

### 2. Transaction Limit Compliance Findings (High Risk)
#### Transaction Approval Violations
- **Transaction 0**: Approved by USER008, exceeding approval limit.
- **Transaction 3**: Approved by USER009, exceeding approval limit.
- **Transaction 7**: Approved by USER010, exceeding approval limit.
- **Transaction 9**: Approved by USER005, exceeding approval limit.
- **Transaction 14**: Approved by USER001, USER002, USER003, exceeding joint approval limit.

#### Root Cause Analysis
- Inadequate training on approval limits.
- Lack of automated controls for high-value transactions.

#### Recommendations
1. Review and adjust approval limits for users with frequent violations.
2. Implement additional controls for high-value transactions.
3. Conduct periodic reviews of transaction approvals.

---

### 3. Change Management Audit Findings (Medium Risk)
#### Verified Transactions
- 6 out of 20 audit records were verified with valid change tickets.

#### Potential Violations
- **Missing Change Tickets**: 10 records lacked associated change tickets.
- **Unauthorized Changes**: 4 records involved unauthorized users making changes.

#### Root Cause Analysis
- Inadequate enforcement of change management policies.
- Lack of awareness among users regarding change management SLAs.

#### Recommendations
1. Investigate and resolve potential violations.
2. Ensure all changes are associated with valid change tickets.
3. Provide additional training to users involved in unauthorized changes.

---

## Conclusion
This audit highlights critical areas requiring immediate attention, particularly in access control and transaction approval processes. Addressing these issues will strengthen the organization's compliance posture and reduce operational risks. Regular follow-up audits are recommended to ensure sustained compliance.
```