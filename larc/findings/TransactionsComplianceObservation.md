# Change Management Audit Findings

## Audit Trail Verification Results

### Verified Transactions
1. **Date**: 2024-01-19 11:45:00  
   **Component Modified**: DatabaseConfig  
   **Modified By**: USER002  
   **Verification Results**: Audit trail record relies on change ticket: CHG003 and was carried out by the authorized user: USER002  

2. **Date**: 2024-01-16 18:30:00  
   **Component Modified**: NetworkSettings  
   **Modified By**: USER007  
   **Verification Results**: Audit trail record relies on change ticket: CHG004 and was carried out by the authorized user: USER007  

3. **Date**: 2024-01-17 11:15:00  
   **Component Modified**: APIEndpoints  
   **Modified By**: USER003  
   **Verification Results**: Audit trail record relies on change ticket: CHG005 and was carried out by the authorized user: USER003  

4. **Date**: 2024-01-17 17:40:00  
   **Component Modified**: LoggingSystem  
   **Modified By**: USER005  
   **Verification Results**: Audit trail record relies on change ticket: CHG006 and was carried out by the authorized user: USER005  

5. **Date**: 2024-01-18 23:25:00  
   **Component Modified**: BackupSystem  
   **Modified By**: USER006  
   **Verification Results**: Audit trail record relies on change ticket: CHG008 and was carried out by the authorized user: USER006  

6. **Date**: 2024-01-21 19:50:00  
   **Component Modified**: UserManagement  
   **Modified By**: USER003  
   **Verification Results**: Audit trail record relies on change ticket: CHG014 and was carried out by the authorized user: USER003  

### Potential Violations
1. **Date**: 2024-01-14 09:30:00  
   **Component Modified**: UserAccessModule  
   **Modified By**: USER001  
   **Verification Results**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.  

2. **Date**: 2024-01-15 04:20:00  
   **Component Modified**: SecuritySettings  
   **Modified By**: USER004  
   **Verification Results**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.  

3. **Date**: 2024-10-18 09:00:00  
   **Component Modified**: UserInterface  
   **Modified By**: USER008  
   **Verification Results**: Audit trail record date is found with the authorized user: USER008; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.  

4. **Date**: 2024-02-19 11:30:00  
   **Component Modified**: AuthModule  
   **Modified By**: USER001  
   **Verification Results**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.  

5. **Date**: 2024-01-19 06:15:00  
   **Component Modified**: ReportingEngine  
   **Modified By**: USER004  
   **Verification Results**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.  

6. **Date**: 2024-01-20 11:45:00  
   **Component Modified**: DataProcessor  
   **Modified By**: USER009  
   **Verification Results**: Audit trail record date is found linked to change ticket: CHG011, however the change was carried out by the unauthorized user: USER009 - while it should have been carried out by: USER002  

7. **Date**: 2024-01-20 19:20:00  
   **Component Modified**: SecurityModule  
   **Modified By**: USER002  
   **Verification Results**: Audit trail record date is found linked to change ticket: CHG012, however the change was carried out by the unauthorized user: USER002 - while it should have been carried out by: USER005  

8. **Date**: 2024-01-21 10:15:00  
   **Component Modified**: ConfigSettings  
   **Modified By**: USER005  
   **Verification Results**: Audit trail record date is found linked to change ticket: CHG013, however the change was carried out by the unauthorized user: USER005 - while it should have been carried out by: USER007  

9. **Date**: 2024-01-29 10:30:00  
   **Component Modified**: APIGateway  
   **Modified By**: USER007  
   **Verification Results**: Could not find any change ticket that is related to this audit trail record.  

10. **Date**: 2024-01-22 15:45:00  
    **Component Modified**: DatabaseIndex  
    **Modified By**: USER001  
    **Verification Results**: Could not find any change ticket that is related to this audit trail record.  

11. **Date**: 2024-01-23 09:45:00  
    **Component Modified**: AccessControl  
    **Modified By**: USER006  
    **Verification Results**: Could not find any change ticket that is related to this audit trail record.  

12. **Date**: 2024-01-23 14:30:00  
    **Component Modified**: SystemCore  
    **Modified By**: USER004  
    **Verification Results**: Could not find any change ticket that is related to this audit trail record.  

13. **Date**: 2024-01-24 11:00:00  
    **Component Modified**: LogAnalyzer  
    **Modified By**: USER008  
    **Verification Results**: Could not find any change ticket that is related to this audit trail record.  

14. **Date**: 2024-01-24 16:00:00  
    **Component Modified**: WebService  
    **Modified By**: USER002  
    **Verification Results**: Could not find any change ticket that is related to this audit trail record.  

## Summary
- **Total Audit Records Reviewed**: 20  
- **Records Verified with Change Tickets**: 6  
- **Records with Potential Violations**: 14  

## Recommendations
1. Investigate and resolve the potential violations identified in the audit trail records.  
2. Ensure all changes are associated with valid change tickets that comply with the change management SLA.  
3. Conduct regular audits to ensure ongoing compliance with change management policies.  
4. Provide additional training to users involved in unauthorized changes to prevent future violations.  
```