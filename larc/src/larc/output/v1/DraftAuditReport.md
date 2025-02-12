# Comprehensive Audit Report

## Executive Summary

### Audit Background
This audit was conducted to review user access levels, transaction limit compliance, and change management processes. The objective was to ensure that access levels align with the access matrix, transactions are within approved limits, and change management processes are followed correctly.

### Aggregated Statistics
- **Access Review Findings**: 24 users were reviewed, with discrepancies found in 15 user access levels.
- **Transaction Limit Compliance Analysis**: 15 transactions were analyzed, with 5 transactions exceeding approval limits.
- **Change Management Audit Findings**: 15 transactions were reviewed, with 5 transactions exceeding approval limits.

## Detailed Findings

### Access Review Findings

#### USER001
- **Observation**: system_b_access level is maker, should be checker.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_b_access level to checker.

#### USER002
- **Observation**: system_b_access level is maker, should be read-only.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_b_access level to read-only.

#### USER003
- **Observation**: system_a_access level is maker, should be read-only.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_a_access level to read-only.

#### USER005
- **Observation**: system_b_access level is maker, should be checker.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_b_access level to checker.

#### USER006
- **Observation**: system_c_access level is maker, should be read-only.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_c_access level to read-only.

#### USER008
- **Observation**: system_c_access level is read-only, should be checker.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_c_access level to checker.

#### USER009
- **Observation**: system_a_access level is checker, should be read-only.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_a_access level to read-only.

#### USER010
- **Observation**: system_c_access level is maker, should be checker.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_c_access level to checker.

#### USER012
- **Observation**: system_b_access level is maker, should be checker.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_b_access level to checker.

#### USER014
- **Observation**: system_b_access level is checker, should be read-only.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_b_access level to read-only.

#### USER016
- **Observation**: system_b_access level is maker, should be checker.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_b_access level to checker.

#### USER017
- **Observation**: system_a_access level is maker, should be checker.
- **Risk Rating**: High
- **Risks**: Unauthorized access to critical functions.
- **Management Actions**: Adjust system_a_access level to checker.

#### USER021
- **Observation**: Unauthorized access to system_a_access, system_b_access, system_c_access.
- **Risk Rating**: Critical
- **Risks**: Severe unauthorized access to all systems.
- **Management Actions**: Revoke all access for USER021.

#### USER022
- **Observation**: Unauthorized access to system_a_access, system_b_access, system_c_access.
- **Risk Rating**: Critical
- **Risks**: Severe unauthorized access to all systems.
- **Management Actions**: Revoke all access for USER022.

#### USER023
- **Observation**: Unauthorized access to system_a_access, system_b_access, system_c_access.
- **Risk Rating**: Critical
- **Risks**: Severe unauthorized access to all systems.
- **Management Actions**: Revoke all access for USER023.

#### USER024
- **Observation**: Unauthorized access to system_a_access, system_b_access, system_c_access.
- **Risk Rating**: Critical
- **Risks**: Severe unauthorized access to all systems.
- **Management Actions**: Revoke all access for USER024.

### Transaction Limit Compliance Analysis

#### Transaction 0
- **Observation**: Transaction Amount Exceed user Approval Level for USER008.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER008's approval limits.

#### Transaction 3
- **Observation**: Transaction Amount Exceed user Approval Level for USER009.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER009's approval limits.

#### Transaction 7
- **Observation**: Transaction Amount Exceed user Approval Level for USER010.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER010's approval limits.

#### Transaction 9
- **Observation**: Transaction Amount Exceed user Approval Level for USER005.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER005's approval limits.

#### Transaction 14
- **Observation**: Transaction Amount Exceed the joint Approval Level of users ['USER001', 'USER002', 'USER003'].
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust joint approval limits for USER001, USER002, and USER003.

### Change Management Audit Findings

#### Transaction 0
- **Observation**: Transaction Amount Exceed user Approval Level for USER008.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER008's approval limits.

#### Transaction 3
- **Observation**: Transaction Amount Exceed user Approval Level for USER009.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER009's approval limits.

#### Transaction 7
- **Observation**: Transaction Amount Exceed user Approval Level for USER010.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER010's approval limits.

#### Transaction 9
- **Observation**: Transaction Amount Exceed user Approval Level for USER005.
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust USER005's approval limits.

#### Transaction 14
- **Observation**: Transaction Amount Exceed the joint Approval Level of users ['USER001', 'USER002', 'USER003'].
- **Risk Rating**: High
- **Risks**: Financial loss due to unauthorized transaction approval.
- **Management Actions**: Review and adjust joint approval limits for USER001, USER002, and USER003.
```