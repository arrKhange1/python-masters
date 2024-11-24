import json
import os
from typing import List, Dict

class JsonManager:

    file_name = 'tasks.json'

    def export_json(self, tasks):
        jsonedTasks = json.dumps(tasks, sort_keys=True, indent=4)
        with open(self.file_name, 'w') as file:
            file.write(jsonedTasks)

    def import_json(self):
        if not os.path.isfile(self.file_name): return []
        with open(self.file_name, 'r') as file:
            return json.load(file)

class TransactionManager:
    transactions: List[Dict[str, any]] = []

    def __init__(self, transactions):
        self.transactions = transactions

    def get_transactions(self):
        return self.transactions

    def add(self, transaction):
        new_transaction_id = self.transactions[-1]['id']+1 if len(self.transactions) else 1
        self.transactions.append({**transaction, 'is_done': 0, 'id': new_transaction_id})
    
    def remove(self, id):
        self.transactions = [transaction for transaction in self.transactions if transaction['id'] != id]

    def print_transactions(self):
        if len(self.transactions) == 0:
            print('--- No transactions ---')
            return
        for transaction in (self.transactions):
            print(f'{transaction['id']}. {transaction['description']} #{transaction['category']}')

class BudgetTracker:
    transactionManager: TransactionManager
    jsonManager: JsonManager

    def __init__(self):
        self.jsonManager = JsonManager()
        transactions_from_json = self.jsonManager.import_json()
        self.transactionManager = TransactionManager(transactions_from_json)

    def start(self):
        while(True):
            self.transactionManager.print_transactions()
            print('\nOptions:\n1. Add transaction\n2. Remove transaction\n3. Export as JSON\n4. Quit')
            match input('Enter desired option: \n'): 
                case '1':
                    self.transactionManager.add({
                            'description': input('Enter transaction description: '), 
                            'category': input('Enter transaction category: ')})
                case '2':
                    self.transactionManager.remove(int(input('Enter id of a transaction to be removed: ')))
                case '3':
                    self.jsonManager.export_json(self.transactionManager.get_tasks())
                case '4':
                    print('Budget Tracker finished work')
                    return

budgetTracker = BudgetTracker()
budgetTracker.start()

