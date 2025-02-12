# tool/transaction_policy_review_tool.py
from crewai.tools import tool
import csv
import PyPDF2
from langchain_ollama import ChatOllama
from tqdm import tqdm
import os, time


class TransactionPolicyReview:
    @tool("transaction_policy_review_tool")
    def transaction_policy_review_tool():
        """Reviews all transactions against policy document using LLM analysis.
        Returns list of transactions with violation status."""
      
        
        # File paths relative to tool directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        CSV_PATH = os.path.join(BASE_DIR, 'data', 'transaction_records.csv')
        PDF_PATH = os.path.join(BASE_DIR, 'data', 'transaction_policy.pdf')
        
        # Load transactions and policy
        def load_transactions():
            with open(CSV_PATH, 'r') as file:
                return [row for row in csv.DictReader(file)]
        
        def extract_policy():
            with open(PDF_PATH, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                return ''.join(page.extract_text() for page in reader.pages)
        
        # LLM configuration
        LLM_MODEL = "deepseek-r1:14b"
        chat_ollama = ChatOllama(model=LLM_MODEL)
        
        # Process transactions
        transactions = load_transactions()
        policy_text = extract_policy()
        
        for transaction in tqdm(transactions, desc="Policy Review"):
            transaction_str = ', '.join(f"{k}: {v}" for k, v in transaction.items())
            messages = [
                {
                    "role": "system",
                    "content": "You are a financial compliance auditor. Analyze transactions for policy violations. Make sure to cover all rules in the policy. If there are multiple policy violations, make sure to add them all including the reference in the policy condition that is violated. "
                },
                {
                    "role": "user",
                    "content": f"Policy: {policy_text}\n\nTransaction: {transaction_str}\n\n"
                            "Answer with ONLY: 'Violation: [Yes/No] - [reason]'"
                }
            ]
            response = chat_ollama.invoke(messages)
            transaction['violation'] = response.content
            
        return transactions