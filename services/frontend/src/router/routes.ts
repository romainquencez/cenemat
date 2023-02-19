import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: 'home',
        path: '',
        component: () => import('pages/IndexPage.vue')
      },
      {
        name: 'legal-mentions',
        path: 'mentions-legales',
        component: () => import('pages/LegalMentionsPage.vue'),
      },
      {
        name: 'login',
        path: 'connexion',
        component: () => import('pages/LoginPage.vue'),
        meta: {
          requiresAuth: false,
        },
      },
      {
        name: 'user',
        path: 'mon-compte',
        component: () => import('pages/UserPage.vue'),
        meta: {
          requiresAuth: true,
        },
      },
      // administration
      {
        path: 'admin',
        meta: {
          requiresAdmin: true,
        },
        children: [
          {
            name: 'admin-users',
            path: 'utilisateurs',
            component: () => import('pages/admin/UsersPage.vue'),
          }
        ]
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
