import argparse
import datetime

parser = argparse.ArgumentParser(description='calc days')
parser.add_argument('start_date', type=str, help='YYYY-MM-DD')
parser.add_argument('end_date', type=str, help='YYYY-MM-DD')

args = parser.parse_args()

def calculate_days(start_date, end_date):
    start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    delta = end_date_obj - start_date_obj

    return delta.days

if __name__ == '__main__':
    days = calculate_days(args.start_date, args.end_date)
    print(f'days between {args.start_date} and {args.end_date} is {days}.')