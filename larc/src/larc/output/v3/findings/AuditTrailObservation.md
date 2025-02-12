# Change Management Audit Findings

## Summary of Audit Findings

The following audit trail records were analyzed against change tickets based on the change management SLA:

### Audit Trail Record 0
- **Date/Time**: 2024-01-14 09:30:00
- **Component Modified**: UserAccessModule
- **Modified By User**: USER001
- **Verification Results**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Audit Trail Record 1
- **Date/Time**: 2024-01-15 04:20:00
- **Component Modified**: SecuritySettings
- **Modified By User**: USER004
- **Verification Results**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Audit Trail Record 2
- **Date/Time**: 2024-01-19 11:45:00
- **Component Modified**: DatabaseConfig
- **Modified By User**: USER002
- **Verification Results**: Audit trail record relies on change ticket: CHG003 and was carried out by the authorized user: USER002

### Audit Trail Record 3
- **Date/Time**: 2024-01-16 18:30:00
- **Component Modified**: NetworkSettings
- **Modified By User**: USER007
- **Verification Results**: Audit trail record relies on change ticket: CHG004 and was carried out by the authorized user: USER007

### Audit Trail Record 4
- **Date/Time**: 2024-01-17 11:15:00
- **Component Modified**: APIEndpoints
- **Modified By User**: USER003
- **Verification Results**: Audit trail record relies on change ticket: CHG005 and was carried out by the authorized user: USER003

### Audit Trail Record 5
- **Date/Time**: 2024-01-17 17:40:00
- **Component Modified**: LoggingSystem
- **Modified By User**: USER005
- **Verification Results**: Audit trail record relies on change ticket: CHG006 and was carried out by the authorized user: USER005

### Audit Trail Record 6
- **Date/Time**: 2024-10-18 09:00:00
- **Component Modified**: UserInterface
- **Modified By User**: USER008
- **Verification Results**: Audit trail record date is found with the authorized user: USER008; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Audit Trail Record 7
- **Date/Time**: 2024-01-18 23:25:00
- **Component Modified**: BackupSystem
- **Modified By User**: USER006
- **Verification Results**: Audit trail record relies on change ticket: CHG008 and was carried out by the authorized user: USER006

### Audit Trail Record 8
- **Date/Time**: 2024-02-19 11:30:00
- **Component Modified**: AuthModule
- **Modified By User**: USER001
- **Verification Results**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Audit Trail Record 9
- **Date/Time**: 2024-01-19 06:15:00
- **Component Modified**: ReportingEngine
- **Modified By User**: USER004
- **Verification Results**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

### Audit Trail Record 10
- **Date/Time**: 2024-01-20 11:45:00
- **Component Modified**: DataProcessor
- **Modified By User**: USER009
- **Verification Results**: Audit trail record date is found linked to change ticket: CHG011, however the change was carried out by the unauthorized user: USER009 - while it should have been carried out by: USER002

### Audit Trail Record 11
- **Date/Time**: 2024-01-20 19:20:00
- **Component Modified**: SecurityModule
- **Modified By User**: USER002
- **Verification Results**: Audit trail record date is found linked to change ticket: CHG012, however the change was carried out by the unauthorized user: USER002 - while it should have been carried out by: USER005

### Audit Trail Record 12
- **Date/Time**: 2024-01-21 10:15:00
- **Component Modified**: ConfigSettings
- **Modified By User**: USER005
- **Verification Results**: Audit trail record date is found linked to change ticket: CHG013, however the change was carried out by the unauthorized user: USER005 - while it should have been carried out by: USER007

### Audit Trail Record 13
- **Date/Time**: 2024-01-21 19:50:00
- **Component Modified**: UserManagement
- **Modified By User**: USER003
- **Verification Results**: Audit trail record relies on change ticket: CHG014 and was carried out by the authorized user: USER003

### Audit Trail Record 14
- **Date/Time**: 2024-01-29 10:30:00
- **Component Modified**: APIGateway
- **Modified By User**: USER007
- **Verification Results**: Could not find any change ticket that is related to this audit trail record.

### Audit Trail Record 15
- **Date/Time**: 2024-01-22 15:45:00
- **Component Modified**: DatabaseIndex
- **Modified By User**: USER001
- **Verification Results**: Could not find any change ticket that is related to this audit trail record.

### Audit Trail Record 16
- **Date/Time**: 2024-01-23 09:45:00
- **Component Modified**: AccessControl
- **Modified By User**: USER006
- **Verification Results**: Could not find any change ticket that is related to this audit trail record.

### Audit Trail Record 17
- **Date/Time**: 2024-01-23 14:30:00
- **Component Modified**: SystemCore
- **Modified By User**: USER004
- **Verification Results**: Could not find any change ticket that is related to this audit trail record.

### Audit Trail Record 18
- **Date/Time**: 2024-01-24 11:00:00
- **Component Modified**: LogAnalyzer
- **Modified By User**: USER008
- **Verification Results**: Could not find any change ticket that is related to this audit trail record.

### Audit Trail Record 19
- **Date/Time**: 2024-01-24 16:00:00
- **Component Modified**: WebService
- **Modified By User**: USER002
- **Verification Results**: Could not find any change ticket that is related to this audit trail record.

## Recommendations
1. **Immediate Review**: Audit trail records with potential change management violations (Audit Trail Records 0, 1, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19) should be reviewed and re-approved by authorized personnel.
2. **Process Improvement**: Consider enhancing the change management process to ensure all changes are properly documented and approved.
3. **Periodic Reviews**: Conduct periodic reviews of audit trail records to ensure compliance with change management policies.

## Conclusion
This report highlights audit trail records that may violate change management policies and those that comply with the authorized change management process. Immediate action is required to address non-compliant records and ensure future compliance.
```