import React, { useState } from 'react';
import { Button, Form, Heading, Message } from 'react-bulma-components';
import { useDispatch, useSelector } from 'react-redux'

import Layout from '../../core/Layout';
import { predict } from '../../redux/Actions';

const PredictBankLeaving = () => {
  const dispatch = useDispatch()
  const [state, setState] = useState({
    creditScore: 502,
    geography: 'France',
    gender: 'Female',
    age: 25,
    tenure: 1,
    balance: 100.00,
    numberOfProducts: 1,
    hasCreditCard: true,
    isActiveMember: false,
    estimatedSalary: 100.00,
  });

  const [sent, setSent] = useState(false);
  const exited = useSelector(state => state.predictBankLeaving.value);

  return (
    <Layout>
      <Heading>
        Predict whether a customer will leave a bank institution
      </Heading>
      <Form.Field>
        <Form.Label>Credit score</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="credit score"
            value={state.creditScore}
            onChange={(evt) => {
              setState({ creditScore: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
  
      <Form.Field>
        <Form.Label>Geography</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="geograpy"
            value={state.geography}
            onChange={(evt) => {
              setState({ geography: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
    
      <Form.Field>
        <Form.Label>Gender</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="gender"
            value={state.gender}
            onChange={(evt) => {
              setState({ gender: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Form.Field>
        <Form.Label>Age</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="age"
            value={state.age}
            onChange={(evt) => {
              setState({ age: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Form.Field>
        <Form.Label>Tenure</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="tenure"
            value={state.tenure}
            onChange={(evt) => {
              setState({ tenure: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Form.Field>
        <Form.Label>Balance</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="balance"
            value={state.balance}
            onChange={(evt) => {
              setState({ balance: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Form.Field>
        <Form.Label>Number of products</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="number of products"
            value={state.numberOfProducts}
            onChange={(evt) => {
              setState({ numberOfProducts: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Form.Field>
        <Form.Label>Has credit card</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="has credit card"
            value={state.hasCreditCard}
            onChange={(evt) => {
              setState({ hasCreditCard: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Form.Field>
        <Form.Label>Is active member</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="is active member"
            value={state.isActiveMember}
            onChange={(evt) => {
              setState({ isActiveMember: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Form.Field>
        <Form.Label>Estimated salary</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="estimated salary"
            value={state.estimatedSalary}
            onChange={(evt) => {
              setState({ estimatedSalary: evt.currentTarget.value });
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>

      <Button
        color="warning"
        onClick={() => {
          dispatch(predict({
            name: 'predictBankLeaving',
            mapResult: (res) => res.exited,
            payload: state,
          }));
          setSent(true);
        }}
      >
        Send
      </Button>
      <br /> <br />
      {sent && (
        <Message>
          <Message.Header>
            Will Leave?
          </Message.Header>
          <Message.Body>
            {exited ? 'Yes' : 'No'}
          </Message.Body>
        </Message>
      )}
    </Layout>
  );
};

export default PredictBankLeaving;