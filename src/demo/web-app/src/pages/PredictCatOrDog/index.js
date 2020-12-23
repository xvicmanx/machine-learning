import React, { useState } from 'react';
import { Button, Form, Heading, Message } from 'react-bulma-components';
import { useDispatch, useSelector } from 'react-redux'
import ImageInput from '../../core/ImageInput';

import Layout from '../../core/Layout';
import { predict } from '../../redux/Actions';

const PredictCatOrDog = () => {
  const dispatch = useDispatch()
  const [img, setImg] = useState('');
  const [sent, setSent] = useState(false);
  const isDog = useSelector(state => state.predictCatOrDog.value)

  return (
    <Layout>
      <Heading>
        Predicts whether a given picture is a cat or dog
      </Heading>
      <Form.Field>
        <Form.Label>Picture</Form.Label>
        <Form.Control>
          <ImageInput
            name="img"
            placeholder="Image"
            previewWidth="100px"
            onChange={(name, image) => {
              setImg(image);
              setSent(false);
            }}
          />
        </Form.Control>
      </Form.Field>
      <Button
        color="warning"
        onClick={() => {
          dispatch(predict({
            name: 'predictCatOrDog',
            mapResult: (res) => res.dog,
            payload: { img },
          }));
          setSent(true);
        }}
      >
        Send
      </Button>
      <br /> <br />
      {!!(img && sent) && (
        <Message>
          <Message.Header>
            Is a dog?
          </Message.Header>
          <Message.Body>
            {isDog ? 'Yes' : 'No'}
          </Message.Body>
        </Message>
      )}
    </Layout>
  );
};

export default PredictCatOrDog;