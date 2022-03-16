![microsoft logo](./images/ms_logo.jpg)

# Microsoft Studio Movies Analysis

**Author**: [Jin-hoon Chung](mailto:ddjh204@gmail.com)

## Overview

This project shows analysis on movie markets to help Microsoft start building a new movie studio. Several key aspects of popular movies are selected for the analysis.

## Business Problem

As Microsoft has no background in filming a movie, concrete information is needed for a guide on creating a new movie studio. Microsoft is interested in what is needed to be successful. It would be a good idea to investigate the aspects of the movies that are successful and fairly recent.

## Data

Data is collected from well-known websites for movie databases. For the analysis, the selected aspects of the movie are [gross & budget](https://www.the-numbers.com/), [genre](https://www.themoviedb.org/), and [runtime](https://www.imdb.com/). Profit is calculated by subtracting budget from gross, and then the film with at least $10 million profit is selected. However, the profit amounts can easily be modified for different results. The movies are chosen again with release years on and after 2000, and this range can be modified as well.

![profit](./images/profit_dist.png)

## Methods

The analysis of this project shows several visualizations. The visualizations describe how much budget can be estimated, what genres are popular, and how long the movies are.

## Results

The majority of movies had a budget below $50 million.

![movie budget](./images/budget_dist.png)

The most popular genres are drama, comedy, action, thriller, and adventure.

![genre](./images/genre_popularity.png)

A typical length of movies is between 90 and 120 minutes.

![runtime](./images/movie_runtime_dist.png)

## Conclusions

There are three recommendations to consider to build a new movie studio.

- **The estimated budget to film a movie is below $50 million.** There are movies that cost more than $50 million, but the analysis shows Microsoft does not have to spend a similar amount. 
- **The recommended genres for a new movie are drama, comedy, action, thriller, and adventure.** Most movies included multiple genres. If a new movie can include recommended genres as much as possible, this would help lead to a successful business.
- **The runtime for a new movie is recommended to be between 90 to 120 minutes.**

### Next Steps

Further analysis could help gain more ideas on creating a new movie.

- **Run the same analysis again after genres are decided.** Running the same analysis for selected genres would help gain a better result because selecting genres narrows down to a more specific data sample.
- **More research on the relationship between profit and budget.** The analysis shows a typical budget for the overall profit. A more sophisticated visualization, such as a scatter plot, on a smaller sample, is advised.
- **Find more aspects of movies such as casting size and age rating** Movies can be analyzed in more ways by including more aspects.

## For More Information

See the full analysis in the [Jupyter Notebook](./MS_Studio_Movie_Analysis.ipynb) or review this [presentation](./Microsoft_Studio_Movie_Analysis.pdf).

For additional info, contact Jin-hoon Chung at [ddjh204@gmail.com](mailto:ddjh204@gmail.com)

![logo](./images/ms_ms.jpg)

## Repository Structure

```
├── code
│   ├── __init__.py
│   ├── data_preparation.py
│   ├── visualizations.py
│   └── eda_notebook.ipynb
├── data
├── images
├── __init__.py
├── README.md
├── Microsoft Studio Movie Analysis.pdf
└── MS Studio Movie Analysis.ipynb
```