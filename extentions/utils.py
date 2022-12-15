from . import jalali
from django.utils import timezone

def latin_to_persian_number(STR):
	numbers = {'0':'۰', '1':'۱', '2':'۲', '3':'۳', '4':'۴', '5':'۵', '6':'۶', '7':'۷', '8':'۸', '9':'۹',}
	for l, p in numbers.items():
		STR = STR.replace(l, p)

	return STR

def jalali_converter(time):
	month_to_str = {
		'1':'فروردین', '2':'اردیبهشت', '3':'خرداد', '4':'تیر', '5':'مرداد', '6':'شهریور', '7':'مهر', '8':'آبان', '9':'آذر', '10':'دی', '11':'بهمن', '12':'اسفند'
	}
	time = timezone.localtime(time)
	time_to_str = "{},{},{}".format(time.year, time.month, time.day)
	time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

	output = "{} {} {} ساعت {}:{}".format(
		time_to_tuple[2],
		month_to_str[f'{time_to_tuple[1]}'],
		time_to_tuple[0],
		time.hour,
		time.minute,
	)
	
	return latin_to_persian_number(output)
