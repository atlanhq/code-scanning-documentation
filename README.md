# code-scanning-documentation

## What is Github Code Scanning?
It  is a feature that developers use to analyze the code in a GitHub repository to find security vulnerabilities and coding errors.
Code Scanning will help developers to find, triage, and prioritize fixes for existing problems in the code. 
Code scanning also prevents developers from introducing new problems. Developers can schedule scans for specific days and times, or trigger scans 
when a specific event occurs in the repository, such as a push.

If code scanning finds a potential vulnerability or error in the code, GitHub displays an alert in the repository.
After developer fix the code that triggered the alert, GitHub closes the alert. 

## About CodeQL Analysis:
CodeQL is the code analysis engine developed by GitHub to automate security checks.
Developer can analyze the code using CodeQL and display the results as code scanning alerts.

## Configuring CodeQL Manifest:
Developers can look after the [manifest available](https://github.com/atlanhq/code-scanning-documentation/blob/main/codeql.yml).
All the details are been mentioned in the comment section.
For understanding it more better, you can refer the following repository [codeql-action from github](https://github.com/github/codeql-action/) for getting
a short walkthrough.

Also, to get information in more detail about configuring code scanning with CodeQL, 
you can refer the official documentation from [github](https://docs.github.com/en/enterprise-server@3.3/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning).

To check how to configure the CodeQL Workflow for the compiled languages, check the following [link](https://docs.github.com/en/enterprise-server@3.3/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-the-codeql-workflow-for-compiled-languages).

To check how to configure the CodeQL Workflow for the containers and run the CodeQL scanning in the container, do check the following [link](https://docs.github.com/en/enterprise-server@3.3/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/running-codeql-code-scanning-in-a-container).

## Troubleshooting

Read about [troubleshooting code scanning](https://help.github.com/en/github/finding-security-vulnerabilities-and-errors-in-your-code/troubleshooting-code-scanning).
