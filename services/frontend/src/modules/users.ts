import { get } from 'src/mixins/fetch'

export async function getUsers () {
  return await get('users/list').then(response => response.data)
}
