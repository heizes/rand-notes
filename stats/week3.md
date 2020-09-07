# Week 3 - Descriptive Statistics (describe set of data)

## Measures of central tendency

1. **Mean** - average of all values in the datasets

        Sample Mean - x̄ = ( Σ xi ) / n
        
        average() function

2. **Median** - middle value

        Even = 
        Odd = get the average of 2 middle

        median() function

3. **Mode** - most frequent value

        1, 4, 2, 4, 9
        mode => 4
        mode.sngl() function

        1, 4, 2, 4, 9, 9
        mode => 4, 9
        mode.mult() function // ctrl + shift + enter

4. **Midrange** -  average of the smallest and largest values

        1, 4, 2, 4, 9

        1 is the smallest and 9 is the smallest

        solve the average of both numbers

        midrage => 1 + 9 / 2 = 5

        min() & max()

## Measure of Dispersion

2 types of dataset => dispersed & not dispersed

1. **Variance** - the higher the variance the more dispersed the sets of data is.

        sample variance (sample data)
        var.s() function

        https://image.prntscr.com/image/1O4uPAaZSHKVzQuVybwSYA.png

        population variance (population data)
        var.p() function

        https://image.prntscr.com/image/-MiUwbYMQCyAmdxfKC2hhg.png

2. **Standard Deviation** - square root of the variance

        S = Sample SD
        σ = Population SD

        SQRT() function
        stdev.s() function (sample)
        stdev.e() function (population)

3. **Percentile**

        35th percentile - higher than 35% of the data

        percentile.exc(cells, 0.00)


4. **Interquartile range**

        - difference between the  25th  and 75th percentiles

        - measures the dispersion of middle values of both percentiles

        percentile.exc(cell, 0.25) - percentile.exc(cell, 0.75)

        https://image.prntscr.com/image/IQjj8k9_T92cVXEJWmZc2g.png

