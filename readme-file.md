# LARC - Logical Access Review Crew

LARC is an AI-powered audit automation framework that performs comprehensive IT compliance audits using a crew of specialized AI agents. This system leverages the CrewAI framework to simulate a team of auditors, each with specific roles, working together to analyze access controls, transaction limits, change management processes, and policy compliance.

## Overview

LARC uses a multi-agent architecture to distribute audit tasks among specialized AI agents, simulating a traditional audit team's workflow. Each agent has a defined role, expertise, and scope of review, leading to a comprehensive and well-structured audit report.

## Architecture

The system consists of the following components:

### Core Components

- **Crew Module (`crew.py`)**: Defines the main LARC class, which orchestrates the entire audit process by creating agents, assigning tasks, and managing the workflow
- **Main Application (`main.py`)**: Entry point that initializes the LARC system with necessary API credentials and kicks off the audit process

### Agents

LARC features five specialized agents (defined in `agents.yaml`):

1. **Logical Access Reviewer**: Analyzes system access levels against authorized access matrices
2. **Limit Reviewer**: Reviews transaction approvals against authorized limits
3. **Audit Trail Reviewer**: Analyzes audit trail records against change management policies
4. **Transaction Reviewer**: Analyzes transactions for policy violations
5. **Audit Report Writer**: Compiles findings into a comprehensive audit report

### Tools

The system includes specialized tools for data analysis:

1. **Access Review Tool** (`access_review.py`): Compares access reports against access matrices
2. **Transaction Approval Review Tool** (`transaction_approval_review.py`): Analyzes transaction approvals based on authorization limits
3. **Change Management Verification Tool** (`change_management_verification.py`): Verifies audit trail records against change tickets
4. **Transaction Policy Review Tool** (`transaction_policy_review.py`): Reviews transactions against policy documentation

### Tasks

Tasks are defined in `tasks.yaml` and include:

1. **Review Logical Access**: Compare system access levels against authorized access matrix
2. **Review Transaction Limits**: Analyze transaction approvals against authorized limits
3. **Review Audit Trail**: Verify change management compliance
4. **Review Transaction Policy**: Verify transaction-level compliance with policies
5. **Compile Audit Report**: Combine all findings into a comprehensive report

## Configuration

The system uses YAML-based configuration files:

- **`agents.yaml`**: Defines agent roles, goals, and backstories
- **`tasks.yaml`**: Defines task descriptions, priorities, and output structures

## Data Structure

LARC expects the following data files in the `data` directory:

- **Access Control Data**:
  - `access_report.csv`: Current system access levels
  - `access_matrix.csv`: Authorized access matrix

- **Transaction Data**:
  - `transaction_logs.csv`: Transaction approval records
  - `limit_authorization.csv`: User approval limits
  - `transaction_records.csv`: Detailed transaction information
  - `transaction_policy.pdf`: Transaction policy documentation

- **Change Management Data**:
  - `audit_trail.csv`: System modification records
  - `change_tickets.csv`: Approved change requests

## LLM Integration

LARC uses multiple language models:
- Primary model: DeepSeek (configured via environment variables)
- Fallback models: Llama 3 variants, Mistral, and Mixtral (via Ollama)

The system includes robust error handling and retry mechanisms for API rate limits and errors through the `EnhancedLLM` and `DeepseekAPIWrapper` classes.

## Execution Flow

1. Initialize LARC with API credentials
2. Create specialized agent instances
3. Define audit tasks with specific tools and output requirements
4. Execute tasks sequentially
5. Generate findings in markdown format in the `findings` directory
6. Compile individual findings into a comprehensive audit report

## Setup and Usage

### Prerequisites

- Python 3.8+
- Required packages (install via `pip install -r requirements.txt`)
- Ollama (for local models)
- DeepSeek API access

### Environment Configuration

Create a `.env` file with the following variables:

```
DEEPSEEK_API_KEY=your_api_key
DEEPSEEK_API_BASE=your_api_base_url
DEEPSEEK_MODEL=your_preferred_model
```

### Running the Audit

```bash
python main.py
```

The system will:
1. Initialize agents with their respective roles
2. Execute audit tasks in sequence
3. Save individual findings to the `findings` directory
4. Generate a final `DraftAuditReport.md` file

## Output

The audit results in several output files:

- **Individual Findings**: Stored in the `findings` directory
  - `LogicalAccessObservation.md`
  - `TransactionsLimitsObservation.md`
  - `AuditTrailObservation.md`
  - `TransactionsComplianceObservation.md`

- **Final Report**: `DraftAuditReport.md` with structured sections:
  - Executive Summary
  - Detailed Findings (organized by audit area)
  - Risk Assessments
  - Management Actions

## Extending the System

To extend LARC:

1. **Add New Agents**: Define new agent roles in `agents.yaml`
2. **Add New Tools**: Create Python tools in the `tools` directory and integrate them into the tasks
3. **Add New Tasks**: Define new tasks in `tasks.yaml` and link them to agents
4. **Modify Output Structure**: Adjust the report structure in `tasks.yaml`

## Logging

The system includes comprehensive logging:
- Console output for immediate feedback
- Log files for detailed tracking:
  - `api_calls.log`: API interaction logs
  - `larc.log`: System operation logs

## Notes

- The system includes exponential backoff retry mechanisms for API rate limits
- Error handling is implemented for file processing and API calls
- Task outputs are structured according to audit best practices
