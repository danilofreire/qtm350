# Workshop presentations

Please publish your presentation materials in a repo that you create in our workshop organization at https://github.com/intro-to-data-science-23-workshop. There's a naming convention for the repos, which should indicate the workshop number (see below), your name (one group member only), and a very brief description, all lowercase and separated by dashes. E.g.: `01-topic-lastname1-lastname2/`. For more information about your task, check out the document `workshop-guidelines.pdf` in this repository.

## R Markdown

Please try to make your presentations using [R Markdown](https://rmarkdown.rstudio.com/). You can use any one of the multiple slide deck options. (For what it's worth, I use the [xaringan package with a modified metropolis theme](https://github.com/yihui/xaringan/wiki/Themes) for my lecture slides). Or you can output as a [GitHub document](https://rmarkdown.rstudio.com/github_document_format.html) or [HTML document](https://bookdown.org/yihui/rmarkdown/html-document.html). If you choose the latter, I would request that you please include `keep_md: true` in your YAML, so that it is readable directly on GitHub.

## Recording

There are multiple ways to record your computer screen and voice for the presentation videos. You can [record MS PowerPoint with audio and video](https://www.youtube.com/watch?v=2m60HT3OMOI), [record a presentation on Zoom](https://www.youtube.com/watch?v=P6cTbnUPwfY), [record a presentation via MS Teams](https://www.youtube.com/watch?v=ymnTVklGtAY), or use [open source software OBS Studio](https://www.youtube.com/watch?v=jKgM18lOsr4). Just make sure the `format is mp4` and the entire thing is `no longer than 15 minutes`! If you need to convert between video formats, I recommend the open source video transcoder [HandBrake](https://handbrake.fr/). For minimal cutting you might want to use lightweight [LosslessCut](https://github.com/mifi/lossless-cut).


## Topics

Topics will be randomly allocated to groups of 2 students. Both of you should contribute to both the presentation and the practice session, but you can divide main responsibilities.

| Workshop | Focus | Topic | Resources | 
|---------|-------|-----------|-----------|
| 01 | Wrangling | Cleaning and wrangling data with janitor and forcats | [a](https://sfirke.github.io/janitor/index.html), [b](https://forcats.tidyverse.org/) |
| 02 | Wrangling | Wrangling data at scale with data.table | [a](https://rdatatable.gitlab.io/data.table/), [b](https://github.com/tidyverse/dtplyr) |
| 03 | Wrangling | Dates and times with lubridate | [a](https://lubridate.tidyverse.org/), [b](https://r4ds.had.co.nz/dates-and-times.html) |
| 04 | Wrangling | Advanced string processing with stringi and stringr | [a](https://stringr.tidyverse.org/), [b](https://stringi.gagolewski.com/) |
| 05 | Analysis | Temporal data with tsibble and fable | [a](https://tsibble.tidyverts.org/), [b](https://fable.tidyverts.org/) |
| 06 | Analysis | Text analysis with quanteda | [a](https://quanteda.io/), [b](https://joss.theoj.org/papers/10.21105/joss.00774) |
| 07 | Analysis | Geospatial analysis with sf | [a](https://r-spatial.github.io/sf/index.html), [b](https://lost-stats.github.io/Geo-Spatial/geocoding.html) |
| 08 | Visualization | Presentation-ready tables with gt and gtExtra | [a](https://gt.rstudio.com/), [b](https://jthomasmock.github.io/gtExtras/) |
| 09 | Visualization | Interactive maps with leaflet | [a](https://github.com/ropensci/plotly), [b](https://leafletjs.com/reference-1.7.1.html) |
| 10 | Visualization | Interactive graphics with plotly | [a](https://github.com/plotly/plotly.R), [b](https://plotly.com/r/) |
| 11 | Workflow | Ensuring reproducibility with renv | [a](https://rstudio.github.io/renv/), [b](https://rstudio.github.io/renv/articles/renv.html) |
| 12 | Workflow | Tidy modeling with tidymodels | [a](https://www.tidymodels.org/), [b](https://www.tmwr.org/) |


