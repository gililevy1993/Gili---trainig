"""
This program calculate number of days between two dates
"""
def calc_days(first_date, last_date):
    
    first_date = first_date.split("/")
    first_days = int(first_date[0])
    first_month = int(first_date[1])
    first_year = int(first_date[2])
    
    last_date = last_date.split("/")
    last_days = int(last_date[0])
    last_month = int(last_date[1])
    last_year = int(last_date[2])
    
    # calculation
    delta_days = last_days - first_days
    if delta_days < 0:
        delta_days *= -1

    delta_month = last_month - first_month
    if delta_month < 0:
        delta_month *= -1

    delta_years = last_year - first_year
    if delta_years < 0:
        delta_dayes *= -1
        
    sum_date = delta_days + delta_month + delta_years
    return sum_date

def main():
    first_date = input("Please enter first date [dd/mm/yyyy]: ")
    last_date = input("Please enter last date [dd/mm/yyyy]: ")
    print(calc_days(first_date, last_date))

if __name__ == "__main__":
    main()

