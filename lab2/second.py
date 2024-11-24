from dataclasses import dataclass
import dataclasses
import json
import os
from typing import List, Dict, Optional

@dataclass
class Transaction:
    description: str
    category: str
    amount: int
    id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)

class TransactionJsonManager:

    def __init__(self, file_name):
        self._file_name = file_name

    def export_json(self, list_of_obj: List[Transaction]):
        jsonedTasks = json.dumps([dataclasses.asdict(obj) for obj in list_of_obj], sort_keys=True, indent=4)
        with open(self._file_name, 'w') as file:
            file.write(jsonedTasks)

    def import_json(self) -> List[Transaction]:
        if not os.path.isfile(self._file_name): return []
        with open(self._file_name, 'r') as file:
            return [Transaction(**obj) for obj in json.load(file)]

class TransactionManager:
    transactions: List[Transaction] = []

    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions

    def get_transactions(self) -> List[Transaction]:
        return self.transactions

    def add(self, transaction: Transaction):
        new_transaction_id = self.transactions[-1]['id']+1 if len(self.transactions) else 1
        self.transactions.append(
            Transaction(
                id=new_transaction_id,
                amount=transaction.amount,
                description=transaction.description,
                category=transaction.category
            ))
    
    def remove(self, id: int):
        self.transactions = [transaction for transaction in self.transactions if transaction['id'] != id]

    def print_transactions(self):
        if len(self.transactions) == 0:
            print('--- No transactions ---')
            return
        for transaction in (self.transactions):
            print(f'{transaction['id']}. {transaction['description']} #{transaction['category']}')

class BudgetTracker:
    transactionManager: TransactionManager
    jsonManager: TransactionJsonManager

    def __init__(self):
        self.jsonManager = TransactionJsonManager('transactions.json')
        transactions_from_json = self.jsonManager.import_json()
        self.transactionManager = TransactionManager(transactions_from_json)

    def start(self):
        while(True):
            self.transactionManager.print_transactions()
            print('\nOptions:\n1. Add transaction\n2. Remove transaction\n3. Export as JSON\n4. Quit')
            match input('Enter desired option: \n'): 
                case '1':
                    self.transactionManager.add(
                        Transaction(
                            description=input('Enter transaction description: '),
                            amount=int(input('Enter transaction amount: ')),
                            category=input('Enter transaction category: ')
                        ))
                case '2':
                    self.transactionManager.remove(int(input('Enter id of a transaction to be removed: ')))
                case '3':
                    self.jsonManager.export_json(self.transactionManager.get_transactions())
                case '4':
                    print('Budget Tracker finished work')
                    return

budgetTracker = BudgetTracker()
budgetTracker.start()

