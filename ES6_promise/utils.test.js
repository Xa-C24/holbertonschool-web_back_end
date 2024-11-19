import { uploadPhoto, createUser } from './utils';

test('uploadPhoto returns a resolved promise with status success', async () => {
  const result = await uploadPhoto();
  expect(result.status).toBe('success');
});

test('createUser returns a resolved promise with user data', async () => {
  const user = await createUser();
  expect(user.firstName).toBe('John');
  expect(user.lastName).toBe('Doe');
});
