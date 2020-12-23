import React, { useState } from 'react';
import { Button, Form, Heading, Message } from 'react-bulma-components';
import { useDispatch, useSelector } from 'react-redux'

import Layout from '../../core/Layout';
import { predict } from '../../redux/Actions';

const PredictCustomerSegment = () => {
  const dispatch = useDispatch()
  const [sent, setSent] = useState(false);
  const [income, setIncome] = useState(0);
  const [score, setScore] = useState(0);
  const segment = useSelector(state => state.predictCustomerSegment.value);

  return (
    <Layout>
      <Heading>
        Customer Segment prediction based on annual income and spending score
      </Heading>
      <Form.Field>
        <Form.Label>Annual Income</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="income"
            value={income}
            onChange={(evt) => {
              setIncome(evt.currentTarget.value);
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
      <Form.Field>
        <Form.Label>Spending Score</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="score"
            value={score}
            onChange={(evt) => {
              setScore(evt.currentTarget.value);
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
      <Button
        color="warning"
        onClick={() => {
          dispatch(predict({
            name: 'predictCustomerSegment',
            mapResult: (res) => res.segment,
            payload: { income, score },
          }));
          setSent(true);
        }}
      >
        Send
      </Button>
      <br /> <br />
      {!!(income && score && sent) && (
        <Message>
          <Message.Header>
            Customer Segment
          </Message.Header>
          <Message.Body>
            {segment}
          </Message.Body>
        </Message>
      )}
    </Layout>
  );
};

export default PredictCustomerSegment;