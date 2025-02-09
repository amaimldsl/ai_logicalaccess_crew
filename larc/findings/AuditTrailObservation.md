# Change Management Audit Findings

## Summary of Findings

The following audit trail records were analyzed against change tickets based on the change management SLA. The results are categorized into compliant and non-compliant records.

---

### **Compliant Records**

1. **Date/Time**: 2024-01-19 11:45:00  
   - **Component Modified**: DatabaseConfig  
   - **Modified by User**: USER002  
   - **Result**: Audit trail record relies on change ticket: CHG003 and was carried out by the authorized user: USER002.

2. **Date/Time**: 2024-01-16 18:30:00  
   - **Component Modified**: NetworkSettings  
   - **Modified by User**: USER007  
   - **Result**: Audit trail record relies on change ticket: CHG004 and was carried out by the authorized user: USER007.

3. **Date/Time**: 2024-01-17 11:15:00  
   - **Component Modified**: APIEndpoints  
   - **Modified by User**: USER003  
   - **Result**: Audit trail record relies on change ticket: CHG005 and was carried out by the authorized user: USER003.

4. **Date/Time**: 2024-01-17 17:40:00  
   - **Component Modified**: LoggingSystem  
   - **Modified by User**: USER005  
   - **Result**: Audit trail record relies on change ticket: CHG006 and was carried out by the authorized user: USER005.

5. **Date/Time**: 2024-01-18 23:25:00  
   - **Component Modified**: BackupSystem  
   - **Modified by User**: USER006  
   - **Result**: Audit trail record relies on change ticket: CHG008 and was carried out by the authorized user: USER006.

6. **Date/Time**: 2024-01-21 19:50:00  
   - **Component Modified**: UserManagement  
   - **Modified by User**: USER003  
   - **Result**: Audit trail record relies on change ticket: CHG014 and was carried out by the authorized user: USER003.

---

### **Non-Compliant Records**

1. **Date/Time**: 2024-01-14 09:30:00  
   - **Component Modified**: UserAccessModule  
   - **Modified by User**: USER001  
   - **Result**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

2. **Date/Time**: 2024-01-15 04:20:00  
   - **Component Modified**: SecuritySettings  
   - **Modified by User**: USER004  
   - **Result**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

3. **Date/Time**: 2024-10-18 09:00:00  
   - **Component Modified**: UserInterface  
   - **Modified by User**: USER008  
   - **Result**: Audit trail record date is found with the authorized user: USER008; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

4. **Date/Time**: 2024-02-19 11:30:00  
   - **Component Modified**: AuthModule  
   - **Modified by User**: USER001  
   - **Result**: Audit trail record date is found with the authorized user: USER001; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

5. **Date/Time**: 2024-01-19 06:15:00  
   - **Component Modified**: ReportingEngine  
   - **Modified by User**: USER004  
   - **Result**: Audit trail record date is found with the authorized user: USER004; however - it might be a change management violation as there were no change tickets found that satisfy the change management SLA.

6. **Date/Time**: 2024-01-20 11:45:00  
   - **Component Modified**: DataProcessor  
   - **Modified by User**: USER009  
   - **Result**: Audit trail record date is found linked to change ticket: CHG011, however the change was carried out by the unauthorized user: USER009 - while it should have been carried out by: USER002.

7. **Date/Time**: 2024-01-20 19:20:00  
   - **Component Modified**: SecurityModule  
   - **Modified by User**: USER002  
   - **Result**: Audit trail record date is found linked to change ticket: CHG012, however the change was carried out by the unauthorized user: USER002 - while it should have been carried out by: USER005.

8. **Date/Time**: 2024-01-21 10:15:00  
   - **Component Modified**: ConfigSettings  
   - **Modified by User**: USER005  
   - **Result**: Audit trail record date is found linked to change ticket: CHG013, however the change was carried out by the unauthorized user: USER005 - while it should have been carried out by: USER007.

9. **Date/Time**: 2024-01-29 10:30:00  
   - **Component Modified**: APIGateway  
   - **Modified by User**: USER007  
   - **Result**: Could not find any change ticket that is related to this audit trail record.

10. **Date/Time**: 2024-01-22 15:45:00  
    - **Component Modified**: DatabaseIndex  
    - **Modified by User**: USER001  
    - **Result**: Could not find any change ticket that is related to this audit trail record.

11. **Date/Time**: 2024-01-23 09:45:00  
    - **Component Modified**: AccessControl  
    - **Modified by User**: USER006  
    - **Result**: Could not find any change ticket that is related to this audit trail record.

12. **Date/Time**: 2024-01-23 14:30:00  
    - **Component Modified**: SystemCore  
    - **Modified by User**: USER004  
    - **Result**: Could not find any change ticket that is related to this audit trail record.

13. **Date/Time**: 2024-01-24 11:00:00  
    - **Component Modified**: LogAnalyzer  
    - **Modified by User**: USER008  
    - **Result**: Could not find any change ticket that is related to this audit trail record.

14. **Date/Time**: 2024-01-24 16:00:00  
    - **Component Modified**: WebService  
    - **Modified by User**: USER002  
    - **Result**: Could not find any change ticket that is related to this audit trail record.

---

## Notes

- **Non-Compliant Records**: These records either lack corresponding change tickets or were carried out by unauthorized users. Immediate action is required to rectify these discrepancies.
- **Compliant Records**: These records are in compliance with the change management SLA and do not require further action.
```