# GHA Demo
## Preparation
### Create a clean gh-pages branch
This branch will be used to store releases of you Helm chart.
```
git checkout --orphan gh-pages
git rm -rf .
git commit -m "Initial commit" --allow-empty
git push --set-upstream origin gh-pages
```
### Python dependencies
```
pip3 install -r requirements.txt
```
## Run the demo locally
Execute the following command at the top level of the repository. You shoudl see some log output. While the program is running you should be abel to see some output in the browser via 'http://localhost:9000'
```
python3 src/ghademo/main.py
```
## Git operations
Some commands typically used in the development workflow.

The workflow assume you are doing changes in a development branch with the following naming convention: <name>-<digits>, e.g. test-1234.

This comes from the best practice to name development branches according to Jira issues. 

### During development
If you do not follow this convention, you will wonder that no containers are build. But in case your branch has the right name the conatiner will be build and pushed to GHCR (GitHub Container Registry).
### Releasing the container
```
git tag -a "My Release" -m "This is a total rebuild of everything"
git push --tags
```
This will build the container too, but pushes the new image to Docker Hub.
You will need to set two secrets in this repository:
```
DOCKER_USERNAME
DOCKER_TOKEN
```
These secrets are used to login into Docker Hub
### Releasing the Helm chart
* Develop your changes
* Set the appropriate versions in the Chart.yml file
* Create a Pull Request to the main branch and review it
* Merge the reviewed changes
* The will build teh new Helm release and store it in the gh-pages branch


