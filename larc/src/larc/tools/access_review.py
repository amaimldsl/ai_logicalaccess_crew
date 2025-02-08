from crewai.tools import tool
import pandas as pd
from pathlib import Path

class AccessReview:

    @tool("access_review_tool")
    def access_review_tool() -> str:
        """Clear description for what this tool is useful for, your agent will need this information to use it."""
        # Function logic here

        #path of access report and access matrix files
        base_dir = Path(__file__).resolve().parent  # path to tool.py
        data_dir = base_dir.parent / 'data'  # going up one level, then into the data directory

        ar_path = data_dir / 'access_report.csv'
        arm_path = data_dir / 'access_matrix.csv'

        # Load CSV files
        ar_df = pd.read_csv(ar_path)
        arm_df = pd.read_csv(arm_path)
        
        # Initialize results dictionary
        results = {}
        
        # Iterate through each user in AR
        for _, ar_row in ar_df.iterrows():
            user_id = ar_row["user_id"]
            review_results = {}
            
            # Find the corresponding row in ARM
            arm_row = arm_df[arm_df["user_id"] == user_id]
            
            for system in ["system_a_access", "system_b_access", "system_c_access"]:
                actual_access = ar_row[system]
                
                if not arm_row.empty:
                    expected_access = arm_row.iloc[0][system]
                    
                    if actual_access == expected_access:
                        result = f"user has actual access level of {actual_access} which is matching his {system} level in access matrix."
                    else:
                        result = f"user has actual {system} access level of {actual_access} in Access Report while he should have {system} access level as {expected_access} according to the access matrix."
                else:
                    result = f"user has {system} access level of {actual_access} in Access Report while he is unauthorized to have access to {system} according to access matrix."
                
                review_results[system] = result
            
            results[user_id] = {"review_results": review_results}
        
        return results

    # Example usage:
    # ar_path = "path/to/access_report.csv"
    # arm_path = "path/to/access_matrix.csv"
    # results = analyze_access_report(ar_path, arm_path)
    # print(results)



