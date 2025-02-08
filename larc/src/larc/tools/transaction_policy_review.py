from crewai.tools import tool
from crewai import LLM
import csv
import PyPDF2
from pathlib import Path
from typing import Dict, Any
from pydantic import BaseModel, Field
import datetime,os
from openai import OpenAI



class TransactionPolicyReview:
    @tool("transaction_policy_review_tool")
    def transaction_policy_review_tool(self) -> Dict[str, Any]:
        """
        Review transactions against a specified policy using an LLM for compliance checking.
        
        Returns:
        dict: Dictionary containing transaction details and their policy compliance analysis
        """
        # Path setup
        base_dir = Path(__file__).resolve().parent
        #data_dir = base_dir.parent / 'data'
        data_dir =  base_dir / 'data'
        docs_dir = data_dir

        # File paths
        csv_path = data_dir / 'transaction_records.csv'
        pdf_path = docs_dir / 'transaction_policy.pdf'

        def load_transactions(csv_file):
            transactions = {}
            with open(csv_file, mode='r') as file:
                csv_reader = csv.DictReader(file)
                for idx, row in enumerate(csv_reader, 1):
                    transaction_id = f"transaction_{idx}"
                    transactions[transaction_id] = {
                        "details": row,
                        "policy_compliance": None
                    }
            return transactions

        def extract_policy_text(pdf_file):
            with open(pdf_file, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                policy_text = ""
                for page_num in range(len(reader.pages)):
                    policy_text += reader.pages[page_num].extract_text()
            return policy_text


        def check_transaction_against_policy(transaction_details, policy_text):
            transaction_str = ', '.join(f"{key}: {value}" for key, value in transaction_details.items())
            
            messages = [
                {"role": "system", "content": "You are a policy compliance assistant. Analyze the transaction and provide a detailed compliance assessment."},
                {"role": "user", "content": f"""
                Review this transaction against the policy and provide a structured response:
                
                Policy:
                {policy_text}
                
                Transaction:
                {transaction_str}
                
                Please provide:
                1. Compliance Status (Compliant/Non-Compliant)
                2. Detailed explanation
                3. Specific policy rules referenced
                """}
            ]

            # Get environment variables
            model = os.getenv('DEEPSEEK_MODEL')
            api_key = os.getenv('DEEPSEEK_API_KEY')
            base_url = os.getenv('DEEPSEEK_API_BASE')

            # Initialize OpenAI client
            client = OpenAI(api_key=api_key, base_url=base_url)

            # Get completion
            result = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=False
            )
            
            # Extract the response content correctly
            return result.choices[0].message.content

        try:
            # Load data
            transactions = load_transactions(csv_path)
            policy_text = extract_policy_text(pdf_path)

            # Create response structure
            response = {
                "analysis_summary": {
                    "total_transactions": len(transactions),
                    "analysis_timestamp": datetime.datetime.now().isoformat(),
                },
                "transactions": {}
            }

            # Analyze each transaction
            for transaction_id, transaction_data in transactions.items():
                compliance_result = check_transaction_against_policy(
                    transaction_data["details"], 
                    policy_text
                )
                
                response["transactions"][transaction_id] = {
                    "transaction_details": transaction_data["details"],
                    "compliance_analysis": compliance_result
                }

            return response

        except Exception as e:
            return {
                "error": str(e),
                "status": "failed",
                "timestamp": datetime.datetime.now().isoformat()
            }