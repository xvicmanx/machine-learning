import React, { useState } from 'react';
import { Button, Form, Heading, Message } from 'react-bulma-components';
import { useDispatch, useSelector } from 'react-redux'

import Layout from '../../core/Layout';
import { predict } from '../../redux/Actions';

const PredictPurchase = () => {
  const dispatch = useDispatch()
  const [sent, setSent] = useState(false);
  const [age, setAge] = useState(0);
  const [salary, setSalary] = useState(0);
  const purchase = useSelector(state => state.predictPurchase.value);

  return (
    <Layout>
      <Heading>
        Purchase prediction based on age and salary
      </Heading>
      <Form.Field>
        <Form.Label>Age</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="age"
            value={age}
            onChange={(evt) => {
              setAge(evt.currentTarget.value);
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
      <Form.Field>
        <Form.Label>Salary</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="salary"
            value={salary}
            onChange={(evt) => {
              setSalary(evt.currentTarget.value);
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
      <Button
        color="warning"
        onClick={() => {
          dispatch(predict({
            name: 'predictPurchase',
            mapResult: (res) => res.purchase,
            payload: { age, salary },
          }));
          setSent(true);
        }}
      >
        Send
      </Button>
      <br /> <br />
      {!!(age && salary && sent) && (
        <Message>
          <Message.Header>
            Will purchase?
          </Message.Header>
          <Message.Body>
            {purchase ? 'Yes' : 'No'}
          </Message.Body>
        </Message>
      )}
    </Layout>
  );
};

export default PredictPurchase;