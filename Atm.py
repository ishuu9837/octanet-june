import time
def main():
    print('Please insert your card')
    time.sleep(1)

    password = 1233
    balance = 5000
    transaction_history = []

    try:
        pin = int(input('Enter your PIN: '))
    except ValueError:
        print('Invalid input. Please enter a numeric PIN.')
        return

    if pin == password:
        while True:
            print('\n1. Check Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transaction History')
            print('5. Transfer')
            print('6. Quit')

            try:
                option = int(input('Please enter your choice: '))
            except ValueError:
                print('Please enter a valid option.')
                continue

            if option == 1:
                print(f'Your current balance is {balance}.')
            elif option == 2:
                try:
                    withdraw_amt = int(input('Please enter withdraw amount: '))
                except ValueError:
                    print('Invalid input. Please enter a numeric amount.')
                    continue

                if withdraw_amt > balance:
                    print('Insufficient balance.')
                else:
                    balance -= withdraw_amt
                    transaction_history.append(f'Withdrawn: {withdraw_amt}')
                    print(f'{withdraw_amt} is debited from your account.')
                    print(f'Your updated balance is {balance}.')
            elif option == 3:
                try:
                    deposit_amt = int(input('Please enter deposit amount: '))
                except ValueError:
                    print('Invalid input. Please enter a numeric amount.')
                    continue

                balance += deposit_amt
                transaction_history.append(f'Deposited: {deposit_amt}')
                print(f'{deposit_amt} is credited to your account.')
                print(f'Your updated balance is {balance}.')
            elif option == 4:
                print('Transaction History:')
                if not transaction_history:
                    print('No transactions yet.')
                else:
                    for transaction in transaction_history:
                        print(transaction)
            elif option == 5:
                try:
                    transfer_amt = int(input('Please enter transfer amount: '))
                    transfer_acc = input('Please enter account number to transfer to: ')
                except ValueError:
                    print('Invalid input. Please enter a numeric amount.')
                    continue

                if transfer_amt > balance:
                    print('Insufficient balance.')
                else:
                    balance -= transfer_amt
                    transaction_history.append(f'Transferred: {transfer_amt} to account {transfer_acc}')
                    print(f'{transfer_amt} is transferred to account {transfer_acc}.')
                    print(f'Your updated balance is {balance}.')
            elif option == 6:
                print('Thank you for using our service.')
                break
            else:
                print('Invalid option. Please try again.')
    else:
        print('You entered the wrong PIN.')


if __name__ == "__main__":
    main()
