# Generating a new client 

1. Install openapi-generator

```$npm install @openapitools/openapi-generator-cli -g```

2. Place the latest swagger.json in `./generate/swagger.json`

3. Generate the client by running this command from the root of the repository
```
openapi-generator-cli version-manager set 5.4.0
openapi-generator-cli generate -g python -i generate/swagger.json -o . --package-name data_bridges_client --git-user-id WFP-VAM --git-repo-id DataBridgesAPI
```