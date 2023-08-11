const personAccount = {
    firstName: 'John',
    lastName: 'Doe',
    incomes: [],
    expenses: [],

    totalIncome: function () {
        let total = 0
        for (const income in this.incomes){
            total += income['income'];
        }
        return total;
    },

    totalExpense: function () {
        let total = 0
        for (const expense in this.expenses){
            total += expense['expense'];
        }
        return total;
    },

    accountInfo() {
    return `Name: ${this.firstName} ${this.lastName}\nTotal Income: $${this.totalIncome()}\nTotal Expense: $${this.totalExpense()}`;
  },

    accountBalance() {
    return this.totalIncome - this.totalExpense;
  },

    addIncome(description, amount) {
    this.incomes.push({ 'description': description, 'income': amount });
  },

    addExpense(description, amount) {
    this.incomes.push({ 'description': description, 'expense': amount });
  },

}


personAccount.addIncome('Salary', 3000);
personAccount.addIncome('Bonus', 500);
personAccount.addExpense('Rent', 1000);
personAccount.addExpense('Groceries', 200);
personAccount.addExpense('Transportation', 100);


console.log(personAccount.accountInfo());
console.log('Account Balance:', personAccount.accountBalance());