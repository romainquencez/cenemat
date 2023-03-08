import { get } from 'src/mixins/fetch'

export async function getFarms () {
  return await get('farms/list').then(response => response.data)
}
