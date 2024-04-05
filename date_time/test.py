# from umalqurra.hijri_date import HijriDate
# print(HijriDate.today().date)

import datetime
import hijri_converter
hijri_months = {
    1: 'محرم',
    2: 'صفر',
    3: 'ربيع الأول',
    4: 'ربيع الثاني',
    5: 'جمادى الأولى',
    6: 'جمادى الآخرة',
    7: 'رجب',
    8: 'شعبان',
    9: 'رمضان',
    10: 'شوال',
    11: 'ذو القعدة',
    12: 'ذو الحجة'
}

def get_hijri_date_with_month_name():
    today = datetime.date.today()
    hijri_date = hijri_converter.Gregorian(today.year, today.month, today.day).to_hijri()
    month_name = hijri_months[hijri_date.month]
    # Format the date with the Hijri month name
    formatted_date = f"{hijri_date.day} {month_name} {hijri_date.year}"
    return formatted_date

# Example usage
hijri_date_with_month_name = get_hijri_date_with_month_name()
print(f"Today's Hijri date is {hijri_date_with_month_name}")