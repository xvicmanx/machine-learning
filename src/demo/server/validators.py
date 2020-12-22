from marshmallow import Schema, fields

class PredictSalaryInputSchema(Schema):
  """
  Parameters:
    - years (int)
  """
  years = fields.Int(required = True)


class PredictPurchaseInputSchema(Schema):
  """
  Parameters:
    - age (int)
    - salary (int)
  """
  age = fields.Int(required = True)
  salary = fields.Int(required = True)


class PredictCustomerSegmentInputSchema(Schema):
  """
  Parameters:
    - anual_income (int)
    - spending_score (int)
  """
  anual_income = fields.Int(required = True)
  spending_score = fields.Int(required = True)


class PredictReviewInputSchema(Schema):
  """
  Parameters:
    - review (str)
  """
  review = fields.String(required = True)


class PredictCatOrDogInputSchema(Schema):
  """
  Parameters:
    - img (str)
  """
  img = fields.String(required = True)


class PredictBankLeavingInputSchema(Schema):
  """
  Parameters:
    - credit_score (int)
    - geography (str)
    - gender (str)
    - age (int)
    - tenure (int)
    - balance (float)
    - number_of_products (int)
    - has_credit_card (bool)
    - is_active_member (bool)
    - estimated_salary (float)
  """
  credit_score = fields.Int(required = True),
  geography = fields.String(required = True),
  gender = fields.String(required = True),
  age = fields.Int(required = True),
  tenure = fields.Int(required = True),
  balance = fields.Float(required = True),
  number_of_products = fields.Int(required = True),
  has_credit_card = fields.Boolean(required = True),
  is_active_member = fields.Boolean(required = True),
  estimated_salary = fields.Float(required = True),
