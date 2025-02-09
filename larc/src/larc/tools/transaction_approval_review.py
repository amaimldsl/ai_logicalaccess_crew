from crewai.tools import tool
import pandas as pd
from pathlib import Path
import time



class TransactionApprovalReview:
    @tool("transalimit_review_tool")
    def limit_review_tool() -> str:
        """
        Analyze transaction approvals based on authorization limits.
        Reviews each transaction to check if it complies with single or joint approval limits.
        
        Returns:
            str: Detailed analysis of transaction approvals
        """

        print("Limit Tool -- Waiting for 2 minutes...")
        time.sleep(120)  # 120 seconds = 2 minutes
        print("2 minutes have passed!")

        # Determine file paths
        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir.parent / 'data'
        
        # Paths to CSV files
        limits_path = data_dir / 'limit_authorization.csv'
        transactions_path = data_dir / 'transaction_logs.csv'
        
        # Read authorization limits
        limits_df = pd.read_csv(limits_path)
        
        # Convert limits to dictionary for easy lookup
        limits = {}
        for _, row in limits_df.iterrows():
            limits[row['user_id']] = {
                'level': row['user_level'],
                'single_approval_limit': row['single_approval_limit'],
                'joint_approval_limit': row['joint_approval_limit']
            }
        
        # Read transaction logs
        df = pd.read_csv(transactions_path)
        
        # Prepare results
        results = {}
        
        for idx, transaction in df.iterrows():
            # Dynamically find all approval users
            approved_users = [
                user for user in transaction.filter(like='approval_').dropna().to_list()
                if pd.notna(user)
            ]
            
            # Transaction details
            transaction_details = {
                'transaction_amount': transaction['transaction_amount'],
                'transaction_date': transaction['date'],
                'approved_users': approved_users
            }
            
            # Single user approval check
            if len(approved_users) == 1:
                user = approved_users[0]
                if user not in limits:
                    transaction_details['Analysis_Result'] = f"User {user} not found in authorization limits"
                    results[f'transaction_{idx}'] = transaction_details
                    continue
                
                single_limit = limits[user]['single_approval_limit']
                if transaction['transaction_amount'] > single_limit:
                    transaction_details['Analysis_Result'] = f"Transaction Amount Exceed user Approval Level for {user}"
                else:
                    transaction_details['Analysis_Result'] = f"Transaction is approved within the single approval limit of {user}"
            
            # Multiple user (joint) approval check
            elif len(approved_users) > 1:
                # Get max joint approval limit among involved users
                max_joint_limit = max(
                    limits.get(user, {}).get('joint_approval_limit', 0) 
                    for user in approved_users
                )
                
                if transaction['transaction_amount'] > max_joint_limit:
                    transaction_details['Analysis_Result'] = f"Transaction Amount Exceed the joint Approval Level of users {approved_users}"
                else:
                    transaction_details['Analysis_Result'] = f"Transaction is approved within the joint approval limit of users {approved_users}"
            
            # No approvers
            else:
                transaction_details['Analysis_Result'] = "No users approved this transaction"
            
            results[f'transaction_{idx}'] = transaction_details
        
        return str(results)