def add_years_to_date(date, years_to_add:int):
    result = date.replace(year=date.year + years_to_add)
    return result

def subtract_years_from_date(date, years_to_subtract:int):
    result = date.replace(year=date.year - years_to_subtract)
    return result