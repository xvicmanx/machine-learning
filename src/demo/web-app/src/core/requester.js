// @flow

type Data = {
  path: string,
  method?: 'POST' | 'GET' | 'PUT' | 'DELETE',
  payload?: Object,
};

const getHost = (): string => {
  const { protocol, host } = window.location;
  const { PORT, NODE_ENV } = process.env;
  return NODE_ENV === 'production'
    ? `${protocol}//${host}/api`
    : `http://localhost:${PORT || 3005}`;
};

const requester = async (data: Data): Promise<Object> => {
  try {
    const response = await fetch(`${getHost()}${data.path}`, {
      method: data.method || 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data.payload),
    }).then((res) => res.json());
    return response;
  } catch (error) {
    return {
      success: false,
      message: 'Unexpected Error',
    };
  }
};

export default requester;
