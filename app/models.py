from . import db


class AppTable(db.Model):
    __tablename__ = "application"

    id = db.Column("id", db.Integer, primary_key=True)
    sd2y = db.Column("SeriousDlqin2yrs", db.Boolean)
    ruul = db.Column("RevolvingUtilizationOfUnsecuredLines", db.Float)
    age = db.Column("age", db.Integer)
    past_due_3059 = db.Column("NumberOfTime30-59DaysPastDueNotWorse", db.Integer)
    debt_ratio = db.Column("DebtRatio", db.Float)
    m_income = db.Column("MonthlyIncome", db.Float)
    open_credit = db.Column("NumberOfOpenCreditLinesAndLoans", db.Integer)
    n_late_90 = db.Column("NumberOfTimes90DaysLate", db.Integer)
    n_loan_real_estate = db.Column("NumberRealEstateLoansOrLines", db.Integer)
    past_due_6089 = db.Column("NumberOfTime60-89DaysPastDueNotWorse", db.Integer)
    n_dependents = db.Column("NumberOfDependents", db.Integer)

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.sd2y = kwargs.get("SeriousDlqin2yrs")
        self.ruul = kwargs.get("RevolvingUtilizationOfUnsecuredLines")
        self.age = kwargs.get("age")
        self.past_due_3059 = kwargs.get("NumberOfTime30-59DaysPastDueNotWorse")
        self.debt_ratio = kwargs.get("DebtRatio")
        self.m_income = kwargs.get("MonthlyIncome")
        self.open_credit = kwargs.get("NumberOfOpenCreditLinesAndLoans")
        self.n_late_90 = kwargs.get("NumberOfTimes90DaysLate")
        self.n_loan_real_estate = kwargs.get("NumberRealEstateLoansOrLines")
        self.past_due_6089 = kwargs.get("NumberOfTime60-89DaysPastDueNotWorse")
        self.n_dependents = kwargs.get("NumberOfDependents")

    def __repr__(self):
        return '<ID: %s>' % self.id


class AppTableService:
    @classmethod
    def insert_data(cls, data):
        data = AppTable(**data)
        db.session.add(data)
        db.session.commit()

    @classmethod
    def query_by_id(cls, my_id):
        return AppTable.query.get(my_id)

