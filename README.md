# Analyzing Gender Bias in Narrative Tropes

## Abstract

Popular media reflects and reinforces societal biases through the use of tropes, which are narrative elements, such as archetypal characters and plot arcs, that occur frequently across media. In this paper, we specifically investigate gender bias within a large collection of tropes. To enable our study, we crawl [tvtropes.org](http://tvtropes.org), an online user-created repository that contains 30K tropes associated with 1.9M examples of their occurrences across film, television, and literature. We automatically score the “genderedness” of each trope in our TVTROPES dataset, which enables an analysis of (1) highly-gendered topics within tropes, (2) the relationship between gender bias and popular reception, and (3) how the gender of a work’s creator correlates with the types of tropes that they use.

## Paper
Here is the [official page for our paper.](https://www.aclweb.org/anthology/2020.nlpcss-1.23/)

## Data
We crawled TVTropes.org to collect a large-scale dataset of 30K tropes and 1.9M examples of their occurrences across 40K works of film, television, and literature. We then connected our data to meta-data from IMDb and Goodreads to augment our dataset and enable analysis of gender bias.

Our data can be found [here.](https://drive.google.com/file/d/1ruAIRtd5ZsrR6OQziX9mGurBp1JsNxXG/view?usp=sharing) It contains the following:
- tropes contains trope names, IDs, and descriptions
- lit_tropes, film_tropes, and tv_tropes contain the trope names, titles, and examples across each form of media
- lit_goodreads_match, film_imdb_match, tv_imdb_match contain the tropes, examples, and titles linked to the metadata

## Code
Each script contains the code for each different analysis conducted in the paper. Please ensure you have the requirements listed in requirements.txt installed to run the scripts. 

## Citation

If you use this dataset or code for your research, please cite:

`@inproceedings{gala-etal-2020-analyzing,
    title = "Analyzing Gender Bias within Narrative Tropes",
    author = "Gala, Dhruvil  and
      Khursheed, Mohammad Omar  and
      Lerner, Hannah  and
      O{'}Connor, Brendan  and
      Iyyer, Mohit",
    booktitle = "Proceedings of the Fourth Workshop on Natural Language Processing and Computational Social Science",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.nlpcss-1.23",
    doi = "10.18653/v1/2020.nlpcss-1.23",
    pages = "212--217",
    abstract = "Popular media reflects and reinforces societal biases through the use of tropes, which are narrative elements, such as archetypal characters and plot arcs, that occur frequently across media. In this paper, we specifically investigate gender bias within a large collection of tropes. To enable our study, we crawl tvtropes.org, an online user-created repository that contains 30K tropes associated with 1.9M examples of their occurrences across film, television, and literature. We automatically score the {``}genderedness{''} of each trope in our TVTROPES dataset, which enables an analysis of (1) highly-gendered topics within tropes, (2) the relationship between gender bias and popular reception, and (3) how the gender of a work{'}s creator correlates with the types of tropes that they use.",
}`
