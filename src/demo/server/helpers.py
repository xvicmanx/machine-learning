from flask import request

def use_schema(schema, part = 'json'):
  def decorator(func):
    def wrapper(*args, **kwargs):
      values = getattr(request, part)
      errors = schema.validate(values)
      if errors:
        return str(errors), 400
      return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
  return decorator
