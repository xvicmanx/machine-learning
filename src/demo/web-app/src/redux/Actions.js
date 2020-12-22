// @flow

import {
  UPDATE_LOADING_STATE,
  SET_ERROR,
  SET_RESULT,
} from './ActionTypes';

import APIService from '../APIService';

type Options = {
  name: string,
  payload: Object,
  mapResult: Function,
};

export const predict = ({
  name,
  payload,
  mapResult,
}: Options): any => async (dispatch) => {
  dispatch({
    type: UPDATE_LOADING_STATE,
    payload: {
      loading: true,
      name,
    },
  });

  const res = await APIService[name](payload);

  if (res.success) {
    dispatch({
      type: SET_RESULT,
      payload: {
        name,
        value: mapResult(res),
      },
    });
  } else {
    dispatch({
      type: SET_ERROR,
      payload: {
        name,
        message: res.message,
      },
    });
  }

  dispatch({
    type: UPDATE_LOADING_STATE,
    payload: {
      loading: false,
      name,
    },
  });
};
