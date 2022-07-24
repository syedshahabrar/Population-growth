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

def graphGrowth(growth_list):
    import turtle
    turtle.speed(100) #for convenience for the TA
    for i in range(len(growth_list)):
        turtle.circle(growth_list[i]//100) #scaling down to a viewable size
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
    turtle.done()

#this and the getGrowth function are used to test and run the graphGrowth
growth_table = getGrowth(1000, 0.02, 1000, 3)
print(growth_table)
graphGrowth(growth_table)