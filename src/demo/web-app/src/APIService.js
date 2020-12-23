import requester from './core/requester';

const APIService = {
  predictSalary: ({ years }) => requester({
    path: '/predict-salary',
    method: 'POST',
    payload: { years },
  }),
  predictPurchase: ({ age, salary }) => requester({
    path: '/predict-purchase',
    method: 'POST',
    payload: { age, salary },
  }),
  predictCustomerSegment: ({ income, score }) => requester({
    path: '/predict-customer-segment',
    method: 'POST',
    payload: {
      annual_income: income,
      spending_score: score,
    },
  }),
  predictReviewOutcome: ({ review }) => requester({
    path: '/predict-review-outcome',
    method: 'POST',
    payload: { review }
  }),
  predictCatOrDog: ({ img }) => requester({
    path: '/predict-cat-or-dog',
    method: 'POST',
    payload: { img },
  }),
  predictBankLeaving: ({
    creditScore,
    geography,
    gender,
    age,
    tenure,
    balance,
    numberOfProducts,
    hasCreditCard,
    isActiveMember,
    estimatedSalary,
  }) => requester({
    path: '/predict-bank-leaving',
    method: 'POST',
    payload: {
      credit_score: creditScore,
      geography,
      gender,
      age,
      tenure,
      balance,
      number_of_products: numberOfProducts,
      has_credit_card: hasCreditCard,
      is_active_member: isActiveMember,
      estimated_salary: estimatedSalary,
    },
  }),
};


export default APIService;
