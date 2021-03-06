from . import Base, Session
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER, REAL, FLOAT, BOOLEAN
from sqlalchemy.orm.session import make_transient


class AppTable(Base):
    __tablename__ = "application"

    id = Column("id", INTEGER, primary_key=True, autoincrement=True)
    sd2y = Column("SeriousDlqin2yrs", BOOLEAN)
    rev_util = Column("RevolvingUtilizationOfUnsecuredLines", FLOAT)
    age = Column("age", INTEGER)
    past_due_3059 = Column("NumberOfTime30-59DaysPastDueNotWorse", INTEGER)
    debt_ratio = Column("DebtRatio", FLOAT)
    m_income = Column("MonthlyIncome", REAL)
    open_credit = Column("NumberOfOpenCreditLinesAndLoans", INTEGER)
    n_late_90 = Column("NumberOfTimes90DaysLate", INTEGER)
    n_loan_real_estate = Column("NumberRealEstateLoansOrLines", INTEGER)
    past_due_6089 = Column("NumberOfTime60-89DaysPastDueNotWorse", INTEGER)
    n_dependents = Column("NumberOfDependents", INTEGER)
    est_credit_line = Column("EstimatedCreditLine", FLOAT)
    avg_income = Column("AverageIncomeUntilApp", FLOAT)

    def __init__(self, id, **kwargs):
        self.id = id
        self.rev_util = kwargs.get("RevolvingUtilizationOfUnsecuredLines")
        self.age = kwargs.get("age")
        self.past_due_3059 = kwargs.get("NumberOfTime30-59DaysPastDueNotWorse")
        self.debt_ratio = kwargs.get("DebtRatio")
        self.m_income = kwargs.get("MonthlyIncome")
        self.open_credit = kwargs.get("NumberOfOpenCreditLinesAndLoans")
        self.n_late_90 = kwargs.get("NumberOfTimes90DaysLate")
        self.n_loan_real_estate = kwargs.get("NumberRealEstateLoansOrLines")
        self.past_due_6089 = kwargs.get("NumberOfTime60-89DaysPastDueNotWorse")
        self.n_dependents = kwargs.get("NumberOfDependents")
        self.est_credit_line = kwargs.get("EstimatedCreditLine")
        self.avg_income = kwargs.get("AverageIncomeUntilApp")


class AppTableService:
    @classmethod
    def update_wallet(cls, ticker, amount, date, tether_amount):
        session = Session()
        current_wallet = session.query(AppTable).order_by(AppTable.id.desc()).first()
        session.expunge(current_wallet)
        make_transient(current_wallet)
        current_wallet.id += 1
        setattr(current_wallet, ticker, getattr(current_wallet, ticker) + amount)
        current_wallet.date = date
        current_wallet.usdt += tether_amount

        try:
            session.add(current_wallet)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()


    @classmethod
    def insert_target_data(cls, id, target_data):
        session = Session()
        selected_row = session.query(AppTable).get(id)
        session.expunge(selected_row)
        make_transient(selected_row)
        # TODO: add the target data to existing row.
        selected_row

    @classmethod
    def insert_data(cls, data: AppTable):
        session = Session()
        try:
            session.add(data)
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()


