from crewai.tools import tool
import pandas as pd
import PyPDF2
import io
from pathlib import Path

class TransactionApprovalReview:
    @tool("transaction_approval_review_tool")
    def access_review_tool() -> str:
        """
        Analyze transaction approvals based on authorization limits.
        Reviews each transaction to check if it complies with single or joint approval limits.
        
        Returns:
            str: Detailed analysis of transaction approvals
        """
        # Determine file paths
        base_dir = Path(__file__).resolve().parent
        data_dir = base_dir.parent / 'data'
        
        # Paths to PDF and CSV
        pdf_path = data_dir / 'limit_authorization.pdf'
        csv_path = data_dir / 'transaction_logs.csv'
        
        # Read PDF content
        with open(pdf_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()
        
        # Create PDF reader
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))
        
        # Extract text from first page
        text = pdf_reader.pages[0].extract_text()
        
        # Parse limits from text
        limits = {}
        for line in text.split('\n')[1:]:  # Skip header
            if line.strip():
                parts = line.split(',')
                if len(parts) == 4:
                    user_level, user_id, single_limit, joint_limit = parts
                    limits[user_id] = {
                        'level': user_level.strip(),
                        'single_approval_limit': float(single_limit.strip()),
                        'joint_approval_limit': float(joint_limit.strip())
                    }
        
        # Read transaction logs
        df = pd.read_csv(csv_path)
        
        # Prepare results
        results = {}
        
        for idx, transaction in df.iterrows():
            # Get approved users for this transaction
            approved_users = [user for user in [
                transaction['approval_one_user'], 
                transaction['approval_two_user'], 
                transaction['approval_three_user']
            ] if pd.notna(user)]
            
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