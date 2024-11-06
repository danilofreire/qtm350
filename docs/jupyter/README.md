# Building Jupyter Lite Pages with Pyodide

I have created a simple JupyterLite page using Pyodide for this website. The
idea is that students can run Python code in the browser without needing to
install Python on their own machines. The page is available at
<https://danilofreire.github.io/qtm151/jupyter>. The code for the page is
available in the `jupyter` folder of this repository.

The main issue I had was that I use the `docs/` folder to build the Quarto
website, and every time I rebuild the whole website with `quarto render`, the
`jupyter` folder is deleted. But the commands below solve the issue by
rebuilding the JupyterLite page after the Quarto website is built:

```bash
mkdir -p docs/jupyter 
cp -r jupyter/* docs/jupyter
cd docs/jupyter
pip install -r requirements.txt
jupyter lite build
mv _output/* ./
git add ../../docs/jupyter -f
git commit -m "update JupyterLite page"
git push
```

JupyterLite should be ready to be published on GitHub Pages. The
following commands will push the changes to the repository:

```bash
git add ../../docs/jupyter -f
git commit -m "update JupyterLite page"
git push
```

If you have any questions, please let me know.
