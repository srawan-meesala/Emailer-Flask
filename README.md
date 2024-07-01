
## Deployed URL
    https://ny5srds0mi.execute-api.us-east-1.amazonaws.com/dev/

## Endpoints

- `/` - Root endpoint (no functionality)
- `/send-email` - Send email to the receiver email given in the form data. The fields required are 
    - receiver_email
    - subject
    - body

Deployed using serverless framework and python3.8 runtime.

Refer to serverless aws documentation for more info on deployment.