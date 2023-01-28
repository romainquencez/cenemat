<template>
  <q-layout view="hHh Lpr lff">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-tabs
          shrink
          stretch
        >
          <q-route-tab
            exact
            name="home"
            label="CENEMAT"
            :to="{ name: 'home' }"
          />
        </q-tabs>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      class="bg-grey-3"
      show-if-above
      bordered
    >
      <q-scroll-area class="fit">
        <q-list>
          <template v-if="userStore.isAuthenticated">
            <q-item
              exact
              clickable
              v-ripple
              :to="{ name: 'user' }"
            >
              <q-item-section avatar>
                <q-icon name="person" />
              </q-item-section>
              <q-item-section>
                Mon compte
              </q-item-section>
            </q-item>

            <q-item
              exact
              clickable
              v-ripple
              @click="logOut()"
            >
              <q-item-section avatar>
                <q-icon name="logout" />
              </q-item-section>
              <q-item-section>
                Déconnexion
              </q-item-section>
            </q-item>
          </template>
          <q-item
            v-else
            exact
            clickable
            v-ripple
            :to="{ name: 'login' }"
          >
            <q-item-section avatar>
              <q-icon name="login" />
            </q-item-section>
            <q-item-section>
              Connexion
            </q-item-section>
          </q-item>

          <q-separator />

          <q-item
            clickable
            v-ripple
            href="http://cenemat.weebly.com"
            target="_blank"
          >
            <q-item-section avatar>
              <q-icon name="public" />
            </q-item-section>
            <q-item-section>
              Site web
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useUserStore } from 'stores/users'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'MainLayout',
  setup () {
    const leftDrawerOpen = ref(false)
    const userStore = useUserStore()
    const router = useRouter()

    return {
      userStore,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      },
      async logOut () {
        return await userStore.logOut().then(() =>{
          // redirect user to home page
          router.push({name: 'home'})
        })
      },
    }
  }
});
</script>
