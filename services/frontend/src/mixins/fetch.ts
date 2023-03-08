/*
This mixin can be used to use the Fetch API through our API endpoint.
Use any method (get() for a GET request, post() for a POST one, etc) that suit your needs.

Specification : https://fetch.spec.whatwg.org
Documentation : https://developer.mozilla.org/fr/docs/Web/API/Fetch_API
*/

export async function _client (endpoint, method, headers, body = undefined) {
  /**
  * Private function called by other methods. Should not be called directly.
  *
  * @param {string} endpoint The API endpoint to fetch; will be prefixed with API_URL constant.
  * @param {string} method A valid HTTP method that will be passed in request headers. See https://fetch.spec.whatwg.org/#methods
  * @param {object} headers A list of headers to include in request. See https://fetch.spec.whatwg.org/#terminology-headers
  * @param {object} body A body to include in request. See https://fetch.spec.whatwg.org/#bodies
  * @return {Promise} The response promise.
  */

  const config = {
    method,
    headers,
    /*
    Set credentials parameter to 'include' value to always includes credentials with this request,
    and always use any credentials sent back in the response. Needed with our cookie-based authentification.
    At login, a token is sent from the server and set in a client's cookie.
    Then, each request that require authentification must include this cookie in the HTTP headers.
    At logout, the server prompt the client to delete the cookie with the token.
    See https://fetch.spec.whatwg.org/#concept-request-credentials-mode
    */
    credentials: 'include',
  }

  if (body !== undefined) config.body = body

  return fetch(`${process.env.API_URL}/${endpoint}`, config)
    .then(async response => {
      /*
      If response is OK (a 2xx HTTP code), returns the response's content in JSON.
      See https://developer.mozilla.org/en-US/docs/Web/API/Response/ok
       */
      if (response.ok) {
        return await response.json()
      }

      // if response is not OK, return a rejected Promise with the error message.
      else {
        const errorMessage = await response.text()
        return Promise.reject(new Error(errorMessage))
      }
    })
}

export async function get (endpoint) {
  /**
  * Public function to fetch a endpoint with the GET HTTP method.
  *
  * @param {string} endpoint The API endpoint to fetch; will be prefixed with API_URL constant.
  * @return {Promise} The response promise.
  */
  return await _client(
    endpoint,
    'GET',
    {'Content-Type': 'application/json'}
  )
}

export async function post (endpoint, body = undefined) {
  /**
  * Public function to fetch a endpoint with the POST HTTP method.
  *
  * @param {string} endpoint The API endpoint to fetch; will be prefixed with API_URL constant.
  * @param {object} body A body to include in request. See https://fetch.spec.whatwg.org/#bodies
  * @return {Promise} The response promise.
  */
  return await _client(
    endpoint,
    'POST',
    {'Content-Type': 'application/json'},
    JSON.stringify(body),
  )
}

export async function postFormData (endpoint, formData = undefined) {
  /**
   * Public function to fetch a endpoint with the POST HTTP method and form data. Used for login.
   * See https://developer.mozilla.org/en-US/docs/Web/API/FormData
   *
   * @param {string} endpoint The API endpoint to fetch; will be prefixed with API_URL constant.
   * @param {formData} formData Form data to send with the HTTP request.
   * @return {Promise} The response promise.
   */
  return await _client(
    endpoint,
    'POST',
    {},
    formData,
  )
}
