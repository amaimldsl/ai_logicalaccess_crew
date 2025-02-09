from crewai.tools import tool
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
import time

class ChangeManagementVerification:

    @tool("change_management_verification_tool")
    def change_management_verification_tool() -> dict:
        """
        Verify audit trail records against change tickets based on change management SLA.
        
        Returns:
        dict: Verification results for each audit trail record
        """
    
        # Paths to input files
        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir.parent / 'data'
        
        audit_trail_path = data_dir / 'audit_trail.csv'
        change_tickets_path = data_dir / 'change_tickets.csv'
        
        # Load CSV files
        audit_trail_df = pd.read_csv(audit_trail_path)
        change_tickets_df = pd.read_csv(change_tickets_path)
        
        # Verification results dictionary
        verification_results = []
        
        # Iterate through each audit trail record
        for _, trail_rec in audit_trail_df.iterrows():
            # Find related change tickets for the same component
            related_tickets = change_tickets_df[
                change_tickets_df['affected_component'] == trail_rec['component_modified']
            ]
            
            # Flag to track if a matching ticket was found
            ticket_found = False
            
            # Process each related ticket
            for _, ticket_rec in related_tickets.iterrows():
                # Convert datetime strings to datetime objects
                trail_datetime = datetime.strptime(trail_rec['date_time'], '%Y-%m-%d %H:%M:%S')
                ticket_datetime = datetime.strptime(ticket_rec['date_time'], '%Y-%m-%d %H:%M:%S')
                
                # SLA Calculation based on change criticality
                sla_map = {
                    'Emergency': (ticket_datetime, ticket_datetime + timedelta(hours=6)),
                    'High': (ticket_datetime, ticket_datetime + timedelta(days=1)),
                    'Medium': (ticket_datetime, ticket_datetime + timedelta(days=2)),
                    'Low': (ticket_datetime, ticket_datetime + timedelta(days=3))
                }
                
                # Get SLA time range for this ticket's criticality
                min_time, max_time = sla_map.get(ticket_rec['change_criticality'], (None, None))
                
                # Condition A: Check if trail datetime is within SLA
                condition_a = min_time and max_time and min_time < trail_datetime <= max_time
                
                # Condition B: Check if modified by authorized user
                condition_b = trail_rec['modified_by_user'] == ticket_rec['assigned_to_user']
                
                # Determine verification result
                if condition_a and condition_b:
                    verification_result = (
                        f"Audit trail record relies on change ticket: {ticket_rec['ticket_number']} "
                        f"and was carried out by the authorized user: {ticket_rec['assigned_to_user']}"
                    )
                    ticket_found = True
                elif condition_a and not condition_b:
                    verification_result = (
                        f"Audit trail record date is found linked to change ticket: {ticket_rec['ticket_number']}, "
                        f"however the change was carried out by the unauthorized user: {trail_rec['modified_by_user']} "
                        f"- while it should have been carried out by: {ticket_rec['assigned_to_user']}"
                    )
                    ticket_found = True
                elif not condition_a and condition_b:
                    verification_result = (
                        f"Audit trail record date is found with the authorized user: {ticket_rec['assigned_to_user']}; "
                        "however - it might be a change management violation as there were no change tickets "
                        "found that satisfy the change management SLA."
                    )
                    ticket_found = True
            
            # If no matching ticket found
            if not ticket_found:
                verification_result = "Could not find any change ticket that is related to this audit trail record."
            
            # Prepare full record with verification result
            result_rec = trail_rec.to_dict()
            result_rec['Verification_Results'] = verification_result
            verification_results.append(result_rec)
        
        return verification_results

# Example usage
# results = ChangeManagementVerification.change_management_verification_tool()
# print(results)