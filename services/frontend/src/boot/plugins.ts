import VueMatomo from 'vue-matomo'
import { boot } from 'quasar/wrappers'

export default boot(async ({ app, router }) => {
  if (process.env.MATOMO_HOST && process.env.MATOMO_SITE_ID) {
    return app.use(VueMatomo, {
      // Configure your matomo server and site by providing
      host: process.env.MATOMO_HOST,
      siteId: process.env.MATOMO_SITE_ID,

      // Enables automatically registering pageviews on the router
      router: router,

      // Enables link tracking on regular links. Note that this won't
      // work for routing links (ie. internal Vue router links)
      // Default: true
      enableLinkTracking: process.env.MATOMO_ENABLE_LINK_TRACKING,

      // Require consent before sending tracking information to matomo
      // Default: false
      requireConsent: process.env.MATOMO_REQUIRE_CONSENT,

      // Whether to track the initial page view
      // Default: true
      trackInitialView: process.env.MATOMO_TRACK_INITIAL_VIEW,

      // Run Matomo without cookies
      // Default: false
      disableCookies: process.env.MATOMO_DISABLE_COOKIES,

      // Enable the heartbeat timer (https://developer.matomo.org/guides/tracking-javascript-guide#accurately-measure-the-time-spent-on-each-page)
      // Default: false
      enableHeartBeatTimer: process.env.MATOMO_ENABLE_HEARTBEAT_TIMER,

      // Set the heartbeat timer interval
      // Default: 15
      heartBeatTimerInterval: process.env.MATOMO_HEARTBEAT_TIMER_INTERVAL,

      // Whether or not to log debug information
      // Default: false
      debug: process.env.MATOMO_DEBUG,

      // UserID passed to Matomo (see https://developer.matomo.org/guides/tracking-javascript-guide#user-id)
      // Default: undefined
      userId: process.env.MATOMO_USER_ID,

      // Share the tracking cookie across subdomains (see https://developer.matomo.org/guides/tracking-javascript-guide#measuring-domains-andor-sub-domains)
      // Default: undefined, example '*.example.com'
      cookieDomain: process.env.MATOMO_COOKIE_DOMAIN,

      // Tell Matomo the website domain so that clicks on these domains are not tracked as 'Outlinks'
      // Default: undefined, example: '*.example.com'
      domains: process.env.MATOMO_DOMAINS,

      // A list of pre-initialization actions that run before matomo is loaded
      // Default: []
      // Example: [
      //   ['API_method_name', parameter_list],
      //   ['setCustomVariable','1','VisitorType','Member'],
      //   ['appendToTrackingUrl', 'new_visit=1'],
      //   etc.
      // ]
      preInitActions: [],

      // Set this to include crossorigin attribute on the matomo script import
      // Default: undefined, possible values : 'anonymous', 'use-credentials'
      crossOrigin: process.env.MATOMO_CROSS_ORIGIN,
    })
  }
  return app
})
