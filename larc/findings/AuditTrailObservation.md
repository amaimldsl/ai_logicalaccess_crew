# Change Management Audit Findings

## Summary
This document outlines the findings from the change management compliance review conducted to verify audit trail records against change tickets based on the change management SLA. The review identified discrepancies and potential process violations for several changes.

---

## Detailed Findings

### Change 0
- **Date and Time**: 2024-01-14 09:30:00
- **Component Modified**: UserAccessModule
- **Modified By User**: USER001
- **Analysis Result**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Change 1
- **Date and Time**: 2024-01-15 04:20:00
- **Component Modified**: SecuritySettings
- **Modified By User**: USER004
- **Analysis Result**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Change 2
- **Date and Time**: 2024-01-19 11:45:00
- **Component Modified**: DatabaseConfig
- **Modified By User**: USER002
- **Analysis Result**: Audit trail record relies on change ticket: CHG003 and was carried out by the authorized user: USER002

### Change 3
- **Date and Time**: 2024-01-16 18:30:00
- **Component Modified**: NetworkSettings
- **Modified By User**: USER007
- **Analysis Result**: Audit trail record relies on change ticket: CHG004 and was carried out by the authorized user: USER007

### Change 4
- **Date and Time**: 2024-01-17 11:15:00
- **Component Modified**: APIEndpoints
- **Modified By User**: USER003
- **Analysis Result**: Audit trail record relies on change ticket: CHG005 and was carried out by the authorized user: USER003

### Change 5
- **Date and Time**: 2024-01-17 17:40:00
- **Component Modified**: LoggingSystem
- **Modified By User**: USER005
- **Analysis Result**: Audit trail record relies on change ticket: CHG006 and was carried out by the authorized user: USER005

### Change 6
- **Date and Time**: 2024-10-18 09:00:00
- **Component Modified**: UserInterface
- **Modified By User**: USER008
- **Analysis Result**: Audit trail record date is found with the authorized user: USER008; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Change 7
- **Date and Time**: 2024-01-18 23:25:00
- **Component Modified**: BackupSystem
- **Modified By User**: USER006
- **Analysis Result**: Audit trail record relies on change ticket: CHG008 and was carried out by the authorized user: USER006

### Change 8
- **Date and Time**: 2024-02-19 11:30:00
- **Component Modified**: AuthModule
- **Modified By User**: USER001
- **Analysis Result**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Change 9
- **Date and Time**: 2024-01-19 06:15:00
- **Component Modified**: ReportingEngine
- **Modified By User**: USER004
- **Analysis Result**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Change 10
- **Date and Time**: 2024-01-20 11:45:00
- **Component Modified**: DataProcessor
- **Modified By User**: USER009
- **Analysis Result**: Audit trail record date is found linked to change ticket: CHG011, however the change was carried out by the unauthorized user: USER009 - while it should have been carried out by: USER002

### Change 11
- **Date and Time**: 2024-01-20 19:20:00
- **Component Modified**: SecurityModule
- **Modified By User**: USER002
- **Analysis Result**: Audit trail record date is found linked to change ticket: CHG012, however the change was carried out by the unauthorized user: USER002 - while it should have been carried out by: USER005

### Change 12
- **Date and Time**: 2024-01-21 10:15:00
- **Component Modified**: ConfigSettings
- **Modified By User**: USER005
- **Analysis Result**: Audit trail record date is found linked to change ticket: CHG013, however the change was carried out by the unauthorized user: USER005 - while it should have been carried out by: USER007

### Change 13
- **Date and Time**: 2024-01-21 19:50:00
- **Component Modified**: UserManagement
- **Modified By User**: USER003
- **Analysis Result**: Audit trail record relies on change ticket: CHG014 and was carried out by the authorized user: USER003

### Change 14
- **Date and Time**: 2024-01-29 10:30:00
- **Component Modified**: APIGateway
- **Modified By User**: USER007
- **Analysis Result**: Could not find any change ticket that is related to this audit trail record.

### Change 15
- **Date and Time**: 2024-01-22 15:45:00
- **Component Modified**: DatabaseIndex
- **Modified By User**: USER001
- **Analysis Result**: Could not find any change ticket that is related to this audit trail record.

### Change 16
- **Date and Time**: 2024-01-23 09:45:00
- **Component Modified**: AccessControl
- **Modified By User**: USER006
- **Analysis Result**: Could not find any change ticket that is related to this audit trail record.

### Change 17
- **Date and Time**: 2024-01-23 14:30:00
- **Component Modified**: SystemCore
- **Modified By User**: USER004
- **Analysis Result**: Could not find any change ticket that is related to this audit trail record.

### Change 18
- **Date and Time**: 2024-01-24 11:00:00
- **Component Modified**: LogAnalyzer
- **Modified By User**: USER008
- **Analysis Result**: Could not find any change ticket that is related to this audit trail record.

### Change 19
- **Date and Time**: 2024-01-24 16:00:00
- **Component Modified**: WebService
- **Modified By User**: USER002
- **Analysis Result**: Could not find any change ticket that is related to this audit trail record.

---

## Recommendations
1. **Immediate Remediation**: Investigate and address changes flagged with discrepancies or unauthorized users.
2. **Process Review**: Ensure all changes are accompanied by valid change tickets that satisfy the change management SLA.
3. **Regular Audits**: Conduct periodic change management reviews to maintain compliance and prevent unauthorized changes.
4. **User Training**: Educate users on change management policies and the importance of adhering to the change management SLA.

--- 

**Prepared by**: Change Management Compliance Analyst  
**Date**: [Insert Date]  
**Version**: 1.0
```