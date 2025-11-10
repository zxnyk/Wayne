from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, DECIMAL, func
import enum
from sqlalchemy.orm import relationship
from db.connection import Base
from decimal import Decimal

class TransactionType(enum.Enum):
    INCOME = "Income"
    EXPENSE = "Expense"
    TRANSFER = "Transfer"


class AccountType(enum.Enum):
    CASH = "Cash"
    BANK = "Bank"
    DIGITAL_WALLET = "Digital_Wallet"
    EMERGENCY_FUND = "Emergency_Fund"
    SAVINGS = "Savings"
    INVESTMENT = "Investment"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String=50, unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # --Relationships--
    accounts = relationship("Account", back_populates="user")
    categories = relationship("Category", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")
    goals = relationship("Goal", back_populates="user")


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(Enum(AccountType), nullable=False, default=AccountType.CASH)
    current_balance = Column(DECIMAL(12,2), nullable=False, default=Decimal('0.00'))
    created_at = Column(DateTime, server_default=func.now())
    
    # --Foreign Key --
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # --Relationships--
    user = relationship("User", back_populates="accounts")

    transactions = relationship("Transcationsq")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)


class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL(10,2), nullable=False)
    type = Column(Enum(TransactionType), nullable=False, default=AccountType.CASH)
    title = Column(String(100))
    notes = Column(String)
    transaction_date = Column(DateTime, server_default=func.now(), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # --Foreign Key--
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_id = Column(Integer, ForeignKey=("accounts.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)


    name = Column(String(100), nullable=False)