import requester from './core/requester';

const APIService = {
  predictSalary: ({ years }) => requester({
    path: `/predict-salary?years=${years}`,
  }),
};

export default APIService;
