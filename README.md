# Unemployment, Income, and Population of California Counties
The Flask app is available for remote viewing at [https://california-demographics.herokuapp.com/](https://california-demographics.herokuapp.com/).

## Project Overview
We are researching the demographics for California’s counties including the
population size, average median income and unemployment rate. Our sources are all government
sites including <a href="https://www.labormarketinfo.edd.ca.gov">The Labor Market Information Division of
California</a>, <a href="https://www.hcd.ca.gov">The California Department of Housing and Community
Development</a>, and <a href="https://dof.ca.gov">The California Department of Finance</a>. The dates range from
2020 to 2021.

We downloaded files from each of the sites and converted the data to excel format. We created a web page for each
data set that showcases the data with a geomap, a bar graph and a table. We have a seperate page for analysis that
compares the data with a bubble graph, and two scatter plots.

## Analysis
Most counties have a population of 1 000 000 or lower. Los Angeles is clear outlier with a population of almost 10 000 000. Lot of counties have a median income around 70 000 or less. There is no strong link between population and median income or between population and unemployment rate. Some counties, like San Franciso, have a high median income and average population. Some others, like Sacramento, have a lower median income for an average population. It may seems like the employment rate is lower for counties with high income but this tendancy is not clear since a lot of counties are grouped in the same area of the graph (1 000 000 population/70 000 median income) making it difficult to read clearly. 

As on the previous plot, we can see here that a lot of counties have a median income of 70 000 or less. The average unmployment rate seems to be lower than 10%. Imperial county is a clear outlier with an unemployment rate of 22.8%. We can here see that the 4 counties with the highest median income (Marin, San Francisco, San Mateo, Santa Clara) also have a low unemployment rate (between 6 and 8%), confirming the observation done with the previous plot. It is possible that highest income are associated with lower unemployment rate but it is not really clear with this plot only. The data for county with income lower than 70 000 would be helpful.

.As seen before, we can see that the average population is less than 1 000 000 (Los Angeles county is still visible as a clear outlier here). The average unmployment rate seems to be lower than 10%. Imperial county is a clear outlier with an unemployment rate of 22.8%. There doesn't seems to be a strong correlation between unemployment rate and population. It may looks like counties with population over 1 000 000 have an unemployment rate slighly lower than the average, but this tendancy is not clear. The data for counties with population lower than 1 000 000 would be helpful. Maybe removing Imperial and Los Angeles county could be helpfull for readability.
