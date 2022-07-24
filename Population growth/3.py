def get_Growth_Recursive(population_year_zero, rate, immigration_per_year, nbr_of_years):

    if nbr_of_years==0:
        return population_year_zero
    population=((1+rate)*population_year_zero)+immigration_per_year
    return get_Growth_Recursive(population,rate,immigration_per_year,nbr_of_years-1)
    # recursive function where it inputs population back into itself until nbr_of_years becomes zero

print(get_Growth_Recursive(1000,0.02,10,3))