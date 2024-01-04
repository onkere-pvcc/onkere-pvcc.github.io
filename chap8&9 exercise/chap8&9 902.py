#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adius
#
# Created:     20/10/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def print_formatted_report(info_tuple):
    name = info_tuple[0]
    date_of_birth = info_tuple[1]
    profession = info_tuple[2]
    place_of_birth = info_tuple[3]
    movies = info_tuple[4]

    print("Name:")
    print(f"    {name[0]} {name[1]}")

    print("Date of birth:")
    print(f"    Day: {date_of_birth[0]}")
    print(f"    Month: {date_of_birth[1]}")
    print(f"    Year: {date_of_birth[2]}")

    print("Place of Birth:")
    print(f"    State: {place_of_birth[0]}")
    print(f"    City: {place_of_birth[1]}")

    print(f"Profession: {profession}")

    print("Movies:")
    for movie in movies:
        title, year = movie
        print(f"    {title} : {year}")

# Usage example with the provided "julia_more_info" tuple
julia_more_info = (("Julia", "Roberts"), (8, "October", 1967),
                  "Actress", ("Atlanta", "Georgia"),
                  [("Duplicity", 2009),
                   ("Notting Hill", 1999),
                   ("Pretty Woman", 1990),
                   ("Erin Brockovich", 2000),
                   ("Eat Pray Love", 2010),
                   ("Mona Lisa Smile", 2003),
                   ("Oceans Twelve", 2004)])

print_formatted_report(julia_more_info)
