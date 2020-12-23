import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ImageUtils from './ImageUtils';

const branch = (
  WrappedComponent,
  conditional,
  defaultValue = null
) => {
  return class PP extends React.Component {
    render() {
      if (conditional(this.props)) {
        return <WrappedComponent {...this.props} />;
      }
      return defaultValue;
    }
  };
};

let styles = null;
let Input = (props) => {
  return <input {...props} />;
};

Input = branch(
  Input,
  ({ show }) => {
    return show;
  },
  null
);

let ImageContainer = ({ image, onEditPressed, width }) => {
  return (
    <div>
      <img
        alt="preview"
        src={image}
        style={styles.preview}
        width={width}
      />
      <button
        style={styles.editButton}
        onClick={onEditPressed}
      >
        Edit
      </button>
    </div>
  );
};

ImageContainer.propTypes = {
  image: PropTypes.string.isRequired,
  onEditPressed: PropTypes.func.isRequired,
  width: PropTypes.string.isRequired,
};

ImageContainer = branch(
  ImageContainer,
  ({ show }) => {
    return show;
  },
  null
);

class ImageInput extends Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      image: '',
      editing: true,
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleInput = this.handleInput.bind(this);
  }

  handleInput(event) {
    const { value } = event.target;
    this.setState({ value });
  }

  handleChange(event) {
    const { value, name } = event.target;
    (async () => {
      const image = await ImageUtils.loadImage(value);
      this.props.onChange(name, image);
      this.setState({ image, editing: false });
    })();
  }

  render() {
    return (
      <div style={styles.container}>
        <Input
          name={this.props.name}
          type="text"
          placeholder={this.props.placeholder}
          onChange={this.handleChange}
          onInput={this.handleInput}
          value={this.state.value}
          show={this.state.editing}
        />
        <ImageContainer
          onEditPressed={() => {
            this.setState({
              editing: true,
              value: '',
            });
          }}
          image={this.state.image}
          show={!this.state.editing}
          width={this.props.previewWidth}
        />
      </div>
    );
  }
}

ImageInput.defaultProps = {
  previewWidth: '80px',
};

ImageInput.propTypes = {
  name: PropTypes.string.isRequired,
  placeholder: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  previewWidth: PropTypes.string,
};

styles = {
  container: {
    display: 'inline-block',
    verticalAlign: 'middle',
  },
  preview: {
    verticalAlign: 'middle',
    marginRight: '5px',
  },
  editButton: {
    backgroundColor: 'transparent',
    color: '#DF740C',
    fontWeight: '600',
    border: '1px solid #DF740C',
    borderRadius: '3px',
    fontSize: '16px',
    cursor: 'pointer',
    verticalAlign: 'middle',
  },
};

export default ImageInput;