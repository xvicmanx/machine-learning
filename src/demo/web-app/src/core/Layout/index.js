import React from 'react';
import { Navbar, Columns } from 'react-bulma-components';
import { Link } from 'react-router-dom';

import './style.css'

const Layout = ({ children }) => (
  <div>
    <Navbar color="warning">
      <Navbar.Brand>
        <Navbar.Item renderAs="a" href="#">
          Machine Learning Demos
        </Navbar.Item>
      </Navbar.Brand>
    </Navbar>
    <Columns>
      <Columns.Column size={3}>
        <ul className="Links">
          <li className="Links__item">
            <Link to="/predict-salary">
              Predict Salary
            </Link>
          </li>
          <li className="Links__item">
            <Link to="/predict-purchase">
              Predict Purchase
            </Link>
          </li>
          <li className="Links__item">
            <Link to="/predict-customer-segment">
              Predict Customer Segment
            </Link>
          </li>
          <li className="Links__item">
            <Link to="/predict-review-outcome">
              Predict Review Outcome
            </Link>
          </li>
          <li className="Links__item">
            <Link to="/predict-bank-leaving">
              Predict Bank Leaving
            </Link>
          </li>
          <li className="Links__item">
            <Link to="/predict-cat-or-dog">
              Predict Cat or Dog
            </Link>
          </li>
        </ul>
      </Columns.Column>
      <Columns.Column size={9}>
        <div className="Layout__Body">
          {children}
        </div>
      </Columns.Column>
    </Columns>
  </div>
);

export default Layout;
