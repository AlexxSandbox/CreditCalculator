from math import ceil, floor, log
import argparse

parser = argparse.ArgumentParser(description='Credit calculator')
parser.add_argument('--type', help='type of payment')
parser.add_argument('--payment', type=float, help='monthly payment')
parser.add_argument('--principal', type=float, help='credit principal')
parser.add_argument('--periods', type=int, help='period to repay the credit')
parser.add_argument('--interest', type=float, help='nominal interest rate')
args = parser.parse_args()

ERROR = 'Incorrect parameters'


def diff_calc():
    principal = args.principal
    periods = args.periods
    interest = args.interest / (12 * 100)
    summ_payment = 0

    for i in range(1, periods + 1):
        diff_payment = ceil(principal / periods + interest * (
                principal - (principal * (i - 1)) / periods))
        summ_payment += diff_payment
        print('Month {}: paid out {:.0f}'.format(i, diff_payment))

    overpayment = summ_payment - principal
    print('\nOverpayment = {:.0f}'.format(overpayment))


def annuity_calc():
    principal = args.principal
    periods = args.periods
    interest = args.interest / (12 * 100)

    annuity_payment = ceil(
        principal * (interest * (1 + interest) ** periods) / (
                (1 + interest) ** periods - 1))
    summ_payment = annuity_payment * periods
    overpayment = summ_payment - principal
    print('Your annuity payment = {:.0f}!'.format(annuity_payment))
    print('Overpayment = {:.0f}'.format(overpayment))


def principal_calc():
    payment = args.payment
    interest = args.interest / (12 * 100)
    periods = args.periods

    max_principal = floor(payment / ((interest * (1 + interest) ** periods) / (
            (1 + interest) ** periods - 1)))
    summ_payment = payment * periods
    overpayment = summ_payment - max_principal
    print('Your credit principal = {:.0f}!'.format(max_principal))
    print('Overpayment = {:.0f}'.format(overpayment))


def period_calc():
    payment = args.payment
    interest = args.interest / (12 * 100)
    principal = args.principal

    period = ceil(
        log(payment / (payment - interest * principal), interest + 1))
    year = period // 12
    month = period % 12

    if year == 1:
        if month == 1:
            print('You need 1 year and 1 month to repay this credit!')
        elif month > 1:
            print('You need 1 year '
                  'and {} months to repay this credit!'.format(month))
        else:
            print('You need 1 year to repay this credit!')
    elif year > 1:
        if month == 1:
            print('You need {:.0f} years '
                  'and 1 month to repay this credit!'.format(year))
        elif month > 1:
            print('You need {:.0f} years '
                  'and {:.0f} months to repay this credit!'.format(year,
                                                                   month))
        else:
            print('You need {:.0f} years to repay this credit!'.format(year))
    else:
        print('You need {} months to repay this credit!'.format(month))

    summ_payment = payment * (year * 12 + month)
    overpayment = summ_payment - principal
    print('Overpayment = {:.0f}'.format(overpayment))


def credit_calc():
    if args.type == 'annuity':

        if args.payment is None and \
                args.principal is not None and \
                args.periods is not None and \
                args.interest is not None:
            return annuity_calc()

        elif args.periods is None \
                and args.principal is not None \
                and args.payment is not None \
                and args.interest is not None:
            return period_calc()

        elif args.principal is None \
                and args.periods is not None \
                and args.payment is not None \
                and args.interest is not None:
            return principal_calc()

        else:
            print(ERROR)

    elif args.type == 'diff' \
            and args.principal > 0 \
            and args.periods > 0 \
            and args.interest > 0:
        return diff_calc()

    else:
        print(ERROR)


def main():
    credit_calc()


main()
