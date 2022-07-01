# Create a clean gh-pages branch
git checkout --orphan gh-pages
git rm -rf .
git commit -m "Initial commit" --allow-empty
git push --set-upstream origin gh-pages
# GHA Demo
```
pip install -r requirements.txt
```

### Docker

```
docker run -it --rm --entrypoint /bin/sh 
```

## Run the demo locally
Execute the following command at the top level of the repository
```
python3 src/ghademo/main.py
```