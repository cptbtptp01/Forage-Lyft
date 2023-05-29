def add_years_to_date(date, years_to_add:int):
    result = date.replace(year=date.year + years_to_add)
    return result

def check_values_in_array(array:list, wear:float) -> bool:
    for val in array:
        if val >= wear:
            return True
        continue
    return False

def check_sums_in_array(array:list, wear:int) -> bool:
    return sum(array) >= wear