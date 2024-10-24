def main():
    outdated_date()

def outdated_date():
    months_list = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]

    while True:
         input_date= input("Date ").strip()

         try:
            # this block tries to know the date format like MM/DD/YYYY
            month, date, year = input_date.split("/")
            month = int(month)
            date = int(date)
            year = int(year)
            if 1<= int(month) <= 12 and 1<= date <= 31:
                print(f"{year}-{month:02}-{date:02}")
                break

         except:
              #
           #if input date is not in the MM/DD/YYYY, try if it is Month date, year format
            try:
               if "," in input_date:

                   input_date = input_date.replace(",", "")
                   month, date, year = input_date.split()

                   if (month.capitalize() in months_list) and ( 1 <= int(date) <=31):
                    month_index = months_list.index(month.capitalize()) + 1

                    formated_date = f"{int(date):02}"
                    print(f"{year}-{month_index:02}-{formated_date}")
                    break
            except :
               pass

main()
