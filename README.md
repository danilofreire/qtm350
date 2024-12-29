# QTM 350 - Data Science Computing

This branch hosts the website for the course [QTM 350 - Data Science
Computing](http://danilofreire.github.io/qtm350) at [Emory
University](http://www.emory.edu). The course provides an introduction to
Python and SQL for data management and analysis. Please refer to the `main`
branch of [this repository](https://github.com/danilofreire/qtm350) for the
course materials.

## Building the website

I used [Quarto](https://quarto.org) to build the website, and the process was
quite straightforward. To keep the website organised, I created a `gh-pages`
branch and removed all unnecessary files. Then, I converted some of the course
materials, such as the syllabus, to `.qmd` format (Quarto Markdown) and added
them to their respective folders. The tutorials were already in `.qmd` format,
so I simply moved them to the `tutorials` folder and added a `tutorials.qmd`
file to list them. Similarly, the lectures are described in the `lectures.qmd`
file.

I decided to keep the Jupyter Notebooks, which will be used in the lectures,
only in the `main` branch. This way, I encourage students to download the
repository and follow the lectures using their local Jupyter environment.

The `_quarto.yml` file contains the configuration for the website, including
the theme, the title, and the navigation bar. The website files are in the
`docs/` folder, as it is one of the easiest ways to host a website on GitHub. I
also added a `.nojekyll` file to the root of the repository to prevent GitHub
from processing the website as a Jekyll project.

I then built the website with `quarto render docs/` and pushed the changes to the
`gh-pages` branch with `git push origin gh-pages`.

## Building JupyterLite pages with Pyodide

I have created a simple JupyterLite page using Pyodide for this website. The
idea is that students can run Python code in the browser without needing to
install Python on their own machines. The page is available at
<https://danilofreire.github.io/qtm30/jupyter>. The code for the page is
available below:

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

For further information on how to build a website with Quarto, please refer to
<https://quarto.org/docs/websites/>.

If you have any questions, please feel free to [open an
issue](https://github.com/danilofreire/qtm350/issues) or [create a pull
request](https://github.com/danilofreire/qtm350/pulls).

## License

The content of this repository is released under the [MIT
License](LICENSE.qmd). You are free to use, modify or distribute it as long as
you provide the attribution to the original author.
