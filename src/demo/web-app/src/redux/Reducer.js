import {
  UPDATE_LOADING_STATE,
  SET_ERROR,
  SET_RESULT,
} from './ActionTypes';

export const INITIAL_STATE = {
  predictSalary: {
    value: 0,
    error: null,
    loading: false,
  },
};

const Reducer = (state = INITIAL_STATE, { type, payload } = {}) => {
  console.log(state);
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
