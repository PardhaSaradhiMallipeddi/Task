class Clerk:
    def __init__(self, name):
        self.name = name
        self.current_bill = []

    def add_item_to_bill(self, item):
        self.current_bill.append(item)
        print(f"{item} added to the bill.")

    def checkout_bill(self):
        total = sum(self.current_bill)
        print(f"Total amount: ${total}")
        return total


class Supervisor:
    def __init__(self):
        self.bills = []

    def view_summary(self):
        for index, bill in enumerate(self.bills, start=1):
            print(f"Bill {index}: ${bill}")

    def view_clerks(self, clerks):
        print("List of Clerks:")
        for clerk in clerks:
            print(clerk.name)

    def summary_of_payments(self):
        total_payments = sum(self.bills)
        print(f"Total payments received: ${total_payments}")


class BillDeskApplication:
    def __init__(self):
        self.clerks = []
        self.supervisor = Supervisor()

    def add_clerk(self, clerk):
        self.clerks.append(clerk)
        print(f"Clerk {clerk.name} added.")

    def save_bill(self, clerk, total):
        self.supervisor.bills.append(total)
        print(f"Bill saved for Clerk {clerk.name}.")
