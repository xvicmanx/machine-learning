import React, { useState } from 'react';
import { Button, Form, Heading, Message } from 'react-bulma-components';
import { useDispatch, useSelector } from 'react-redux'

import Layout from '../../core/Layout';
import { predict } from '../../redux/Actions';

const PredictReviewOutcome = () => {
  const dispatch = useDispatch()
  const [review, setReview] = useState('');
  const [sent, setSent] = useState(false);
  const liked = useSelector(state => state.predictReviewOutcome.value)

  return (
    <Layout>
      <Heading>
        Predict restaurant's review outcome (liked or not)
      </Heading>
      <Form.Field>
        <Form.Label>Review</Form.Label>
        <Form.Control>
          <Form.Input
            placeholder="review"
            value={review}
            onChange={(evt) => {
              setReview(evt.currentTarget.value);
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
      <Button
        color="warning"
        onClick={() => {
          dispatch(predict({
            name: 'predictReviewOutcome',
            mapResult: (res) => res.liked,
            payload: { review },
          }));
          setSent(true);
        }}
      >
        Send
      </Button>
      <br /> <br />
      {!!(review && sent) && (
        <Message>
          <Message.Header>
            Liked?
          </Message.Header>
          <Message.Body>
            {liked ? 'Yes' : 'No'}
          </Message.Body>
        </Message>
      )}
    </Layout>
  );
};

export default PredictReviewOutcome;