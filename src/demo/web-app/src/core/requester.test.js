import requester from './requester';

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ success: true }),
  })
);

describe('requester', () => {
  beforeEach(() => {
    global.fetch.mockClear();
  });

  it('works as expected', async () => {
    const result = await requester({
      path: '/test-path',
      method: 'POST',
      payload: { name: 'test' },
    });
    expect(result).toEqual({ success: true });
    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(global.fetch).toHaveBeenCalledWith(
      'http://localhost:4500/test-path',
      {
        body: '{"name":"test"}',
        headers: {
          'Content-Type': 'application/json',
        },
        method: 'POST',
      }
    );
  });

  it('handles unexpected errors properly', async () => {
    global.fetch = jest.fn(() => Promise.reject('Error'));
    const result = await requester({
      path: '/test-path',
      method: 'POST',
      payload: { name: 'test' },
    });

    expect(result).toEqual({ success: false, message: 'Unexpected Error' });
    expect(global.fetch).toHaveBeenCalledTimes(1);
    expect(global.fetch).toHaveBeenCalledWith(
      'http://localhost:4500/test-path',
      {
        body: '{"name":"test"}',
        headers: {
          'Content-Type': 'application/json',
        },
        method: 'POST',
      }
    );
  });
});
