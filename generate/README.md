# Generating a new client 

Every time


1. Create a new branch `git checkout -b new_branch_name`
2. Install openapi-generator

```npm install @openapitools/openapi-generator-cli -g```

2. Place the latest swagger.json in `./generate/swagger.json`

3. Remove the current files except the `token.py` file

```
mv data_bridges_client/token.py .
rm -rf test docs data_bridges_client
mkdir data_bridges_client
mv ./token.py data_bridges_client/
```

5. Generate the client by running this command from the root of the repository.
```
openapi-generator-cli generate -g python -i generate/swagger.json -o . --package-name data_bridges_client --git-user-id WFP-VAM --git-repo-id DataBridgesAPI
```
4. Manually revert changes to `setup.py` and `README.md`. These relate to additional functionality we developed to handle the WFP token refresh workflow.
5. Commit, push and open a PR into `dev` for review.