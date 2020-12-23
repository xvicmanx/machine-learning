import React from 'react';
import { render } from 'react-snapshot';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';

import store from './store';
import PredictSalary from './pages/PredictSalary';
import PredictPurchase from './pages/PredictPurchase';
import PredictCustomerSegment from './pages/PredictCustomerSegment';
import PredictReviewOutcome from './pages/PredictReviewOutcome';
import PredictBankLeaving from './pages/PredictBankLeaving';
import PredictCatOrDog from './pages/PredictCatOrDog';

import 'react-bulma-components/dist/react-bulma-components.min.css';
import './index.css';


render(
  <Router>
    <Provider store={store}>
      <div className="App">
        <Switch>
          <Route path="/" component={PredictSalary} exact />
          <Route path="/predict-salary" component={PredictSalary} />
          <Route path="/predict-purchase" component={PredictPurchase} />
          <Route path="/predict-customer-segment" component={PredictCustomerSegment} />
          <Route path="/predict-review-outcome" component={PredictReviewOutcome} />
          <Route path="/predict-bank-leaving" component={PredictBankLeaving} />
          <Route path="/predict-cat-or-dog" component={PredictCatOrDog} />
        </Switch>
      </div>
    </Provider>
  </Router>,
  document.getElementById('root')
);
