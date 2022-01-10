# Vader Sentiment as Lambda
We need `VaderSentiment` package to make this work. We will add the package using the following command:

```
$ pip3 install --target ./packages vaderSentiment
```

# Create the zip package
Use the following commands to create the deploy package:

```
$ cd packagesf 
$ zip -r ../vader-lambda-deployment.zip .
$ cd ..
$ zip -g vader-lambda-deployment.zip lambda_function.py
```

# Upload the zip package to AWS
Before uploading the package we have to create a Lambda function, `vadersentiment` using AWS console. Run the following command to puish the package to AWS. Make sure you configured aws cli.

```
$ aws lambda update-function-code --function-name vadersentiment --zip-file fileb://vader-lambda-deployment.zip
```

# Adding an API trigger
Add a REST API trigger with default settings and make the API open to public from AWS Lambda console. An API endpoint will be created with method ANY. The current code is written for GET (queryparameters). Use the following `curl` command to test the API:

```
$ curl -v -X GET 'https://<API code>.execute-api.us-east-2.amazonaws.com/default/vadersentiment?sentence=very%20beautiful%20day'
```