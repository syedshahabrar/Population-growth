def getGrowth(population_year_zero, rate, immigration_per_year, nbr_of_years):
    
    population_list = []
    previous_population = population_year_zero
    #this is set to be the population used in the loop

    for i in range(nbr_of_years):
        final_population = (1+rate)*previous_population + immigration_per_year
        population_list.append(final_population)
        previous_population = final_population
    #this loop iterated next years population using previous years one
    return population_list

print(getGrowth(1000,0.02,10,3))