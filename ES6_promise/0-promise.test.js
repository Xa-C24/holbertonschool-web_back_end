import getResponseFromAPI from './0-promise';

test('getResponseFromAPI should return a Promise', () => {
  const response = getResponseFromAPI();
  expect(response).toBeInstanceOf(Promise);
});
