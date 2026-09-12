# Run Instructions

This guide explains how to generate the Serverless Computing presentation on Windows using PowerShell.

## Steps

1. Open PowerShell and navigate to your project directory:
   ```powershell
   cd "C:\Users\johnl\OneDrive\Desktop\EMERGING REPORT"
   ```

2. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```

3. Activate the virtual environment:
   ```powershell
   .venv\Scripts\activate
   ```

4. Install the required libraries:
   ```powershell
   pip install -r requirements.txt
   ```

5. Run the Python script to generate the presentation:
   ```powershell
   python create_serverless_presentation.py
   ```

## Output

After running the script, the presentation will be saved in the same directory as:
`SERVERLESS_COMPUTING_REPORT.pptx`

You can then open this file using Microsoft PowerPoint.
