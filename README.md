# QTM 350 - Data Science Computing

## Course Description

Welcome to [QTM 350](https://github.com/danilofreire/qtm350)! This course introduces key tools in modern data science, focusing on three essential aspects: reliability, reproducibility, and robustness. We will cover command line interfaces and [vim](https://www.vim.org/), version control with [Git](https://git-scm.com/) and [GitHub](https://github.com/), and literate programming using [Quarto](https://quarto.org/) and [Jupyter Notebooks](https://jupyter.org/). You will also learn about data storage and manipulation with [SQL](https://www.w3schools.com/sql/) and [Pandas](https://pandas.pydata.org/), data visualisation using [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) and [plotnine](https://plotnine.readthedocs.io/), and parallel computing with [Dask](https://www.dask.org/). We will explore artificial intelligence-assisted programming with [GitHub Copilot](https://github.com/features/copilot) and finish with [Docker](https://www.docker.com/) and containerisation. Throughout the course, you will learn how to use these tools to improve your data science workflow and create more reliable, reproducible, and robust analyses.

## Contact Information

- [Danilo Freire](https://danilofreire.github.io/)
  - Email: [`danilofreire@gmail.com`](mailto:danilofreire@gmail.com)
  - Office hours: [By appointment at any time (online or in person)](https://calendly.com/danilofreire/office-hours).

## Learning Outcomes

By the end of this course, students will be able to:

- Use data science tools for project collaboration and version control
- Apply advanced techniques for data storage, manipulation, and querying
- Create clear data visualisations and write well-documented code
- Use AI tools to help with programming tasks
- Understand the basics of containerisation and parallel computing

## Repository Structure

This repository is organised as follows:

- [`assignments/`](https://github.com/danilofreire/qtm350/tree/main/assigments): Contains all course assignments
- [`lectures/`](https://github.com/danilofreire/qtm350/tree/main/lectures): Includes lecture materials and code
- [`quizzes/`](https://github.com/danilofreire/qtm350/tree/main/quizzes): Quiz materials
- [`tutorials/`](https://github.com/danilofreire/qtm350/tree/main/tutorials): Step-by-step guides for the tools used in the course
- [`README.md`](https://github.com/danilofreire/qtm350/blob/main/README.md): This file, providing an overview of the course and repository
- [`syllabus.pdf`](https://github.com/danilofreire/qtm350/blob/main/syllabus.pdf): Course syllabus in PDF format

The course website is available at <https://danilofreire.github.io/qtm350/>.

## Course Content

### Course Requirements

- Prerequisites: Some knowledge of programming is recommended, and familiarity with basic data manipulation and visualisation techniques is helpful. However, no prior experience with the tools covered in the course is required.
- Software: [Anaconda distribution of Python 3.x](https://www.anaconda.com/), [VS Code](https://code.visualstudio.com/), [PostgreSQL](https://www.postgresql.org/), [GitHub Desktop](https://github.com/apps/desktop), [Git](https://git-scm.com/), [Docker](https://www.docker.com/), [Quarto](https://quarto.org/), [Dask](https://dask.org/), [GitHub Co-Pilot](https://copilot.github.com/).

Please feel free to reach out if you have any questions about the course content or your readiness to take the class.

### Lectures (Tentative Schedule)

The course covers the following topics, with corresponding lecture
materials available in the [lectures
folder](https://github.com/danilofreire/qtm350/tree/main/lectures):

- Wednesday, August 28: [Lecture 01: Welcome to QTM 350 - Introduction](https://danilofreire.github.io/qtm350/lectures/lecture-01/01-introduction.html). [Course Tutorials: How to Install Anaconda, Jupyter, PostgreSQL, VSCode, and Open a Free Educational Account on GitHub](https://danilofreire.github.io/qtm350/tutorials/tutorials.html).

- Monday, September 02: Labour Day (no class)

- Wednesday, September 04: [Lecture 02: GitHub Review](https://danilofreire.github.io/qtm350/lectures/lecture-02/02-github-review.html) and [Introduction to Jupyter Notebooks](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-02/02-jupyter.ipynb)
  - **Assignment 01:** [Problem Set 01](https://github.com/danilofreire/qtm350/blob/main/assignments/01-assignment.ipynb)

- Monday, September 09: [Lecture 03: Variables and Lists](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-03/03-variables-lists.ipynb)

- Wednesday, September 11: [Lecture 04: Mathematical Operations, Arrays, and Random Numbers](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-04/04-maths-arrays-random.ipynb)
  - **Assignment 01 due (5%)**
  - **Assignment 02:** [Problem Set 02](https://github.com/danilofreire/qtm350/blob/main/assignments/02-assignment.ipynb)

- Monday, September 16: [Lecture 05: Boolean Variables and If/Else Statements](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-05/05-boolean-if-else.ipynb)

- Wednesday, September 18: [Lecture 06: While Loops and For Loops](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-06/06-while-for.ipynb)
  - **Assignment 02 due (5%)**
  - **Assignment 03:** [Problem Set 03](https://github.com/danilofreire/qtm350/blob/main/assignments/03-assignment.ipynb)

- Monday, September 23: [Lecture 07: Applications 1: Simulation Studies](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-07/07-applications-simulation.ipynb)

- Wednesday, September 25: [Lecture 08: Functions and Arguments](https://danilofreire.github.io/qtm350/lectures/lecture-08/08-functions-arguments.ipynb)
  - **Assignment 03 due (5%)**
  - **Assignment 04:** [Problem Set 04](https://github.com/danilofreire/qtm350/blob/main/assignments/04-assignment.ipynb)

- Monday, September 30: [Lecture 09: Global and Local Variables](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-09/09-global-local.ipynb)

- Wednesday, October 02: [Lecture 10: Quiz 01: Application 02 - Operations over Multiple Datasets (6%)](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-10/10-operations-multiple-datasets.ipynb)
  - **Assignment 05:** [Problem Set 05](https://github.com/danilofreire/qtm350/blob/main/assignments/05-assignment.ipynb)

- Friday, October 04: **Assignment 04 due (5%)**

- Monday, October 07: [Lecture 11: Subsetting Data](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-11/11-subsetting-data.ipynb)

- Wednesday, October 09: [Lecture 12: Application 03: Linear Models](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-12/12-linear-models.ipynb)
  - **Assignment 05 due (5%)**
  - **Assignment 06:** [Problem Set 06](https://github.com/danilofreire/qtm350/blob/main/assignments/06-assignment.ipynb)

- Monday, October 14: Fall Break (no class)

- Wednesday, October 16: [Lecture 13: Creating and Replacing Variables](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-13/13-creating-replacing-variables.ipynb)
  - **Assignment 06 due (5%)**
  - **Assignment 07:** [Problem Set 07](https://github.com/danilofreire/qtm350/blob/main/assignments/07-assignment.ipynb)

- Monday, October 21: [Lecture 14: Quiz 2: Application 4: Random Assignment (6%)](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-14/14-random-assignment.ipynb)

- Wednesday, October 23: [Lecture 15: Aggregating Data](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-15/15-aggregating-data.ipynb)
  - **Assignment 07 due (5%)**
  - **Assignment 08:** [Problem Set 08](https://github.com/danilofreire/qtm350/blob/main/assignments/08-assignment.ipynb)

- Monday, October 28: [Lecture 16: Merging Data](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-16/16-merging-data.ipynb)

- Wednesday, October 30: [Lecture 17: Introduction to SQL](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-17/17-introduction-sql.ipynb)
  - **Assignment 08 due (5%)**
  - **Assignment 09:** [Problem Set 09](https://github.com/danilofreire/qtm350/blob/main/assignments/09-assignment.ipynb)
  - **Instructions for the Final Project:** [Final Project](https://github.com/danilofreire/qtm350/blob/main/final-project)

- Monday, November 04: [Lecture 18: Quiz 3: Application 5: Practicing Chaining (6%)](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-18/18-chaining.ipynb)

- Wednesday, November 06: [Lecture 19: Import SQL Data into Python](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-19/19-sql-python.ipynb)
  - **Assignment 09 due (5%)**
  - **Assignment 10:** [Problem Set 10](https://github.com/danilofreire/qtm350/blob/main/assignments/10-assignment.ipynb)

- Monday, November 11: [Lecture 20: Merging Tables in SQL](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-20/20-sql-merging.ipynb)

- Wednesday, November 13: [Lecture 21: Time Series Analysis](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-21/21-time-series.ipynb)
  - **Assignment 10 due (5%)**

- Monday, November 18: [Lecture 22: Quiz 4: Application 6: Practice SQL Queries (6%)](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-22/22-sql-queries.ipynb)

- Wednesday, November 20: [Lecture 23: Pivot Tables](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-23/23-pivot-tables.ipynb)

- Monday, November 25: [Lecture 24: Quiz 5: Application 8: Time Data, Panel Data, and Plots (6%)](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-24/24-time-panel-plots.ipynb)

- Wednesday, November 27: Thanksgiving Break (no class)

- Monday, December 02: [Lecture 25: Manipulating Text Data](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-25/25-text-data.ipynb)

- Wednesday, December 04: [Lecture 26: Advanced Plots](https://github.com/danilofreire/qtm350/blob/main/lectures/lecture-26/26-advanced-plots.ipynb)

- Monday, December 09: **Final Project due (20%)**

Each lecture folder contains an HTML file or a Jupyter notebook (`.ipynb`) with code examples and explanations, along with any additional resources or datasets used in the lecture.

### Assignments and Quizzes

Throughout the course, students will complete various assignments and quizzes
to reinforce their learning. These will be posted in the respective
[`assignments/`](https://github.com/danilofreire/qtm350/tree/main/assigments)
and [`quizzes/`](https://github.com/danilofreire/qtm350/tree/main/quizzes)
folders as the course progresses. We will also announce these in class and on
Canvas. Please refer to the syllabus for due dates and submission guidelines.

### Tutorials

The [`tutorials/`](https://github.com/danilofreire/qtm350/tree/main/tutorials)
folder contains step-by-step guides for various tools and techniques used in
the course. These include:

- [VSCode and Anaconda Tutorial](https://github.com/danilofreire/qtm350/blob/main/tutorials/01-vscode-anaconda-tutorial.pdf)
- [Jupyter Notebook and Markdown Tutorial](https://github.com/danilofreire/qtm350/blob/main/tutorials/02-jupyter-markdown-tutorial.pdf)
- [GitHub Tutorial](https://github.com/danilofreire/qtm350/blob/main/tutorials/03-github-tutorial.pdf)
- [PostgreSQL Tutorial](https://github.com/danilofreire/qtm350/blob/main/tutorials/04-postgresql-tutorial.pdf)

## Grading

- Assignments: 50%
- Class Quizzes: 30%
- Final Project: 20%

## Course Policies and Expectations

For detailed information on course policies, grading criteria, attendance
requirements, and academic integrity guidelines, please refer to the
[`syllabus.pdf`](https://github.com/danilofreire/qtm350/blob/main/syllabus.pdf)
file in the repository root.

## Suggested Resources

To supplement your learning, you may find the following resources helpful:

### Books

- [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney
- [Elements of Data Science](https://allendowney.github.io/ElementsOfDataScience/README.html) by Allen Downey
- [SQL for Data Scientists](https://sqlfordatascientists.com/) by Renee M. P. Teate
- [Data Science on the Command Line](https://www.datascienceatthecommandline.com/) by Jeroen Janssens
- [Docker for Data Science](https://www.oreilly.com/library/view/docker-for-data/9781484230121/) by Joshua Cook
- [Pro Git](https://git-scm.com/book/en/v2) by Scott Chacon and Ben Straub
- [Free programming books](https://github.com/EbookFoundation/free-programming-books)

### Online Courses

- [Coursera: Python for Everybody Specialisation](https://www.coursera.org/specializations/python)
- [edX: Python Basics for Data Science](https://www.edx.org/learn/python/ibm-python-basics-for-data-science)
- [Codecademy: Learn Python](https://www.codecademy.com/learn/learn-python-3)
- [DataCamp: Introduction to SQL](https://www.datacamp.com/courses/intro-to-sql-for-data-science)
- [Coursera: SQL for Data Science](https://www.coursera.org/learn/sql-for-data-science)
- [Coursera: Introduction to Git and GitHub](https://www.classcentral.com/course/introduction-git-github-18060)
- [Microsoft Learn: GitHub Copilot Fundamentals](https://learn.microsoft.com/en-us/training/paths/copilot/)

### Documentation

- [Official Python Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Documentation](https://docs.github.com/en)
- [Dask Documentation](https://docs.dask.org/en/latest/)
- [GitHub Co-Pilot Documentation](https://copilot.github.com/)
- [Docker Documentation](https://docs.docker.com/)

The syllabus also includes a list of additional readings and resources for each week.

## Academic Integrity

Students are expected to adhere to the [Emory University Honour
Code](https://catalog.college.emory.edu/policies/honor-code.html). Any
suspected violations will be reported to the Honour Council.

## Accessibility

If you require any accommodations for this course, please contact the
[Department of Accessibility Services](https://accessibility.emory.edu/) and
the instructor as soon as possible.

## Getting Help

If you encounter any issues with the course materials or have questions about the content, please:

1. Check the [course syllabus](https://github.com/danilofreire/qtm350/blob/main/syllabus.pdf) and this README for relevant information
2. Review the [lecture materials](https://github.com/danilofreire/qtm350/tree/main/lectures) and [tutorials](https://github.com/danilofreire/qtm350/tree/main/tutorials) in the repository
3. Consult with your classmates or post in the [course discussion forum](https://github.com/danilofreire/qtm350/discussions)
4. Attend office hours or schedule an appointment with the instructor

## Contributing to the Repository

While this repository is primarily maintained by the course instructor,
everyone is welcome to contribute. Please feel free to suggest improvements or
report issues by [opening a GitHub
issue](https://github.com/danilofreire/qtm350/issues), [submitting a pull
request](https://github.com/danilofreire/qtm350/pulls), [creating a discussion
post](https://github.com/danilofreire/qtm350/discussions), or [contacting the
instructor directly](mailto:danilo.freire@emory.edu).

## License

This repository is licensed under the [MIT
License](https://github.com/danilofreire/qtm350/blob/main/LICENSE.qmd). You are
free to use, modify, and distribute the materials as needed, with appropriate
attribution to the original source.

-----

We look forward to an engaging and productive semester! Good luck, and happy coding! :smiley:
