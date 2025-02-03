/*Assume that a bank maintains two kinds of accounts for customers, 
one called as savings account and the other as current account. 
The savings account provides compound intrest and withdrawl facilities 
but no cheque book facility. The Curreent account provides cheque book facility 
but no intrest. Current account holders should also maintain a minimum 
balanve and if the balance falls below this level, a service charge */

#include <iostream>
#include <string>

class BankAccount {
public:
    BankAccount(std::string name, double balance, bool isSavings) :
        name(name), balance(balance), isSavings(isSavings) {}

    virtual void deposit(double amount) {
        balance += amount;
    }

    virtual void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
        } else {
            std::cout << "Insufficient funds.\n";
        }
    }

    virtual void displayBalance() const {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Balance: " << balance << std::endl;
    }

    virtual void addInterest() {
        // This is a placeholder for interest calculation.
        // Implement it according to your specific interest rate and calculation method.
    }

protected:
    std::string name;
    double balance;
    bool isSavings;
};

class SavingsAccount : public BankAccount {
public:
    SavingsAccount(std::string name, double balance) : BankAccount(name, balance, true) {}

    void addInterest() override {
        // Implement your interest calculation logic here.
        // For example, you could use a compound interest formula.
        double interestRate = 0.05; // Example interest rate
        balance *= (1 + interestRate);
    }
};

class CurrentAccount : public BankAccount {
public:
    CurrentAccount(std::string name, double balance, double minimumBalance) :
        BankAccount(name, balance, false), minimumBalance(minimumBalance) {}

    void withdraw(double amount) override {
        if (balance >= amount + minimumBalance) {
            balance -= amount;
        } else {
            std::cout << "Insufficient funds or minimum balance requirement not met\n";
        }
    }

    void displayBalance() const override {
        BankAccount::displayBalance();
        std::cout << "Mini Balance: " << minimumBalance << std::endl;
    }

private:
    double minimumBalance;
};

int main() {
    SavingsAccount savingsAccount("John Doe", 1000.0);
    CurrentAccount currentAccount("Jane Smith", 5000.0, 2000.0);

    savingsAccount.deposit(500.0);
    savingsAccount.withdraw(200.0);
    savingsAccount.addInterest();
    savingsAccount.displayBalance();

    currentAccount.deposit(1000.0);
    currentAccount.withdraw(3000.0);
    currentAccount.displayBalance();

    return 0;
}