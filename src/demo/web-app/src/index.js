import React from 'react';
import { render } from 'react-snapshot';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Provider } from 'react-redux';

import store from './store';
import PredictSalary from './pages/PredictSalary';

import 'react-bulma-components/dist/react-bulma-components.min.css';
import './index.css';


render(
  <Router>
    <Provider store={store}>
      <div className="App">
        <Switch>
          <Route path="/" component={PredictSalary} />
        </Switch>
      </div>
    </Provider>
  </Router>,
  document.getElementById('root')
);
