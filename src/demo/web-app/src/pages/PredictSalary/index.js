import React, { useState } from 'react';
import { Button, Form, Heading, Message } from 'react-bulma-components';
import { useDispatch, useSelector } from 'react-redux'

import Layout from '../../core/Layout';
import { predict } from '../../redux/Actions';

const PredictSalary = () => {
  const dispatch = useDispatch()
  const [years, setYears] = useState(0);
  const salary = useSelector(state => state.predictSalary.value)

  return (
    <Layout>
      <Heading>
        Salary prediction based on years of experience
      </Heading>
      <Form.Field>
        <Form.Label>Years</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="years"
            value={years}
            onChange={(evt) => {
              setYears(evt.currentTarget.value);
            }}
          />
        </Form.Control>
      </Form.Field>
      <Button
        color="warning"
        onClick={() => {
          dispatch(predict({
            name: 'predictSalary',
            mapResult: (res) => res.salary,
            payload: { years },
          }));
        }}
      >
        Send
      </Button>
      <br /> <br />
      <Message>
        <Message.Header>
          Predicted salary
        </Message.Header>
        <Message.Body>
          {salary}
        </Message.Body>
      </Message>
    </Layout>
  );
};

export default PredictSalary;