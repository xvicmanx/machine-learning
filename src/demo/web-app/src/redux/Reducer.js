import {
  UPDATE_LOADING_STATE,
  SET_ERROR,
  SET_RESULT,
} from './ActionTypes';

const getDefaultValue = (value = 0) => ({
  value,
  error: null,
  loading: false,
});

export const INITIAL_STATE = {
  predictSalary: getDefaultValue(),
  predictPurchase: getDefaultValue(false),
  predictCustomerSegment: getDefaultValue(),
  predictReviewOutcome: getDefaultValue(false),
  predictBankLeaving: getDefaultValue(false),
  predictCatOrDog: getDefaultValue(false),
};

const Reducer = (state = INITIAL_STATE, { type, payload } = {}) => {
  switch (type) {
    case UPDATE_LOADING_STATE:
      return {
        ...state,
        [payload.name]: {
          ...state[payload.name],
          loading: payload.loading,
        },
      };

    case SET_ERROR:
      return {
        ...state,
        [payload.name]: {
          ...state[payload.name],
          error: payload.message,
        },
      };

    case SET_RESULT:
      return {
        ...state,
        [payload.name]: {
          ...state[payload.name],
          value: payload.value,
        },
      };

    default:
      return state;
  }
};

export default Reducer;
